# Sample dataset (500 models)

`hf.db` is the SQLite database from the phase-3 test crawl (2026-10-26). It has 10 seed base
models plus 490 direct derivatives, already cleaned. Use it to run the analysis, charts and
family tree without crawling:

```bash
HF_ECOSYSTEM_DATA=sample_data .venv/Scripts/python -m mining.report
HF_ECOSYSTEM_DATA=sample_data .venv/Scripts/python -m viz.charts
HF_ECOSYSTEM_DATA=sample_data .venv/Scripts/python -m viz.family_tree
```

(PowerShell: `$env:HF_ECOSYSTEM_DATA = "sample_data"` first, then the commands.)

| Table | Rows | What |
|---|---|---|
| `models` | 500 | raw scraped metadata (written by `crawler/crawl.py`) |
| `edges` | 7 495 | raw lineage edges, `source` = `tags` (child's page) or `listing` (parent's listing) |
| `crawl_queue` | 500 | BFS bookkeeping: depth, seed family, status |
| `clean_models` | 500 | normalised models (`preprocess/clean.py`) |
| `clean_edges` | 7 003 | merged, flagged edges |
| `quality_issues` | 294 | one row per data-quality problem found |

Notes:
- The clean tables are already built, so start from `mining.report`. Running
  `preprocess.clean` on it works, but rewrites the file.
- `crawler.crawl` refuses to run against this folder, so the demo data can't be overwritten by
  accident.
- `validate.api_spotcheck` needs the raw HTTP cache, which isn't bundled. Without the cache it
  would make live API requests. Its last result is already in `results/api_spotcheck.csv`.
- Contents: public model-repo metadata only (no user profiles; see `docs/ethics.md`). Download
  counts are a snapshot from the crawl date.
