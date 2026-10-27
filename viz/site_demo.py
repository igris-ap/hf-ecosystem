"""Export the step-by-step pipeline demo for the explorer site (site/demo.js).

    python -m viz.site_demo          # needs the live crawl cache in the data dir

For a handful of real models it replays what the pipeline did, from the
cached responses: the listing page that surfaced the model, the model page's
embedded JSON, the parsed record, the raw row vs the cleaned row, and the
quality issues cleaning raised. Nothing is fetched; it all comes from the
cache and the database, so the demo shows exactly what the crawler saw.

Only whitelisted JSON keys are exported. The page's author block (avatar,
user ids) is left out, the same as in the crawl itself (docs/ethics.md).
"""
import gzip
import hashlib
import json
import re
import sqlite3

from bs4 import BeautifulSoup

import config
from crawler.common import find_props
from crawler.parse_listing import listing_url, parse_listing
from crawler.parse_model import parse_model_page
from preprocess import clean

OUT = config.ROOT / "site" / "demo.js"

# (label, model id, what this case shows)
CASES = [
    ("Typical path", "bartowski/Meta-Llama-3.1-8B-Instruct-GGUF",
     "One of the most downloaded quantizations of Llama 3.1. Everything on its page is well-formed."),
    ("Messy model card", "mradermacher/AstroSage-8B-GGUF",
     "Its card says license: [llama3.1], a list instead of text. This model crashed the crawler at "
     "9,025 models, until the parser learned to normalise list values."),
    ("License conflict", "DiTy/gemma-2-9b-it-function-calling-GGUF",
     "A quantization of a Gemma model that is published as Apache-2.0, a looser license than its parent's."),
    ("Renamed parent", "NousResearch/Hermes-3-Llama-3.1-8B-GGUF",
     "Its card names meta-llama/Meta-Llama-3.1-8B, the old name of a repo Meta later renamed."),
    ("Doubtful lineage", "Kukedlc/NeuralLLaMa-3-8b-ORPO-v0.3",
     "Claims Llama-3.1-8B-Instruct as its parent, but was created two months before that model existed."),
]

MODEL_KEYS = ("id", "author", "downloads", "likes", "createdAt", "lastModified", "pipeline_tag",
              "library_name", "gated", "tags")
CARD_KEYS = ("license", "license_name", "base_model", "base_model_relation", "pipeline_tag",
             "datasets", "language")
LISTING_ITEM_KEYS = ("id", "downloads", "likes", "pipeline_tag")


def cached(url):
    """(meta, body text) for a URL from the crawl cache, or (None, None).
    File names follow crawler/fetch.py: sha1 of the URL."""
    key = hashlib.sha1(url.encode("utf-8")).hexdigest()
    meta_path = config.CACHE_DIR / f"{key}.json"
    if not meta_path.exists():
        return None, None
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    body_path = config.CACHE_DIR / f"{key}.body.gz"
    raw = body_path.read_bytes()
    meta["bytes"], meta["bytes_gz"] = len(gzip.decompress(raw)), len(raw)
    return meta, gzip.decompress(raw).decode("utf-8", errors="replace")


def _trim(value, n=6):
    if isinstance(value, list) and len(value) > n:
        return value[:n] + [f"… {len(value) - n} more"]
    return value


def page_excerpt(text, model_id):
    """The bits of raw HTML the parser reads, shortened for display."""
    soup = BeautifulSoup(text, "html.parser")
    targets = [el["data-target"] for el in soup.find_all(attrs={"data-target": True, "data-props": True})]
    i = text.find('data-target="ModelHeader"')
    start = text.rfind("<div", 0, i)
    end = text.find('"', text.find("data-props=", i) + len('data-props="'))
    props_len = end - (text.find("data-props=", i) + len('data-props="'))
    first_key = text.find("&quot;,", i)          # cut after the first key, before the author block
    tag = text[start:first_key + len("&quot;,")] + f" … {props_len / 1000:.0f} KB of HTML-escaped JSON … }}\">"
    links = []
    pattern = re.compile(r"/models\?other=base_model:(\w+):" + re.escape(model_id) + "$")
    for a in soup.find_all("a", href=pattern):
        links.append({"href": a["href"], "text": a.get_text(" ", strip=True)})
    return {"targets": targets, "header_tag": tag, "tree_links": links}


def header_json(text):
    model = find_props(BeautifulSoup(text, "html.parser"), "ModelHeader")["model"]
    out = {k: model.get(k) for k in MODEL_KEYS if k in model}
    if isinstance(out.get("author"), dict):          # never export the profile block
        out["author"] = out["author"].get("name")
    card = model.get("cardData") or {}
    out["cardData"] = {k: _trim(card[k]) for k in CARD_KEYS if k in card}
    return out


def discovery(conn, model_id):
    """The listing page that brought this model into the crawl, if any."""
    for parent, relation in conn.execute(
            "SELECT parent_id, relation FROM clean_edges WHERE child_id = ? AND in_listing = 1 "
            "ORDER BY parent_in_sample DESC", (model_id,)):
        for page in range(0, 20):
            url = listing_url(parent, relation, page)
            meta, text = cached(url)
            if meta is None:
                break
            listing = parse_listing(text)
            ids = [c for c, _ in listing["children"]]
            if model_id not in ids:
                if listing["next_page"] is None:
                    break
                continue
            values = find_props(BeautifulSoup(text, "html.parser"), "ModelList")["initialValues"]
            pos = ids.index(model_id)
            items = values["models"]
            keep = sorted({0, 1, 2, pos})
            shown = []
            for k in keep:
                if shown and k - keep[keep.index(k) - 1] > 1:
                    shown.append(f"… {k - keep[keep.index(k) - 1] - 1} more models …")
                shown.append({key: items[k].get(key) for key in LISTING_ITEM_KEYS})
            return {
                "url": url, "status": meta["status"], "fetched_at": meta["fetched_at"],
                "parent": parent, "relation": relation, "page": page,
                "position": page * int(values["numItemsPerPage"]) + pos + 1,
                "json": {"activeFilters": {"other": values["activeFilters"]["other"]},
                         "numTotalItems": values["numTotalItems"],
                         "numItemsPerPage": values["numItemsPerPage"],
                         "pageIndex": values["pageIndex"], "models": shown},
                "parsed": {"parent_id": listing["parent_id"], "relation": listing["relation"],
                           "children": len(ids), "total": listing["total"],
                           "next_page": listing["next_page"]},
            }
    return None


def _row(conn, sql, *args):
    cur = conn.execute(sql, args)
    row = cur.fetchone()
    return dict(zip([d[0] for d in cur.description], row)) if row else None


def case(conn, label, model_id, blurb):
    url = f"{config.BASE_URL}/{model_id}"
    meta, text = cached(url)
    if meta is None:
        raise SystemExit(f"{model_id} is not in the cache")
    parsed = parse_model_page(text)
    raw = _row(conn, "SELECT * FROM models WHERE id = ?", model_id)
    cleaned = _row(conn, "SELECT * FROM clean_models WHERE id = ?", model_id)
    queue = _row(conn, "SELECT depth, root, rank FROM crawl_queue WHERE model_id = ? "
                       "ORDER BY depth LIMIT 1", model_id)
    edges = [dict(zip(("parent", "relation", "in_tags", "in_listing", "temporal_anomaly",
                       "parent_created_at"), r))
             for r in conn.execute(
                 "SELECT e.parent_id, e.relation, e.in_tags, e.in_listing, e.temporal_anomaly, p.created_at "
                 "FROM clean_edges e LEFT JOIN clean_models p ON p.id = e.parent_id "
                 "WHERE e.child_id = ?", (model_id,))]
    issues = [list(r) for r in conn.execute(
        "SELECT issue, detail FROM quality_issues WHERE entity_id = ?", (model_id,))]
    parsed.pop("parse_errors", None)
    parsed["tags"] = _trim(parsed["tags"], 8)
    return {
        "label": label, "id": model_id, "blurb": blurb, "queue": queue,
        "discovery": discovery(conn, model_id),
        "page": {"url": url, "status": meta["status"], "fetched_at": meta["fetched_at"],
                 "bytes": meta["bytes"], "bytes_gz": meta["bytes_gz"], **page_excerpt(text, model_id)},
        "json": header_json(text),
        "parsed": parsed,
        "raw": {k: raw[k] for k in ("license", "pipeline_tag", "created_at", "card_base_model_json",
                                    "children_counts_json", "gated")},
        "clean": {k: cleaned[k] for k in ("license", "license_category", "pipeline_tag",
                                          "pipeline_tag_source", "created_month", "created_at_is_floor",
                                          "declared_bases_json", "hf_children_total", "depth", "root")},
        "edges": edges, "issues": issues,
    }


def export():
    # Work on an in-memory copy: the crawler may be writing to the live DB, and
    # cleaning takes about a second, so the demo always matches the cache.
    live = sqlite3.connect(config.DB_PATH.as_uri() + "?mode=ro", uri=True, timeout=60)
    conn = sqlite3.connect(":memory:")
    live.backup(conn)
    live.close()
    clean.run(conn)
    conn.row_factory = None
    return {
        "config": {"min_interval": config.MIN_REQUEST_INTERVAL, "max_depth": config.MAX_DEPTH,
                   "max_models": config.MAX_MODELS, "cap": config.MAX_CHILDREN_PER_RELATION,
                   "user_agent": config.USER_AGENT, "relations": list(config.RELATIONS),
                   "temporal_tolerance_days": clean.TEMPORAL_TOLERANCE_DAYS,
                   "created_at_floor": clean.CREATED_AT_FLOOR},
        "cases": [case(conn, *c) for c in CASES],
    }


def main():
    data = export()
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    OUT.write_text(f"window.DEMO={payload};\n", encoding="utf-8")
    print(f"{OUT}  ({OUT.stat().st_size / 1e3:.0f} KB, {len(data['cases'])} cases)")


if __name__ == "__main__":
    main()
