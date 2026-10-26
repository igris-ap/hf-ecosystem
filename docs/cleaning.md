# Preprocessing rules (`preprocess/clean.py`)

The raw tables (`models`, `edges`, `crawl_queue`) are never modified. `clean.py` rebuilds
`clean_models`, `clean_edges` and `quality_issues` from scratch every run. That way a rule can be
changed and re-applied without re-crawling. Numbers below are from the 500-model test crawl
(2026-10-26).

## Rules

| What | Rule | Why |
|---|---|---|
| Edge set | union of tag edges (child's page) and listing edges (parent's listing), one row per (child, parent, relation) with `in_tags` / `in_listing` flags | the two sources see the same edge from opposite ends; agreement between them is a quality metric |
| Self-loops | dropped, logged as `self_loop` | a model can't derive from itself |
| Relation conflict | same child + parent with different relations → logged | the child's own tags are treated as authoritative |
| Declared `base_model` ids | normalised: URL prefix stripped (`https://huggingface.co/…`, `hf.co/…`), `/tree/main`, `/blob/…` and whitespace removed; local paths and free text dropped and logged | cards contain URLs, paths and typos (the brief's gotcha) |
| Renamed repos | **learned from the data**: if a card declares exactly one base HF didn't link and HF linked exactly one parent the card didn't declare, those two ids are the same repo. Conflicting evidence → no alias | repos get renamed (`meta-llama/Meta-Llama-3.1-8B` → `meta-llama/Llama-3.1-8B`); HF follows renames but old cards keep the old name |
| Broken parent links | declared bases that are neither linked by HF nor explained by a learned rename → `declared_base_not_linked` | typos, deleted/private repos, or renames we lack evidence for |
| Licenses | lower-cased HF id, then grouped: permissive / copyleft / noncommercial / restricted / other / unknown | drift analysis compares categories, not 30+ raw ids. `restricted` = model-specific licenses with use restrictions (Llama, Gemma, OpenRAIL…). `cc-by-nd` counts as restricted, because "no derivatives" forbids fine-tuning |
| Task (`pipeline_tag`) | if missing, inherited from the in-sample parent(s), but only when all parents agree; `pipeline_tag_source` = own / inherited / none | adapters and quantizations rarely set a task but do the parent's task. The flag keeps the imputation visible and reversible |
| Dates | ISO-8601 → UTC `YYYY-MM-DDTHH:MM:SSZ`, plus `created_month` | consistent grouping for trends |
| Created-at floor | `created_at < 2022-03-03` → `created_at_is_floor = 1` | HF has no creation dates before March 2022; older repos all show ~2022-03-02 (bert-base-uncased, from 2018). Trends must exclude or caveat these |
| Child older than parent | flagged when the child was created **> 7 days** before its parent (`temporal_anomaly`). Floor dates are never used as evidence | impossible for real lineage. Small gaps are normal: a base and its instruct version are uploaded minutes apart |
| Depth / family | from the crawl queue (shallowest depth wins) | needed for per-family and per-generation stats |

## What it found in the 500-model sample

| Issue | Count | Note |
|---|---|---|
| `missing_pipeline_tag` | 118 (23.6 %) | **all 118** could be inherited from a parent |
| `missing_license` | 94 (18.8 %) | |
| `declared_base_renamed` | 42 | e.g. `bert-base-uncased → google-bert/bert-base-uncased`, `cognitivecomputations/WestLake-7B-v2-laser → QuixiAI/WestLake-7B-v2-laser` |
| `declared_base_not_linked` | 34 | e.g. `meta-llama/Meta-Llama-3.1-8B-Instruct` (a rename, but no 1-to-1 evidence), `prajjwal1/bert-tiny` |
| `child_older_than_parent` | 5 | **all five claim `deepseek-ai/DeepSeek-R1` as base** but were created 26–326 days before R1 existed (e.g. `runningsnail13/snail`, 326 days). These are re-used repos or lineage spam |
| `created_at_floor` | 1 | `google-bert/bert-base-uncased` |
| self-loops, relation conflicts, malformed ids, listing edges not confirmed by tags | 0 each | |

**Listing vs tags agreement:** 492 / 492 listing edges whose child we scraped are confirmed by
the child's own tags. That's expected, because HF builds the listings from those same tags.

## Graph (`mining/graph.py`)

- Edge direction **child → parent**, so PageRank influence flows to base models.
- `build_graph(conn)` contains only scraped models. `include_external=True` adds every model an
  edge mentions (unscraped children, out-of-sample parents) as `in_sample=False` nodes with no
  metadata.
- **Cycles:** detected as strongly connected components (linear time). `break_cycles` removes,
  from each cycle, the edge whose parent is the newest model, since a model can't derive from
  something uploaded after it. The 500 sample has **no cycles**.
- Edges flagged `temporal_anomaly` stay in the graph with the flag set. Analyses can filter them.
