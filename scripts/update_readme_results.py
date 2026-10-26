"""Regenerate the README's "Results" section from results/*.csv.

    python scripts/update_readme_results.py --done 5000 --target 20000
    python scripts/update_readme_results.py --done 20000 --target 20000 --final

Every number in the section is read from the result tables, never typed by
hand, so the README can't drift from the data. The section sits between
<!-- RESULTS:START --> and <!-- RESULTS:END --> (or replaces the one-line
<!-- RESULTS --> placeholder the first time).
"""
import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config  # noqa: E402
from viz.palette import short_name  # noqa: E402

R = config.RESULTS_DIR
README = config.ROOT / "README.md"
START, END = "<!-- RESULTS:START -->", "<!-- RESULTS:END -->"


def _csv(name):
    return pd.read_csv(R / f"{name}.csv")


def _pct(x):
    return f"{100 * x:.0f} %"


def _quality(metric):
    q = _csv("data_quality").set_index("metric")
    row = q.loc[metric]
    return row["value"], row["detail"]


def build_section(done, target, final):
    stats = _csv("graph_stats").set_index("statistic")
    rank = _csv("ranking_top20")
    shares = _csv("lineage_relation_shares").set_index("relation")
    gens = _csv("lineage_generations").set_index("generation")
    comms = _csv("communities")
    cross = _csv("cross_family_links")
    by_family = _csv("license_by_family")
    outcomes = _csv("license_outcomes").set_index("outcome")["count"]
    trend_n = _csv("trend_relation_quarterly").set_index("quarter")

    sampled = comms[comms["in_sample"] > 0]
    purity = (sampled["purity"] * sampled["in_sample"]).sum() / sampled["in_sample"].sum()
    conflicts = int(outcomes.get("loosened", 0))
    no_license_children = int(outcomes.get("child_unknown", 0))
    edges_compared = int(outcomes.sum())
    worst = by_family[by_family["loosened"] > 0].sort_values("conflict_rate", ascending=False).head(3)
    missing_license, _ = _quality("missing license")
    broken, broken_detail = _quality("  not linked (broken parent link)")
    spot, spot_detail = _quality("API spot-check accuracy")
    g1 = gens.loc[1] if 1 in gens.index else None

    stamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    if final:
        status = f"**Final results:** {done:,} models scraped (crawl finished {stamp})."
    else:
        status = (f"**Snapshot of a crawl in progress:** {done:,} of {target:,} models scraped "
                  f"(updated {stamp}). This section is regenerated every 1,000 models.")

    lines = [START, "", "## Results", "", f"> {status}", ""]

    lines += ["### At a glance", "", "| | |", "|---|---|",
              f"| Models scraped | {int(stats.loc['nodes_in_sample', 'sample graph']):,} |",
              f"| Models seen in total (incl. unscraped children and parents) | "
              f"{int(stats.loc['nodes', 'all known edges']):,} |",
              f"| Lineage edges | {int(stats.loc['edges', 'all known edges']):,} |",
              f"| Model families found (Louvain) | {len(comms):,}, matching the seed families "
              f"with {_pct(purity)} purity |",
              f"| Deepest derivation chain | {int(gens.index.max())} generations |",
              f"| Likely license conflicts | {conflicts:,} of {edges_compared:,} parent-child pairs |",
              f"| Scraped models with no license | {missing_license} ({_quality('missing license')[1]}) |",
              f"| Broken parent links in model cards | {broken} ({broken_detail}) |",
              f"| API spot-check | {spot} match ({spot_detail}) |",
              ""]

    lines += ["### Most influential models", "",
              "Weighted PageRank over all known lineage edges (see *Why a weighted PageRank*, below). "
              "*Plain rank* is the position before correcting for the crawl cap.", "",
              "| # | Model | Weighted PageRank | Plain rank | Direct children on HF | Seed family |",
              "|---|---|---|---|---|---|"]
    for _, r in rank.head(10).iterrows():
        kids = "–" if pd.isna(r["hf_children_total"]) else f"{int(r['hf_children_total']):,}"
        fam = short_name(r["family"]) if isinstance(r["family"], str) else "–"
        lines.append(f"| {r['rank']} | `{r['model']}` | {r['weighted_pagerank']:.4f} | "
                     f"{r['plain_pagerank_rank']} | {kids} | {fam} |")
    lines.append("")

    findings = []
    findings.append(
        "**What derivatives are made of.** Across the direct children Hugging Face lists for every "
        "scraped model: " + ", ".join(
            f"{label} {_pct(shares.loc[rel, 'population_share'])}" for rel, label in
            [("finetune", "fine-tunes"), ("adapter", "adapters"), ("quantized", "quantizations"),
             ("merge", "merges")] if rel in shares.index)
        + ". The crawl sample is deliberately balanced, so it shows each at roughly "
        + _pct(shares["sample_share"].mean()) + " instead.")
    if g1 is not None:
        findings.append(
            f"**Most derivatives are dead ends.** Of {int(g1['models']):,} first-generation "
            f"derivatives, {_pct(1 - g1['share_with_children'])} have no children of their own. "
            f"The median is {g1['branching_median']:.0f} children, but the mean is "
            f"{g1['branching_mean']:.0f}, pulled up by a few models that are major bases themselves "
            f"(up to {int(g1['branching_max']):,} children).")
    if conflicts:
        worst_txt = ", ".join(f"{short_name(r['family'])} {_pct(r['conflict_rate'])}" for _, r in worst.iterrows())
        pairs = _csv("license_conflicts").groupby(["parent_license", "child_license"]).size()
        (top_parent, top_child), top_n = pairs.idxmax(), int(pairs.max())
        findings.append(
            f"**License drift.** {conflicts:,} derivatives carry a *less* restrictive license than "
            f"their parent. The most common case is a `{top_parent}` model republished as "
            f"`{top_child}` ({top_n:,} times). The highest conflict rates are {worst_txt}. Another "
            f"{no_license_children:,} derivatives declare no license at all.")
    merge_share = cross["relation"].eq("merge").mean() if len(cross) else 0
    findings.append(
        f"**Families mostly stay apart.** Louvain finds {len(comms):,} communities that match the "
        f"seed families with {_pct(purity)} purity. The exceptions are {len(cross):,} lineage links "
        f"between families, {_pct(merge_share)} of them merges.")
    recent = trend_n[trend_n.sum(axis=1) >= 10]
    if len(recent):
        q = recent.index[-1]
        mix = (recent.loc[q] / recent.loc[q].sum()).sort_values(ascending=False)
        findings.append(
            f"**Latest quarter ({q}, {int(recent.loc[q].sum())} sampled derivatives):** "
            + ", ".join(f"{rel} {_pct(v)}" for rel, v in mix.items()) + ".")
    lines += ["### Findings so far" if not final else "### Findings", ""]
    lines += [f"- {f}" for f in findings] + [""]

    lines += ["### Figures", "",
              "| | |", "|---|---|",
              "| ![Top models by weighted PageRank](results/figures/ranking_top20.png) | "
              "![Derivatives per base model](results/figures/family_sizes.png) |",
              "| ![License drift by family](results/figures/license_drift.png) | "
              "![Relation types: population vs sample](results/figures/relation_share.png) |",
              "| ![Relation mix over time](results/figures/trend_relation_share.png) | "
              "![Release waves by family](results/figures/trend_by_family.png) |",
              "",
              "All tables: [`results/summary.md`](results/summary.md) (CSV files in [`results/`](results/)). "
              "Interactive family tree: download the repo and open `results/tree/family_tree.html` "
              "(GitHub shows HTML files as source).",
              "", END]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--done", type=int, required=True)
    ap.add_argument("--target", type=int, default=config.MAX_MODELS)
    ap.add_argument("--final", action="store_true")
    args = ap.parse_args()

    section = build_section(args.done, args.target, args.final)
    text = README.read_text(encoding="utf-8")
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: section, text, flags=re.S)
    elif "<!-- RESULTS -->" in text:
        text = text.replace("<!-- RESULTS -->", section, 1)
    else:
        sys.exit("README has no results placeholder")
    README.write_text(text, encoding="utf-8")
    print(f"README results updated ({args.done:,} models)")


if __name__ == "__main__":
    main()
