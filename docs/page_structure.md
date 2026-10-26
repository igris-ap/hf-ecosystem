# Hugging Face page structure (as observed 2026-10-26)

All findings below come from the files in `samples/`, fetched with
`scripts/fetch_samples.py` (≈27 requests, ≥1.5 s apart). HF's HTML can change.
If a parser starts returning nulls, re-fetch a sample and compare it with this doc.

## TL;DR for the parsers

| Need | Best source | Fallback |
|---|---|---|
| model metadata (license, task, tags, downloads, likes, createdAt, gated) | **Model page → `ModelHeader` JSON** | none needed |
| card YAML (`base_model`, `datasets`, `language`, `license`, `base_model_relation`) | **Model page → `ModelHeader.model.cardData`** (already-parsed YAML) | raw `README.md` (fails for gated repos, see below) |
| parent edges + relation type | **Model page → `tags`** entries `base_model:<relation>:<parent_id>` | `cardData.base_model` (no relation) |
| how many children, per relation | Model page → Model-tree links `…base_model:<rel>:<id>` with text `N models` | listing page `numTotalItems` |
| child ids (crawl frontier) | **Listing page → `ModelList` JSON** `initialValues.models[].id` | none needed |

Rule of thumb: **every page we need embeds its data as JSON in an HTML attribute.**
We read JSON, not visible text. The only visible-text parsing is the child count
("979 models") on Model-tree links, and that count is also available as JSON on
the listing page.

## How the embedded JSON works

HF pages are server-rendered Svelte. Each interactive component is a
`<div class="SVELTE_HYDRATER" data-target="<ComponentName>" data-props="<HTML-escaped JSON>">`.
BeautifulSoup unescapes the attribute, so it's just:

```python
el = soup.find(attrs={"data-target": "ModelHeader"})
props = json.loads(el["data-props"])
```

Components seen on a model page: `ModelHeader` (the main one), `ModelTensorsParams`,
`InferenceWidget`, `LinkedSpacesList`, `ModelEvalResults`, plus layout ones.
On a listing page: `ModelList`.

---

## 1. Model page: `https://huggingface.co/<org>/<model>`

Samples: `model_qwen2.5-7b.html` (base), `model_llama-3.1-8b.html` (gated base),
`model_qwen2.5-7b-instruct.html` (fine-tune), `model_adapter-srt-v1.0.html` (adapter),
`model_quantfactory-qwen2.5-coder-7b-gguf.html` (quantized),
`model_optitransfer-converge-v2.html` (merge, 14 parents),
`model_mlx-qwen2.5-7b-instruct-4bit.html` (mislabelled conversion), `seeds/*.html`.

### Fields: `ModelHeader` → `props["model"]`

| Our column | JSON path | Example | Notes |
|---|---|---|---|
| `id` | `model.id` | `Qwen/Qwen2.5-7B` | Canonical id. Use this, not the URL we requested (legacy ids redirect). |
| `author` | `model.author` | `Qwen` | Org/user **name only**. Do *not* store `props["author"]` (avatar, follower count). |
| `license` | `model.cardData.license` | `apache-2.0`, `llama3.1`, `other` | Also present as tag `license:<x>`. `other` often comes with `cardData.license_name`. |
| `pipeline_tag` | `model.pipeline_tag` | `text-generation` | May be missing on small community repos. |
| `tags_json` | `model.tags` | `["transformers","safetensors",…]` | Full list. Includes `base_model:*`, `license:*`, `dataset:*`, `arxiv:*`, `region:*`. |
| `downloads` | `model.downloads` | `437832` | **Last 30 days**, snapshot at scrape time. `model.downloadsAllTime` also exists. |
| `likes` | `model.likes` | `338` | |
| `created_at` | `model.createdAt` | `2024-09-15T12:17:40.000Z` | ISO-8601 UTC. ⚠ see "createdAt floor" below. |
| `gated` | `model.gated` | `false`, `"manual"`, `"auto"` | Gated pages are still public HTML. |
| card YAML | `model.cardData` | `{"license":…, "base_model": …}` | Same content as README front matter, already parsed by HF. |
| `card_base_model` | `model.cardData.base_model` | `"Qwen/Qwen2.5-7B"` **or** `["a/b","c/d"]` | **str or list.** Normalise to list. |
| relation hint | `model.cardData.base_model_relation` | `adapter`, `merge` | Optional; author-declared. Usually absent. |
| `card_datasets_json` | `model.cardData.datasets` | list or str | Optional. |
| also useful | `model.lastModified`, `model.library_name`, `model.isQuantized`, `model.private`, `model.cardExists`, `props["hasQuantizations"]` | | |

### Parent edges: the `base_model:` tags

HF computes these from the card and puts them in `model.tags`:

```
base_model:Qwen/Qwen2.5-7B                 ← plain "has parent X"
base_model:finetune:Qwen/Qwen2.5-7B        ← parent X with relation (finetune|adapter|quantized|merge)
```

Observed:

| Model | `cardData.base_model` | relation tags |
|---|---|---|
| Qwen2.5-7B-Instruct | `Qwen/Qwen2.5-7B` | `finetune:Qwen/Qwen2.5-7B` |
| srt-adapter-v1.0 | `[Qwen/Qwen2.5-7B]` + `base_model_relation: adapter` | `adapter:Qwen/Qwen2.5-7B` |
| QuantFactory Coder-7B-GGUF | `[Qwen/Qwen2.5-7B]` | `quantized:Qwen/Qwen2.5-7B` (HF inferred from GGUF files) |
| Optitransfer converge-v2 | list of **14** ids | 14 × `merge:<id>` |
| mlx Qwen2.5-7B-Instruct-4bit | `Qwen/Qwen2.5-7B` | `finetune:Qwen/Qwen2.5-7B` |

So **the tags give us child → parent edges with relation types from the child's own
page.** That is the authoritative edge source. Listing pages give the same edges seen
from the parent's side. That makes the brief's "listing vs card agreement" check cheap.

### Model-tree box (children counts)

Not a hydrated component. It's plain HTML under `<h2>Model tree for <span>{id}</span>`.
The parts we use:

```html
<p>Base model</p> … <a href="/Qwen/Qwen2.5-7B">Qwen/Qwen2.5-7B</a>        ← parent(s)
<a href="/models?other=base_model:finetune:Qwen/Qwen2.5-7B">979</a>        ← sibling count (parent's children!)
<a href="/models?other=base_model:adapter:<this id>">2838 models</a>       ← this model's children
<a href="/models?other=base_model:quantized:<this id>">Browse Quantizations</a>   ← no count, ignore
```

Parse with: links matching `^/models\?other=base_model:(\w+):<this id>$` whose text matches
`([\d,]+)\s+models?`. **Filter on `<this id>`.** Child pages also link to the *parent's*
listing (sibling count), and counting that would be wrong. Missing link = 0 children of that
relation. **This lets the crawler skip listing requests entirely for leaf models,** which is
most of them.

Seed counts measured this way (direct children, all relations):

| Seed | gated | license | children (ft / adapter / quant / merge) | total |
|---|---|---|---|---|
| google-bert/bert-base-uncased | no | apache-2.0 | 7033 / 144 / 38 / 7 | 7222 |
| mistralai/Mistral-7B-v0.1 | no | apache-2.0 | 948 / 2467 / 195 / 390 | 4000 |
| meta-llama/Llama-3.1-8B | manual | llama3.1 | 1506 / 1355 / 335 / 71 | 3267 |
| Qwen/Qwen2.5-7B | no | apache-2.0 | 979 / 883 / 87 / 137 | 2086 |
| meta-llama/Llama-3.2-1B | manual | llama3.2 | 956 / 753 / 263 / 26 | 1998 |
| microsoft/phi-2 | no | mit | 413 / 994 / 64 / 8 | 1479 |
| Qwen/Qwen3-8B-Base | no | apache-2.0 | 643 / 148 / 51 / 14 | 856 |
| deepseek-ai/DeepSeek-R1 | no | mit | 327 / 122 / 70 / 5 | 524 |
| google/gemma-2-9b | manual | gemma | 331 / 67 / 55 / 5 | 458 |
| google/gemma-3-4b-pt | manual | gemma | 349 / 19 / 26 / 1 | 395 |

---

## 2. Children listing: `https://huggingface.co/models?other=base_model:<rel>:<id>`

Samples: `listing_qwen2.5-7b_{finetune,adapter,merge,quantized}_*.html`.

`ModelList` → `props["initialValues"]`:

| Key | Example | Use |
|---|---|---|
| `models[]` | 30 items | frontier |
| `models[].id` | `Qwen/Qwen2.5-7B-Instruct` | child id |
| `models[].downloads`, `.likes`, `.pipeline_tag`, `.gated`, `.lastModified`, `.numParameters` | | handy for prioritising, but **no `createdAt`**, so we still need the model page |
| `models[].authorData` | avatar, follower count… | ⚠ **do not store** (personal-ish data) |
| `numItemsPerPage` | `30` | |
| `numTotalItems` | `980` | pages = ceil(total / 30) |
| `pageIndex` | `0` | 0-based |
| `sortBy` | `downloads` / `""` | confirms sort was applied |
| `activeFilters.other` | `["base_model:finetune:Qwen/Qwen2.5-7B"]` | sanity-check we got the filter we asked for |

**Query params:** `&sort=downloads` (verified: results strictly descending by downloads; default
is "trending", which is not monotonic), `&p=<n>` 0-based page. **Out-of-range page → HTTP 400**
(`p=999`), so treat 400 on a listing as "no more pages", not an error to retry.

**Listings are direct children only.** `mlx-community/Qwen2.5-7B-Instruct-4bit` appears under
`Qwen2.5-7B` finetunes, not because the listing is transitive, but because its card *declares*
`base_model: Qwen/Qwen2.5-7B`. Its own README says it was converted from `Qwen2.5-7B-Instruct`.
That's a metadata-quality issue for the data-quality section, not a crawler bug.

---

## 3. Raw model card: `https://huggingface.co/<id>/raw/main/README.md`

Samples: `card_*.md`.

- YAML front matter between `---` lines. Fields seen: `license`, `license_link`, `language`,
  `pipeline_tag`, `library_name`, `tags`, `base_model` (str **or** list), `base_model_relation`,
  `datasets`.
- ⚠ **Front matter doesn't always start at byte 0.** `card_quantfactory-…-gguf.md` starts with
  `\n---`. Strip leading whitespace/BOM before checking for `---`.
- ⚠ **Gated repos return HTTP 401** for the raw README (`meta-llama/Llama-3.1-8B`), but their
  model page HTML still has the full `cardData`. Since gated content is out of scope anyway,
  we never fetch raw files for `gated != false`.
- Compared the parsed front matter with `ModelHeader.cardData` on all 6 non-gated samples:
  **identical keys and identical values in every case.** So the raw README adds no metadata we
  can't get from the model page, and it doubles the request count (see ethics.md for the time
  budget). Its only extra content is the free-text body, which we don't mine.

---

## Status codes & edge cases observed

| Situation | Observed | Crawler should |
|---|---|---|
| Normal page | 200 | parse |
| Legacy un-namespaced id (`bert-base-uncased`) | 200 after redirect to `google-bert/bert-base-uncased` | follow redirect; key the DB by `model.id` from JSON; record alias |
| Nonexistent repo | **401** (not 404; HF hides existence of private repos) | mark `failed: missing_or_private`, never retry |
| Gated repo, model page | 200, `gated: "manual"` | store public metadata; skip raw files |
| Gated repo, raw README | 401 | don't request it |
| Listing page past the end | 400 | stop paginating |
| 429 / 5xx | not seen yet | exponential backoff (phase 2) |

## Data-quality quirks to expect

1. **Wrong declared parents**: the mlx conversion of *Instruct* declares the *base*; HF then
   labels it `finetune` even though it's a 4-bit conversion. Relation labels on community
   uploads are noisy.
2. **Absurd merges**: `Optitransfer/…converge-collective-v2` lists 14 parents across Qwen,
   Mistral, Phi, Pythia, OPT, Granite, SmolLM. One node like that links families together, so
   community detection should be robust to it (or merges down-weighted).
3. **`base_model` str vs list**: always normalise to list.
4. **`createdAt` floor**: `google-bert/bert-base-uncased` shows `createdAt = 2022-03-02`
   though BERT is from 2018. Repos older than HF's created-date tracking all collapse onto
   ~2022-03-02, so trends should start after that date or flag it.
5. **`license: other`**: needs `license_name` / `license_link` to be meaningful for drift analysis.
6. **`downloads` is a rolling 30-day count**, not all-time. Use `downloadsAllTime` if we want
   lifetime popularity. Either way, record `scraped_at`.
