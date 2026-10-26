"""Time trends by creation date: per family, per task, per relation type.

    python -m mining.trends

Counted over scraped *derivatives* (seeds excluded), grouped by the quarter
they were created in. Quarters rather than months, because a 500-model sample
spread over ~3 years is too thin per month (the full crawl can use months).

Two caveats, which belong in the report next to every trend chart:
  - Repos older than March 2022 all carry HF's placeholder date
    (created_at_is_floor) and are excluded, as are models created long before
    every parent they claim (temporal anomalies, e.g. repos re-labelled as
    DeepSeek-R1 fine-tunes months before R1 existed).
  - The crawl takes the most-downloaded children first, so the sample leans
    towards models that have had time to collect downloads. Recent quarters,
    especially the current one, are under-counted. Read shares, not totals.
"""
import sqlite3

import pandas as pd

import config
from mining.graph import build_graph


def derivatives(G):
    """One row per scraped derivative with the fields the trends need."""
    rows = []
    for node, a in G.nodes(data=True):
        if not a.get("in_sample") or not a.get("depth") or a.get("created_at_is_floor"):
            continue
        if not a.get("created_at"):
            continue
        parent_edges = list(G.out_edges(node, data=True))
        # A model created long before every parent it claims (preprocess.clean's
        # temporal_anomaly) isn't really a derivative from that period; skip it.
        if parent_edges and all(d["temporal_anomaly"] for _, _, d in parent_edges):
            continue
        relations = {d["relation"] for _, _, d in parent_edges}
        year, month = int(a["created_at"][:4]), int(a["created_at"][5:7])
        rows.append({
            "model": node,
            "quarter": f"{year}-Q{(month - 1) // 3 + 1}",
            "family": a.get("root"),
            "task": a.get("pipeline_tag") or "unknown",
            # a model's relation to its parent(s); merges have several parents, same label
            "relation": relations.pop() if len(relations) == 1 else ("none" if not relations else "mixed"),
        })
    return pd.DataFrame(rows, columns=["model", "quarter", "family", "task", "relation"])


def per_quarter(df, column, top=None):
    """Quarter x category counts. top=N keeps the N biggest categories, rest -> 'other'."""
    values = df[column]
    if top:
        keep = values.value_counts().nlargest(top).index
        values = values.where(values.isin(keep), "other")
    table = pd.crosstab(df["quarter"], values).sort_index()
    table.columns.name = None
    return table


def shares(table):
    """Row-normalise: each quarter's mix, summing to 1."""
    return table.div(table.sum(axis=1), axis=0)


def report_tables(G):
    df = derivatives(G)
    by_relation = per_quarter(df, "relation")
    return {
        "trend_family_quarterly": per_quarter(df, "family"),
        "trend_task_quarterly": per_quarter(df, "task", top=6),
        "trend_relation_quarterly": by_relation,
        "trend_relation_share_quarterly": shares(by_relation).round(3),
    }


def main():
    conn = sqlite3.connect(config.DB_PATH)
    pd.set_option("display.width", 220)
    for name, table in report_tables(build_graph(conn)).items():
        print(f"== {name}")
        print(table.to_string())


if __name__ == "__main__":
    main()
