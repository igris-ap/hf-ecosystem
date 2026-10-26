"""Run every mining module and write the results for the report.

    python -m mining.report

Writes into results/ (small, committed to the repo):
    <table>.csv   every table, for charts (phase 6) and the notebook
    summary.md    all tables in one readable page, with run metadata
"""
import sqlite3
from datetime import datetime, timezone

import pandas as pd

import config
from mining import communities, licenses, lineage, quality, ranking, trends
from mining.graph import break_cycles, build_graph, describe, find_cycle_groups


def collect(conn):
    """Return [(section title, note, {table name: DataFrame})]."""
    sample = build_graph(conn)
    full = build_graph(conn, include_external=True)
    for G in (sample, full):
        if find_cycle_groups(G):        # brief: detect and log cycles before ranking
            break_cycles(G)

    graph_stats = pd.DataFrame({"sample graph": describe(sample), "all known edges": describe(full)})
    graph_stats.index.name = "statistic"

    comm_sample = communities.detect(sample)
    edges = licenses.edge_table(sample)
    depth = lineage.depth_summary(sample)

    return [
        ("Graph", "Sample graph = scraped models only. 'All known edges' also includes unscraped "
         "children (from listings) and out-of-sample parents.",
         {"graph_stats": graph_stats.reset_index().astype(str)}),
        ("1. Influence ranking",
         "Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. "
         "Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children "
         "per relation, and the weighting adds the skipped ones back using HF's real child "
         "counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.",
         {"ranking_verification_sample": ranking.compare_with_networkx(sample),
          "ranking_verification_all_edges": ranking.compare_with_networkx(full),
          "ranking_top20": ranking.ranking_table(full).reset_index(),
          "ranking_top20_sample_graph": ranking.ranking_table(sample).reset_index(),
          "ranking_top_hubs": ranking.top_hubs(full)}),
        ("2. Model families (Louvain, sample graph)", str(communities.summary(sample, comm_sample)),
         {"communities": communities.community_table(sample, comm_sample),
          "cross_family_links": communities.cross_family_links(sample)}),
        ("3. Lineage", f"max generation {depth['max_generation']}, mean generation of derived models "
         f"{depth['mean_generation_of_derived']:.2f}, models per generation {depth['models_per_generation']}. "
         "Branching uses HF's exact child counts; relation share compares population vs sample.",
         {"lineage_generations": lineage.generation_table(sample),
          "lineage_relation_shares": lineage.relation_shares(sample)}),
        ("4. License drift", "Edges with both ends scraped. 'loosened' = child's license is less "
         "restrictive than its parent's: a likely conflict.",
         {"license_outcomes": edges["outcome"].value_counts().rename_axis("outcome").reset_index(),
          "license_transitions": licenses.transition_matrix(edges).reset_index(),
          "license_by_family": licenses.by_group(edges, "family"),
          "license_by_relation": licenses.by_group(edges, "relation"),
          "license_conflicts": licenses.conflicts(edges)[
              ["child", "parent", "relation", "family", "child_license", "parent_license"]]}),
        ("5. Trends", "Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. "
         "The sample favours well-downloaded models, so recent quarters are under-counted. "
         "Compare shares, not totals.",
         {name: t.reset_index() for name, t in trends.report_tables(sample).items()}),
        ("6. Data quality", "", {"data_quality": quality.quality_table(conn)}),
    ]


def to_markdown(df, max_rows=40):
    """Minimal DataFrame -> GitHub table (avoids an extra dependency)."""
    def fmt(v):
        if isinstance(v, float):
            return "" if pd.isna(v) else f"{v:.4g}"
        return "" if v is None else str(v).replace("|", "\\|")
    shown = df.head(max_rows)
    lines = ["| " + " | ".join(map(str, df.columns)) + " |",
             "|" + "---|" * len(df.columns)]
    lines += ["| " + " | ".join(fmt(v) for v in row) + " |" for row in shown.itertuples(index=False)]
    if len(df) > max_rows:
        lines.append(f"\n*… {len(df) - max_rows} more rows in the CSV*")
    return "\n".join(lines)


def main():
    conn = sqlite3.connect(config.DB_PATH)
    out = config.RESULTS_DIR
    out.mkdir(exist_ok=True)
    sections = collect(conn)

    n, first, last = conn.execute("SELECT COUNT(*), MIN(scraped_at), MAX(scraped_at) FROM clean_models").fetchone()
    md = ["# Mining results", "",
          f"Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC from {n} scraped models "
          f"(scraped {first[:10]} to {last[:10]}; download counts are a snapshot of that time).", ""]
    for title, note, tables in sections:
        md += [f"## {title}", "", note, ""] if note else [f"## {title}", ""]
        for name, df in tables.items():
            df.to_csv(out / f"{name}.csv", index=False)
            md += [f"**{name}**", "", to_markdown(df), ""]
    (out / "summary.md").write_text("\n".join(md), encoding="utf-8")
    print(f"wrote {sum(len(t) for _, _, t in sections)} tables to {out}")


if __name__ == "__main__":
    main()
