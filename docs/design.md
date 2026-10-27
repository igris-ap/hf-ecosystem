# How the project works, and why it's built this way

This is the long version: every stage of the pipeline, what it does, and the reason behind each
design choice, including the ones we changed after something went wrong. The
[README](../README.md) is the short version, and the live numbers are in its *Results* section
and on the site's **Findings** tab. The other docs go deeper on single topics:
[page_structure.md](page_structure.md) (what Hugging Face pages contain),
[ethics.md](ethics.md) (robots.txt, politeness, data scope), [cleaning.md](cleaning.md)
(every cleaning rule) and [mining.md](mining.md) (the algorithms).

---

## 1. The question

Hugging Face hosts hundreds of thousands of models that are built from other models: fine-tunes,
adapters (LoRA), quantizations (GGUF, 4-bit) and merges. Each model card can declare its
`base_model`, so together they form a **lineage graph**. The project asks:

- Which models are the most influential bases, once you count everything built on them?
- What are derivatives made of (fine-tunes vs adapters vs quantizations vs merges), and how has
  that changed over time?
- How deep do chains go, and how many derivatives become bases themselves?
- Do derivatives keep their parent's license, or relicense it (often invalidly)?
- Do families stay separate, and how clean is the metadata people publish?

The ground rules came from the brief: scrape public model pages (requests + BeautifulSoup, the
official API only for validation), respect robots.txt, stay at or below ~1 request per second,
cache and resume, store in SQLite, Python 3.11+, and implement the ranking algorithms ourselves.

## 2. The pipeline at a glance

```
seeds ──► crawl (BFS) ──► raw SQLite tables ──► clean ──► graph ──► mine ──► results/*.csv
              │                                             │                    │
              └── gzip cache of every response              │                    ├─► README results
                                                            │                    ├─► charts + tree pages
                                                            └────────────────────┴─► site (3 tabs)
```

| Step | Module | Input → output |
|---|---|---|
| 1. Crawl | `crawler/` | 10 seed ids → `models`, `edges`, `crawl_queue` tables + response cache |
| 2. Clean | `preprocess/clean.py` | raw tables → `clean_models`, `clean_edges`, `quality_issues` |
| 3. Validate | `validate/api_spotcheck.py` | 50 random clean rows vs the official API |
| 4. Mine | `mining/` | clean tables → graph → `results/*.csv` + `summary.md` |
| 5. Visualise | `viz/charts.py`, `viz/family_tree.py` | results → PNG charts, interactive tree pages |
| 6. Site | `viz/site_data.py`, `site_findings.py`, `site_demo.py` | graph + results + cache → `site/*.js` |

**Design choice: each step reads only what the previous one wrote.** Any step can be re-run on
its own, and a change to cleaning or mining never needs a re-crawl, which matters when the crawl
takes a day.

---

## 3. Where the data comes from

### 3.1 Embedded JSON, not visible text

Hugging Face renders pages on the server and embeds each interactive component's data as JSON:

```html
<div class="SVELTE_HYDRATER contents" data-target="ModelHeader" data-props="{&quot;model&quot;:{...}}">
```

The parser finds the component by its `data-target` and decodes `data-props`
(`crawler/common.py: find_props`).

**Why:** it's the same data the page renders itself from, already structured and typed. Visible
text changes every time the site is restyled; this JSON has to stay stable or HF's own page breaks.
It's also more honest scraping: we read the page exactly as a browser receives it.

### 3.2 Three kinds of pages

| Page | What we take | Why this page |
|---|---|---|
| Model page `huggingface.co/<id>` (`ModelHeader`) | id, author, license, task, library, tags, downloads, likes, dates, gated, card fields | everything about one model in one request |
| Same page, "Model tree" links | how many children of each relation the model has (`children_counts`) | exact population counts, and it tells us *which* listings are worth requesting |
| Listing `models?other=base_model:<relation>:<parent>&sort=downloads` (`ModelList`) | the parent's children, most downloaded first, with the total count | it's HF's own index of who declares this parent |

**Lineage comes from HF's computed tags, not the raw card field.** For every declared parent HF
adds `base_model:<parent>` and `base_model:<relation>:<parent>`. HF resolves renames and
validates ids when it computes these tags, while the card's `base_model` is whatever the uploader
typed (URLs, typos, old names). We keep the card field too, because the difference between the two
is itself a data-quality finding (broken and renamed links).

**Each edge is seen from both ends.** The child's tags say "my parent is X" and X's listing says
"my children include this one". Cleaning merges the two (`in_tags`, `in_listing` flags), and their
agreement (100 %) is a validation of the parser.

**Rejected: the raw README.** Downloading `raw/main/README.md` would double the requests, gated
models return 401 for it, and the JSON already carries the parsed card data we need.

**Rejected: the API for crawling.** The brief asked for page scraping; the API is used only to
check our scraped data (section 8).

### 3.3 Reading the listing back

The listing parser reads the filter HF says it *applied* (`activeFilters`) instead of trusting the
URL it requested. If HF ever ignored or rewrote a filter, we'd log it and skip the page instead of
recording wrong edges.

---

## 4. The crawl

### 4.1 Seeds

Ten base models covering seven families: Llama-3.1-8B, Llama-3.2-1B, Mistral-7B-v0.1,
Qwen2.5-7B, Qwen3-8B-Base, gemma-2-9b, gemma-3-4b-pt, phi-2, DeepSeek-R1 and bert-base-uncased.

**Why these:** popular, with large and varied derivative trees, a mix of license types (permissive
Apache/MIT vs restricted Llama/Gemma, which is what makes license drift measurable), two
generations for several families (so trends show waves), and one non-LLM (BERT) as a contrast.
Each seed was checked to have a working Model tree before the crawl.

### 4.2 Breadth-first, level by level

The crawl is a BFS: scrape every model at level *n*, read their listings, choose level *n + 1*,
repeat, up to depth 3 or 20 000 models.

- **Why BFS:** the important models are near the seeds. Depth-first would spend the budget deep
  inside one family.
- **Shallowest level first, even across runs.** `enqueue_next_level` always tops up the
  shallowest level that still has unqueued children. If a later run raises `--max-models`,
  level 1 gets filled before anything new at level 2.
- **Depth 3:** levels 1–2 already contain most of the influential derivatives; depth 3 is where
  merges of merges live. Deeper *generations* (up to 18) still appear, because sampled models can
  derive from each other within those levels.

### 4.3 Which children to take: a cap and fair turns

A seed like BERT has 7 000+ children. Taking all of them would spend the whole budget on a few
families. So:

- **At most 300 children per (parent, relation), most downloaded first.** Sorting by downloads
  means the budget goes to models people actually use, not whatever is trending today.
- **Fair round-robin, two levels deep** (`select_fair`): families take turns, and within a family
  the (parent, relation) lists take turns. Fine-tunes can't crowd out adapters, and Mistral can't
  crowd out Phi.
- **A model reachable from several parents (a merge) is taken once.**

**The trade-off, stated openly:** the sample is *balanced by design*, so it does not show the true
mix of relations. That's why every population-level claim uses HF's exact Model-tree counts
instead of our sample (section 7.3), and why the ranking needed a correction (section 7.1).

### 4.4 Politeness

| Choice | Detail | Why |
|---|---|---|
| robots.txt | fetched first; disallowed URLs raise `RobotsDisallowed` and are never requested | required, and the brief said so |
| 1 request per 3 s | `MIN_REQUEST_INTERVAL = 3.0` | HF's `RateLimit-Policy` header is 100 pages per 300 s. Our first run at 1 req/s hit HTTP 429 every window, so we matched the published policy instead |
| RateLimit header | when `RateLimit: r=0;t=N` says the window is used up, sleep N + 1 s | stay under the limit instead of bouncing off it |
| Backoff | 2ⁿ seconds on 429/5xx/network errors; `Retry-After` honoured (capped at 300 s) | standard, and it keeps a bad minute from becoming a ban |
| Identifying User-Agent | `hf-ecosystem-crawler/1.0 (+https://github.com/igris-ap/hf-ecosystem)` | the site owner can see who we are and why |
| Data scope | the author profile block (avatars, user ids, follower counts) is never read or stored | personal data isn't needed for lineage; see ethics.md |

At 3 s per request, 20 000 models take about a day. The listing pages are skipped for models
whose Model tree shows no children, which saves most of the requests for leaf models.

### 4.5 Crash safety and resuming

- **Every response is cached** as `<sha1(url)>.body.gz` plus a small `.json` with status and
  time. Gzip shrinks HF pages about 4×. A re-run never fetches a page twice.
- **The metadata file is written last**, via write-to-temp-then-rename. If the process dies
  mid-write, the cache entry simply doesn't exist yet. The rename retries a few times, because
  Windows antivirus briefly locks new files (`WinError 32`).
- **One transaction per model:** the model row, its tag edges and its queue status commit
  together. A crash loses at most the model being processed.
- **The queue is the state.** `crawl_queue` holds every chosen model with `pending` / `done` /
  `failed`. Restarting the same command continues where it stopped. Transient failures (network,
  429, 5xx) go back to `pending` on restart; permanent ones (private/deleted repo) stay failed.
- **Windows sleep is blocked** while the crawl runs (`SetThreadExecutionState`).
- The data directory lives outside OneDrive, so sync never fights the crawler for file locks.

### 4.6 One bad field must never stop the crawl

Each field is parsed on its own (`parse_model.py: field()`). A failure is logged, the field is set
to null and its name goes into `parse_errors`, which feeds the data-quality report.

**Learned the hard way:** at model 9 025, a card said `license: [llama3.1]`, a list. The parser
passed it through and SQLite refused to store a list, which crashed the crawl. The fix had two
parts: single-value fields now go through `_text()` (`["llama3.1"]` → `"llama3.1"`; anything
stranger becomes a parse error), and the database insert has a safety net that records the model
as `store_error` instead of crashing. The **How it works** tab replays this model.

---

## 5. Storage

SQLite, one file.

- **Raw tables** (`models`, `edges`, `crawl_queue`) are written only by the crawler and never
  edited: they're a faithful record of what HF served.
- **Clean tables** (`clean_models`, `clean_edges`, `quality_issues`) are rebuilt from scratch by
  every cleaning run.

**Why rebuild instead of fixing in place:** any rule can be changed and re-applied in about a
second, without re-crawling, and the raw data is always there to check a rule against. Lists
(tags, datasets) are stored as JSON text, which keeps the schema flat and readable.

---

## 6. Cleaning

Full rule table in [cleaning.md](cleaning.md). The main choices:

| Rule | Why |
|---|---|
| **Edges = union of tags and listings**, with flags for which source saw each | two independent views of the same edge; their agreement is a quality metric |
| **Declared base ids are normalised** (URL prefixes, `/tree/main`, whitespace stripped; free text dropped and logged) | cards contain URLs, paths and typos |
| **Renamed repos are learned from the data:** if a card declares exactly one base that HF didn't link, and HF linked exactly one parent the card didn't declare, they're the same repo | repos get renamed (`Meta-Llama-3.1-8B` → `Llama-3.1-8B`); HF follows the rename but old cards keep the old name. Requiring a one-to-one match avoids false aliases |
| **Licenses grouped into categories** ordered by restrictiveness: permissive < copyleft < restricted < non-commercial (plus other / unknown) | 30+ raw license ids can't be compared directly; drift needs an order. Llama/Gemma/OpenRAIL are "restricted" (use policies); `cc-by-nd` counts as restricted because it forbids derivatives |
| **Missing task inherited from the parent**, only when all parents agree, and marked `inherited` | quantizations and adapters rarely declare a task but obviously share the parent's; the flag keeps the guess visible and reversible |
| **HF's pre-2022 date is a placeholder:** `created_at < 2022-03-03` is flagged | HF has no creation dates before March 2022 (BERT shows 2022 although it's from 2018) |
| **Child created > 7 days before its claimed parent → temporal anomaly** | impossible for real lineage. 7 days of tolerance because a base and its instruct version are often uploaded hours apart. Flagged edges stay in the graph but are kept out of trends |
| **BFS depth and seed family from the crawl queue** (shallowest wins) | needed for per-family and per-generation statistics |

Every problem found is one row in `quality_issues`, so the data-quality section is evidence, not
an estimate.

---

## 7. The graph and the mining

**Edges point child → parent** (`mining/graph.py`). That's the direction influence flows in
PageRank: a model "votes" for what it was built on.

**Two graphs:**
- the **sample graph**, only scraped models, used for anything that needs metadata (licenses,
  trends, families);
- **all known edges**, which also includes children seen only in listings and parents outside the
  sample, used for ranking, because those links are real even without metadata.

The graph is checked for cycles (a cycle would mean bad metadata); if any appear, the edge into
the newest model is dropped. Model ids that look like credentials (a repo named like an HF token)
are left out of the graph and everything published from it.

### 7.1 Influence ranking

- **PageRank, HITS, and a weighted PageRank, all written by hand** (power iteration, d = 0.85,
  dangling rank spread uniformly) with the math in comment blocks in `ranking.py`.
- **The crawl cap distorts plain PageRank.** With at most 300 sampled children per relation,
  Mistral (300 in all four relations) looked more influential than BERT (7 000+ real children,
  almost all fine-tunes). Edge weights can't fix that, since most models have one parent and
  pass 100 % of their rank whatever the weight. The cap removes *sources* of rank.
- **So the weighted PageRank puts the missing children back:** for each parent and relation, one
  virtual node stands for `HF count − sampled count` models and gets that many models' share of
  the random jump. It's exact when the unsampled children are leaves (a test checks that one
  virtual node for 8 leaves gives the same ranks as 8 real leaves), and it matches networkx's
  personalised PageRank to ~10⁻¹⁰.
- The report keeps `plain_pagerank_rank` next to the weighted rank, so the effect of the
  correction is visible (e.g. `unsloth/Qwen2.5-7B-Instruct` jumps from #1 683 to #9: 5 360
  children on HF, 1 in our sample).
- **HITS is reported but not used for the headline ranking.** Without a random jump it piles
  almost all authority onto one tightly connected cluster (Mistral merges). The eigengap σ₂/σ₁ is
  reported too: when it's close to 1, HITS converges slowly and its order is fragile.

### 7.2 Families

Louvain community detection (networkx, fixed seed 42) on the undirected graph, **without telling
it the families**. Then each community is compared with the seed family its models were crawled
from. High purity means lineage alone recovers the families; the rare cross-family links are
listed (almost all merges).

### 7.3 Lineage depth and branching

Generation = the longest chain of parents back to a model with none (one pass over a topological
order). Branching uses **HF's exact Model-tree counts**, not our capped sample. This is also where
the population relation mix comes from (fine-tunes vs adapters vs quantizations vs merges), shown
next to the sample's mix so the sampling bias is explicit.

### 7.4 License drift

For every parent→child pair with both ends scraped, compare license categories. A child in a
*less* restrictive category than its parent is **loosened**, a likely conflict (e.g. a Gemma
quantization relicensed as Apache-2.0: a quantization changes the file format, not the license).
"Other" and "unknown" aren't ordered, so they're counted separately. It's a flag, not a legal
judgement.

### 7.5 Trends

Scraped derivatives grouped by creation quarter. Placeholder dates and models whose every parent
link is a temporal anomaly are excluded (otherwise "DeepSeek-R1 derivatives" appear before R1
existed). Shares, not counts, are used for the relation mix, since the sample is balanced.

### 7.6 Data quality

`quality.py` turns `quality_issues` and the crawl tables into one table: crawl failures, parse
errors, missing fields, declared bases (linked / renamed / broken / malformed), listing-vs-tag
agreement, temporal anomalies, and the API spot-check result.

---

## 8. Validation

| Check | How | Result |
|---|---|---|
| Our PageRank, weighted PageRank, HITS | compared with networkx on both graphs | max difference ~10⁻⁹–10⁻¹⁰, top-20 identical |
| Scraped data vs the official API | 50 random models (fixed seed) re-fetched through the API, 11 fields each | ~99.5 % match; only download counts drift, because they change between scrape and check |
| Two edge sources | listing edges confirmed by the child's own tags | 100 % |
| Unit tests | 215 tests: parsers on saved real pages, crawl logic with fake fetchers, every cleaning rule, the algorithms on hand-solved graphs, the site exports | all pass |

The spot-check proves the parsers extract what HF's backend serves. It can't prove HF's metadata
is right (a wrong declared base looks the same in both); that's what the cleaning checks are for.

---

## 9. Visualisation

- **Static charts** (`results/figures/`) are drawn by the same functions that write the CSVs, so a
  chart can't disagree with its table.
- **Colours were validated, not eyeballed** (colour-blindness simulation plus contrast checks).
  Up to 4 colours pass in bar and line charts, so the four relations get fixed colours everywhere.
  In a network graph every pair of colours touches, and only 3 colours pass that test, so graphs
  highlight at most 3 families and show the rest in grey (told apart by shape, label and tooltip).
- **Interactive family tree** (`results/tree/`, pyvis): node size = influence, edge dash = relation,
  arrows child → parent; physics is switched off once the layout settles; fully offline (the
  Bootstrap CDN link pyvis adds is stripped).

---

## 10. The website (`site/`)

A static site: `index.html` plus three data scripts. No server, no build step; it opens from the
file system or any static host.

| Tab | What it shows | Data |
|---|---|---|
| **Findings** | every result as charts and tables, each with a one-sentence headline computed from the data | `findings.js`, exported from `results/*.csv` |
| **Graph** | the most influential 150–1,000 models as one force-directed network, by family or license | `data.js` |
| **Explorer** | one model: card, origin, drawbacks, better alternatives, every chain back to a root, family graph, charts | `data.js`, exported from the graph |
| **How it works** | the pipeline replayed for 5 real models, step by step | `demo.js`, exported from the crawl cache |

**Design choices:**
- **One search bar on every tab**, and every model name anywhere (charts, tables, chains) opens
  that model in the Explorer. The URL (`#model/<id>`) is shareable.
- **Compact data:** `data.js` stores models as arrays with a field list, and edges as a flat number
  array, so 22 000 models and 25 000 edges load as one ~3 MB file.
- **Headlines are computed, never typed.** A sentence like "1,935 derivatives claim a looser
  license" is built from `findings.js`, so it can't go stale as the crawl grows.
- **Search ranking:** exact id (or a pasted HF URL) first, then name-starts-with, id-starts-with,
  contains; ties broken by influence.
- **Drawbacks are rules over the metadata**, ordered by severity: likely license conflict
  (critical); no / non-commercial license, doubtful lineage date, many-parent merge, low adoption
  vs siblings (warnings); restricted license, broken parent link, gated, quantization/adapter
  caveats, inferred task (notes).
- **Better alternatives** come from the model's own neighbourhood (parent, siblings, children, same
  seed base, same task), scored by `log10(downloads) + 0.4·log10(likes) + license bonus`, minus 1
  for a license conflict and minus 1 for a doubtful lineage date, and must beat the model by a
  margin. Candidates are limited to the same base because the data has no parameter counts, and an
  8B model isn't a drop-in replacement for a 1B one. Each comes with its reasons.
- **Both graphs use the results-tree encoding:** force-directed layout (frozen once it settles,
  so dragging stays smooth), size = weighted PageRank, shape = family, dash = relation, arrows to
  the parent. The whole-graph view colours at most 3 families (or the license classes), because
  only 3 hues stay distinguishable when any two nodes can touch.
- **The model graph shows only edges that explain the model** (ancestor chain, siblings to the
  shared parent, derivatives to it). Big merges show their 8 most influential parents. Showing
  every edge produced unreadable spaghetti. An earlier version used strict rows by generation,
  but with 16 derivatives in one row it zoomed out until labels vanished.
- **The demo replays the cache, it doesn't simulate.** Every request line, JSON excerpt and table
  in **How it works** is the real response and the real database row. Only whitelisted JSON keys
  are exported, so no author profile data reaches the site. The five cases were picked to show one
  normal path and four kinds of mess: a malformed card, a license conflict, a renamed parent and a
  doubtful date.
- Light and dark themes, phone layout, and charts as inline SVG coloured through CSS variables (so
  they follow the theme).

---

## 11. Automation while the crawl runs

`scripts/snapshot_watch.py` runs next to the crawler. Every 1 000 models it:

1. copies the live database with SQLite's backup API (a consistent copy; the analysis never locks
   the crawler's file),
2. runs clean → API spot-check → report → charts → tree → site exports on the copy,
3. regenerates the README's Results section (every number read from the result tables),
4. commits and pushes.

It reads the crawl log to tell a normal finish from a crash, and only a normal finish is published
as **Final results**. A crash publishes a snapshot and says so.

One snapshot was blocked by GitHub's push protection: a model repo on HF is literally named like
an access token. Rather than bypass the protection, ids that look like credentials are now
filtered out of everything we publish.

---

## 12. Biases and limitations

- **Balanced, download-ordered sample.** It over-represents quantizations and merges and popular
  models. Population claims use HF's counts; sample-based shares are labelled as such.
- **Depth 3 and 20 000 models** is a slice, not the whole of Hugging Face. Rankings use the
  correction in 7.1, but metadata-based findings (licenses, trends) describe the sample.
- **Self-declared lineage.** If an uploader declares the wrong base, every source we have agrees
  with them. The temporal check catches only the impossible cases.
- **Downloads are a 30-day snapshot** from the day each page was scraped (the crawl took about a
  day).
- **A gap in HF's own data:** `meta-llama/Llama-3.2-1B-Instruct` declares no base model, so it's
  invisible from its base.
- **License categories are a simplification**, and a "conflict" is a flag for a human to check,
  not a legal finding.

---

## 13. Reproducing it

```bash
python -m crawler.crawl --max-models 20000     # about a day; resumable
python -m preprocess.clean
python -m validate.api_spotcheck
python -m mining.report
python -m viz.charts && python -m viz.family_tree
python -m viz.site_data && python -m viz.site_findings && python -m viz.site_demo
```

Or skip the crawl: `sample_data/hf.db` is a 500-model database for trying every step offline
(see the README's Quick start).
