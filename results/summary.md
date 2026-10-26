# Mining results

Generated 2026-10-26 16:22 UTC from 10002 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 9999 | 22380 |
| nodes_in_sample | 9999 | 9999 |
| edges | 10587 | 24613 |
| relations | {'finetune': 3948, 'adapter': 2507, 'quantized': 2693, 'merge': 1428, 'unknown': 11} | {'finetune': 8498, 'adapter': 6601, 'quantized': 5211, 'merge': 4287, 'unknown': 16} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 5822 | 20296 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 556 |
| leaves | 9080 | 20840 |
| multi_parent_nodes | 351 | 1009 |
| temporal_anomaly_edges | 20 | 20 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 37 | 2.228e-10 | 20 | 1 |  |
| Weighted PageRank | 52 | 4.155e-10 | 20 | 1 |  |
| HITS authority | 174 | 3.681e-10 | 20 | 0.9295 | 0.9397 |
| HITS hub | 174 | 3.735e-13 | 20 | 0.9972 | 0.9397 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 78 | 1.053e-09 | 20 | 1 |  |
| Weighted PageRank | 52 | 9.705e-10 | 20 | 1 |  |
| HITS authority | 192 | 1.839e-10 | 20 | 0.9896 | 0.9446 |
| HITS hub | 192 | 5.12e-13 | 20 | 0.9991 | 0.9446 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06709 | 0.04594 | 3 | 6.202e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06547 | 0.05938 | 2 | 0.002087 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05 | 0.01729 | 8 | 3.524e-05 | 1.047e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04841 | 0.01588 | 9 | 0.0003008 | 3.523e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03481 | 0.06845 | 1 | 0.4781 | 0 | 1102 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03198 | 0.008546 | 18 | 4.214e-76 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03053 | 0.02944 | 5 | 5.631e-13 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02865 | 0.01528 | 10 | 3.862e-11 | 9.507e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02361 | 2.04e-05 | 1508 | 7.218e-07 | 5.949e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02134 | 0.022 | 7 | 1.355e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01865 | 0.01478 | 11 | 3.774e-25 | 2.287e-30 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.0133 | 0.02984 | 4 | 8.388e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01214 | 0.02634 | 6 | 2.678e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01068 | 2.931e-05 | 1048 | 4.449e-08 | 5.079e-07 | 3 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | google/gemma-2-9b-it | 0.008073 | 0.01285 | 12 | 1.306e-08 | 4.521e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 16 | Qwen/Qwen2.5-Coder-7B | 0.007897 | 0.00475 | 27 | 4.831e-07 | 1.047e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007382 | 0.0003445 | 73 | 1.122e-06 | 8.156e-10 | 48 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.007011 | 0.006167 | 25 | 9.904e-07 | 1.047e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006911 | 1.923e-05 | 9317 | 0 | 5.079e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006882 | 0.01211 | 13 | 4.834e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06767 | 0.04719 | 4 | 1.055e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06594 | 0.05318 | 2 | 0.007144 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04997 | 0.001999 | 20 | 6.923e-06 | 1.032e-09 | 63 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04843 | 0.00166 | 22 | 0.0002186 | 6.986e-06 | 47 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03647 | 0.05891 | 1 | 0.9218 | 0 | 1101 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03206 | 0.02167 | 10 | 4.036e-62 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03068 | 0.03581 | 5 | 2.589e-58 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02874 | 0.00338 | 15 | 5.959e-60 | 2.532e-61 | 79 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02362 | 5.413e-05 | 919 | 7.393e-09 | 6.77e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02137 | 0.02956 | 8 | 3.001e-88 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01866 | 0.008974 | 11 | 4.801e-90 | 2.935e-91 | 221 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01369 | 0.05068 | 3 | 5.979e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01229 | 0.0325 | 6 | 1.059e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01069 | 0.0001012 | 527 | 4.272e-08 | 2.137e-07 | 3 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | google/gemma-2-9b-it | 0.008122 | 0.006917 | 12 | 2.282e-08 | 1.036e-08 | 170 | 1213 | google/gemma-2-9b | gemma | True |
| 16 | Qwen/Qwen2.5-Coder-7B | 0.007948 | 0.001337 | 27 | 3.543e-08 | 1.032e-09 | 22 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007392 | 0.000853 | 33 | 8.041e-08 | 3.465e-11 | 48 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.007108 | 0.00136 | 25 | 9.028e-08 | 1.032e-09 | 30 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006915 | 4.742e-05 | 8696 | 0 | 2.137e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006912 | 0.03006 | 7 | 5.121e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.00132 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.00132 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.00132 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 64, 'modularity': 0.9049736409300017, 'largest': 1263, 'weighted_purity': 0.9996999699969997, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1263 | 1263 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1291 | 288 | 315 | 368 | 311 | permissive |
| 1 | 1218 | 1218 | Qwen/Qwen2.5-7B | 0.9975 | 3 | Qwen/Qwen2.5-7B | 1461 | 355 | 326 | 346 | 434 | permissive |
| 2 | 1131 | 1131 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1134 | 335 | 313 | 449 | 37 | restricted |
| 3 | 1008 | 1008 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1017 | 311 | 316 | 347 | 43 | restricted |
| 4 | 726 | 726 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 730 | 313 | 301 | 103 | 12 | permissive |
| 5 | 645 | 645 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 653 | 327 | 162 | 146 | 17 | permissive |
| 6 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 7 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 8 | 482 | 482 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 485 | 312 | 71 | 93 | 9 | restricted |
| 9 | 396 | 396 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 396 | 309 | 25 | 62 | 0 | unknown |
| 10 | 235 | 235 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 249 | 59 | 61 | 73 | 56 | restricted |
| 11 | 232 | 232 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 240 | 73 | 73 | 75 | 19 | restricted |
| 12 | 190 | 190 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 256 | 24 | 19 | 66 | 147 | unknown |
| 13 | 188 | 188 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 220 | 23 | 25 | 61 | 111 | permissive |
| 14 | 145 | 145 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 144 | 49 | 46 | 49 | 0 | permissive |
| 15 | 102 | 102 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 104 | 19 | 21 | 37 | 27 | permissive |
| 16 | 90 | 90 | meta-llama/Llama-3.2-1B | 1 | 1 | dphn/Dolphin3.0-Llama3.2-1B | 114 | 6 | 2 | 29 | 77 | restricted |
| 17 | 85 | 85 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 84 | 72 | 8 | 4 | 0 | permissive |
| 18 | 76 | 76 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 75 | 24 | 25 | 22 | 4 | permissive |
| 19 | 69 | 69 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 68 | 25 | 18 | 25 | 0 | permissive |
| 20 | 56 | 56 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 55 | 25 | 6 | 24 | 0 | permissive |
| 21 | 54 | 54 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 53 | 18 | 18 | 17 | 0 | permissive |
| 22 | 34 | 34 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 33 | 17 | 11 | 5 | 0 | permissive |
| 23 | 33 | 33 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 32 | 9 | 6 | 17 | 0 | permissive |
| 24 | 26 | 26 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt | 25 | 22 | 3 | 0 | 0 | permissive |
| 25 | 24 | 24 | microsoft/phi-2 | 1 | 1 | ma921/phi-2-sft-golden-hh | 23 | 22 | 0 | 1 | 0 | permissive |
| 26 | 23 | 23 | google/gemma-3-4b-pt | 1 | 1 | google/medgemma-4b-pt | 22 | 16 | 1 | 5 | 0 | other |
| 27 | 22 | 22 | google/gemma-3-4b-pt | 1 | 1 | CEIA-UFG/Gemma-3-Gaia-PT-BR-4b-it | 21 | 1 | 0 | 19 | 1 | restricted |
| 28 | 21 | 21 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 20 | 17 | 1 | 2 | 0 | permissive |
| 29 | 18 | 18 | google/gemma-3-4b-pt | 1 | 1 | MBZUAI-Paris/Nile-Chat-4B | 17 | 5 | 5 | 7 | 0 | unknown |
| 30 | 18 | 18 | Qwen/Qwen3-8B-Base | 1 | 1 | McGill-NLP/AfriqueQwen-8B | 17 | 2 | 13 | 2 | 0 | permissive |
| 31 | 18 | 18 | Qwen/Qwen3-8B-Base | 1 | 1 | jackf857/qwen3-8b-base-sft-ultrachat-4xh200-batch-128 | 17 | 17 | 0 | 0 | 0 | unknown |
| 32 | 18 | 18 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 17 | 17 | 0 | 0 | 0 | unknown |
| 33 | 15 | 15 | Qwen/Qwen3-8B-Base | 1 | 1 | formalmathatepfl/qwen3-cpt | 14 | 14 | 0 | 0 | 0 | other |
| 34 | 13 | 13 | Qwen/Qwen2.5-7B | 1 | 1 | Tsunami-th/Tsunami-1.0-7B-Instruct | 12 | 2 | 0 | 6 | 4 | permissive |
| 35 | 13 | 13 | google/gemma-2-9b | 1 | 1 | aisingapore/Gemma-SEA-LION-v3-9B | 12 | 5 | 1 | 6 | 0 | restricted |
| 36 | 12 | 12 | meta-llama/Llama-3.2-1B | 1 | 1 | jkminder/lorentz-logitlens-paraphrase-stage1-l0.7 | 11 | 11 | 0 | 0 | 0 | restricted |
| 37 | 11 | 11 | meta-llama/Llama-3.1-8B | 1 | 1 | fdtn-ai/Foundation-Sec-8B | 10 | 3 | 3 | 3 | 1 | permissive |
| 38 | 10 | 10 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 9 | 3 | 3 | 3 | 0 | permissive |
| 39 | 10 | 10 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 9 | 3 | 3 | 3 | 0 | permissive |

*… 24 more rows in the CSV*

**cross_family_links**

| child | parent | relation | child_family | parent_family |
|---|---|---|---|---|
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2 | microsoft/phi-2 | merge | Qwen/Qwen2.5-7B | microsoft/phi-2 |
| Optitransfer/Qwen2.5-7B-Instruct-converge-v1remerge-maskn_project | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1 | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Haker18/Llama-Gemma-Hybrid-9B | meta-llama/Llama-3.1-8B | merge | google/gemma-2-9b | meta-llama/Llama-3.1-8B |
| Davidsv/CosmeticVentureV2 | mistralai/Mistral-7B-v0.1 | merge | meta-llama/Llama-3.1-8B | mistralai/Mistral-7B-v0.1 |
| Abigail45/Chyio | Qwen/Qwen2.5-7B-Instruct | merge | meta-llama/Llama-3.1-8B | Qwen/Qwen2.5-7B |

## 3. Lineage

max generation 17, mean generation of derived models 1.43, models per generation {0: 10, 1: 6496, 2: 3154, 3: 224, 4: 55, 5: 17, 6: 5, 7: 3, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 5, 14: 7, 15: 4, 16: 3, 17: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 673.1 | 13485 | 6952 | 1184 | 664 |
| 1 | 6496 | 763 | 0.1177 | 5.314 | 0 | 7302 | 0.5242 | 15459 | 12620 | 5010 | 1374 |
| 2 | 3154 | 486 | 0.1542 | 6.301 | 0 | 5360 | 0.09258 | 13032 | 3863 | 2163 | 798 |
| 3 | 224 | 64 | 0.2909 | 0.8136 | 0 | 14 | 0.2812 | 5 | 3 | 111 | 60 |
| 4 | 55 | 17 | 0.3091 | 1.127 | 0 | 8 | 0.3455 | 3 | 0 | 40 | 19 |
| 5 | 17 | 7 | 0.4118 | 1.765 | 0 | 10 | 0.6471 | 0 | 0 | 18 | 12 |
| 6 | 5 | 2 | 0.4 | 3.6 | 0 | 14 | 2.8 | 0 | 0 | 5 | 13 |
| 7 | 3 | 2 | 0.6667 | 3 | 4 | 5 | 1.667 | 0 | 0 | 5 | 4 |
| 8 | 2 | 1 | 0.5 | 2 | 2 | 4 | 2 | 0 | 0 | 1 | 3 |
| 9 | 2 | 1 | 0.5 | 2 | 2 | 4 | 2 | 0 | 0 | 2 | 2 |
| 10 | 3 | 1 | 0.3333 | 1 | 0 | 3 | 1 | 0 | 0 | 2 | 1 |
| 11 | 3 | 1 | 0.3333 | 2 | 0 | 6 | 2 | 0 | 0 | 2 | 4 |
| 12 | 3 | 1 | 0.3333 | 2 | 0 | 6 | 2 | 0 | 0 | 2 | 4 |
| 13 | 5 | 3 | 0.6 | 2.6 | 3 | 6 | 2.6 | 0 | 0 | 6 | 7 |
| 14 | 7 | 1 | 0.1429 | 0.7143 | 0 | 5 | 0.7143 | 0 | 0 | 2 | 3 |
| 15 | 4 | 2 | 0.5 | 1.5 | 1.5 | 3 | 0.75 | 0 | 0 | 5 | 1 |
| 16 | 3 | 1 | 0.3333 | 1 | 0 | 3 | 1 | 0 | 0 | 2 | 1 |
| 17 | 3 | 1 | 0.3333 | 1.333 | 0 | 4 | 0 | 0 | 0 | 2 | 2 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 41984 | 3948 | 0.5456 | 0.3733 |
| adapter | 23438 | 2507 | 0.3046 | 0.237 |
| quantized | 8562 | 2693 | 0.1113 | 0.2546 |
| merge | 2972 | 1428 | 0.03862 | 0.135 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 5552 |
| child_unknown | 2882 |
| loosened | 723 |
| changed_same_category | 555 |
| parent_unknown | 415 |
| changed_custom | 271 |
| tightened | 189 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 0 |
| noncommercial | 0 | 42 | 0 | 3 | 3 | 30 |
| other | 0 | 2 | 62 | 7 | 0 | 19 |
| permissive | 16 | 59 | 147 | 3794 | 68 | 1700 |
| restricted | 12 | 46 | 115 | 705 | 2207 | 1133 |
| unknown | 0 | 0 | 3 | 32 | 6 | 374 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 36 | 30 | 622 | 0 | 138 | 673 | 5 | 1504 | 0.09543 | 0 |
| Qwen/Qwen3-8B-Base | 27 | 36 | 208 | 0 | 54 | 645 | 11 | 981 | 0.1029 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 27 | 1 | 280 | 153 | 5 | 406 | 28 | 900 | 0.3398 | 0.2488 |
| google/gemma-3-4b-pt | 19 | 0 | 258 | 164 | 9 | 363 | 3 | 816 | 0.3388 | 0.2987 |
| meta-llama/Llama-3.1-8B | 28 | 79 | 379 | 154 | 125 | 742 | 14 | 1521 | 0.2704 | 0.1514 |
| meta-llama/Llama-3.2-1B | 48 | 10 | 263 | 250 | 32 | 762 | 3 | 1368 | 0.2898 | 0.233 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 14 | 98 | 484 | 2 | 37 | 959 | 46 | 1640 | 0.143 | 0.001787 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 70 | 147 | 968 | 93 | 21 | 1173 | 35 | 2507 | 0.2273 | 0.06126 |
| finetune | 120 | 300 | 753 | 359 | 61 | 2253 | 102 | 3948 | 0.2811 | 0.1146 |
| merge | 16 | 35 | 931 | 41 | 131 | 238 | 36 | 1428 | 0.3497 | 0.112 |
| quantized | 64 | 73 | 227 | 230 | 202 | 1881 | 16 | 2693 | 0.1692 | 0.1016 |
| unknown | 1 | 0 | 3 | 0 | 0 | 7 | 0 | 11 | 0.125 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 2024-mcm-everitt-ryan/gemma-2-9b-job-bias-qlora-seq-cls | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-CA/gem-monika-ddlc-9b-v1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-CA/gem-monika-ddlc-9b-v1-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-Narra/gemma-2-9b-tagalog-chat | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-Narra/gemma-2-9b-tagalog-chat-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-SY/gemma-2-9b-dt2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-SY/gemma-2-9b-dt2-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922CA/gemma-2-9b-etude-2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922CA/gemma-2-9b-etude-2-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| AhmedSaghir/doc_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AlekseyCalvin/LYRICAL_MT_ru2en_TowerPlus9b | Unbabel/Tower-Plus-9B | finetune | google/gemma-2-9b | apache-2.0 | cc-by-nc-sa-4.0 |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cannae-AI/TANIT-V0.5-Medium-9B-IT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cesarbasurto/FullNameSplit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cran-May/Apollo2-9B-Q5_K_M-GGUF | FreedomIntelligence/Apollo2-9B | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/gemma2-9b_law_with_val_1_epoch_callback_v3.7 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati_v1 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Deeokay/gemma2-9B-GGUF | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Denisijcu/Vertex-Core-Gemma | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Devavrat28/Gemmarathi2 | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| DiTy/gemma-2-9b-it-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| DiTy/gemma-2-9b-it-russian-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Diluzx/gemma-2-9b-bnb-4bit | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Erland/Gemma_Reward_Merged | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Futuresony/future_12_10_2024 | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Himalayan-wildcat/gemma-2-9b-finetune | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| Hizaneko/gemma-2-9b-nyan100 | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Jaamie/gemma-mental-health-qlora | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Jaamie/gemma_mental_health_qlora_v2 | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Jiangxz/Tax_Model | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Kohsaku/gemma-2-9b-finetune-4 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| Koomemartin/unsloth-gemma2-9b-version3-100k | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | mit | gemma |
| Melinne/QConception-Qwen2 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| MichiganNLP/hacking-fairness-benchmarks-gemma-2-9b-z1 | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| MohammadAbuSaleh/gemma2-9b-lora-finetuned-for-llm | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Naotaka/gemma-2-9b-r16-768-512-it_lora | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |

*… 683 more rows in the CSV*

## 5. Trends

Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. The sample favours well-downloaded models, so recent quarters are under-counted. Compare shares, not totals.

**trend_family_quarterly**

| quarter | Qwen/Qwen2.5-7B | Qwen/Qwen3-8B-Base | deepseek-ai/DeepSeek-R1 | google-bert/bert-base-uncased | google/gemma-2-9b | google/gemma-3-4b-pt | meta-llama/Llama-3.1-8B | meta-llama/Llama-3.2-1B | microsoft/phi-2 | mistralai/Mistral-7B-v0.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 11 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 180 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 440 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 18 | 0 | 0 | 0 | 196 | 206 |
| 2024-Q3 | 73 | 0 | 0 | 26 | 217 | 0 | 256 | 27 | 33 | 69 |
| 2024-Q4 | 207 | 0 | 0 | 45 | 154 | 0 | 230 | 279 | 25 | 135 |
| 2025-Q1 | 321 | 0 | 457 | 62 | 81 | 92 | 286 | 293 | 27 | 118 |
| 2025-Q2 | 164 | 153 | 25 | 63 | 172 | 190 | 169 | 242 | 76 | 87 |
| 2025-Q3 | 153 | 134 | 30 | 49 | 29 | 147 | 89 | 183 | 53 | 180 |
| 2025-Q4 | 48 | 104 | 2 | 49 | 45 | 85 | 76 | 125 | 53 | 25 |
| 2026-Q1 | 72 | 99 | 12 | 28 | 65 | 98 | 50 | 52 | 23 | 33 |
| 2026-Q2 | 74 | 152 | 2 | 21 | 57 | 70 | 78 | 64 | 11 | 24 |
| 2026-Q3 | 121 | 224 | 10 | 65 | 26 | 78 | 134 | 48 | 7 | 16 |
| 2026-Q4 | 24 | 91 | 0 | 36 | 10 | 41 | 21 | 9 | 4 | 7 |

**trend_task_quarterly**

| quarter | fill-mask | image-text-to-text | other | question-answering | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2023-Q2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2023-Q3 | 2 | 0 | 4 | 1 | 0 | 2 | 11 |
| 2023-Q4 | 8 | 1 | 0 | 1 | 0 | 6 | 219 |
| 2024-Q1 | 11 | 0 | 4 | 1 | 0 | 8 | 647 |
| 2024-Q2 | 16 | 0 | 6 | 0 | 7 | 4 | 421 |
| 2024-Q3 | 10 | 3 | 6 | 5 | 6 | 9 | 662 |
| 2024-Q4 | 13 | 0 | 14 | 19 | 11 | 21 | 997 |
| 2025-Q1 | 15 | 74 | 115 | 27 | 25 | 135 | 1346 |
| 2025-Q2 | 14 | 167 | 43 | 13 | 7 | 73 | 1024 |
| 2025-Q3 | 21 | 133 | 27 | 3 | 2 | 34 | 827 |
| 2025-Q4 | 19 | 63 | 20 | 8 | 8 | 32 | 462 |
| 2026-Q1 | 10 | 55 | 65 | 2 | 8 | 18 | 374 |
| 2026-Q2 | 8 | 33 | 42 | 0 | 8 | 12 | 450 |
| 2026-Q3 | 6 | 33 | 43 | 5 | 6 | 51 | 585 |
| 2026-Q4 | 6 | 10 | 18 | 1 | 13 | 21 | 174 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 12 | 0 | 0 | 7 |
| 2023-Q4 | 86 | 97 | 3 | 0 | 49 |
| 2024-Q1 | 250 | 227 | 97 | 7 | 90 |
| 2024-Q2 | 129 | 187 | 67 | 3 | 68 |
| 2024-Q3 | 121 | 211 | 51 | 0 | 318 |
| 2024-Q4 | 156 | 364 | 90 | 0 | 465 |
| 2025-Q1 | 415 | 679 | 156 | 0 | 487 |
| 2025-Q2 | 197 | 657 | 88 | 0 | 399 |
| 2025-Q3 | 248 | 358 | 200 | 0 | 241 |
| 2025-Q4 | 162 | 278 | 28 | 0 | 144 |
| 2026-Q1 | 151 | 199 | 19 | 0 | 163 |
| 2026-Q2 | 195 | 216 | 26 | 5 | 111 |
| 2026-Q3 | 324 | 297 | 11 | 1 | 96 |
| 2026-Q4 | 62 | 130 | 15 | 1 | 35 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.05 | 0.6 | 0 | 0 | 0.35 |
| 2023-Q4 | 0.366 | 0.413 | 0.013 | 0 | 0.209 |
| 2024-Q1 | 0.373 | 0.338 | 0.145 | 0.01 | 0.134 |
| 2024-Q2 | 0.284 | 0.412 | 0.148 | 0.007 | 0.15 |
| 2024-Q3 | 0.173 | 0.301 | 0.073 | 0 | 0.454 |
| 2024-Q4 | 0.145 | 0.339 | 0.084 | 0 | 0.433 |
| 2025-Q1 | 0.239 | 0.391 | 0.09 | 0 | 0.28 |
| 2025-Q2 | 0.147 | 0.49 | 0.066 | 0 | 0.298 |
| 2025-Q3 | 0.237 | 0.342 | 0.191 | 0 | 0.23 |
| 2025-Q4 | 0.265 | 0.454 | 0.046 | 0 | 0.235 |
| 2026-Q1 | 0.284 | 0.374 | 0.036 | 0 | 0.306 |
| 2026-Q2 | 0.353 | 0.391 | 0.047 | 0.009 | 0.201 |
| 2026-Q3 | 0.444 | 0.407 | 0.015 | 0.001 | 0.132 |
| 2026-Q4 | 0.255 | 0.535 | 0.062 | 0.004 | 0.144 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 10002 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 2832 | 28.3 % |
| missing pipeline_tag (as published) | 3970 | 39.7 % |
|   of which filled from parent | 3969 | see pipeline_tag_source |
| missing library_name | 1625 | 16.2 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 12947 |  |
|   linked by HF | 11837 | 91.4 % |
|   old name of a renamed repo | 725 | 5.6 % |
|   not linked (broken parent link) | 385 | 3.0 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 10378 | 100.0 % of 10378 |
| tag edges to a parent outside the sample | 2086 | 16.5 % |
| child created >7 days before its parent | 20 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.6% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 96% |
