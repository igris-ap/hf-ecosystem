"""Data-quality metrics (mining task 6) as one table.

Pulls together what the crawler and preprocess.clean recorded, plus the
API spot-check result if validate/api_spotcheck.py has been run.
"""
import sqlite3

import pandas as pd

import config


def quality_table(conn):
    conn.row_factory = None
    one = lambda sql, *params: conn.execute(sql, params).fetchone()[0]
    issue = lambda name: one("SELECT COUNT(*) FROM quality_issues WHERE issue = ?", name)
    pct = lambda part, whole: f"{100 * part / whole:.1f} %" if whole else "n/a"

    n = one("SELECT COUNT(*) FROM clean_models")
    queued = one("SELECT COUNT(*) FROM crawl_queue")
    failed = one("SELECT COUNT(*) FROM crawl_queue WHERE status = 'failed'")
    parse_err = one("SELECT COUNT(DISTINCT entity_id) FROM quality_issues WHERE issue = 'parse_error'")
    declared = one("SELECT COALESCE(SUM(json_array_length(declared_bases_json)), 0) FROM clean_models")
    renamed, not_linked = issue("declared_base_renamed"), issue("declared_base_not_linked")
    listing_checked = one("SELECT COUNT(*) FROM clean_edges WHERE in_listing AND child_in_sample")
    listing_confirmed = one("SELECT COUNT(*) FROM clean_edges WHERE in_listing AND child_in_sample AND in_tags")
    tags_edges = one("SELECT COUNT(*) FROM clean_edges WHERE in_tags")
    tags_outside = one("SELECT COUNT(*) FROM clean_edges WHERE in_tags AND NOT parent_in_sample")
    inherited = one("SELECT COUNT(*) FROM clean_models WHERE pipeline_tag_source = 'inherited'")

    def missing(column):
        k = one(f"SELECT COUNT(*) FROM models WHERE {column} IS NULL")
        return k, pct(k, n)

    rows = [
        ("models scraped", n, f"of {queued} queued"),
        ("crawl failures", failed, pct(failed, queued)),
        ("models with a parse error", parse_err, pct(parse_err, n)),
        ("missing license", *missing("license")),
        ("missing pipeline_tag (as published)", *missing("pipeline_tag")),
        ("  of which filled from parent", inherited, "see pipeline_tag_source"),
        ("missing library_name", *missing("library_name")),
        ("missing created_at", *missing("created_at")),
        ("created_at is HF's pre-2022 placeholder", issue("created_at_floor"), "excluded from trends"),
        ("declared base_model values", declared, ""),
        ("  linked by HF", declared - renamed - not_linked, pct(declared - renamed - not_linked, declared)),
        ("  old name of a renamed repo", renamed, pct(renamed, declared)),
        ("  not linked (broken parent link)", not_linked, pct(not_linked, declared)),
        ("  malformed (URL/path/free text)", issue("declared_base_malformed"), ""),
        ("listing edges confirmed by child's tags", listing_confirmed,
         f"{pct(listing_confirmed, listing_checked)} of {listing_checked}"),
        ("tag edges to a parent outside the sample", tags_outside, pct(tags_outside, tags_edges)),
        ("child created >7 days before its parent", issue("child_older_than_parent"), "temporal anomaly"),
        ("self-loops", issue("self_loop"), ""),
        ("relation conflicts (tags vs listing)", issue("relation_conflict"), ""),
        _spotcheck_row(),
    ]
    return pd.DataFrame(rows, columns=["metric", "value", "detail"])


def _spotcheck_row():
    """Summarise results/api_spotcheck.csv (written by validate/api_spotcheck.py)."""
    path = config.RESULTS_DIR / "api_spotcheck.csv"
    if not path.exists():
        return ("API spot-check accuracy", "not run", "python -m validate.api_spotcheck")
    df = pd.read_csv(path)
    worst = df.loc[df["accuracy"].idxmin()]
    models = int(df["compared"].max())
    lowest = ("every field 100 %" if worst["accuracy"] == 1
              else f"lowest field: {worst['field']} {worst['accuracy']:.0%}")
    return ("API spot-check accuracy", f"{df['matches'].sum() / df['compared'].sum():.1%}",
            f"{models} random models x {len(df)} fields; {lowest}")


if __name__ == "__main__":
    print(quality_table(sqlite3.connect(config.DB_PATH)).to_string(index=False))
