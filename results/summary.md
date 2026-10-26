# Mining results

Generated 2026-10-26 18:02 UTC from 12004 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 11996 | 22425 |
| nodes_in_sample | 11996 | 11996 |
| edges | 12734 | 24953 |
| relations | {'finetune': 4736, 'adapter': 2873, 'quantized': 3400, 'merge': 1709, 'unknown': 16} | {'finetune': 8498, 'adapter': 6604, 'quantized': 5212, 'merge': 4618, 'unknown': 21} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 6931 | 20340 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 601 |
| leaves | 11051 | 20832 |
| multi_parent_nodes | 441 | 1118 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 47 | 1.804e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 2.422e-10 | 20 | 1 |  |
| HITS authority | 169 | 3.902e-10 | 20 | 0.9209 | 0.9381 |
| HITS hub | 169 | 3.913e-13 | 20 | 0.9978 | 0.9381 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 77 | 8.899e-10 | 20 | 1 |  |
| Weighted PageRank | 52 | 9.567e-10 | 20 | 1 |  |
| HITS authority | 186 | 1.819e-10 | 20 | 0.9886 | 0.9428 |
| HITS hub | 186 | 5.029e-13 | 20 | 0.9992 | 0.9428 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06814 | 0.04578 | 3 | 5.935e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06443 | 0.05922 | 2 | 0.002042 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05062 | 0.01727 | 8 | 3.356e-05 | 1.001e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04766 | 0.01589 | 9 | 0.0002883 | 3.445e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03412 | 0.0682 | 1 | 0.4755 | 0 | 1107 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.0312 | 0.008544 | 18 | 4.489e-74 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03014 | 0.02932 | 5 | 5.265e-13 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02835 | 0.01515 | 10 | 3.621e-11 | 8.884e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02303 | 2.039e-05 | 1561 | 7.11e-07 | 5.662e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02106 | 0.02198 | 7 | 3.692e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01847 | 0.01477 | 11 | 1.028e-24 | 6.229e-30 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01294 | 0.02971 | 4 | 7.897e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01209 | 0.02633 | 6 | 2.604e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01041 | 4.47e-05 | 619 | 9.235e-08 | 4.865e-07 | 8 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008748 | 0.004736 | 27 | 4.636e-07 | 1.001e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008156 | 0.01285 | 12 | 1.256e-08 | 4.394e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007207 | 0.0003989 | 66 | 1.189e-06 | 7.823e-10 | 55 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006914 | 0.006166 | 25 | 9.392e-07 | 1.001e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006742 | 1.923e-05 | 9366 | 0 | 4.865e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006714 | 0.0121 | 13 | 4.739e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06872 | 0.04522 | 4 | 1.039e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06498 | 0.04998 | 2 | 0.006902 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05054 | 0.00257 | 20 | 6.905e-06 | 1.016e-09 | 100 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04773 | 0.002051 | 23 | 0.000214 | 6.748e-06 | 66 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03591 | 0.05494 | 1 | 0.9177 | 0 | 1106 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03128 | 0.01741 | 10 | 1.079e-60 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03034 | 0.03677 | 5 | 5.559e-57 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02851 | 0.006257 | 15 | 1.701e-58 | 5.435e-60 | 187 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02304 | 4.347e-05 | 945 | 7.369e-09 | 6.75e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02109 | 0.03193 | 7 | 5.051e-64 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01849 | 0.01557 | 11 | 3.36e-62 | 4.938e-67 | 479 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01335 | 0.04888 | 3 | 8.048e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01223 | 0.03417 | 6 | 1.016e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01044 | 0.0001568 | 247 | 4.232e-08 | 2.092e-07 | 8 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.00883 | 0.001984 | 24 | 3.657e-08 | 1.016e-09 | 48 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008223 | 0.01124 | 12 | 2.683e-08 | 9.932e-09 | 344 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007222 | 0.0008246 | 38 | 1e-07 | 3.575e-11 | 55 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.007004 | 0.001901 | 25 | 9.85e-08 | 1.016e-09 | 57 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006746 | 3.808e-05 | 8718 | 0 | 2.092e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006743 | 0.02414 | 8 | 5.056e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.00131 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.00131 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.00131 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 78, 'modularity': 0.9185631965059353, 'largest': 1342, 'weighted_purity': 0.9995831943981327, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1342 | 1342 | mistralai/Mistral-7B-v0.1 | 0.9985 | 2 | mistralai/Mistral-7B-v0.1 | 1371 | 284 | 318 | 440 | 322 | permissive |
| 1 | 1315 | 1315 | Qwen/Qwen2.5-7B | 0.9977 | 3 | Qwen/Qwen2.5-7B | 1595 | 365 | 341 | 392 | 497 | permissive |
| 2 | 1247 | 1247 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1357 | 332 | 322 | 508 | 194 | restricted |
| 3 | 1008 | 1008 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1017 | 311 | 316 | 347 | 43 | restricted |
| 4 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 5 | 641 | 641 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 649 | 326 | 162 | 144 | 16 | permissive |
| 6 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 7 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 8 | 485 | 485 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 495 | 159 | 159 | 158 | 19 | restricted |
| 9 | 483 | 483 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 486 | 314 | 72 | 93 | 7 | restricted |
| 10 | 421 | 421 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 446 | 122 | 116 | 138 | 70 | restricted |
| 11 | 402 | 402 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 402 | 311 | 25 | 64 | 2 | unknown |
| 12 | 301 | 301 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 352 | 40 | 50 | 113 | 149 | permissive |
| 13 | 265 | 265 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 264 | 109 | 46 | 109 | 0 | permissive |
| 14 | 238 | 238 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 270 | 95 | 8 | 70 | 97 | permissive |
| 15 | 214 | 214 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 217 | 51 | 52 | 70 | 44 | permissive |
| 16 | 205 | 205 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 204 | 89 | 89 | 22 | 4 | restricted |
| 17 | 146 | 146 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 145 | 89 | 18 | 38 | 0 | permissive |
| 18 | 134 | 134 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 147 | 35 | 21 | 39 | 52 | restricted |
| 19 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 20 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 21 | 95 | 95 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 95 | 17 | 16 | 41 | 21 | permissive |
| 22 | 80 | 80 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/DeepHermes-3-Llama-3-8B-Preview | 84 | 23 | 10 | 28 | 23 | restricted |
| 23 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 24 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 64 | 48 | 11 | 5 | 0 | permissive |
| 25 | 52 | 52 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 51 | 48 | 1 | 2 | 0 | permissive |
| 26 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 27 | 31 | 31 | Qwen/Qwen3-8B-Base | 1 | 1 | jackf857/qwen3-8b-base-sft-ultrachat-4xh200-batch-128 | 30 | 30 | 0 | 0 | 0 | unknown |
| 28 | 27 | 27 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 26 | 10 | 9 | 7 | 0 | permissive |
| 29 | 26 | 26 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt | 25 | 22 | 3 | 0 | 0 | permissive |
| 30 | 24 | 24 | microsoft/phi-2 | 1 | 1 | ma921/phi-2-sft-golden-hh | 23 | 22 | 0 | 1 | 0 | permissive |
| 31 | 23 | 23 | google/gemma-3-4b-pt | 1 | 1 | google/medgemma-4b-pt | 22 | 16 | 1 | 5 | 0 | other |
| 32 | 22 | 22 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 21 | 7 | 7 | 7 | 0 | permissive |
| 33 | 22 | 22 | mistralai/Mistral-7B-v0.1 | 1 | 1 | danish-foundation-models/munin-7b-alpha | 23 | 5 | 4 | 4 | 10 | unknown |
| 34 | 21 | 21 | google/gemma-3-4b-pt | 1 | 1 | CEIA-UFG/Gemma-3-Gaia-PT-BR-4b-it | 20 | 1 | 0 | 19 | 0 | restricted |
| 35 | 21 | 21 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mlabonne/Daredevil-7B | 20 | 6 | 0 | 8 | 6 | permissive |
| 36 | 20 | 20 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 19 | 7 | 7 | 5 | 0 | permissive |
| 37 | 19 | 19 | Qwen/Qwen2.5-7B | 1 | 1 | sail/Sailor2-8B | 18 | 9 | 3 | 6 | 0 | permissive |
| 38 | 18 | 18 | google/gemma-3-4b-pt | 1 | 1 | MBZUAI-Paris/Nile-Chat-4B | 17 | 5 | 5 | 7 | 0 | restricted |
| 39 | 18 | 18 | Qwen/Qwen2.5-7B | 1 | 1 | mlx-community/Qwen2.5-7B-Instruct-4bit | 17 | 3 | 10 | 4 | 0 | permissive |

*… 38 more rows in the CSV*

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

max generation 17, mean generation of derived models 1.54, models per generation {0: 10, 1: 6488, 2: 5078, 3: 274, 4: 85, 5: 18, 6: 5, 7: 3, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 5, 14: 7, 15: 4, 16: 3, 17: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 673.7 | 13485 | 6952 | 1184 | 664 |
| 1 | 6488 | 762 | 0.1176 | 5.32 | 0 | 7302 | 0.8374 | 15458 | 12620 | 5008 | 1374 |
| 2 | 5078 | 684 | 0.1349 | 4.209 | 0 | 5360 | 0.07326 | 13471 | 4266 | 2630 | 980 |
| 3 | 274 | 93 | 0.3444 | 0.9852 | 0 | 14 | 0.3467 | 11 | 2 | 178 | 75 |
| 4 | 85 | 28 | 0.3294 | 1.118 | 0 | 8 | 0.2353 | 4 | 1 | 56 | 34 |
| 5 | 18 | 8 | 0.4444 | 1.833 | 0 | 10 | 0.6111 | 0 | 0 | 20 | 13 |
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
| finetune | 42429 | 4736 | 0.54 | 0.3724 |
| adapter | 23841 | 2873 | 0.3034 | 0.2259 |
| quantized | 9112 | 3400 | 0.116 | 0.2673 |
| merge | 3185 | 1709 | 0.04054 | 0.1344 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 6536 |
| child_unknown | 3354 |
| loosened | 1230 |
| changed_same_category | 591 |
| parent_unknown | 496 |
| changed_custom | 319 |
| tightened | 208 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 1 |
| noncommercial | 0 | 62 | 1 | 3 | 3 | 63 |
| other | 0 | 2 | 69 | 8 | 0 | 23 |
| permissive | 17 | 68 | 164 | 4394 | 71 | 1947 |
| restricted | 13 | 52 | 144 | 1211 | 2600 | 1320 |
| unknown | 0 | 0 | 3 | 39 | 9 | 445 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 41 | 37 | 743 | 0 | 180 | 824 | 7 | 1832 | 0.09351 | 0 |
| Qwen/Qwen3-8B-Base | 35 | 46 | 272 | 0 | 67 | 842 | 13 | 1275 | 0.1004 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 46 | 1 | 329 | 286 | 15 | 499 | 30 | 1206 | 0.4211 | 0.3318 |
| google/gemma-3-4b-pt | 23 | 0 | 310 | 273 | 10 | 493 | 8 | 1117 | 0.3814 | 0.3425 |
| meta-llama/Llama-3.1-8B | 36 | 89 | 460 | 204 | 139 | 878 | 16 | 1822 | 0.2821 | 0.1668 |
| meta-llama/Llama-3.2-1B | 48 | 10 | 293 | 464 | 32 | 825 | 3 | 1675 | 0.3889 | 0.3437 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 18 | 107 | 559 | 3 | 38 | 1173 | 52 | 1950 | 0.133 | 0.002217 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 95 | 151 | 1111 | 135 | 21 | 1321 | 39 | 2873 | 0.2412 | 0.07754 |
| finetune | 134 | 313 | 847 | 703 | 94 | 2535 | 110 | 4736 | 0.332 | 0.1852 |
| merge | 19 | 49 | 1091 | 51 | 168 | 288 | 43 | 1709 | 0.36 | 0.1133 |
| quantized | 69 | 78 | 302 | 341 | 213 | 2381 | 16 | 3400 | 0.1747 | 0.1182 |
| unknown | 2 | 0 | 3 | 0 | 0 | 11 | 0 | 16 | 0.1538 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 1-800-SHARED-TASKS/Kan_Gemma-2-9b-ChipsalSubtaskA-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1024m/CHIPSAL-C-GEMMA2-9B-001-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1998rajdeo/gemma-2-9b-bnb-4bit-csv | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
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
| Alfaxad/gemma2-9b-swahili-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CSLin3303/20241204 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Cannae-AI/TANIT-V0.5-Medium-9B-IT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CerebrumTech/cere-gemma-2-9b-tr | google/gemma-2-9b-it | quantized | google/gemma-2-9b | mit | gemma |
| Cesarbasurto/FullNameSplit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| ChetKao/Bohdi-gemma-2-9b-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | mit | gemma |
| CogYB/CneoGET | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
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
| Elcaida/gemma9bgguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Erland/Gemma_Reward_Merged | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Faust345/gemma-2-9b-it-ult | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Futuresony/future_12_10_2024 | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Gameplayer18m/grabbe-ai | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |

*… 1190 more rows in the CSV*

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
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 12 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 216 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 498 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 23 | 0 | 0 | 0 | 196 | 231 |
| 2024-Q3 | 94 | 0 | 0 | 26 | 300 | 0 | 294 | 30 | 33 | 78 |
| 2024-Q4 | 269 | 0 | 0 | 45 | 227 | 0 | 283 | 390 | 25 | 211 |
| 2025-Q1 | 404 | 0 | 457 | 62 | 128 | 127 | 336 | 335 | 27 | 153 |
| 2025-Q2 | 189 | 201 | 25 | 63 | 193 | 218 | 203 | 335 | 76 | 99 |
| 2025-Q3 | 176 | 174 | 30 | 49 | 42 | 174 | 109 | 192 | 53 | 183 |
| 2025-Q4 | 51 | 140 | 2 | 49 | 52 | 125 | 93 | 157 | 53 | 28 |
| 2026-Q1 | 81 | 125 | 12 | 28 | 75 | 177 | 58 | 52 | 23 | 48 |
| 2026-Q2 | 92 | 249 | 2 | 21 | 77 | 115 | 100 | 71 | 11 | 26 |
| 2026-Q3 | 141 | 260 | 10 | 65 | 40 | 111 | 155 | 49 | 7 | 17 |
| 2026-Q4 | 29 | 100 | 0 | 36 | 11 | 52 | 23 | 9 | 4 | 10 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 1 | 0 | 1 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| 2023-Q3 | 0 | 2 | 0 | 5 | 0 | 2 | 12 |
| 2023-Q4 | 0 | 8 | 1 | 1 | 0 | 6 | 255 |
| 2024-Q1 | 1 | 11 | 0 | 4 | 0 | 8 | 705 |
| 2024-Q2 | 0 | 16 | 0 | 6 | 7 | 4 | 451 |
| 2024-Q3 | 1 | 10 | 3 | 11 | 6 | 9 | 815 |
| 2024-Q4 | 0 | 13 | 0 | 37 | 11 | 21 | 1368 |
| 2025-Q1 | 9 | 15 | 99 | 135 | 25 | 135 | 1611 |
| 2025-Q2 | 10 | 14 | 186 | 53 | 7 | 81 | 1251 |
| 2025-Q3 | 7 | 21 | 152 | 39 | 6 | 34 | 923 |
| 2025-Q4 | 11 | 19 | 98 | 35 | 8 | 33 | 546 |
| 2026-Q1 | 21 | 10 | 76 | 88 | 11 | 18 | 455 |
| 2026-Q2 | 31 | 8 | 57 | 26 | 12 | 13 | 617 |
| 2026-Q3 | 21 | 6 | 56 | 31 | 11 | 51 | 679 |
| 2026-Q4 | 12 | 6 | 18 | 12 | 15 | 21 | 190 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 12 | 0 | 0 | 8 |
| 2023-Q4 | 97 | 107 | 3 | 0 | 64 |
| 2024-Q1 | 262 | 231 | 121 | 11 | 104 |
| 2024-Q2 | 131 | 191 | 74 | 3 | 85 |
| 2024-Q3 | 128 | 279 | 55 | 0 | 393 |
| 2024-Q4 | 198 | 495 | 116 | 0 | 641 |
| 2025-Q1 | 457 | 742 | 204 | 0 | 626 |
| 2025-Q2 | 216 | 809 | 97 | 0 | 480 |
| 2025-Q3 | 287 | 405 | 209 | 0 | 281 |
| 2025-Q4 | 186 | 352 | 30 | 0 | 182 |
| 2026-Q1 | 203 | 251 | 19 | 0 | 206 |
| 2026-Q2 | 264 | 326 | 28 | 6 | 140 |
| 2026-Q3 | 363 | 356 | 13 | 2 | 121 |
| 2026-Q4 | 70 | 140 | 19 | 1 | 44 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.048 | 0.571 | 0 | 0 | 0.381 |
| 2023-Q4 | 0.358 | 0.395 | 0.011 | 0 | 0.236 |
| 2024-Q1 | 0.359 | 0.317 | 0.166 | 0.015 | 0.143 |
| 2024-Q2 | 0.271 | 0.395 | 0.153 | 0.006 | 0.176 |
| 2024-Q3 | 0.15 | 0.326 | 0.064 | 0 | 0.46 |
| 2024-Q4 | 0.137 | 0.341 | 0.08 | 0 | 0.442 |
| 2025-Q1 | 0.225 | 0.366 | 0.101 | 0 | 0.309 |
| 2025-Q2 | 0.135 | 0.505 | 0.061 | 0 | 0.3 |
| 2025-Q3 | 0.243 | 0.343 | 0.177 | 0 | 0.238 |
| 2025-Q4 | 0.248 | 0.469 | 0.04 | 0 | 0.243 |
| 2026-Q1 | 0.299 | 0.37 | 0.028 | 0 | 0.303 |
| 2026-Q2 | 0.346 | 0.427 | 0.037 | 0.008 | 0.183 |
| 2026-Q3 | 0.425 | 0.416 | 0.015 | 0.002 | 0.142 |
| 2026-Q4 | 0.255 | 0.511 | 0.069 | 0.004 | 0.161 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 12004 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 3270 | 27.2 % |
| missing pipeline_tag (as published) | 4783 | 39.8 % |
|   of which filled from parent | 4782 | see pipeline_tag_source |
| missing library_name | 1914 | 15.9 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 15412 |  |
|   linked by HF | 14141 | 91.8 % |
|   old name of a renamed repo | 799 | 5.2 % |
|   not linked (broken parent link) | 472 | 3.1 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 12432 | 100.0 % of 12432 |
| tag edges to a parent outside the sample | 2328 | 15.4 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.8% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 98% |
