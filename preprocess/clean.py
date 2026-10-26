"""Raw crawl tables -> cleaned tables for mining.

    python -m preprocess.clean

Reads `models`, `edges`, `crawl_queue` (written by the crawler, never modified)
and rebuilds three tables from scratch on every run:

  clean_models    one row per scraped model, with normalised license/task/dates,
                  its BFS depth and seed family
  clean_edges     one row per (child, parent, relation): the union of what the
                  child's tags say and what the parent's listing says, plus flags
  quality_issues  one row per problem found: the evidence for the report's
                  data-quality section

Why rebuild instead of editing in place: the raw tables stay a faithful record
of what HF served, so every cleaning rule can be changed and re-run without
re-crawling.
"""
import json
import logging
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import config

log = logging.getLogger(__name__)

# HF began recording repo creation dates in early March 2022; every older repo
# shows this date (e.g. bert-base-uncased, released 2018). Dates before the
# cutoff mean "created on or before", not "created on".
CREATED_AT_FLOOR = "2022-03-03"

# A child created *before* its parent is impossible for real lineage. A small
# gap is normal, since a base and its instruct version are often uploaded
# minutes or hours apart. Gaps longer than this are flagged.
TEMPORAL_TOLERANCE_DAYS = 7

# --- licenses -------------------------------------------------------------------
# HF already stores licenses as ids from its fixed list, so the work is
# grouping them. "restricted" = a model-specific license with use restrictions
# (acceptable-use policies, user caps), e.g. Llama and Gemma licenses and the
# OpenRAIL family.
_LICENSE_CATEGORY = {
    "apache-2.0": "permissive", "mit": "permissive", "cc-by-4.0": "permissive",
    "cc-by-3.0": "permissive", "cc-by-2.0": "permissive", "cc0-1.0": "permissive",
    "unlicense": "permissive", "bsl-1.0": "permissive", "isc": "permissive",
    "artistic-2.0": "permissive", "zlib": "permissive", "wtfpl": "permissive",
    "afl-3.0": "permissive", "ecl-2.0": "permissive", "pddl": "permissive",
    "odc-by": "permissive", "postgresql": "permissive", "ncsa": "permissive",
    "mpl-2.0": "copyleft", "osl-3.0": "copyleft", "odbl": "copyleft",
    "cdla-sharing-1.0": "copyleft",
    "other": "other", "cc": "other",
}
_LICENSE_PREFIX_CATEGORY = [          # checked in order, first match wins
    ("bsd", "permissive"), ("cdla-permissive", "permissive"),
    ("cc-by-nc", "noncommercial"),     # before the others: cc-by-nc-sa / -nd are non-commercial
    ("cc-by-sa", "copyleft"),
    ("cc-by-nd", "restricted"),        # "no derivatives" forbids exactly what a fine-tune is
    ("gpl", "copyleft"), ("agpl", "copyleft"), ("lgpl", "copyleft"),
    ("epl", "copyleft"), ("eupl", "copyleft"), ("gfdl", "copyleft"),
    ("llama", "restricted"), ("gemma", "restricted"), ("deepseek", "restricted"),
    ("openrail", "restricted"), ("creativeml-openrail", "restricted"),
    ("bigscience-", "restricted"), ("bigcode-openrail", "restricted"),
]
LICENSE_CATEGORIES = ("permissive", "copyleft", "noncommercial", "restricted", "other", "unknown")


def normalise_license(raw):
    """'Apache-2.0 ' -> 'apache-2.0'; empty -> None."""
    if raw is None:
        return None
    value = str(raw).strip().lower()
    return value or None


def license_category(license_id):
    if license_id is None:
        return "unknown"
    if license_id in _LICENSE_CATEGORY:
        return _LICENSE_CATEGORY[license_id]
    for prefix, category in _LICENSE_PREFIX_CATEGORY:
        if license_id.startswith(prefix):
            return category
    return "other"


# --- model ids ------------------------------------------------------------------
_URL_PREFIX = re.compile(r"^(https?://)?(www\.)?(huggingface\.co|hf\.co)/", re.IGNORECASE)
_ID_PART = re.compile(r"^[A-Za-z0-9][\w.\-]*$")


def normalise_model_id(raw):
    """Turn a declared base_model value into 'org/model' (or a legacy 'model' id).

    Handles the malformed values people put in cards: full URLs, URLs to a
    file or branch, and stray whitespace. Returns None for values that can't be
    a Hub id (local paths like './checkpoints/x', free text, empty strings).
    """
    if not isinstance(raw, str):
        return None
    value = _URL_PREFIX.sub("", raw.strip()).strip("/")
    if value.startswith("models/"):          # https://huggingface.co/models/... is not a repo
        return None
    parts = value.split("/")
    # 'org/model/tree/main' or 'org/model/blob/main/x.bin' -> 'org/model'
    if len(parts) > 2 and parts[2] in ("tree", "blob", "resolve", "raw", "commit"):
        parts = parts[:2]
    if len(parts) not in (1, 2) or not all(_ID_PART.match(p) for p in parts):
        return None
    return "/".join(parts)


# --- dates ----------------------------------------------------------------------

def normalise_timestamp(raw):
    """'2024-09-15T12:17:40.000Z' -> '2024-09-15T12:17:40Z' (UTC, seconds)."""
    if not raw:
        return None
    try:
        dt = datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _days_between(earlier, later):
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return (datetime.strptime(later, fmt) - datetime.strptime(earlier, fmt)).total_seconds() / 86400


# --- schema ---------------------------------------------------------------------

CLEAN_SCHEMA = """
DROP TABLE IF EXISTS clean_models;
DROP TABLE IF EXISTS clean_edges;
DROP TABLE IF EXISTS quality_issues;

CREATE TABLE clean_models (
    id                  TEXT PRIMARY KEY,
    author              TEXT,
    license             TEXT,        -- normalised HF license id, NULL if none declared
    license_name        TEXT,        -- custom name when license = 'other'
    license_category    TEXT NOT NULL,
    pipeline_tag        TEXT,        -- own task, or inherited (see pipeline_tag_source)
    pipeline_tag_source TEXT NOT NULL CHECK (pipeline_tag_source IN ('own','inherited','none')),
    library_name        TEXT,
    tags_json           TEXT,
    downloads           INTEGER,
    downloads_all_time  INTEGER,
    likes               INTEGER,
    created_at          TEXT,        -- UTC 'YYYY-MM-DDTHH:MM:SSZ'
    created_month       TEXT,        -- 'YYYY-MM', for trends
    created_at_is_floor INTEGER NOT NULL,   -- 1 = HF's pre-2022 placeholder date
    gated               TEXT,
    depth               INTEGER,     -- BFS depth (0 = seed)
    root                TEXT,        -- seed family it was reached from
    declared_bases_json TEXT,        -- card base_model, normalised
    hf_children_json    TEXT,        -- {relation: n} as HF reports it (Model tree box)
    hf_children_total   INTEGER,     -- sum of the above; NULL if a count was unknown
    scraped_at          TEXT
);

CREATE TABLE clean_edges (
    child_id         TEXT NOT NULL,
    parent_id        TEXT NOT NULL,
    relation         TEXT NOT NULL,
    in_tags          INTEGER NOT NULL,   -- child's own page lists this parent
    in_listing       INTEGER NOT NULL,   -- parent's children listing lists this child
    child_in_sample  INTEGER NOT NULL,   -- child was scraped
    parent_in_sample INTEGER NOT NULL,   -- parent was scraped
    temporal_anomaly INTEGER NOT NULL,   -- child created > tolerance before parent
    PRIMARY KEY (child_id, parent_id, relation)
);

CREATE TABLE quality_issues (
    entity_id TEXT NOT NULL,     -- model id, or 'child -> parent' for edges
    issue     TEXT NOT NULL,
    detail    TEXT
);
"""


# --- main steps -----------------------------------------------------------------

def run(conn):
    """Rebuild the clean tables. Returns {issue: count}."""
    conn.row_factory = sqlite3.Row
    issues = []                                    # (entity, issue, detail)
    models = _load_models(conn, issues)
    edges = _merge_edges(conn, models, issues)
    aliases = infer_aliases(models, edges)
    _check_declared_bases(models, edges, aliases, issues)
    _inherit_pipeline_tags(models, edges)
    _write(conn, models, edges, issues)
    return dict(Counter(issue for _, issue, _ in issues))


def _load_models(conn, issues):
    """Read raw models + their BFS position; normalise per-model fields."""
    position = {}
    for row in conn.execute("SELECT model_id, depth, root FROM crawl_queue "
                            "WHERE status = 'done' ORDER BY depth, rank"):
        position.setdefault(row["model_id"], (row["depth"], row["root"]))   # shallowest wins

    models = {}
    for row in conn.execute("SELECT * FROM models"):
        m = dict(row)
        mid = m["id"]
        m["license"] = normalise_license(m["license"])
        m["license_category"] = license_category(m["license"])
        m["created_at"] = normalise_timestamp(m["created_at"])
        m["created_month"] = m["created_at"][:7] if m["created_at"] else None
        m["created_at_is_floor"] = int(bool(m["created_at"]) and m["created_at"] < CREATED_AT_FLOOR)
        m["pipeline_tag_source"] = "own" if m["pipeline_tag"] else "none"
        m["depth"], m["root"] = position.get(mid, (None, None))
        # HF's own child counts are exact, unlike our capped sample of children,
        # so population-level stats (branching factor, relation shares) use these.
        m["hf_children"] = json.loads(m["children_counts_json"] or "{}")
        counts = list(m["hf_children"].values())
        m["hf_children_total"] = None if None in counts else sum(counts)

        declared = []
        for raw in json.loads(m["card_base_model_json"] or "[]"):
            norm = normalise_model_id(raw)
            if norm is None:
                issues.append((mid, "declared_base_malformed", raw))
            elif norm != raw:
                issues.append((mid, "declared_base_normalised", f"{raw!r} -> {norm}"))
            if norm and norm != mid and norm not in declared:
                declared.append(norm)
        m["declared_bases"] = declared

        if m["license"] is None:
            issues.append((mid, "missing_license", None))
        if m["pipeline_tag"] is None:
            issues.append((mid, "missing_pipeline_tag", None))
        if m["created_at"] is None:
            issues.append((mid, "missing_created_at", None))
        if m["created_at_is_floor"]:
            issues.append((mid, "created_at_floor", m["created_at"]))
        for field in json.loads(m["parse_errors_json"] or "[]"):
            issues.append((mid, "parse_error", field))
        models[mid] = m
    return models


def _merge_edges(conn, models, issues):
    """Union of tag edges and listing edges -> {(child, parent, relation): flags}."""
    edges = {}
    for row in conn.execute("SELECT child_id, parent_id, relation, source FROM edges"):
        child, parent, rel = row["child_id"], row["parent_id"], row["relation"]
        if child == parent:
            issues.append((child, "self_loop", rel))
            continue
        e = edges.setdefault((child, parent, rel), {"in_tags": 0, "in_listing": 0})
        e["in_" + row["source"]] = 1

    # Same child + parent with different relations depending on the source.
    by_pair = defaultdict(set)
    for child, parent, rel in edges:
        by_pair[(child, parent)].add(rel)
    for (child, parent), rels in by_pair.items():
        if len(rels) > 1:
            issues.append((f"{child} -> {parent}", "relation_conflict", ",".join(sorted(rels))))

    for (child, parent, rel), e in edges.items():
        e["child_in_sample"] = int(child in models)
        e["parent_in_sample"] = int(parent in models)
        e["temporal_anomaly"] = 0
        # A child we scraped whose own page doesn't confirm a listing edge.
        if e["in_listing"] and not e["in_tags"] and e["child_in_sample"]:
            issues.append((f"{child} -> {parent}", "listing_not_in_child_tags", rel))
        c, p = models.get(child, {}), models.get(parent, {})
        c_at, p_at = c.get("created_at"), p.get("created_at")
        if c_at and p_at and not (c["created_at_is_floor"] or p["created_at_is_floor"]):
            gap = _days_between(c_at, p_at)          # > 0 means child is older
            if gap > TEMPORAL_TOLERANCE_DAYS:
                e["temporal_anomaly"] = 1
                issues.append((f"{child} -> {parent}", "child_older_than_parent",
                               f"{gap:.0f} days"))
    return edges


def infer_aliases(models, edges):
    """Learn renamed ids from the data itself: {old declared id: id HF resolved}.

    Example: a card says `base_model: meta-llama/Meta-Llama-3.1-8B`, but HF's
    tag for it says `meta-llama/Llama-3.1-8B` (the repo was renamed). When a
    model declares exactly one base that HF didn't tag, and HF tagged exactly
    one parent the card didn't declare, the two must be the same repo. Ids
    whose evidence conflicts are dropped.
    """
    tag_parents = defaultdict(set)
    for (child, parent, _), e in edges.items():
        if e["in_tags"]:
            tag_parents[child].add(parent)
    votes = defaultdict(set)
    for mid, m in models.items():
        declared = set(m["declared_bases"])
        untagged = declared - tag_parents[mid]
        undeclared = tag_parents[mid] - declared
        if len(untagged) == 1 and len(undeclared) == 1:
            votes[untagged.pop()].add(undeclared.pop())
    return {old: next(iter(new)) for old, new in votes.items() if len(new) == 1}


def _check_declared_bases(models, edges, aliases, issues):
    """Compare each card-declared base with what HF actually linked (tags)."""
    tag_parents = defaultdict(set)
    for (child, parent, _), e in edges.items():
        if e["in_tags"]:
            tag_parents[child].add(parent)
    for mid, m in models.items():
        for base in m["declared_bases"]:
            if base in tag_parents[mid]:
                continue
            if aliases.get(base) in tag_parents[mid]:
                issues.append((mid, "declared_base_renamed", f"{base} -> {aliases[base]}"))
            else:
                # HF didn't create a link: a typo, a deleted/private repo, or a
                # rename we have no 1-to-1 evidence for. These are the "broken"
                # parent links; we can't tell which cause it is without fetching
                # the declared id, so the label stays neutral.
                issues.append((mid, "declared_base_not_linked", base))


def _inherit_pipeline_tags(models, edges):
    """Fill a missing task from the parent(s), and record that we did.

    Adapters and quantizations almost never set pipeline_tag but do the same
    task as their parent. We only inherit when all in-sample parents agree.
    Models are processed shallow-first, so inheritance can chain.
    """
    parents = defaultdict(list)
    for (child, parent, _), e in edges.items():
        if e["in_tags"] and parent in models:
            parents[child].append(parent)
    for m in sorted(models.values(), key=lambda m: (m["depth"] is None, m["depth"] or 0)):
        if m["pipeline_tag"]:
            continue
        tasks = {models[p]["pipeline_tag"] for p in parents[m["id"]]} - {None}
        if len(tasks) == 1:
            m["pipeline_tag"] = tasks.pop()
            m["pipeline_tag_source"] = "inherited"


def _write(conn, models, edges, issues):
    with conn:
        conn.executescript(CLEAN_SCHEMA)
        conn.executemany(
            "INSERT INTO clean_models VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [(m["id"], m["author"], m["license"], m["license_name"], m["license_category"],
              m["pipeline_tag"], m["pipeline_tag_source"], m["library_name"], m["tags_json"],
              m["downloads"], m["downloads_all_time"], m["likes"], m["created_at"],
              m["created_month"], m["created_at_is_floor"], m["gated"], m["depth"], m["root"],
              json.dumps(m["declared_bases"]), json.dumps(m["hf_children"]),
              m["hf_children_total"], m["scraped_at"])
             for m in models.values()])
        conn.executemany(
            "INSERT INTO clean_edges VALUES (?,?,?,?,?,?,?,?)",
            [(c, p, r, e["in_tags"], e["in_listing"], e["child_in_sample"],
              e["parent_in_sample"], e["temporal_anomaly"])
             for (c, p, r), e in edges.items()])
        conn.executemany("INSERT INTO quality_issues VALUES (?,?,?)", issues)


def report(conn):
    """Human-readable summary of the clean tables (the numbers for the report)."""
    q = lambda sql: conn.execute(sql).fetchall()
    n = q("SELECT COUNT(*) FROM clean_models")[0][0]
    lines = [f"clean_models: {n}"]
    for col, label in [("license", "license"), ("created_at", "created_at")]:
        k = q(f"SELECT COUNT(*) FROM clean_models WHERE {col} IS NULL")[0][0]
        lines.append(f"  missing {label:<14} {k:>5}  ({100 * k / max(n, 1):.1f} %)")
    for src, k in q("SELECT pipeline_tag_source, COUNT(*) FROM clean_models GROUP BY 1"):
        lines.append(f"  pipeline_tag {src:<10} {k:>5}  ({100 * k / max(n, 1):.1f} %)")
    lines.append("  license categories: " + ", ".join(
        f"{c} {k}" for c, k in q("SELECT license_category, COUNT(*) n FROM clean_models GROUP BY 1 ORDER BY n DESC")))
    e = q("SELECT COUNT(*), SUM(in_tags), SUM(in_listing), SUM(in_tags AND in_listing), "
          "SUM(child_in_sample AND parent_in_sample), SUM(temporal_anomaly) FROM clean_edges")[0]
    lines.append(f"clean_edges: {e[0]} (from tags {e[1]}, from listings {e[2]}, both {e[3]}; "
                 f"both ends scraped {e[4]}; temporal anomalies {e[5]})")
    agree = q("SELECT SUM(in_tags), COUNT(*) FROM clean_edges WHERE in_listing AND child_in_sample")[0]
    if agree[1]:
        lines.append(f"  listing edges confirmed by the child's tags: {agree[0]}/{agree[1]} "
                     f"({100 * agree[0] / agree[1]:.1f} %)")
    lines.append("quality_issues:")
    for issue, k in q("SELECT issue, COUNT(*) n FROM quality_issues GROUP BY 1 ORDER BY n DESC"):
        lines.append(f"  {issue:<28} {k}")
    return "\n".join(lines)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s",
                        stream=sys.stdout)
    conn = sqlite3.connect(config.DB_PATH)
    run(conn)
    print(report(conn))


if __name__ == "__main__":
    main()
