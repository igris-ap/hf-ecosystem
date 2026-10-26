# Hugging Face Model Ecosystem Graph

Web Data Mining (R5CO4201T) mini project. We scrape public Hugging Face model pages, build the
model lineage graph (base model → fine-tunes, adapters, quantizations, merges), mine it, and
visualise it.

**Status:** All six phases are built and tested: robots.txt check, page-structure notes,
fetcher, parsers, resumable crawler, preprocessing, graph build, mining, visualisation and API
validation. Results so far are from the 500-model test crawl. See
[`results/summary.md`](results/summary.md), [`results/figures/`](results/figures/), and the
interactive tree in `results/tree/`. The full 20 000-model crawl hasn't been run yet.

**Demo:** open `results/tree/family_tree.html` (overview) or `results/tree/family_<name>.html`
(one family) directly in a browser. They're self-contained and work offline, with no server.

- [`docs/page_structure.md`](docs/page_structure.md): where every field lives in the HTML
- [`docs/ethics.md`](docs/ethics.md): robots.txt findings, rate limiting, data scope, crawl budget, sampling biases
- [`docs/cleaning.md`](docs/cleaning.md): every preprocessing rule, and what it found in the 500-model data
- [`docs/mining.md`](docs/mining.md): method and findings for each mining task, with caveats
- `config.py`: seeds, caps, rate limit, paths
- `crawler/fetch.py`: the only code that talks to the network (rate limit, backoff, gzip disk cache, robots.txt)
- `crawler/parse_*.py`: page → dict. They never raise on bad pages; failed fields become `None` and are listed in `parse_errors`
- `crawler/crawl.py`: fair level-by-level BFS → SQLite
- `preprocess/clean.py`: raw tables → `clean_models`, `clean_edges`, `quality_issues`
- `mining/graph.py`: clean tables → networkx `DiGraph` (edges child → parent)
- `mining/ranking.py` (own PageRank, cap-corrected weighted PageRank, HITS), `communities.py`
  (Louvain), `lineage.py`, `licenses.py`, `trends.py`, `quality.py`; `mining/report.py` runs them
  all → `results/`
- `viz/charts.py`: report figures → `results/figures/*.png`; `viz/family_tree.py`: interactive
  pyvis pages → `results/tree/*.html`; `viz/palette.py`: shared colours and family names
- `validate/api_spotcheck.py`: compares a random sample with the official HF API (the only
  place the API is used)
- `samples/`: saved pages used for parser unit tests (no network in tests)

## Where the data lives

Crawl data is kept **outside the repo**: by default in `~/hf-ecosystem-data/`
(`C:\Users\<you>\hf-ecosystem-data` on Windows). The full crawl's cache is gigabytes, and the repo
sits in a OneDrive-synced folder. To use another location, set the environment variable before
running anything:

```bash
export HF_ECOSYSTEM_DATA=/path/to/data
```

It contains `hf.db` (SQLite), `cache/` (gzip-compressed raw responses) and `crawl.log`.

### Running without crawling: the bundled sample

[`sample_data/`](sample_data/) holds the 500-model test crawl as a ready-cleaned SQLite DB (3 MB).
Point the pipeline at it to regenerate every table, chart and tree page without any network
access:

```bash
HF_ECOSYSTEM_DATA=sample_data .venv/Scripts/python -m mining.report
HF_ECOSYSTEM_DATA=sample_data .venv/Scripts/python -m viz.charts
HF_ECOSYSTEM_DATA=sample_data .venv/Scripts/python -m viz.family_tree
```

PowerShell: run `$env:HF_ECOSYSTEM_DATA = "sample_data"` first. The crawler refuses to write
into `sample_data/`.

## Pipeline

```bash
.venv/Scripts/python -m crawler.crawl --max-models 500   # 1. crawl
.venv/Scripts/python -m preprocess.clean                 # 2. clean (rebuilds clean_* tables)
.venv/Scripts/python -m mining.graph                     # 3. build graph, print stats
.venv/Scripts/python -m validate.api_spotcheck           # 4. compare 50 random models with the HF API
.venv/Scripts/python -m mining.report                    # 5. all mining tasks -> results/*.csv + summary.md
.venv/Scripts/python -m viz.charts                       # 6. report figures -> results/figures/
.venv/Scripts/python -m viz.family_tree                  # 7. interactive tree -> results/tree/
```

`viz.family_tree` options: `--family Llama` (one family), `--highlight Qwen,Gemma,Phi` (which
families get colour, max 3), `--top 200` (fewer nodes for a slow laptop).

Each mining module can also be run on its own (`python -m mining.ranking`, `mining.communities`,
`mining.lineage`, `mining.licenses`, `mining.trends`, `mining.quality`) to print its tables.

### Crawling

- **Resumable:** if it crashes or you press Ctrl+C, run the same command again. Every response is
  cached, so nothing is downloaded twice.
- **Growing the crawl:** a later run with a bigger `--max-models` (e.g. 20000) continues the same
  BFS. It tops up the current level before going deeper.
- **Sampling:** BFS runs level by level. Each level's budget is split round-robin across seed
  families, then across (parent, relation) lists, taking the most-downloaded children first.
  Without this, the first seed would fill the whole budget.
- **Politeness:** 1 request / 3 s, following HF's advertised 100-requests-per-5-minutes policy,
  with a pause when the `RateLimit` header says the window is used up.
- `edges.source` is `tags` (the child's own page) or `listing` (the parent's children listing).

### Phase-3 test run (500 models, 2026-10-26)

| | |
|---|---|
| Models scraped | 500 (10 seeds + 490 at depth 1), **0 failed, 0 parse errors** |
| Per family | 49–51 each (fair split working) |
| Requests | 736 cached responses (500 model pages + 236 listing pages), plus robots.txt |
| Wall time | ~35 min (first part at 1 req/s with 2 × HTTP 429, then 3 s pacing with 0 × 429) |
| Crash test | hard-killed at 126/500, resumed with the same command: DB intact, 0 pages re-downloaded |
| Listing vs tags | 492 listing edges whose child we scraped: **100 % match** the child's own tags |
| Cache size | 182 MB raw → **44 MB gzipped** |

**Projection for the full 20 000-model run:** about 29 000 requests, roughly 24 h at 3 s/request,
and about 1.7 GB of gzipped cache. This is an upper-end estimate, since the sampled depth-1 models
are the most-downloaded and have more children than average.

### Phase-4 graph (500-model sample)

| | sample graph | with external nodes |
|---|---|---|
| nodes | 500 | 6 860 |
| edges | 529 | 7 003 |
| is a DAG / cycles | yes / 0 | yes / 0 |
| weakly connected components | 8 (10 seed families, joined by merges) | 7 |
| multi-parent nodes (merges) | 34 | 88 |

## Tests

```bash
.venv/Scripts/python -m pytest
```

## Setup

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

If pip itself fails with `CERTIFICATE_VERIFY_FAILED`, add `--use-feature=truststore`.

## Maintenance scripts

- `scripts/fetch_samples.py "name.html=https://huggingface.co/org/model"`: save a page into
  `samples/`. Existing files are never overwritten.
- `scripts/migrate_cache_gzip.py`: one-off conversion of an old uncompressed cache to gzip. It
  verifies each file before deleting the original and is safe to re-run.
