"""Export the mining results for the explorer site's Findings tab (site/findings.js).

    python -m viz.site_findings [--final]

Reads results/*.csv (written by mining.report), so the page shows the same
numbers as the README and summary.md. The snapshot watcher runs it after every
report, which keeps the tab current while the crawl is running.
"""
import argparse
import json
from datetime import datetime, timezone

import pandas as pd

import config

R = config.RESULTS_DIR
OUT = config.ROOT / "site" / "findings.js"


def _csv(name):
    return pd.read_csv(R / f"{name}.csv")


def _records(df):
    # NaN -> None, so the JSON has nulls instead of invalid NaN tokens
    return json.loads(df.to_json(orient="records"))


def export(final=False):
    stats = _csv("graph_stats").set_index("statistic")
    comms = _csv("communities")
    sampled = comms[comms["in_sample"] > 0]
    quality = _csv("data_quality")
    outcomes = _csv("license_outcomes").set_index("outcome")["count"]
    conflicts = _csv("license_conflicts")
    pairs = (conflicts.groupby(["parent_license", "child_license"]).size()
             .sort_values(ascending=False).head(8))
    gens = _csv("lineage_generations")
    trend = _csv("trend_relation_share_quarterly")
    trend_n = _csv("trend_relation_quarterly").set_index("quarter")
    families = _csv("trend_family_quarterly").set_index("quarter")
    q = quality.set_index("metric")["value"]

    return {
        "generated": datetime.now(timezone.utc).isoformat(timespec="minutes"),
        "final": final,
        "target": config.MAX_MODELS,
        "glance": {
            "scraped": int(stats.loc["nodes_in_sample", "sample graph"]),
            "known": int(stats.loc["nodes", "all known edges"]),
            "edges": int(stats.loc["edges", "all known edges"]),
            "roots": int(stats.loc["roots", "all known edges"]),
            "multi_parent": int(stats.loc["multi_parent_nodes", "all known edges"]),
            "communities": len(comms),
            "purity": float((sampled["purity"] * sampled["in_sample"]).sum() / sampled["in_sample"].sum()),
            "max_generation": int(gens["generation"].max()),
            "pairs_compared": int(outcomes.sum()),
            "conflicts": int(outcomes.get("loosened", 0)),
            "child_unknown": int(outcomes.get("child_unknown", 0)),
            "missing_license": int(q["missing license"]),
            "broken_links": int(q["  not linked (broken parent link)"]),
            "declared_bases": int(q["declared base_model values"]),
            "temporal_anomalies": int(q["child created >7 days before its parent"]),
            "spotcheck": q["API spot-check accuracy"],
        },
        "ranking": _records(_csv("ranking_top20")[[
            "rank", "model", "weighted_pagerank", "pagerank", "plain_pagerank_rank",
            "hf_children_total", "derivatives_in_graph", "family", "license"]]),
        "verification": _records(_csv("ranking_verification_all_edges")),
        "relations": _records(_csv("lineage_relation_shares")),
        "generations": _records(gens[["generation", "models", "share_with_children",
                                      "branching_mean", "branching_median", "branching_max"]]),
        "license": {
            "outcomes": {k: int(v) for k, v in outcomes.items()},
            "by_family": _records(_csv("license_by_family")[[
                "family", "edges", "loosened", "child_unknown", "conflict_rate", "drift_rate"]]),
            "top_pairs": [[p, c, int(n)] for (p, c), n in pairs.items()],
        },
        "communities": _records(comms.head(15)[[
            "community", "size", "dominant_family", "purity", "most_derived_from",
            "rel_finetune", "rel_adapter", "rel_quantized", "rel_merge", "top_license_category"]]),
        "cross_family": _records(_csv("cross_family_links")),
        "trends": {
            "quarters": trend["quarter"].tolist(),
            "share": {c: trend[c].round(3).tolist() for c in ("finetune", "adapter", "quantized", "merge")},
            "counts": trend_n.sum(axis=1).astype(int).tolist(),
            "families": {f: families[f].astype(int).tolist() for f in families.columns},
            "family_quarters": families.index.tolist(),
        },
        "quality": _records(quality),
        "spotcheck": _records(_csv("api_spotcheck")),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--final", action="store_true", help="the crawl has finished")
    args = ap.parse_args()
    data = export(args.final)
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    OUT.write_text(f"window.FINDINGS={payload};\n", encoding="utf-8")
    print(f"{OUT}  ({OUT.stat().st_size / 1e3:.0f} KB)")


if __name__ == "__main__":
    main()
