# Mining: methods and findings

All numbers come from the **500-model test crawl** (10 seeds + 490 depth-1 derivatives,
2026-10-26). Every table is in [`results/`](../results/) and collected in
[`results/summary.md`](../results/summary.md). Re-run with `python -m mining.report` after any
crawl.

**Read the findings as provisional.** The machinery is verified, but the sample is shallow
(depth 1) and deliberately balanced (≈ 50 models per family, round-robin across relation types).
Everything marked ⚠ needs the full crawl before it goes in the report as a claim.

## Two graphs

| | nodes | edges | used for |
|---|---|---|---|
| sample graph | 500 | 529 | anything needing node metadata: licenses, trends, lineage, families |
| all known edges | 6 860 | 7 003 | ranking (adds unscraped children from listings + out-of-sample parents) |

Both are DAGs (0 cycles). Edges point **child → parent**.

## 1. Influence ranking (`ranking.py`)

**Method.** PageRank by power iteration (d = 0.85; dangling-node rank spread uniformly), a
cap-corrected weighted PageRank (below), and HITS by alternating updates with L1 normalisation.
All three are written by hand, with the math in the comment blocks above each function. They're
checked against `networkx.pagerank` (personalised for the weighted version) and `networkx.hits`.

**Verification:** max absolute difference ≤ 5 × 10⁻⁹, top-20 overlap 20/20, Spearman 1.000 on
both graphs. The one exception is HITS authority on the sample graph (18/20 overlap): ranks
11–20 there have scores around 10⁻⁶⁹, so their order is numerical noise. Tests include a
hand-solved 3-node case (PR = 1/4.7).

**The crawl cap distorts plain PageRank, so the reported ranking is a weighted one.**
Listings are capped at 300 per relation, so a seed's in-degree reaches at most 1 200. Plain
PageRank put Mistral #1 (≥ 195 children in *all four* relations) and BERT #8, although BERT has
the most real children (7 222, almost all fine-tunes). Ordinary edge weights can't fix this:
most models have one parent, so one edge gets 100 % of the rank whatever its weight. The cap
removes *sources* of rank, not the way rank is split.

**Weighted PageRank** therefore puts the missing children back. For each scraped parent and
relation, one virtual node stands for `HF count − sampled count` models and gets that many
nodes' share of the random jump. The formula and the argument are in the comment block in
`ranking.py`. It is exact if the unscraped children are leaves. A test checks this: one virtual
node standing for 8 leaves gives the same ranks as 8 real leaves. It matches networkx's
personalised PageRank to 2.4 × 10⁻¹⁰. 342 virtual nodes stand for 46 867 unscraped models.

**Findings (weighted, `ranking_top20.csv`).**
- **Llama-3.1-8B #1**, Qwen2.5-7B #2, **Llama-3.1-8B-Instruct #3**, BERT #4 (was #8), Mistral
  #5 (was #1).
- **Official instruct models are major bases in their own right:** Llama-3.1-8B-Instruct (7 302
  real children), Qwen2.5-7B-Instruct (6 669) and Qwen3-8B (5 133) jump from ranks 11–16 into
  the top 8. They pass rank on to their bases, which is why Llama-3.1-8B overtakes Mistral.
- `plain_pagerank_rank` stays in the table, so the effect of the correction is visible.
- **HITS concentrates on one model:** Mistral gets 0.95 of all authority. That's Kleinberg's
  "tightly-knit community" effect, driven by Mistral's many multi-parent merges (hubs). HITS has
  no random jump, so other families fall to ~0. This is the textbook reason PageRank is preferred
  here.
- **HITS can be unreliable on balanced data.** On the sample graph the eigengap σ₂/σ₁ = 0.996,
  because the fair sample makes all families almost the same size. So HITS needs ~2 650 rounds,
  and with an exact tie the answer would depend on the starting vector. `hits_eigengap()` reports
  this. On all known edges it's 0.94 (180 rounds).
- **Top hubs = Mistral-family merges** with many parents (`bartowski/Oumuamua-7b-instruct-v2-GGUF`
  has 15). These hubs are *why* HITS piles authority onto Mistral: hubs and authorities
  reinforce each other inside that one cluster.

## 2. Model families (`communities.py`)

**Method.** Louvain modularity maximisation (networkx, seed 42) on the undirected projection.
The detected communities are then compared with the seed family each model was crawled from.

**Findings (sample graph).** 10 communities, modularity 0.89, weighted purity 99.4 %. So the
detected communities match the seed families almost exactly. The two impure ones come from
**cross-family merges** (`cross_family_links.csv`): Optitransfer's Qwen + phi-2 merges, and
`Haker18/Llama-Gemma-Hybrid-9B` (a Gemma-family model that also lists Llama-3.1-8B). On all known
edges there are 17 communities: the 10 families plus small merge-centred clusters, e.g. around
`Llama-3.2-1B-Instruct`. ⚠ With depth-1 data, families ≈ seed stars by construction. The full
crawl is where Louvain gets interesting, e.g. sub-families such as "Llama-3.1-8B-Instruct and its
descendants".

## 3. Lineage (`lineage.py`)

**Method.** Generation = longest chain of derived-from links up to a parent-less model, computed
in one pass over a topological order. Branching factor uses **HF's exact Model-tree counts** per
scraped model, not our capped sample.

**Findings.**
- Max generation 3, even though the crawl is depth 1: merges of depth-1 models sit below them
  (generation 2–3, 33 models).
- **Branching is extremely skewed:** depth-1 derivatives have on average 68 children each, but
  the **median is 0**. 68 % have none at all, while a few (Llama-3.1-8B-Instruct: 7 302;
  Qwen2.5-7B-Instruct: 6 669) are bases in their own right. That's a heavy-tailed,
  preferential-attachment-like pattern.
- **Relation shares, population vs sample** (`lineage_relation_shares.csv`). This is the
  clearest picture of the sampling bias:

  | relation | population (HF counts) | our sample |
  |---|---|---|
  | finetune | **52.0 %** | 26.3 % |
  | adapter | 35.2 % | 25.5 % |
  | quantized | 9.6 % | 24.8 % |
  | merge | 3.1 % | 23.4 % |

  Use the population column for any "share of each relation type" claim.

## 4. License drift (`licenses.py`)

**Method.** For every edge with both ends scraped, compare child and parent license. Categories
are ordered by how much they restrict derivatives: permissive < copyleft < restricted <
noncommercial. A child *below* its parent = **loosened** = likely conflict. 'other' and 'unknown'
aren't ordered.

**Findings (529 edges).** 314 same license; 110 children with **no license at all**; 44
changed within a category; 27 involve a custom license; **19 likely conflicts**; 12 tightened.
- **All 19 conflicts are Llama or Gemma derivatives relicensed as Apache-2.0, MIT or CC-BY-4.0.**
  They include `microsoft/UserLM-8b` and `fdtn-ai/Foundation-Sec-8B` (both on Llama-3.1-8B), and
  several GGUF quantizations: a quantization changes the file format, not the license.
- Conflict rate by family: Llama-3.2-1B 21 %, Llama-3.1-8B 11 %, Gemma-3 8 %, Gemma-2 8 %,
  permissive families 0 % (by definition you can't loosen Apache/MIT).
- Merges have the most missing licenses (56 of 124).
- ⚠ A flag, not a legal judgement: the parent's license text decides.

## 5. Trends (`trends.py`)

**Method.** Scraped derivatives grouped by creation quarter. Excluded: pre-2022 placeholder
dates, and models created long before every parent they claim. The trend chart showed these as
"DeepSeek-R1 derivatives" in 2023–24, before R1 existed.

**Findings.** Each family's derivatives appear in a wave after its release: Mistral peaks in
2024-Q1, Llama-3.1 in 2024-Q3, DeepSeek-R1 in 2025-Q1, Qwen3 in 2025-Q2. Adapters' share of new
derivatives rises from 2025-Q3 (≈ 45–70 % per quarter, vs ≈ 15–30 % before). Image-text-to-text
appears from 2025-Q1 (Gemma-3).
⚠ Per-quarter counts are mostly < 30 and the sample is download-biased (older models had longer
to collect downloads), so "are quantized/merged models overtaking fine-tunes?" **can't be
answered from this sample**. The tables exist so the full crawl can answer it.

## 6. Data quality (`quality.py`)

See `data_quality.csv`. Headlines: 0 crawl failures, 0 parse errors. 18.8 % missing license,
23.6 % missing task (all filled from parents). Of 794 declared bases, 90.4 % are linked by HF,
5.3 % are old names of renamed repos, and 4.3 % are broken. Listing vs tags agree 100 %. 5 temporal
anomalies, all claiming DeepSeek-R1.

**API spot-check (`validate/api_spotcheck.py`): 50 random models × 11 fields, 100 % match.**
The fields are id, author, license, task, library, created date, gated, parent edges, the exact
tag set, downloads and likes. The comparison isn't vacuous: it covered 39 non-empty licenses, 44
tasks and 49 models with parent links, and a test confirms each field's mismatch is detected.
Downloads matched exactly because HF updates them about daily and the check ran ~1.5 h after the
crawl. What it shows: the parsers extract exactly what HF's backend serves. What it can't show:
whether HF's metadata is right (e.g. a wrong declared base). The page and the API share one
backend, which is what the cleaning checks are for.

**A gap in HF's own lineage:** `meta-llama/Llama-3.2-1B-Instruct` declares no `base_model`, so
it's in no listing and can't be reached from its base. Only 7 sampled merges point to it. The
other official instruct models checked (Llama-3.1, Qwen2.5, Gemma 2/3, Mistral) are linked
correctly.

## Visualisation (`viz/`)

**Static figures** (`results/figures/`, from `viz/charts.py`): top-20 ranking, family sizes by
relation, population-vs-sample relation shares, license drift by family, relation mix over time,
and per-family release waves (small multiples). Each is drawn from the same function as its CSV.

**Colour was validated, not eyeballed.** The palette was checked with a colour-vision validator
(protan/deutan simulation plus a normal-vision floor):
- **Bar, stack and line charts (≤ 4 colours): pass.** Aqua and yellow fall below 3:1 contrast
  on white, so those charts carry direct labels, and the CSVs serve as the table view.
- **Network graph with 7 family colours: fail.** Every pair of colours sits side by side, and
  blue vs violet is too close even with full colour vision. So the overview colours at most 3
  families and shows the rest in grey, told apart by shape, seed label and tooltip. Each family
  also has its own page.

**Interactive tree** (`results/tree/`, from `viz/family_tree.py`, pyvis):
- **Encoding:** node size = weighted PageRank; colour = family (max 3 highlighted); shape =
  family; edge dashes = relation; arrows point child → parent.
- **Responsiveness:** shows the top-N nodes, and physics turns off once the layout settles.
- **Offline:** self-contained. vis.js is inlined, and pyvis's Bootstrap CDN link is stripped.
- **Verified in a browser:** 300 nodes and 326 edges render, physics switches off, tooltips and
  edge styles are correct.

## Before the full crawl

1. Put a real contact email in `config.USER_AGENT`.
2. Consider adding `meta-llama/Llama-3.2-1B-Instruct` as an extra seed (see above), and check
   the other seeds' official instruct models the same way.
3. Budget: roughly a day at 3 s/request (see ethics.md). Re-run the same pipeline commands
   afterwards; every table, chart and tree page regenerates.
