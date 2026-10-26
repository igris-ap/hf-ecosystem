# Ethics, robots.txt and crawl budget

## robots.txt (fetched 2026-10-26, saved as `samples/robots.txt`)

```
User-agent: *
Allow: /

Sitemap: https://huggingface.co/sitemap.xml
```

**Every path is allowed for every user agent; nothing is disallowed.** That includes the three
path types we need: `/<org>/<model>`, `/models?other=…`, and `/<org>/<model>/raw/main/README.md`.
robots.txt also has no `Crawl-delay`, so we pick our own conservative rate (below).
The crawler re-checks robots.txt at startup with `urllib.robotparser` and refuses to fetch any
URL it disallows. That way the guarantee holds even if HF changes the file mid-project.

The sitemap index (`/sitemap.xml`) links to `sitemap-models.xml`. We don't need it, because
BFS from seeds via listing pages gives us the lineage structure directly. We note it here as
an alternative discovery source.

## Politeness

| Rule | Value | Why |
|---|---|---|
| Rate | **1 request / 3 s** | HF's response headers advertise `RateLimit-Policy: "fixed window";"pages";q=100;w=300` (100 pages per 5 min for anonymous clients), so 300 s / 100 = 3 s. Stricter than the brief's ~1 req/s ceiling. |
| Quota header | read `RateLimit: "pages";r=<left>;t=<reset s>` on every response; when `r=0`, pause until the reset | never send a request we know will be refused |
| Backoff | exponential on 429 / 5xx (2, 4, 8, 16, 32 s, then mark failed), or the server's `Retry-After` if longer (capped at 300 s) | don't hammer a struggling server |
| User-Agent | `hf-ecosystem-crawler/1.0 (+https://github.com/igris-ap/hf-ecosystem)` | identifies the bot and points HF to the project page to reach us |
| Caching | every raw response stored on disk; never re-fetched | crawl is resumable and repeatable without new load |
| Concurrency | 1 connection, synchronous | no async or parallel crawling |
| Terminal statuses | 401 (missing/private/gated file) and 400 (listing past end) are never retried | they won't change on retry |

## Data scope

**Collected:** public model-repo metadata only. That means id, author *name*, license, task,
tags, download/like counts, creation date, declared base models/datasets, gated flag, and
parent/child relations.

**Not collected:**
- user profiles, avatars, follower counts, or `authorData`. The listing JSON embeds these for
  every model, and the parser drops them.
- gated or private content. For gated repos (`gated != false`) we keep only what the public
  model page shows to logged-out visitors, and never request their files. The raw README for a
  gated repo returns 401 anyway. `extra_gated_*` fields in `cardData` (access-form config) are
  dropped.
- model weights or any file other than the model page, listing pages and (optionally) README.md.
- anything behind a login. The crawler sends no cookies or tokens.

The HF API is used **only** in `validate/api_spotcheck.py`, to spot-check a random sample of
scraped records. It is never used for collection.

## Crawl budget (estimate)

Request counts per model, from the structure in `page_structure.md`:

- 1 model page (always)
- listing pages: only where the Model tree shows children for that relation, `ceil(n/30)` each.
  Most models are leaves, so they need 0 listing requests.
- raw README: optional. It's identical to `cardData` on the page (verified on 6 samples).

Phase-1 estimate, made before we knew HF's rate limit (READMEs were dropped later):

| Run | Model pages | Listing pages (approx.) | README | Total | Time @ 1 req/s |
|---|---|---|---|---|---|
| test, 500 models | 500 | ~50 | +500 | 550 – 1 050 | 9 – 18 min |
| full, 20 000 models | 20 000 | ~1 000 – 2 000 | +20 000 | 21 000 – 42 000 | 6 – 12 h |

**Revised after the 500-model test run** (no READMEs, 3 s/request): the seed listings alone took
~250 pages, because every seed has hundreds of children per relation. See the phase-3 notes in
the README for the measured numbers. Expect the full 20 000-model crawl to take **roughly a day**
of wall-clock time. Because the crawler is resumable, it can run in several overnight sessions:
re-run the same command and it continues.

### What happened in the first test run (kept as a lesson)

The first 500-model run used 1 req/s. HF answered with HTTP 429 roughly every 100 requests, and
the fetcher correctly waited out `Retry-After` each time. That worked, but it meant hitting HF's
limit every 5 minutes. Reading the `RateLimit-Policy` header showed why, so we switched to 3 s
pacing plus the quota-header pause. The run was then hard-killed and resumed, which also served
as a live crash/resume test (see README).

The direct children of the 10 candidate seeds alone already add up to ~22 000 models. So under
a 20 000 cap, a plain BFS will mostly stop at depth 1–2, and `bert-base-uncased` alone (7 033
fine-tunes) would take a third of the budget.

## Sampling design (and its biases, for the report)

Two choices keep the request count bounded and the sample balanced:

1. **Per-parent cap:** at most 300 children per (parent, relation), taken from the listing sorted
   by downloads, so ≤ 10 listing pages per relation.
2. **Fair level-by-level BFS:** each level's remaining budget is shared round-robin, first across
   seed families, then across each family's (parent, relation) lists.

Consequences to state in the report:
- **The sample favours popular models**, because each list is sorted by downloads. Low-download
  long-tail fine-tunes are under-represented.
- **Relation shares in the sample are not population shares.** Round-robin gives merges and
  quantizations as many turns as fine-tunes. For the "share of each relation type" statistic,
  use `children_counts_json` (HF's exact per-relation totals from each Model tree box), not
  counts of sampled edges.
- **Family sizes in the sample are not population sizes,** since every family gets an equal
  share. The true sizes are the sums of the Model-tree counts.
