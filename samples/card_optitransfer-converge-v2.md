---
language: en
license: other
license_name: opt-175b-noncommercial-and-upstream
license_link: https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md
pipeline_tag: text-generation
library_name: transformers
tags: [text-generation, conversational, model-merging, merge, open-weights, qwen2.5, qwen2, 7b, reproducible-evaluation, collective-intelligence, converge]
base_model:
  - Qwen/Qwen2.5-7B-Instruct
  - mistralai/Mistral-7B-Instruct-v0.3
  - microsoft/Phi-3-mini-4k-instruct
  - microsoft/phi-2
  - HuggingFaceTB/SmolLM2-1.7B-Instruct
  - ibm-granite/granite-3.0-2b-instruct
  - EleutherAI/pythia-2.8b
  - EleutherAI/pythia-1.4b
  - facebook/opt-2.7b
  - Qwen/Qwen2.5-Coder-7B-Instruct
  - Qwen/Qwen2.5-7B
  - unsloth/Qwen2.5-7B-Instruct
  - unsloth/Qwen2.5-Coder-7B-Instruct
  - Qwen/Qwen2.5-7B-Instruct-1M
base_model_relation: merge
model-index:
  - name: Qwen2.5-7B-Instruct-converge-collective-v2
    results:
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "GSM8K, HELM Lite v1.9.0 request replay (1,000 test instances)"
          type: openai/gsm8k
          config: main
          split: test
          args: {protocol: "HELM Lite requests, 5-shot Q:/A:, greedy, max 400 tokens, final-number exact match", request_file_sha256: 8648fd3f19c91a0470bc72f04256b5e9dcaacd4a6e7f08dfc5c7ca0f495231cc, calibration: "CALIBRATED (seed 83.3 vs HELM 83.0)", seed_same_instrument: 83.3}
        metrics:
          - {type: exact_match, name: "final-number exact match (HELM)", value: 87.0, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "MMLU, HELM MMLU v1.9.0 request replay (14,042 test questions, 57 subjects)"
          type: cais/mmlu
          config: all
          split: test
          args: {protocol: "HELM multiple_choice_joint, 5-shot, single letter, greedy; mean over 57 subjects", request_file_sha256: ac06828a2ad026c29164b8b152939cb0360cbdf7d45a35cf1ba403b21ada33c0, calibration: "CALIBRATED (seed 72.92 vs HELM 72.87)", seed_same_instrument: 72.92}
        metrics:
          - {type: exact_match, name: "exact match, mean over 57 subjects (HELM)", value: 73.40, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "MATH Level 5 (1,324 test problems)"
          type: EleutherAI/hendrycks_math
          split: test
          revision: 21a5633873b6a120296cce3e2df9d5550074f4a3
          args: {protocol: "0-shot, chat template, boxed answer, greedy, max 4,096 tokens, math-verify 0.9.0", calibration: uncalibrated, seed_same_instrument: 54.31}
        metrics:
          - {type: accuracy, name: "math-verify accuracy", value: 48.56, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "MMLU-Pro (12,032 test questions)"
          type: TIGER-Lab/MMLU-Pro
          split: test
          revision: b189ec765aa7ed75c8acfea42df31fdae71f97be
          args: {protocol: "lm-eval 0.4.13 mmlu_pro, 5-shot CoT, chat off, greedy, max 2,048 tokens", calibration: uncalibrated, seed_same_instrument: 56.77}
        metrics:
          - {type: exact_match, name: "exact match (custom-extract)", value: 54.88, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "GSM8K (1,319 test problems), lm-eval 5-shot"
          type: openai/gsm8k
          config: main
          split: test
          revision: 740312add88f781978c0658806c59bc2815b9866
          args: {protocol: "lm-eval 0.4.13 gsm8k, 5-shot, chat off, greedy, max 1,024 tokens", calibration: uncalibrated, seed_same_instrument: 87.49}
        metrics:
          - {type: exact_match, name: "exact match, flexible-extract", value: 88.32, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "GSM8K (1,319 test problems), lm-eval 0-shot CoT"
          type: openai/gsm8k
          config: main
          split: test
          revision: 740312add88f781978c0658806c59bc2815b9866
          args: {protocol: "lm-eval 0.4.13 gsm8k_cot_zeroshot, chat template, greedy, max 1,024 tokens", calibration: uncalibrated, seed_same_instrument: 78.77}
        metrics:
          - {type: exact_match, name: "exact match, flexible-extract", value: 79.45, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "MATH-500"
          type: HuggingFaceH4/MATH-500
          split: test
          revision: 6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be
          args: {protocol: "0-shot, chat template, boxed answer, greedy, max 4,096 tokens, math-verify 0.9.0", calibration: uncalibrated, seed_same_instrument: 74.8}
        metrics:
          - {type: accuracy, name: "math-verify accuracy", value: 73.6, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "AIME 2024 + AIME 2025 (60 problems; exploratory)"
          type: Maxwell-Jia/AIME_2024
          split: train
          revision: 8d88b2876a82a080e2f172cc9b25d0d9d2cb4792
          args: {also: "math-ai/aime25 test @ 563bb8404243c5f09de6ec262f2db674fe5bce9b", protocol: "8 samples, T 0.6, top_p 0.95, max 16,384 tokens, math-verify", calibration: "report-only", seed_same_instrument: 9.583}
        metrics:
          - {type: accuracy, name: "avg@8", value: 8.125, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "HumanEval+ (EvalPlus v0.1.10)"
          type: evalplus/humanevalplus
          split: test
          args: {protocol: "EvalPlus 0.3.1, instruct prompt, greedy, max 768 tokens", calibration: uncalibrated, seed_same_instrument: 75.0}
        metrics:
          - {type: pass@1, name: "pass@1 (base + plus tests)", value: 78.05, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "MBPP+ (EvalPlus v0.2.0)"
          type: evalplus/mbppplus
          split: test
          args: {protocol: "EvalPlus 0.3.1, instruct prompt, greedy, max 768 tokens", calibration: uncalibrated, seed_same_instrument: 68.78}
        metrics:
          - {type: pass@1, name: "pass@1 (base + plus tests)", value: 70.63, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "IFEval (541 prompts)"
          type: google/IFEval
          split: train
          revision: 966cd89545d6b6acfd7638bc708b98261ca58e84
          args: {protocol: "lm-eval 0.4.13 ifeval, chat template, greedy, max 1,280 tokens", calibration: uncalibrated, seed_same_instrument: 71.53}
        metrics:
          - {type: accuracy, name: "prompt-level strict accuracy", value: 73.01, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
      - task: {type: text-generation, name: Text Generation}
        dataset:
          name: "ARC-Challenge (1,172 test questions)"
          type: allenai/ai2_arc
          config: ARC-Challenge
          split: test
          revision: 210d026faf9955653af8916fad021475a3f00453
          args: {protocol: "lm-eval 0.4.13 arc_challenge, 25-shot, log-likelihood", calibration: uncalibrated, seed_same_instrument: 66.98}
        metrics:
          - {type: acc_norm, name: "length-normalised accuracy", value: 65.87, verified: false}
        source: {name: "Converge v2 V&V pack (self-reported)", url: "https://huggingface.co/Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"}
---

# Qwen2.5-7B-Instruct — Converge Collective v2


> [!WARNING]
> **Notice (2026-10-03): a defect in v1, the release v2 is built on, has been identified and corrected.**
>
> **What was wrong.** The merge that produced v1 had an engineering defect. It weakened the base model's own weights instead of keeping them at full strength. Measured on TIGER-Lab MMLU-Pro (12,032 questions, paired with Qwen2.5-7B-Instruct in one session), v1 scores about 4 points below its base model, and its step-by-step answers are markedly shorter. v2 was built on v1 and inherits the defect from it.
>
> **What is being done.** The cause has been found and fixed in the merge. A corrected v1, built with the same recipe and the defect removed, measures at its base model's level on the same benchmark, with its answer length restored. A corrected v2, v2's exact recipe and code rebuilt on the corrected v1, has been built. Both corrected models are being benchmarked across the full board now. Their results will be published here, with per-item evidence, before either replaces this release.
>
> Until then, the results on this card describe the release as published, defect included.

> **Optitransfer · converge:** open models built to place at the top of their class on public leaderboards, from the work the open-source community has already published. Measured against the base model, published with the evidence. [About the programme](https://huggingface.co/OptiTransferData)

**What it is.** v2 is the second released state of the **converge** project: a 7.6B-parameter, training-free, weight-space merge built on [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct). No gradient training and no training data were used. It loads and prompts exactly like Qwen2.5-7B-Instruct: same architecture, tokenizer, chat template and configuration files.

- **Pre-registered headline:** on a 12-benchmark board run against Qwen2.5-7B-Instruct on identical items, v2 **improves on 2** (both calibrated against published HELM rows), **regresses on 2** (MATH Level 5 and MMLU-Pro), and shows **no measurable difference on 8**. Nothing is netted.
- **Strongest result:** GSM8K under HELM's own protocol, **87.0** vs 83.3 for Qwen2.5-7B-Instruct on the same 1,000 prompts: +3.7 points, paired 95% CI [+1.5, +5.8], exact McNemar p = 0.001. The harness reproduces HELM's published score for the base model (83.3 vs 83.0).
- **Weights:** `model.safetensors`, sha256 (LFS oid) `1c0d2060b805878a3c70126befd0d2ec128543acfac423cdf86ed85a11c01169`. The file has had this one hash since it was first uploaded, and every result on this card is pinned to these bytes.
- **Evidence:** every number on this card is recomputed from per-item outputs in the release's V&V pack. The pack is published with the leaderboard submissions, and links are added to this card when they are accepted; until then it is available on request through this repository's Community tab.

## The goal of the project

Optitransfer's converge programme aims for top placements in each model class across the public leaderboards, starting with 7B. It brings the compatible fine-tunes the open-weights community has published into a single model per class. Every release is measured against its base model on identical items and published with its regressions and per-item evidence. The construction method is proprietary; the evaluation is public. See the [programme page](https://huggingface.co/OptiTransferData).

## Lineage

| State | What it is | Measured standing |
|---|---|---|
| v1 (`Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1`, 2026-09-18) | The first release, built on Qwen2.5-7B-Instruct | From the v1 card. On v1's published weights, full GSM8K paired with Qwen2.5-7B-Instruct (lm-eval 0.4.13, 5-shot): strict-match +3.71 (improvement, answer format), flexible-extract −0.08 (no measurable difference); 30-item checks on GSM8K, ARC-Challenge and HumanEval: no measurable difference. No other benchmark has been run on v1's published weights, and v1 was not run on the v2 board. |
| **v2** (weights 2026-09-19, evaluated 2026-09-28) | The second release, built on v1 | The board on this card: 2 improvements (GSM8K-HELM +3.7, MMLU-HELM +0.47, both calibrated), 2 regressions (MATH Level 5 −5.74, MMLU-Pro −1.89), 8 with no measurable difference. |
| v3 (in progress) | The next release. The lineage is being rebuilt and benchmarked across the full board, against Qwen2.5-7B-Instruct and v2 on identical items, before release | No v3 result exists yet; nothing about v3 on this card is a measurement. |

## What is proven (MEASURED)

Each item names its evidence in the V&V pack.

1. **GSM8K under HELM's protocol: +3.7 points over the base model**, calibrated. Seed 83.3 / v2 87.0 on HELM Lite's 1,000 GSM8K requests replayed byte for byte; CI [+1.5, +5.8], p = 0.001. On the 968 items where neither model hit the 400-token cap the gain is +3.6 (p = 0.001). (`RESULTS.md`, `items/gsm8k_helm`, `raw/gsm8k_helm__*`)
2. **MMLU under HELM's protocol: +0.47 points (macro), calibrated, small and format-sensitive.** Item-level +0.57, CI [+0.11, +1.03], p = 0.016; on the 13,998 items where both models answered with a valid letter, +0.41 (p = 0.084, not significant). (`RESULTS.md` note 1)
3. **Two regressions:** MATH Level 5 −5.74 (CI [−8.23, −3.32]) and MMLU-Pro −1.89 (CI [−2.64, −1.16]). Both on uncalibrated harnesses; the paired differences are valid. (`RESULTS.md`)
4. **No measurable difference on eight benchmarks:** GSM8K lm-eval 5-shot and 0-shot CoT, MATH-500, AIME 2024+2025 (exploratory), HumanEval+, MBPP+, IFEval, ARC-Challenge.
5. **The harness is honest about itself:** it reproduces HELM's published Qwen2.5-7B-Instruct scores on GSM8K (83.3 vs 83.0) and MMLU (72.92 vs 72.87); its HELM scorers reproduce HELM's own per-instance scores on 1,000/1,000 and 14,042/14,042 of HELM's completions; both models' served weights were hashed against their published sha256 before the run. (`calibration.json`, `models.json`, `tools/helm_replay.py --selftest`)
6. **The weights are exactly what was measured:** `model.safetensors` sha256 above, unchanged from the first weight upload through the current HEAD (later commits change the README only).

## What v3 is built to deliver (EXPECTED, not a result)

- **EXPECTED:** v3 assimilates further compatible fine-tunes from the open ecosystem. It is built to raise the axes where v2 regresses (MATH Level 5, MMLU-Pro) and where v2 shows no measurable difference, while keeping v2's measured gains. It is the next iteration, and it is published with its board against both Qwen2.5-7B-Instruct and v2.
- **EXPECTED:** v3 will be published only with the same kind of V&V pack: the same instrument, Qwen2.5-7B-Instruct and v2 as paired controls on identical items, every regression reported, calibration labelled.
- No v3 score is stated here, because none has been measured.

## Public components

- **[crdt-merge](https://github.com/mgillr/crdt-merge)**: conflict-free (CRDT) merge for data, JSON, ML models and distributed agents; includes **E4 trust scoring** ([E4 architecture](https://github.com/mgillr/crdt-merge/blob/main/docs/e4/E4-MASTER-ARCHITECTURE.md)).
- **[acfa-rs](https://github.com/mgillr/acfa-rs)**: accountable federated aggregation with verifiable receipts, Apache-2.0 ([arXiv:2607.10305](https://arxiv.org/abs/2607.10305)).

ACFA receipts and E4 trust scoring were not applied to this release.

## Results: v2 vs Qwen2.5-7B-Instruct (one pinned instrument, identical items)

Both models ran on the same engine with the same prompts, items and decoding, on 2026-09-28. Scores are percent on each benchmark's primary metric.

- **v2-only / seed-only** are the discordant counts: items only v2 got right, and items only the base model got right.
- **Reading rule, fixed before the run:** a difference is an **improvement** or a **regression** only if the paired-bootstrap 95% CI excludes 0 **and** the exact McNemar p < 0.05. Anything else is "no measurable difference".
- **CALIBRATED** means our harness reproduces the published score for Qwen2.5-7B-Instruct under that exact protocol. **Uncalibrated** means no published reference with a matching protocol exists: the absolute score is specific to this harness, while the paired difference is valid on every row.

| Axis | Benchmark (protocol) | n | Qwen2.5-7B-Instruct | **v2** | Δ | 95% CI | p | v2-only / seed-only | Reading | Calibration |
|---|---|---:|---:|---:|---:|---|---:|---:|---|---|
| Math | GSM8K, HELM Lite replay (5-shot, greedy, final-number match) | 1,000 | 83.3 | **87.0** | **+3.7** | [+1.5, +5.8] | 0.0011 | 80 / 43 | **improvement** | CALIBRATED: HELM Lite v1.13.0 83.0 (ours 83.3; band ±2.38) |
| Knowledge | MMLU, HELM replay (5-shot, single letter; macro over 57 subjects) ¹ | 14,042 | 72.92 | **73.40** | **+0.47** | [+0.11, +1.03] (items) ¹ | 0.016 (items) ¹ | 576 / 496 | **improvement** ¹ | CALIBRATED: HELM MMLU v1.13.0 72.87 (ours 72.92; band ±1.0) |
| Math | MATH Level 5, 0-shot CoT, math-verify | 1,324 | 54.31 | 48.56 | **−5.74** | [−8.23, −3.32] | 6.0×10⁻⁶ | 101 / 177 | **regression** | uncalibrated |
| Knowledge | MMLU-Pro, lm-eval 5-shot CoT, exact match | 12,032 | 56.77 | 54.88 | **−1.89** | [−2.64, −1.16] | 6.5×10⁻⁷ | 920 / 1,147 | **regression** | uncalibrated |
| Math | GSM8K, lm-eval 5-shot, flexible extract | 1,319 | 87.49 | 88.32 | +0.83 | [−0.83, +2.43] | 0.375 | 69 / 58 | no measurable difference | uncalibrated |
| Math | GSM8K, lm-eval 0-shot CoT, flexible extract | 1,319 | 78.77 | 79.45 | +0.68 | [−0.76, +2.12] | 0.426 | 55 / 46 | no measurable difference | uncalibrated |
| Math | MATH-500, 0-shot CoT, math-verify | 500 | 74.8 | 73.6 | −1.2 | [−4.2, +1.8] | 0.519 | 27 / 33 | no measurable difference | uncalibrated |
| Math | AIME 2024+2025, avg@8, T 0.6 (exploratory) | 60 | 9.583 | 8.125 | −1.46 | [−3.96, +1.04] | — | — | no measurable difference | report-only |
| Code | HumanEval+, EvalPlus 0.3.1, greedy pass@1 | 164 | 75.00 | 78.05 | +3.05 | [−1.83, +7.93] | 0.332 | 11 / 6 | no measurable difference | uncalibrated ² |
| Code | MBPP+, EvalPlus 0.3.1, greedy pass@1 | 378 | 68.78 | 70.63 | +1.85 | [−1.59, +5.29] | 0.382 | 27 / 20 | no measurable difference | uncalibrated ² |
| Instruction following | IFEval, prompt-level strict | 541 | 71.53 | 73.01 | +1.48 | [−1.85, +4.62] | 0.422 | 42 / 34 | no measurable difference ³ | uncalibrated |
| Reasoning | ARC-Challenge, 25-shot, acc_norm | 1,172 | 66.98 | 65.87 | −1.11 | [−2.56, +0.34] | 0.177 | 33 / 46 | no measurable difference | uncalibrated |

**Scoreline (pre-registered): 2 improvements / 2 regressions / 8 no measurable difference.** Every benchmark on the board is reported. Regressions are not netted against improvements.

¹ **MMLU.** The scores are the macro average over 57 subjects, the calibrated aggregate on HELM's scale; its Δ is +0.47. The pre-registered paired test runs on the 14,042 items: 72.11 vs 71.54 item-level exact match, +0.57, CI [+0.11, +1.03], p = 0.016. Part of the gain is answer format: the base model gave 44 answers that are not one of the option letters A–D, v2 gave 3, and v2 answered 23 of those 44 items correctly, which accounts for 0.16 of the 0.57 points. Two further checks are not significant: on the 13,998 items where both models gave a valid letter the difference is +0.41 (p = 0.084), and a post-hoc subject-stratified bootstrap of the macro difference gives CI [−0.06, +1.01]. Treat the MMLU improvement as small and format-sensitive.

² **Code.** HumanEval+ and MBPP+ were scored with EvalPlus 0.3.1's own evaluator, the tool behind the EvalPlus leaderboard. That leaderboard has no Qwen2.5-7B-Instruct row, and the positive-control model we ran through the same instrument (CodeQwen1.5-7B-Chat, which has a leaderboard row) failed to decode its outputs and scored 0.0. So the code instrument is not calibrated: the absolute numbers are not shown to be on the leaderboard's scale. The paired comparison is unaffected (both models' outputs are decoded text, executed by EvalPlus's tests). A second session with different engine batching gave v2 78.66 / 70.37 and the base model 75.00 / 67.99: greedy decoding on vLLM is not batch-invariant.

³ **IFEval.** lm-eval 0.4.13's IFEval scorer is not fully deterministic: one checker substitutes a random letter, and language detection is unseeded. Rescoring moves the prompt-strict difference within about +0.9 to +1.8 points. The reading is "no measurable difference" either way.

**How robust the GSM8K-HELM gain is.** Removing every item where either model hit the 400-token cap leaves 968 items; there the gain is +3.6 points (p = 0.001). Mean output length is essentially unchanged: 198.0 tokens for v2 vs 199.3 for the base model.

The gain is tied to HELM's protocol. Under lm-eval's 5-shot and 0-shot CoT GSM8K protocols the flexible-extract primary metric shows no measurable difference; the 5-shot strict-match scorer shows +2.73, mostly from formatting (the base model left 59 answers without a `#### N` line, v2 left 30). Do not read the HELM result as a general "better at math" claim: MATH Level 5 regresses.

<details>
<summary>Behaviour differences worth knowing</summary>

- **Format compliance.** Malformed or unparsed answers, base model → v2: MMLU answers that are not an option letter A–D, 44 → 3; GSM8K-HELM completions with no final number, 9 → 3; GSM8K 5-shot answers without a `#### N` line, 59 → 30; MMLU-Pro unparsed answers, 48 → 79 (the one suite where v2 does worse).
- **Less answer-repetition on MMLU-Pro.** 11.9% of the base model's responses repeat "the answer is (X)" five or more times, often until the 2,048-token cap; for v2 it is 1.7%. Total generated tokens: 5.23M for the base model vs 2.39M for v2.
- **More generation-cap hits on hard math:** MATH Level 5 33 vs 22 at 4,096 tokens; MATH-500 11 vs 4; AIME 21 vs 4 of 480 samples at 16,384 tokens. The MATH Level 5 regression persists on the items both models finished: −5.9 points on 1,274 items.
- **Item-level churn.** On GSM8K-HELM, v2 fixed 80 items the base model got wrong and got 43 items wrong that the base model got right. We have not tested whether that churn is stable across runs.
</details>

<details>
<summary>Every other banked metric (secondary; many tests, no multiplicity correction; no claim rests on these)</summary>

| Benchmark, metric | Qwen2.5-7B-Instruct | v2 | Δ | 95% CI | p |
|---|---:|---:|---:|---|---:|
| MMLU (HELM), item-level exact match | 71.54 | 72.11 | +0.57 | [+0.11, +1.03] | 0.016 |
| GSM8K 5-shot, strict match (`#### N` format) | 83.32 | 86.05 | +2.73 | [+0.83, +4.62] | 0.006 |
| GSM8K 5-shot, numeric | 89.54 | 88.78 | −0.76 | [−2.27, +0.68] | 0.373 |
| GSM8K 5-shot, math-verify | 89.23 | 88.78 | −0.45 | [−1.97, +1.06] | 0.627 |
| GSM8K 0-shot CoT, numeric | 82.41 | 82.87 | +0.45 | [−0.99, +1.90] | 0.606 |
| GSM8K 0-shot CoT, math-verify | 82.03 | 83.02 | +0.99 | [−0.53, +2.50] | 0.237 |
| HumanEval, base tests | 81.71 | 84.76 | +3.05 | [−1.22, +7.93] | 0.302 |
| MBPP, base tests | 79.10 | 82.80 | +3.70 | [+0.26, +7.14] | 0.049 |
| MATH Level 5, boxed-answer match | 50.68 | 45.32 | −5.36 | [−7.78, −2.95] | 1.5×10⁻⁵ |
| MATH-500, boxed-answer match | 69.0 | 67.2 | −1.8 | [−4.8, +1.2] | 0.306 |
| ARC-Challenge, acc (unnormalised) | 64.33 | 62.54 | −1.79 | [−3.24, −0.34] | 0.022 |
| IFEval, prompt-level loose | 73.57 | 75.79 | +2.22 | [−0.92, +5.36] | 0.207 |
| IFEval, instruction-level strict / loose | 78.90 / 80.70 | 80.58 / 82.49 | +1.68 / +1.80 | — | — |
| AIME 2024 / AIME 2025, avg@8 (exploratory) | 12.08 / 7.08 | 8.75 / 7.50 | −3.33 / +0.42 | — | — |
| AIME 2024+2025, pass@8 (exploratory) | 28.33 | 25.00 | −3.33 | [−13.33, +5.00] | 0.727 |

- The GSM8K 0-shot CoT strict-match scorer is excluded: its answer pattern never matches either model's output, so it scores 0 for both.

**Majority voting on GSM8K.** 32 samples at T = 0.7 per problem, for both models. No paired test was run on these rows.

| Protocol, scorer | maj@8 seed | maj@8 v2 | Δ | maj@32 seed | maj@32 v2 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| 5-shot, flexible | 91.43 | 92.19 | +0.76 | 92.27 | 92.65 | +0.38 |
| 5-shot, strict | 91.51 | 92.12 | +0.61 | 92.12 | 92.57 | +0.45 |
| 5-shot, numeric | 92.87 | 92.27 | −0.61 | 93.48 | 92.87 | −0.61 |
| 5-shot, math-verify | 92.72 | 92.19 | −0.53 | 93.48 | 92.72 | −0.76 |
| 0-shot CoT, flexible | 81.27 | 80.67 | −0.61 | 81.05 | 81.12 | +0.08 |
| 0-shot CoT, numeric | 84.99 | 84.15 | −0.83 | 84.76 | 84.69 | −0.08 |
| 0-shot CoT, math-verify | 85.37 | 84.15 | −1.21 | 84.99 | 84.61 | −0.38 |

Voting lifts both models by similar amounts. On the numeric and math-verify scorers the base model's vote is higher.
</details>

## How v2's scores sit among published 7B-class rows

The tested claim on every axis is the paired difference between v2 and Qwen2.5-7B-Instruct. The published rows below are other projects' results for other models, shown as reference points; they are not a ranking, and no leaderboard has evaluated, listed or endorsed v2. "Protocol-matched" means the published row ran under exactly the run specification we replay. Model names, sizes and scores are as each source publishes them.

### GSM8K, HELM Lite v1.13.0 (1,000 problems, 5-shot, greedy, no stop sequence, final-number exact match). CALIBRATED.

| Model | Size | GSM8K | Source |
|---|---|---:|---|
| **Converge Collective v2** | 7B | **87.0** | our replay |
| Qwen2.5-7B-Instruct | 7B | 83.3 | our replay, same harness as v2 |
| Qwen2.5 Instruct Turbo (7B) | 7B | 83.0 | HELM published row |
| Llama 3.1 Instruct Turbo (8B) | 8B | 79.8 | HELM published row |
| Gemma 2 Instruct (9B) | 9B | 76.2 | HELM published row |
| Mistral Instruct v0.3 (7B) | 7B | 53.8 | HELM published row |

These are all the table's 6–10B rows whose run uses the same HELM adapter specification as the Qwen2.5-7B-Instruct row we replay. Eight other 6–9B rows ran with HELM's default stop sequence and are not protocol-matched: Qwen1.5 (7B) 60.0, Gemma (7B) 55.9, Llama 3 (8B) 49.9, Mistral v0.1 (7B) 37.7, Yi (6B) 37.5, Llama 2 (7B) 15.4, Falcon (7B) 5.5 and OLMo (7B) 4.4.

### MMLU, HELM MMLU v1.13.0 (14,042 questions, 57 subjects, 5-shot, single-letter answer, macro average). CALIBRATED.

| Model | Size | MMLU | Source |
|---|---|---:|---|
| Phi-3 (7B) (HELM label; microsoft/phi-3-small-8k-instruct) | 7B | 75.68 | HELM published row |
| **Converge Collective v2** | 7B | **73.40** | our replay |
| Qwen2.5-7B-Instruct | 7B | 72.92 | our replay, same harness as v2 |
| Qwen2.5 Instruct Turbo (7B) | 7B | 72.87 | HELM published row |
| Mistral Instruct v0.3 (7B) | 7B | 59.91 | HELM published row |
| Llama 3.1 Instruct Turbo (8B) | 8B | 56.06 | HELM published row |

These are all the 6–10B rows whose 57 per-subject run specifications are identical to the Qwen2.5-7B-Instruct run we replay. Nine other 6–9B rows use different prompt instructions and are excluded: Gemma 2 (9B), Llama 3 (8B), Gemma (7B), Yi (6B), Qwen1.5 (7B), Mistral v0.1 (7B), OLMo 1.7 (7B), Llama 2 (7B) and OLMo (7B).

> **About the HELM rows.** They are frozen results published by the HELM project, obtained through Together AI endpoints (Phi-3 (7B) through HELM's Hugging Face deployment). Our numbers come from a self-run replay of HELM's exact request prompts, using the published weights in bf16 on vLLM. The replay reproduces HELM's aggregate for Qwen2.5-7B-Instruct; per item it agrees with HELM's own record on 939 of 1,000 GSM8K items and 13,822 of 14,042 MMLU items, so serving differences exist. HELM has not evaluated, listed or endorsed this model.

### HumanEval+ and MBPP+, EvalPlus leaderboard snapshot of 2026-09-27 (greedy pass@1). Uncalibrated (note ²).

Rows shown: the five highest-scoring 6–9B rows on each benchmark (ties included); every general-purpose 7–8B chat model EvalPlus evaluated with its instruction prompt; and Qwen2.5-Coder-7B-Instruct, whose figure is vendor-reported and not on the snapshot. gemma-1.1-2b-it is excluded: the snapshot lists it at 7.0B, but it is a 2B model.

| Model | Size | HumanEval+ | MBPP+ | Source |
|---|---|---:|---:|---|
| Qwen2.5-Coder-7B-Instruct (code specialist) | 7B | 84.1 | 71.7 | vendor report, arXiv:2409.12186 Table 16 |
| CodeQwen1.5-7B-Chat | 7B | 78.7 | 69.0 | EvalPlus leaderboard |
| **Converge Collective v2** | 7B | **78.05** | **70.63** | our run, EvalPlus 0.3.1 |
| OpenCoder-8B-Instruct | 8B | 77.4 | 71.4 | EvalPlus leaderboard |
| Qwen2.5-7B-Instruct | 7B | 75.00 | 68.78 | our run, same harness as v2 |
| Artigenz-Coder-DS-6.7B | 6.7B | 72.6 | 69.6 | EvalPlus leaderboard |
| OpenCodeInterpreter-DS-6.7B | 6.7B | 72.0 | 66.4 | EvalPlus leaderboard |
| DeepSeek-Coder-6.7B-instruct | 6.7B | 71.3 | 65.6 | EvalPlus leaderboard |
| DeepSeek-Coder-7B-instruct-v1.5 | 7B | 71.3 | 62.2 | EvalPlus leaderboard |
| Magicoder-S-DS-6.7B | 6.7B | 71.3 | 69.0 | EvalPlus leaderboard |
| OpenChat-3.5-7B-0106 | 7B | 67.7 | 54.5 | EvalPlus leaderboard |
| Llama3.1-8B-instruct | 8B | 62.8 | 55.6 | EvalPlus leaderboard |
| Llama3-8B-instruct | 8B | 56.7 | 54.8 | EvalPlus leaderboard |
| Mistral-7B-Instruct-v0.2 | 7B | 36.0 | 37.0 | EvalPlus leaderboard |
| gemma-1.1-7b-it | 7B | 35.4 | 45.0 | EvalPlus leaderboard |
| xDAN-L1-Chat-RL-v1-7B | 7B | 32.9 | 41.3 | EvalPlus leaderboard |
| gemma-7b-it | 7B | 25.0 | 36.8 | EvalPlus leaderboard |

v2 does not differ measurably from its base model on either code benchmark. It is not a code specialist. The full list of the snapshot's 6–9B rows is in the V&V pack (`references/evalplus_results_2026-09-27.json`, `placements.json`; see **Evidence** above).

### Axes with no matched public reference

MATH-500, MATH Level 5, AIME 2024+2025, GSM8K via lm-eval, MMLU-Pro, IFEval and ARC-Challenge: we found no published table that runs other models under our protocol. The 7B comparison on these axes is Qwen2.5-7B-Instruct on identical items (the board above). We make no cross-model claim on them.

### Open LLM Leaderboard v2 protocol replication (pending)

The Open LLM Leaderboard is archived and no longer evaluates submissions. A self-run replication of its v2 protocol on v2 and on Qwen2.5-7B-Instruct, with the base model calibrated against its archived row, is being prepared. When it is banked it will appear here and in the V&V pack labelled "OLL v2 protocol replication vs the archive": a self-run comparison, not a leaderboard entry, with v2 disclosed as a merge. No numbers exist yet.

## Limitations

- **A static merge is a trade, not a lift.** v2 gains on GSM8K under HELM's protocol and, slightly, on MMLU. It loses on MATH Level 5 and MMLU-Pro. Eight benchmarks show no measurable difference.
- **Weaker than the base model on MATH Level 5 and MMLU-Pro** (see the board). On MMLU-Pro v2 also leaves more answers unparsed (79 vs 48), although it repeats itself far less (responses repeating "the answer is (X)" five or more times: 1.7% vs 11.9%). On hard math it hits the generation cap more often (MATH Level 5: 33 vs 22 at 4,096 tokens; AIME: 21 vs 4 of 480 samples at 16,384 tokens); the MATH Level 5 regression persists on the 1,274 items both models finished (−5.9 points).
- **Not a code specialist.** HumanEval+ and MBPP+ show no measurable difference from the base model, and the code harness is not calibrated.
- **Not a long-context model.** It is configured for 32,768 tokens (`max_position_embeddings`; no rope scaling). `tokenizer_config.json` inherits `model_max_length: 131072` from the base model; that value is not v2's configured context. A reduced-size long-context reading under a rope-scaling override that is not in the published config is in progress; it is incomplete and uncalibrated, and no long-context claim is made.
- **Identifies as Qwen.** With no system message, the inherited chat template inserts "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." The model may describe itself as Qwen.
- **Default decoding samples.** The repository's generation settings sample (T 0.7, top_p 0.8, top_k 20, repetition penalty 1.05). The board's scores are greedy, except the AIME and majority-vote rows.
- **Self-reported results.** These are first-party evaluations by the model's developers, backed by per-item outputs in the V&V pack (see **Evidence** above). Item-level churn between the two models is real (GSM8K-HELM: 80 items fixed, 43 broken); whether it is stable across runs has not been tested.
- **Contamination.** v2 was not built by optimising on any of these test sets. The source models' training data is third-party and cannot be certified free of benchmark contamination.
- **Not evaluated for safety, bias or toxicity.** Evaluated in English only. It may produce incorrect, biased or harmful content; do not use it for high-stakes decisions without independent evaluation.

## Quick start

v2 loads and prompts exactly like Qwen2.5-7B-Instruct. The board's greedy scores were produced in bfloat16.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(
    repo, dtype=torch.bfloat16, device_map="auto"  # use torch_dtype= on older transformers
)

messages = [{"role": "user", "content": "A train travels 180 km in 2.5 hours. What is its average speed in km/h?"}]
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(text, return_tensors="pt").to(model.device)

# Greedy, as evaluated. The repo's generation_config samples by default (T=0.7, top_p=0.8, top_k=20, repetition_penalty=1.05).
out = model.generate(**inputs, max_new_tokens=512, do_sample=False, repetition_penalty=1.0)
print(tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2",
    dtype="bfloat16",
    max_model_len=32768,
    generation_config="vllm",  # ignore the repo's sampling defaults, as in our evaluation
)
params = SamplingParams(temperature=0.0, max_tokens=512)
out = llm.chat([{"role": "user", "content": "Explain the difference between a list and a tuple in Python."}], params)
print(out[0].outputs[0].text)
```

## Evaluation setup

- **Models:** v2 (`model.safetensors` sha256 `1c0d2060b805878a3c70126befd0d2ec128543acfac423cdf86ed85a11c01169`) and Qwen/Qwen2.5-7B-Instruct at revision `a09a35458c702b33eeacc393d103063234e8bc28` (the control), on identical items. Before the run the served weight bytes of both were checked against their sha256.
- **Engine:** vLLM 0.30.0, bfloat16, `max_model_len` 32,768, seed 1234, prefix caching on, one NVIDIA A100-SXM4-80GB (driver 580.82.07, CUDA 13.0). HumanEval+ and MBPP+ ran through EvalPlus's own vLLM provider (`max_model_len` 2,048). Software: Python 3.13.15, torch 2.13.0, transformers 5.17.0, lm-eval 0.4.13, EvalPlus 0.3.1, math-verify 0.9.0, datasets 4.8.5. The build was checked against these pins before any run.
- **Prompt format:** GSM8K-HELM and MMLU-HELM: HELM's own request text, sent as one user turn. GSM8K 0-shot CoT, MATH, IFEval and AIME: the chat template. GSM8K 5-shot, ARC-Challenge and MMLU-Pro: plain completion, chat template off. HumanEval+ and MBPP+: EvalPlus's own instruct prompting. Where the chat template was used no system prompt was passed, so the template's default applied.
- **Decoding:** greedy (temperature 0, top_p 1, top_k off, repetition penalty 1.0), except AIME (8 samples at T 0.6, top_p 0.95, up to 16,384 new tokens) and the majority-vote rows (32 samples at T 0.7). The repository's `generation_config.json` sampling defaults were disabled.
- **Generation budgets (max new tokens):** GSM8K-HELM 400; GSM8K 5-shot and 0-shot CoT 1,024; HumanEval+ and MBPP+ 768; MATH 4,096; IFEval 1,280; MMLU-Pro 2,048; MMLU-HELM 1; ARC-Challenge log-likelihood scoring, no generation.
- **Data:** GSM8K and MMLU replay HELM's published request files (sha256 in the V&V pack). Pinned Hugging Face dataset revisions: openai/gsm8k `740312a`, HuggingFaceH4/MATH-500 `6e4ed1a`, EleutherAI/hendrycks_math `21a5633`, allenai/ai2_arc `210d026`, google/IFEval `966cd89`, Maxwell-Jia/AIME_2024 `8d88b28`, math-ai/aime25 `563bb84` and TIGER-Lab/MMLU-Pro `b189ec7`. HumanEval+ v0.1.10 and MBPP+ v0.2.0 from EvalPlus 0.3.1.
- **Statistics:** paired bootstrap, 10,000 resamples, 95% percentile CI; exact two-sided McNemar test on the same items; the reading rule was fixed in the evaluation code before the run. The run's own code computed the paired test for GSM8K-HELM, MATH-500, HumanEval+ and AIME; for the other rows the same test, with the same method and seed, was computed after the run from the banked per-item outputs. Every number on this card is recomputed from the per-item outputs by the pack's `tools/vv_stats.py`, and the pack's `MANIFEST.json` gives the sha256 of every file.
- **Checks:** every suite completed with full item coverage, identical item sets for both models, a passing decoding audit and no voided blocks.
- **Evaluation date:** 2026-09-28.
- **Reproduction:** with public tools only (lm-eval, EvalPlus, vLLM and HELM's request files); see `REPRODUCE.md` in the V&V pack (see **Evidence** above).

## Model details

| | |
|---|---|
| Architecture | Qwen2ForCausalLM (Qwen2.5-7B-Instruct's), 28 layers, hidden size 3,584 |
| Parameters | 7,615,616,512 |
| Weights | one `model.safetensors`, 15,231,271,784 bytes, stored as float16 |
| Configured context | 32,768 tokens (`max_position_embeddings`; RoPE θ = 1,000,000; no rope scaling) |
| Unchanged from Qwen2.5-7B-Instruct | `config.json`, `generation_config.json`, `tokenizer.json`, `tokenizer_config.json`, all byte-identical |
| Training | none: no fine-tuning, no gradient training, no training data |

- **dtype note.** `config.json` declares `torch_dtype: bfloat16`, unchanged from the base model, while the stored tensors are float16. All reported results loaded the weights in bfloat16. Float16 inference was not evaluated.
- **File hashes (sha256):** `config.json` `7463bb0ea78315365e6c6b74de4e73bbcc8359dfb0c5a737584e077d42c0b03c`; `generation_config.json` `3a8f9087e486054c8a4a08dae2e5a3ba62e23da212b5b8c08bc42cb983c3459f`; `tokenizer.json` `c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539`; `tokenizer_config.json` `5b5d4f65d0acd3b2d56a35b56d374a36cbc1c8fa5cf3b3febbbfabf22f359583`.
- **Check a download** against the `model.safetensors` sha256 above. A card-only commit changes the revision hash, not the weights.

## License

This model descends, through v1, from facebook/opt-2.7b. That model is distributed under the [OPT-175B License Agreement](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/MODEL_LICENSE.md), which limits use to non-commercial research. This model is therefore made available **for non-commercial research use only**, subject to three sets of terms:

- the OPT-175B License Agreement;
- the Apache-2.0 licenses of the Qwen, Mistral, SmolLM2, Granite and Pythia sources;
- the MIT licenses of microsoft/phi-2 and microsoft/Phi-3-mini-4k-instruct.

No rights are granted beyond those licenses. OPT-175B is licensed under the OPT-175B license, Copyright (c) Meta Platforms, Inc. All Rights Reserved.

`model.safetensors` is modified relative to every source model. `config.json`, `generation_config.json`, `tokenizer.json` and `tokenizer_config.json` are Qwen2.5-7B-Instruct's files, unmodified.

Not affiliated with or endorsed by Alibaba Cloud, the Qwen team, the HELM project or EvalPlus. "Qwen" is used only to identify the model this one is derived from.

## Corrections

Earlier versions of this card contained the following, now withdrawn; they should not be relied on:

- an `apache-2.0` license declaration;
- build-process statements;
- a lineage count;
- an evaluation table that is not hash-linked to these weights.

The weights have not changed since the first weight upload.
