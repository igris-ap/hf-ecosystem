"""Static charts for the report (PNG).

    python -m viz.charts            # writes results/figures/*.png

Every chart is drawn from the same mining functions that write results/*.csv,
so each figure has a table view with the exact numbers behind it.

Style: thin bars, 2 px lines, hairline gridlines, text in ink colours (never in
series colours), legends whenever there are 2+ series, labels only where they
help. Colours come from viz/palette.py in a fixed order.
"""
import sqlite3

import matplotlib

matplotlib.use("Agg")                      # no window: render straight to files
import matplotlib.pyplot as plt            # noqa: E402
import pandas as pd                        # noqa: E402

import config                              # noqa: E402
from mining import licenses, lineage, ranking, trends   # noqa: E402
from mining.graph import build_graph       # noqa: E402
from viz.palette import (AXIS, GRID, INK, INK_2, MUTED, RELATION_COLOUR, SLOTS,  # noqa: E402
                         SURFACE, short_name)

FIG_DIR = config.RESULTS_DIR / "figures"
DPI = 200

plt.rcParams.update({
    "font.family": ["Segoe UI", "DejaVu Sans"],
    "font.size": 9,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": AXIS, "axes.labelcolor": INK_2, "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": INK_2, "text.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "legend.frameon": False,
})


def _title(ax, title, subtitle=None):
    ax.set_title(title, loc="left", fontsize=11, fontweight="semibold", pad=22 if subtitle else 8)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, fontsize=8.5, color=INK_2, va="bottom")


def _hbar_axes(ax):
    """Horizontal bars: gridlines only along the value axis, no left spine."""
    ax.grid(axis="y", visible=False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)


def _save(fig, name):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / f"{name}.png"
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return path


# ---- 1. ranking ----------------------------------------------------------------------

def ranking_chart(full_graph):
    df = ranking.ranking_table(full_graph, n=20).iloc[::-1]       # biggest at the top
    fig, ax = plt.subplots(figsize=(7.5, 6.2))
    y = range(len(df))
    ax.barh(y, df["weighted_pagerank"], height=0.62, color=SLOTS[0])
    labels = [f"{short_name(m)}" for m in df["model"]]
    ax.set_yticks(list(y), labels)
    for yi, (score, plain) in enumerate(zip(df["weighted_pagerank"], df["plain_pagerank_rank"])):
        ax.text(score, yi, f"  {score:.3f}  (plain #{plain})", va="center", fontsize=7.5, color=INK_2)
    ax.set_xlim(0, df["weighted_pagerank"].max() * 1.35)
    ax.set_xlabel("weighted PageRank")
    _hbar_axes(ax)
    _title(ax, "Most influential models (top 20)",
           "Weighted PageRank: children the crawl cap skipped are added back with HF's real counts.")
    return _save(fig, "ranking_top20")


# ---- 2. family sizes ---------------------------------------------------------------

def family_size_chart(sample_graph):
    """Direct derivatives of each seed by relation type: HF's exact counts."""
    rows = []
    for node, a in sample_graph.nodes(data=True):
        if a.get("depth") == 0:
            rows.append({"seed": node, **{r: (a.get("hf_children") or {}).get(r) or 0 for r in RELATION_COLOUR}})
    df = pd.DataFrame(rows).set_index("seed")
    df = df.loc[df.sum(axis=1).sort_values().index]
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    left = pd.Series(0, index=df.index)
    for relation, colour in RELATION_COLOUR.items():
        # surface-coloured edge = the 2 px gap between stacked segments
        ax.barh([short_name(s) for s in df.index], df[relation], left=left, height=0.62,
                color=colour, edgecolor=SURFACE, linewidth=1.2, label=relation)
        left += df[relation]
    for yi, total in enumerate(left):
        ax.text(total, yi, f"  {total:,}", va="center", fontsize=8, color=INK_2)
    ax.set_xlim(0, left.max() * 1.12)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v / 1000:g}K" if v else "0"))
    ax.set_xlabel("direct derivatives on Hugging Face")
    ax.legend(ncol=4, loc="lower left", bbox_to_anchor=(0, 1.0), fontsize=8, handlelength=1, borderaxespad=0.2)
    _hbar_axes(ax)
    _title(ax, "How many models build directly on each base", None)
    ax.set_title(ax.get_title(loc="left"), loc="left", fontsize=11, fontweight="semibold", pad=26)
    return _save(fig, "family_sizes")


# ---- 3. relation share: population vs sample -----------------------------------------------

def relation_share_chart(sample_graph):
    df = lineage.relation_shares(sample_graph).set_index("relation")
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    y = list(range(len(df)))[::-1]
    h = 0.32
    ax.barh([v + h / 2 + 0.02 for v in y], df["population_share"], height=h, color=SLOTS[0],
            label="all direct children on HF (exact)")
    ax.barh([v - h / 2 - 0.02 for v in y], df["sample_share"], height=h, color=SLOTS[1],
            label="our crawl sample")
    for v, (p, s) in zip(y, zip(df["population_share"], df["sample_share"])):
        ax.text(p, v + h / 2 + 0.02, f" {p:.0%}", va="center", fontsize=8, color=INK_2)
        ax.text(s, v - h / 2 - 0.02, f" {s:.0%}", va="center", fontsize=8, color=INK_2)
    ax.set_yticks(y, df.index)
    ax.set_xlim(0, 0.62)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.legend(loc="lower right", fontsize=8)
    _hbar_axes(ax)
    _title(ax, "Relation types: the population vs our sample",
           "The crawler gives each relation an equal turn, so merges and quantizations are over-represented.")
    return _save(fig, "relation_share")


# ---- 4. license drift ----------------------------------------------------------------

_DRIFT_GROUPS = {          # outcome -> displayed group, in slot order
    "same": "same license",
    "loosened": "likely conflict (less restrictive)",
    "changed_same_category": "changed", "changed_custom": "changed", "tightened": "changed",
    "child_unknown": "no license",
}


def license_drift_chart(sample_graph):
    edges = licenses.edge_table(sample_graph)
    edges = edges[edges["outcome"] != "parent_unknown"].copy()
    edges["group"] = edges["outcome"].map(_DRIFT_GROUPS)
    groups = list(dict.fromkeys(_DRIFT_GROUPS.values()))
    counts = pd.crosstab(edges["family"], edges["group"]).reindex(columns=groups, fill_value=0)
    shares = counts.div(counts.sum(axis=1), axis=0)
    shares = shares.loc[shares["likely conflict (less restrictive)"].sort_values().index]

    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    left = pd.Series(0.0, index=shares.index)
    names = [short_name(f) for f in shares.index]
    for colour, group in zip(SLOTS, groups):
        ax.barh(names, shares[group], left=left, height=0.62, color=colour,
                edgecolor=SURFACE, linewidth=1.2, label=group)
        left += shares[group]
    for yi, family in enumerate(shares.index):
        n = counts.loc[family, "likely conflict (less restrictive)"]
        ax.text(1.01, yi, f"{n} conflict{'s' if n != 1 else ''}" if n else "none", va="center",
                fontsize=8, color=INK if n else MUTED, transform=ax.get_yaxis_transform())
    ax.set_xlim(0, 1)
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("share of the family's parent-child edges")
    ax.legend(ncol=2, loc="lower left", bbox_to_anchor=(0, 1.0), fontsize=8, handlelength=1, borderaxespad=0.2)
    _hbar_axes(ax)
    ax.set_title("Does a derivative keep its parent's license?", loc="left", fontsize=11,
                 fontweight="semibold", pad=40)
    return _save(fig, "license_drift")


# ---- 5. trends -------------------------------------------------------------------------

MIN_PER_QUARTER = 10      # thinner quarters make shares meaningless


def relation_trend_chart(sample_graph):
    table = trends.report_tables(sample_graph)["trend_relation_quarterly"]
    table = table[table.sum(axis=1) >= MIN_PER_QUARTER]
    share = trends.shares(table)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    x = list(range(len(share)))
    for relation, colour in RELATION_COLOUR.items():
        if relation not in share:
            continue
        ax.plot(x, share[relation], color=colour, linewidth=2, solid_capstyle="round", label=relation)
        ax.plot(x[-1], share[relation].iloc[-1], "o", color=colour, markersize=5,
                markeredgecolor=SURFACE, markeredgewidth=1.5)
        # direct end label, in ink (the dot beside it carries the colour)
        ax.text(x[-1] + 0.25, share[relation].iloc[-1], f"{relation} {share[relation].iloc[-1]:.0%}",
                va="center", fontsize=8, color=INK_2)
    ax.set_xlim(-0.3, x[-1] + 2.2)
    ax.set_xticks(x, share.index, rotation=45, ha="right")
    ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    ax.set_ylim(0, max(0.8, share.max().max() * 1.1))
    ax.grid(axis="x", visible=False)
    for xi, n in zip(x, table.sum(axis=1)):
        ax.text(xi, -0.02, f"n={n}", ha="center", va="top", fontsize=6.5, color=MUTED,
                transform=ax.get_xaxis_transform())
    ax.tick_params(axis="x", pad=12)
    ax.legend(ncol=4, loc="upper left", fontsize=8, handlelength=1.5)
    _title(ax, "Relation mix of new derivatives, by quarter",
           f"Share within each quarter; quarters with fewer than {MIN_PER_QUARTER} sampled models omitted.")
    return _save(fig, "trend_relation_share")


def family_trend_chart(sample_graph):
    """Small multiples: one panel per seed, the same y-scale everywhere."""
    table = trends.report_tables(sample_graph)["trend_family_quarterly"]
    seeds = list(table.sum().sort_values(ascending=False).index)
    cols = 5
    rows = -(-len(seeds) // cols)
    fig, axes = plt.subplots(rows, cols, figsize=(10, 2.3 * rows), sharex=True, sharey=True)
    x = list(range(len(table)))
    for ax, seed in zip(axes.flat, seeds):
        ax.bar(x, table[seed], width=0.7, color=SLOTS[0])
        ax.set_title(short_name(seed), loc="left", fontsize=8.5, fontweight="semibold", pad=4)
        ax.grid(axis="x", visible=False)
    for ax in axes.flat[len(seeds):]:
        ax.set_visible(False)
    step = max(1, len(x) // 4)
    for ax in axes[-1]:
        ax.set_xticks(x[::step], [table.index[i] for i in x[::step]], rotation=45, ha="right", fontsize=7)
    fig.suptitle("New sampled derivatives per quarter, by base model", x=0.06, y=1.0, ha="left",
                 fontsize=11, fontweight="semibold")
    fig.text(0.06, 0.925, "Each family's release wave. The sample takes the most-downloaded children, "
             "so recent quarters are under-counted.", fontsize=8.5, color=INK_2)
    fig.subplots_adjust(top=0.82, hspace=0.45)
    return _save(fig, "trend_by_family")


def main():
    conn = sqlite3.connect(config.DB_PATH)
    sample = build_graph(conn)
    full = build_graph(conn, include_external=True)
    paths = [ranking_chart(full), family_size_chart(sample), relation_share_chart(sample),
             license_drift_chart(sample), relation_trend_chart(sample), family_trend_chart(sample)]
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
