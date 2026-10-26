"""Breadth-first crawl of the model lineage graph into SQLite.

    python -m crawler.crawl --max-models 500

How it works, one level at a time:
  1. Scrape every *pending* model in crawl_queue: model page -> `models` row
     plus child->parent edges from its tags (source='tags').
  2. Expand the shallowest level that still has unqueued children. For each
     scraped model there, read its children listings (most-downloaded first,
     up to MAX_CHILDREN_PER_RELATION per relation) and store the parent->child
     edges seen there (source='listing').
  3. Choose which of those children to scrape next, fairly (see select_fair),
     and enqueue them as the next level. Repeat until the depth limit or the
     model budget is reached.

Why level-by-level instead of a plain FIFO queue: with a FIFO, the first
seed's listings would fill the whole budget before any other seed was looked
at (Llama-3.1-8B alone has 3k+ children). Splitting each level's budget
round-robin across seed families keeps the sample balanced.

Resumable: each model is committed on its own, and each level is enqueued in
one transaction. Every HTTP response is cached (crawler/fetch.py), so
re-running after a crash just continues and re-downloads nothing.
"""
import argparse
import json
import logging
import sqlite3
import sys
import time

import config
from crawler.fetch import Fetcher, RobotsDisallowed
from crawler.parse_listing import listing_url, parse_listing
from crawler.parse_model import parse_model_page

log = logging.getLogger("crawler")

SCHEMA = """
CREATE TABLE IF NOT EXISTS models (
    id                       TEXT PRIMARY KEY,   -- canonical id from the page JSON
    author                   TEXT,
    license                  TEXT,
    license_name             TEXT,
    pipeline_tag             TEXT,
    library_name             TEXT,
    tags_json                TEXT,
    downloads                INTEGER,            -- last 30 days, as of scraped_at
    downloads_all_time       INTEGER,
    likes                    INTEGER,
    created_at               TEXT,
    last_modified            TEXT,
    gated                    TEXT,               -- 'no' | 'auto' | 'manual'
    card_base_model_json     TEXT,               -- declared parents (list)
    card_base_model_relation TEXT,
    card_datasets_json       TEXT,
    card_language_json       TEXT,
    children_counts_json     TEXT,               -- {relation: n} from the Model tree box
    parse_errors_json        TEXT,
    scraped_at               TEXT
);

-- One row per (child, parent, relation) *per source*, so we can compare what the
-- child's own page says ('tags') with what the parent's listing says ('listing').
CREATE TABLE IF NOT EXISTS edges (
    child_id  TEXT NOT NULL,
    parent_id TEXT NOT NULL,
    relation  TEXT NOT NULL CHECK (relation IN ('finetune','adapter','quantized','merge','unknown')),
    source    TEXT NOT NULL CHECK (source IN ('tags','listing')),
    PRIMARY KEY (child_id, parent_id, relation, source)
);

CREATE TABLE IF NOT EXISTS crawl_queue (
    id       TEXT PRIMARY KEY,                   -- id as we found it (may be a legacy alias)
    depth    INTEGER NOT NULL,                   -- seeds are 0
    root     TEXT NOT NULL,                      -- seed this model was reached from
    rank     INTEGER NOT NULL,                   -- scrape order
    status   TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','done','failed')),
    error    TEXT,                               -- why it failed
    model_id TEXT                                -- canonical id once scraped
);
CREATE INDEX IF NOT EXISTS idx_queue_status ON crawl_queue(status, depth, rank);
"""

# HTTP status -> crawl_queue.error. None of these are retried (docs/ethics.md).
_ERRORS = {0: "network", 401: "missing_or_private", 404: "not_found"}


# ---- database ----------------------------------------------------------------

def connect(db_path):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


def add_seeds(conn, seeds):
    with conn:
        for rank, seed in enumerate(seeds):
            conn.execute("INSERT OR IGNORE INTO crawl_queue (id, depth, root, rank) VALUES (?, 0, ?, ?)",
                         (seed, seed, rank))


def _count(conn, where, params=()):
    return conn.execute(f"SELECT COUNT(*) FROM crawl_queue WHERE {where}", params).fetchone()[0]


# ---- main loop ---------------------------------------------------------------

def crawl(conn, fetcher, max_models, max_depth=config.MAX_DEPTH,
          per_relation_cap=config.MAX_CHILDREN_PER_RELATION):
    """Run until the depth limit or the model budget is reached.

    Budget = scraped + still-pending models; failed ones don't use it up.
    """
    while True:
        scrape_pending(conn, fetcher, max_models)
        if _count(conn, "status = 'pending'"):
            log.info("model budget reached with models still pending; stopping")
            return
        budget = max_models - _count(conn, "status = 'done'")
        if budget <= 0:
            log.info("model budget of %d reached", max_models)
            return
        if not enqueue_next_level(conn, fetcher, budget, max_depth, per_relation_cap):
            log.info("no more children within depth %d; crawl complete", max_depth)
            return


def enqueue_next_level(conn, fetcher, budget, max_depth, per_relation_cap):
    """Find the shallowest level with unqueued children; enqueue up to `budget`.

    Looking at the shallowest level first keeps it a true BFS even across
    runs: if a later run raises --max-models, level 1 gets topped up before
    anything at level 2 is scraped. Re-reading a level's listings is cheap
    because they're all cached.
    """
    queued = _queued_ids(conn)
    for depth in range(max_depth):
        streams = expand_level(conn, fetcher, depth, per_relation_cap)
        chosen = select_fair(streams, budget, queued)
        if chosen:
            _enqueue(conn, chosen, depth + 1)
            per_root = {}
            for _, root in chosen:
                per_root[root] = per_root.get(root, 0) + 1
            log.info("level %d: enqueued %d models %s", depth + 1, len(chosen), per_root)
            return True
    return False


# ---- step 1: scrape model pages ------------------------------------------------

def scrape_pending(conn, fetcher, max_models):
    started = time.monotonic()
    done_before = last_logged = _count(conn, "status = 'done'")
    while _count(conn, "status = 'done'") < max_models:
        row = conn.execute("SELECT id FROM crawl_queue WHERE status = 'pending' "
                           "ORDER BY depth, rank LIMIT 1").fetchone()
        if row is None:
            return
        scrape_one(conn, fetcher, row["id"])
        done = _count(conn, "status = 'done'")
        if done % 25 == 0 and done != last_logged:
            last_logged = done
            _log_progress(conn, fetcher, max_models, started, done - done_before)


def scrape_one(conn, fetcher, queue_id):
    """Scrape one model page and commit it. Never raises for a bad page."""
    try:
        result = fetcher.get(f"{config.BASE_URL}/{queue_id}")
    except RobotsDisallowed:
        return _fail(conn, queue_id, "robots_disallowed")
    if not result.ok:
        return _fail(conn, queue_id, _ERRORS.get(result.status, f"http_{result.status}"))

    m = parse_model_page(result.text)
    if not m["id"]:
        return _fail(conn, queue_id, "parse_error")
    if m["id"] != queue_id:
        log.info("%s is now %s", queue_id, m["id"])   # renamed / legacy id redirect

    with conn:
        conn.execute(
            "INSERT OR REPLACE INTO models VALUES "
            "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (m["id"], m["author"], m["license"], m["license_name"], m["pipeline_tag"],
             m["library_name"], _json(m["tags"]), m["downloads"], m["downloads_all_time"],
             m["likes"], m["created_at"], m["last_modified"], _gated(m["gated"]),
             _json(m["card_base_model"]), m["card_base_model_relation"],
             _json(m["card_datasets"]), _json(m["card_language"]),
             _json(m["children_counts"]), _json(m["parse_errors"]), result.fetched_at))
        conn.execute("DELETE FROM edges WHERE child_id = ? AND source = 'tags'", (m["id"],))
        conn.executemany("INSERT OR IGNORE INTO edges VALUES (?, ?, ?, 'tags')",
                         [(m["id"], parent, rel) for parent, rel in (m["parents"] or [])])
        conn.execute("UPDATE crawl_queue SET status = 'done', error = NULL, model_id = ? WHERE id = ?",
                     (m["id"], queue_id))
    if m["parse_errors"]:
        log.warning("%s parsed with errors in %s", m["id"], m["parse_errors"])


def _fail(conn, queue_id, error):
    log.warning("failed %s: %s", queue_id, error)
    with conn:
        conn.execute("UPDATE crawl_queue SET status = 'failed', error = ? WHERE id = ?",
                     (error, queue_id))


# ---- step 2: read children listings --------------------------------------------

def expand_level(conn, fetcher, depth, per_relation_cap):
    """Return {root: [child-id list per (parent, relation)]} for one level.

    Lists keep the listing order (most downloads first). Listing edges are
    stored as a side effect, including for children we won't scrape.
    """
    rows = conn.execute(
        "SELECT q.model_id, q.root, m.children_counts_json FROM crawl_queue q "
        "JOIN models m ON m.id = q.model_id "
        "WHERE q.depth = ? AND q.status = 'done' ORDER BY q.rank", (depth,)).fetchall()
    streams, seen = {}, set()
    for row in rows:
        if row["model_id"] in seen:     # two queue ids can redirect to one model
            continue
        seen.add(row["model_id"])
        counts = json.loads(row["children_counts_json"] or "{}")
        read = {}
        for relation in config.RELATIONS:
            if relation not in counts:   # no Model tree link = no children: skip the request
                continue
            children = fetch_children(conn, fetcher, row["model_id"], relation, per_relation_cap)
            read[relation] = len(children)
            if children:
                streams.setdefault(row["root"], []).append(children)
        if read:
            log.info("level %d listings for %s: %s | requests so far %d",
                     depth, row["model_id"], read, fetcher.stats["network"])
    return streams


def fetch_children(conn, fetcher, parent_id, relation, cap):
    """Read listing pages for one parent+relation until `cap` children or the end."""
    children, page = [], 0
    while len(children) < cap:
        url = listing_url(parent_id, relation, page)
        try:
            result = fetcher.get(url)
        except RobotsDisallowed:
            log.error("robots.txt disallows %s", url)
            break
        if result.status == 400:         # HF's answer for a page past the end
            break
        if not result.ok:
            log.warning("listing %s returned %s", url, result.status)
            break
        listing = parse_listing(result.text)
        if (listing["parent_id"], listing["relation"]) != (parent_id, relation):
            log.warning("listing %s shows filter %s:%s, skipped", url,
                        listing["relation"], listing["parent_id"])
            break
        children += [child for child, _ in listing["children"]]
        if listing["next_page"] is None:
            break
        page = listing["next_page"]

    children = children[:cap]
    with conn:
        conn.executemany("INSERT OR IGNORE INTO edges VALUES (?, ?, ?, 'listing')",
                         [(child, parent_id, relation) for child in children])
    return children


# ---- step 3: choose what to scrape next ----------------------------------------

def select_fair(streams_by_root, budget, already_queued):
    """Pick up to `budget` new children, sharing the budget fairly.

    Two levels of round-robin:
      - within a seed family, take turns between its (parent, relation) lists,
        so e.g. finetunes don't crowd out adapters and merges;
      - across seed families, take turns too, so each family gets an equal
        share until it runs out of children.
    Each list is already sorted by downloads, so every turn takes the most-used
    remaining child. A model reachable from several parents (merges) is only
    taken once.
    """
    per_root = [[(child, root) for child in round_robin(lists)]
                for root, lists in streams_by_root.items()]
    chosen, seen = [], set(already_queued)
    for child, root in round_robin(per_root):
        if len(chosen) >= budget:
            break
        if child not in seen:
            seen.add(child)
            chosen.append((child, root))
    return chosen


def round_robin(lists):
    """[[a1, a2, a3], [b1]] -> [a1, b1, a2, a3]"""
    merged = []
    for i in range(max((len(lst) for lst in lists), default=0)):
        for lst in lists:
            if i < len(lst):
                merged.append(lst[i])
    return merged


def _queued_ids(conn):
    ids = set()
    for row in conn.execute("SELECT id, model_id FROM crawl_queue"):
        ids.add(row["id"])
        if row["model_id"]:
            ids.add(row["model_id"])
    return ids


def _enqueue(conn, chosen, depth):
    next_rank = conn.execute("SELECT COALESCE(MAX(rank), -1) + 1 FROM crawl_queue").fetchone()[0]
    with conn:   # one transaction: a crash leaves the whole level or none of it
        conn.executemany("INSERT INTO crawl_queue (id, depth, root, rank) VALUES (?, ?, ?, ?)",
                         [(child, depth, root, next_rank + i) for i, (child, root) in enumerate(chosen)])


# ---- reporting -------------------------------------------------------------------

def _log_progress(conn, fetcher, max_models, started, scraped_now):
    done = _count(conn, "status = 'done'")
    rate = scraped_now / max(time.monotonic() - started, 1e-9)
    log.info("done %d/%d | failed %d | pending %d | requests %d, cache hits %d, retries %d | %.2f models/s",
             done, max_models, _count(conn, "status = 'failed'"), _count(conn, "status = 'pending'"),
             fetcher.stats["network"], fetcher.stats["cache_hits"], fetcher.stats["retries"], rate)


def summary(conn):
    """Short end-of-crawl report (the full analysis comes in later phases)."""
    q = conn.execute
    lines = ["crawl summary:"]
    for row in q("SELECT status, COUNT(*) n FROM crawl_queue GROUP BY status"):
        lines.append(f"  queue {row['status']:<8} {row['n']}")
    for row in q("SELECT error, COUNT(*) n FROM crawl_queue WHERE status='failed' GROUP BY error"):
        lines.append(f"  failed: {row['error']:<20} {row['n']}")
    for row in q("SELECT depth, COUNT(*) n FROM crawl_queue WHERE status='done' GROUP BY depth"):
        lines.append(f"  depth {row['depth']}: {row['n']} models")
    for row in q("SELECT root, COUNT(*) n FROM crawl_queue WHERE status='done' GROUP BY root ORDER BY n DESC"):
        lines.append(f"  family {row['root']:<32} {row['n']}")
    for row in q("SELECT source, relation, COUNT(*) n FROM edges GROUP BY source, relation"):
        lines.append(f"  edges {row['source']:<8} {row['relation']:<10} {row['n']}")
    return "\n".join(lines)


def _json(value):
    return None if value is None else json.dumps(value)


def _gated(value):
    return "no" if value is False else value


def _setup_logging():
    config.LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")
    for handler in (logging.StreamHandler(sys.stdout), logging.FileHandler(config.LOG_PATH, encoding="utf-8")):
        handler.setFormatter(fmt)
        logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--max-models", type=int, default=config.MAX_MODELS)
    parser.add_argument("--max-depth", type=int, default=config.MAX_DEPTH)
    parser.add_argument("--per-relation-cap", type=int, default=config.MAX_CHILDREN_PER_RELATION)
    args = parser.parse_args(argv)

    if config.DATA_DIR.resolve() == config.SAMPLE_DATA_DIR.resolve():
        sys.exit("refusing to crawl into sample_data/: it's the committed demo dataset. "
                 "Unset HF_ECOSYSTEM_DATA (or point it elsewhere) to crawl.")
    _setup_logging()
    conn = connect(config.DB_PATH)
    add_seeds(conn, config.SEEDS)
    fetcher = Fetcher()
    log.info("crawl start: max_models=%d max_depth=%d per_relation_cap=%d",
             args.max_models, args.max_depth, args.per_relation_cap)
    try:
        crawl(conn, fetcher, args.max_models, args.max_depth, args.per_relation_cap)
    except KeyboardInterrupt:
        log.warning("interrupted; run the same command again to resume")
    log.info("requests %d, cache hits %d, retries %d",
             fetcher.stats["network"], fetcher.stats["cache_hits"], fetcher.stats["retries"])
    log.info(summary(conn))


if __name__ == "__main__":
    main()
