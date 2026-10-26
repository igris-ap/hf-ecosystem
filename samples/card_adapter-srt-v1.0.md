---
license: apache-2.0
base_model:
- Qwen/Qwen2.5-7B
tags:
- adapter
- semiotics
- sentence-similarity
- sentence-embeddings
- bifurcation-detection
- frozen-backbone
- pytorch
- custom_code
- srt
- semiotic-reflexive-transformer
- introspection
- interpretability
language:
- en
library_name: srt-adapter
pipeline_tag: feature-extraction
inference: false
base_model_relation: adapter
---

# SRT-Adapter v1.0

A 14.5M-parameter adapter on a **frozen** `Qwen/Qwen2.5-7B` that exposes per-token *semiotic* readouts — community vector, divergence vectors, reflexivity estimate $\hat{r}$, regime classification — and produces a sentence-embedding space that competes on English STS while preserving the v8a interpretability surface.

> **v1.0 = the v15a checkpoint.** v15a warm-starts from v8a and adds one epoch of InfoNCE on 396K English public sentence pairs (NLI + Quora). It is the first SRT-Adapter that is simultaneously a *useful embedding model* and a *semiotic readout*.

> **Custom-code model.** Not `AutoModel`-loadable. Clone this repo and load through the bundled `SRTAdapter` class. See [How to get started](#how-to-get-started).

> **Training source code is held back during patent and publication review.** Inference, evaluation, capability bench, and reproduction scripts are included.

---

## What changed since v8a

v8a's headline claims were *interpretability* claims (calibrated $\hat{r}$, community recall, regime AUROC on internal validation). They survive in v1.0 — we re-measured every external benchmark and they reproduce within 0.003. What v8a *did not* do was produce a usable sentence-embedding space: external STS Spearman was around 0.21 averaged across 40 multilingual splits.

v1.0 fixes that without breaking anything else.

| Axis | v8a (2026-04-26) | v1.0 / v15a (2026-05-01) | Δ |
|---|---:|---:|---:|
| **STS, English mean Spearman** (17 splits, MTEB 2.12) | 0.20 | **0.5894** | **+0.39** |
| **STS, all-40-split mean** | 0.21 | **0.3634** | +0.15 |
| **STS top-line (HUMESICK-R)** | 0.55 | **0.7973** | +0.25 |
| **Cap-A community NMI vs Banking77** (3-seed mean) | 0.4427 ± 0.005 | **0.5391 ± 0.008** | **+0.10** (~13σ) |
| **Cap-C paraphrase invariance** (mean cos μ ± σ, n=162) | 0.874 ± 0.144 | **0.913 ± 0.066** | μ +0.04, σ halved |
| **TruthfulQA hallucination AUROC** (mean_r_hat, n=1476) | 0.5747 | 0.5762 | +0.001 (preserved) |
| **TruthfulQA mean_ce AUROC** | 0.4150 | 0.4148 | unchanged |
| **BEN regime fractions** (Banking77, n=6156 positions) | 96.9% sup / 3.1% sub | 96.9% / 3.1% | identical |
| **MAH boundary F1** (concat probe, n=200) | 0.309 | 0.315 | +0.006 (within noise) |
| **Trainable params** | 14,562,627 | 14,562,627 | same architecture |

**Read.** v1.0 dominates v8a on every embedding-quality axis (STS, NMI, paraphrase invariance) and matches it on every interpretability axis (hallucination AUROC, regime distribution, MAH boundaries). Same forward pass. Same 4 readouts. Same VRAM and latency.

---

## Honest scope

What v1.0 is good at:

- **English sentence similarity** (HUMESICK-R 0.797, STS17 0.740, SICK-R 0.644, mean 0.589 across 17 English splits)
- **Per-token diagnostics** that come for free from the same forward pass — community vector, divergence norms, $\hat{r}$, regime logits
- **Cluster discovery on intent-labelled corpora** (Banking77 NMI 0.54)
- **Paraphrase-invariant embedding** (cos 0.913 ± 0.066 on STSB high-similarity pairs)

What v1.0 is **not** good at, despite what v8a's model card suggested:

- **Retrieval.** SciFact nDCG@10 = 0.028, NFCorpus = 0.011, ArguAna = 0.20. STS-only training did not produce a retrievable embedding space. If you need retrieval, use [`mxbai-embed-large-v1`](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) (SciFact 0.733).
- **Cross-lingual STS** (12 IndicCrosslingual splits all near zero or negative — training data was English-only)
- **Hallucination detection at production thresholds.** The TruthfulQA AUROCs (0.57–0.58 best channel) reproduce v8a's number but are not a deployable detector. They are an honest non-trivial-vs-chance signal, not a SOTA hallucination filter.
- **BEN regime classification as a discriminative tool.** The classifier is stuck at ~97% supercritical on most modern English text. The continuous $\hat{r}$ varies (μ ≈ 0.55, σ ≈ 0.39); the binary head does not.

The framing for v1.0 is: **"a frozen 7B + 14M-param side-net that learns interpretable community structure, with a real English STS embedding space attached."** Not a general-purpose SOTA encoder, not a hallucination detector. A diagnostic instrument that now also embeds usefully.

---

## Capability bench (this release)

Four-task probe of the SRT-specific readouts, evaluated bf16 on a single GPU. Reproducible with `scripts/capability_eval.py`.

| Task | What it measures | v8a | v1.0 | Notes |
|---|---|---:|---:|---|
| **Cap-A** community NMI vs Banking77 (n=1000, K=77) | Can community_encoded recover known intent labels via K-means? | 0.443 ± 0.005 | **0.539 ± 0.008** | 3-seed mean ± SD. Δ = +0.10, ~13σ |
| **Cap-B** MAH boundary F1 on 5-sentence concatenations (n=200) | Does last-MAH divergence-norm peak at sentence boundaries? | 0.309 | 0.315 | Tied; weak signal — likely tokenizer-driven, **not recommended as headline** |
| **Cap-C** paraphrase mean cos on STSB ≥ 4.5 (n=162) | Embedding stability under paraphrase | 0.874 ± 0.144 | **0.913 ± 0.066** | μ +0.04, σ halved |
| **Cap-D** BEN regime coverage on Banking77 (n=6156 positions) | Distribution of binary regime predictions | 96.9% sup / 3.1% sub | 96.9% / 3.1% | Stuck. Diagnostic only. Reported as honest negative. |

**Cap-A is the headline.** It is the only capability metric with both (a) a clear tie to the SRT thesis (community structure as the learned representation) and (b) a robust seed-stable separation from baseline.

---

## STS evaluation (MTEB 2.12, 40 splits, full results)

Run with `mteb==2.12.30`, task type STS. See `mteb/summary.json` for the per-split JSON.

**English-only** (17 splits, dev + test combined):

| Spearman | Task |
|---:|---|
| **0.7973** | HUMESICK-R |
| 0.7413 | SemRel24STS (eng) |
| 0.7397 | STS17 (en-en) |
| 0.6898 | STSBenchmarkMultilingualSTS (en-dev) |
| 0.6555 | STS15 |
| 0.6441 | SICK-R |
| 0.6148 | HUMESTS22 (en) |
| 0.5994 | HUMESTS12 |
| **mean = 0.5894** across all 17 English splits |

**All 40 splits** (English + multilingual): mean 0.3634, median 0.4867. The 12 IndicCrosslingual splits are all near zero or negative — expected, training data was English-only.

For comparison, v8a's published mean across the same 40-split cohort is +0.21.

---

## Per-token readouts (preserved from v8a)

A single forward pass returns four readouts at every token position. None of these heads were retrained for v1.0; they are bit-stable with v8a within 3 decimals on the same input.

- **Community vector** — 64-D continuous output of the CDH community head. Use cosine similarity for clustering, k-NN, or as a sentence embedding (mean-pool then L2-normalize).
- **Divergence vectors** — per-MAH-layer residuals between the community-conditioned prediction and the actual hidden state. L2 norm is a per-token "where does meaning fork" signal.
- **Reflexivity estimate** $\hat{r}$ — continuous BEN scalar (μ ≈ 0.55, σ ≈ 0.39 on Banking77). Tracks information density and contestation. **Do not use the binary regime head.**
- **Regime logits** — 2-class subcritical/supercritical. Stuck at ~97% supercritical on modern English. Reported for completeness, not recommended for use.

External hallucination-AUROC numbers reproduce v8a's published figures (TruthfulQA, n=1476): max_r_hat 0.536, mean_r_hat 0.576, mean_ce 0.415. These are honest non-trivial-vs-chance signals, not deployable detectors.

---

## Lineage

v1.0 is the production embedding-quality stage of a multi-year program on computational semiotics.

- **Stages 1–2 (synthetic + Supabase, 2026-03):** core architectural claims (subspace specialization, community differentiation, divergence tracking, bifurcation detection) validated. See `VALIDATION_HISTORY.md` in the v8a release.
- **Stage 3 Phase 1 (TinyLlama-1.1B, 2026-03/04):** 105 training rounds; community detection silhouette 6.93×, $\hat{r}$↔polarization Pearson 0.66, regime accuracy 85% on curated. Plateau on 2-community Supabase data triggered the data-first pivot.
- **v5 → v8a (Qwen 2.5-7B + Reddit, 2026-04):** scalable adapter at 0.19% parameter overhead. v8a is canonical for the **interpretability claims** in the original SRT paper.
- **v9 → v14 (2026-04):** target-norm, MARINA exploration, contrastive data assembly. Several negative results documented.
- **v15a (this release, 2026-05-01):** v8a + 1 epoch InfoNCE on NLI + Quora (396K pairs), 12,373 steps on a single A6000. The first checkpoint that is simultaneously a useful embedding and a semiotic instrument.
- **v16 → v22c, v23 (2026-05):** alternative recipes (gte distillation, model souping, beyond-STS retrieval). All non-improving on the v15a Pareto frontier; v22c won multilingual STS at the cost of English STS and Cap-A NMI. Documented as ablations; not shipped.

For the program-level theoretical foundation see Lancaster (2025), "The Treachery of Signs," SSRN [5987495](https://papers.ssrn.com/abstract=5987495). For the Stage 1 + Stage 2 spec see Lancaster (2026a), SSRN [6349978](https://papers.ssrn.com/abstract=6349978).

---

## Package contents

```
srt-adapter-v1.0/
├── README.md                   ← you are here
├── LICENSE                     ← Apache-2.0
├── config.json                 ← v15a hyperparameters
├── adapter.pt                  ← v15a weights (~28 MB, PyTorch state-dict)
├── adapter.safetensors         ← same weights, safetensors format
├── SHA256SUMS                  ← integrity hashes for weights + config
├── requirements.txt            ← torch + transformers + numpy + safetensors
├── src/srt/                    ← inference-only model code (CDH, MAH, RRM, BEN)
├── examples/
│   ├── README.md
│   ├── load_and_score.py       ← per-token readouts demo
│   └── encode_sentences.py     ← sentence-embedding demo
├── scripts/
│   ├── reproduce_capability.sh ← rerun Cap-A/B/C/D on this checkpoint
│   ├── capability_eval.py      ← capability bench source
│   ├── run_mteb.py             ← English STS reproduction
│   └── hallucination_probe.py  ← TruthfulQA AUROC reproduction
├── benchmarks/
│   ├── capability_summary.json ← Cap-A/B/C/D results, this checkpoint
│   ├── capability_seed_s{0,1,2}.json ← 3-seed Cap-A sweep
│   ├── mteb_summary.json       ← English STS suite results
│   └── hallucination_tqa.json  ← TruthfulQA AUROCs
└── data/
    └── val_200.jsonl           ← held-out validation samples
```

---

## How to get started

```bash
pip install -r requirements.txt
cd examples
python load_and_score.py --text "Vaccine mandates are an obvious public health win."
python encode_sentences.py --sentences "A man is playing guitar." "Someone is performing music."
```

First run downloads `Qwen/Qwen2.5-7B` (~15 GB).

### Reproduce the capability bench

```bash
bash scripts/reproduce_capability.sh
# Expected (3-seed mean):
#   Cap-A NMI = 0.539 ± 0.008
#   Cap-C cos = 0.913 ± 0.066
```

### Reproduce the STS evaluation

```bash
python scripts/run_mteb.py --output benchmarks/mteb_summary.json
# Expected:
#   English-mean Spearman ≈ 0.589
#   HUMESICK-R              ≈ 0.797
```

---

## Citation

```bibtex
@misc{lancaster2026srtadapter,
  title  = {SRT-Adapter v1.0: Frozen-Backbone Semiotic Readouts with Contrastive Embedding},
  author = {Lancaster, James Burton},
  year   = {2026},
  doi    = {10.57967/hf/8560},
  url    = {https://huggingface.co/RiverRider/srt-adapter-v1.0}
}
```

---

## Changelog from v8a

- **+ contrastive embedding head** — `community_output.encoded` is now usable as a sentence embedding (mean-pooled, L2-normalized). English STS mean 0.21 → 0.589.
- **+ capability bench** (`scripts/capability_eval.py`) — Cap-A/B/C/D probes for community structure, MAH boundaries, paraphrase invariance, regime coverage.
- **= preserved interpretability surface** — TruthfulQA AUROCs and BEN regime distribution match v8a within noise.
- **− removed claims that did not reproduce** — calibrated $\hat{r}$↔r_true Pearson on curated probe (was 0.005, never had signal in v8a either), HaluEval AUROC (0.635 best channel was a max-over-tokens artifact), retrieval claims (never made for v8a, but ablated and disconfirmed for v15a so we say so explicitly).
- **= same architecture, same VRAM, same latency** — 14,562,627 trainable params, ~+5–8% latency on A6000 bf16.
