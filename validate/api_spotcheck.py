"""Spot-check scraped records against the official Hugging Face API.

    python -m validate.api_spotcheck            # 50 random models
    python -m validate.api_spotcheck --n 100

The ONLY place the project touches the API (collection is pure scraping; see
docs/ethics.md). It answers: "does what we scraped from HTML match what HF
itself reports?" For a random sample of scraped models, it fetches
https://huggingface.co/api/models/<id> (through the same polite, cached
Fetcher) and compares field by field.

Exact fields must match exactly. Downloads and likes change between our crawl
and this check, so they count as a match within a tolerance. Tags can gain or
lose entries over time, so we report exact match plus average overlap.

What a pass does and doesn't show: the model page embeds data from the same
backend as the API, so a match shows that our *parsers* extract exactly what
HF serves (no lost or garbled fields). It can't show that HF's metadata is
itself correct (e.g. a wrong declared base_model); preprocess.clean checks that.

Writes results/api_spotcheck.csv (accuracy per field) and
results/api_spotcheck_mismatches.csv (every disagreement, for inspection).
"""
import argparse
import json
import random
import sqlite3
import statistics

import pandas as pd

import config
from config import BASE_URL, RELATIONS
from crawler.fetch import Fetcher
from crawler.parse_model import parents_from_tags
from preprocess.clean import normalise_timestamp

SEED = 7                  # fixed, so the sample is reproducible
COUNT_TOLERANCE = 0.10    # downloads/likes within 10 % count as a match


def scraped_records(conn, n, seed=SEED):
    """n random scraped models, with raw (pre-cleaning) values where it matters."""
    conn.row_factory = sqlite3.Row
    ids = sorted(r[0] for r in conn.execute("SELECT id FROM models"))
    sample = random.Random(seed).sample(ids, min(n, len(ids)))
    records = {}
    for mid in sample:
        m = dict(conn.execute("SELECT * FROM models WHERE id = ?", (mid,)).fetchone())
        m["parents"] = {(p, r) for p, r in conn.execute(
            "SELECT parent_id, relation FROM edges WHERE child_id = ? AND source = 'tags'", (mid,))}
        records[mid] = m
    return records


def api_view(api):
    """Reduce an API JSON record to the fields we compare, in our formats."""
    card = api.get("cardData") or {}
    tags = api.get("tags") or []
    license_tag = next((t.split(":", 1)[1] for t in tags if t.startswith("license:")), None)
    gated = api.get("gated", False)
    return {
        "id": api.get("id"),
        "author": api.get("author"),
        "license": card.get("license") or license_tag,
        "pipeline_tag": api.get("pipeline_tag"),
        "library_name": api.get("library_name"),
        "created_at": normalise_timestamp(api.get("createdAt")),
        "gated": "no" if gated is False else gated,
        "parents": {(p, r) for p, r in parents_from_tags(tags) if r in RELATIONS or r == "unknown"},
        "tags": set(tags),
        "downloads": api.get("downloads"),
        "likes": api.get("likes"),
    }


def compare(ours, theirs):
    """Return {field: (match, our value, api value)} for one model."""
    def close(a, b):
        if a is None or b is None:
            return a == b
        return abs(a - b) <= COUNT_TOLERANCE * max(a, b, 1)

    our_tags = set(json.loads(ours["tags_json"] or "[]"))
    return {
        "id": (ours["id"] == theirs["id"], ours["id"], theirs["id"]),
        "author": (ours["author"] == theirs["author"], ours["author"], theirs["author"]),
        "license": (ours["license"] == theirs["license"], ours["license"], theirs["license"]),
        "pipeline_tag": (ours["pipeline_tag"] == theirs["pipeline_tag"], ours["pipeline_tag"], theirs["pipeline_tag"]),
        "library_name": (ours["library_name"] == theirs["library_name"], ours["library_name"], theirs["library_name"]),
        "created_at": (normalise_timestamp(ours["created_at"]) == theirs["created_at"],
                       ours["created_at"], theirs["created_at"]),
        "gated": (ours["gated"] == theirs["gated"], ours["gated"], theirs["gated"]),
        "parents (edges)": (ours["parents"] == theirs["parents"], sorted(ours["parents"]), sorted(theirs["parents"])),
        "tags (exact set)": (our_tags == theirs["tags"], len(our_tags), len(theirs["tags"])),
        "downloads (within 10 %)": (close(ours["downloads"], theirs["downloads"]), ours["downloads"], theirs["downloads"]),
        "likes (within 10 %)": (close(ours["likes"], theirs["likes"]), ours["likes"], theirs["likes"]),
    }, _jaccard(our_tags, theirs["tags"])


def _jaccard(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0


def run(conn, fetcher, n):
    records = scraped_records(conn, n)
    per_field, mismatches, overlaps, failed = {}, [], [], []
    for mid, ours in records.items():
        result = fetcher.get(f"{BASE_URL}/api/models/{mid}")
        if not result.ok:
            failed.append((mid, result.status))
            continue
        fields, overlap = compare(ours, api_view(json.loads(result.text)))
        overlaps.append(overlap)
        for field, (match, mine, theirs) in fields.items():
            per_field.setdefault(field, []).append(match)
            if not match:
                mismatches.append({"model": mid, "field": field, "scraped": str(mine), "api": str(theirs)})

    summary = pd.DataFrame([
        {"field": f, "compared": len(v), "matches": sum(v), "accuracy": sum(v) / len(v)}
        for f, v in per_field.items()])
    meta = {"sampled": len(records), "api_failures": failed,
            "mean_tag_overlap": statistics.mean(overlaps) if overlaps else None}
    return summary, pd.DataFrame(mismatches, columns=["model", "field", "scraped", "api"]), meta


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--n", type=int, default=50)
    args = parser.parse_args(argv)
    conn = sqlite3.connect(config.DB_PATH)
    summary, mismatches, meta = run(conn, Fetcher(), args.n)
    config.RESULTS_DIR.mkdir(exist_ok=True)
    summary.to_csv(config.RESULTS_DIR / "api_spotcheck.csv", index=False)
    mismatches.to_csv(config.RESULTS_DIR / "api_spotcheck_mismatches.csv", index=False)
    pd.set_option("display.width", 200)
    print(summary.to_string(index=False))
    print(meta)
    if len(mismatches):
        print(mismatches.to_string(index=False))


if __name__ == "__main__":
    main()
