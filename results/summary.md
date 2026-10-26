# Mining results

Generated 2026-10-26 10:53 UTC from 5036 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 5036 | 7061 |
| nodes_in_sample | 5036 | 5036 |
| edges | 5293 | 8003 |
| relations | {'finetune': 2378, 'adapter': 1379, 'quantized': 870, 'merge': 666} | {'finetune': 3000, 'adapter': 2040, 'quantized': 1155, 'merge': 1808} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 5 |
| largest_component | 2635 | 4781 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 341 |
| leaves | 4961 | 6650 |
| multi_parent_nodes | 165 | 455 |
| temporal_anomaly_edges | 8 | 8 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | note | hits_eigengap |
|---|---|---|---|---|---|---|
| PageRank | 156 | 1.204e-10 | 20 | 1 |  |  |
| Weighted PageRank | 69 | 3.349e-10 | 20 | 1 |  |  |
| HITS authority | 10000 |  |  |  | networkx did not converge | 0.9994 |
| HITS hub | 10000 |  |  |  | networkx did not converge | 0.9994 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 128 | 2.095e-10 | 20 | 1 |  |
| Weighted PageRank | 68 | 3.075e-10 | 20 | 1 |  |
| HITS authority | 177 | 2.733e-10 | 20 | 1 | 0.9407 |
| HITS hub | 177 | 4.195e-13 | 20 | 1 | 0.9407 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07579 | 0.0618 | 2 | 0.005479 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06172 | 0.05062 | 4 | 6.505e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04969 | 0.06651 | 1 | 0.6959 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04777 | 0.0007182 | 16 | 0.0001693 | 7.104e-06 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04756 | 0.0315 | 8 | 4.558e-63 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04362 | 0.001068 | 11 | 9.224e-06 | 8.434e-09 | 44 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03749 | 0.03351 | 6 | 1.686e-59 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03367 | 0.0003232 | 22 | 3.374e-61 | 2.185e-62 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01931 | 0.05773 | 3 | 3.245e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01442 | 0.023 | 10 | 7.794e-90 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01424 | 0.02827 | 9 | 8.134e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01213 | 0.0001443 | 64 | 4.531e-92 | 1.011e-92 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01015 | 0.04427 | 5 | 9.262e-06 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.00795 | 0.0001244 | 88 | 1.483e-08 | 1.055e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.0073 | 0.0004746 | 19 | 2.029e-07 | 8.434e-09 | 19 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006064 | 7.798e-05 | 540 | 0 | 7.104e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005556 | 0.0001719 | 50 | 0.002557 | 0.0009023 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004549 | 0.0001949 | 40 | 0.003892 | 0.0009023 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004386 | 7.798e-05 | 431 | 0 | 1.055e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003659 | 0.0328 | 7 | 1.669e-08 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07636 | 0.0495 | 5 | 0.06705 | 0 | 552 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.0625 | 0.04959 | 4 | 0.6181 | 0 | 551 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.05078 | 0.04987 | 2 | 0.01957 | 0 | 552 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04794 | 0.001384 | 12 | 0.004159 | 0.0001389 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04775 | 0.04441 | 8 | 8.399e-321 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04376 | 0.001908 | 11 | 0.05119 | 0.00128 | 44 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03768 | 0.04649 | 6 | 1.322e-320 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03376 | 0.0005369 | 14 | 2.569e-322 | 2.964e-323 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01948 | 0.05 | 1 | 7.89e-38 | 0 | 551 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01445 | 0.03143 | 10 | 1.487e-321 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01428 | 0.03871 | 9 | 0.0005211 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01215 | 0.0001972 | 31 | 9.881e-324 | 4.941e-324 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01021 | 0.04986 | 3 | 0.1656 | 0 | 551 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.007968 | 0.0001972 | 30 | 1.882e-06 | 1.079e-06 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007319 | 0.0006728 | 13 | 0.02304 | 0.00128 | 19 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006077 | 0.0001066 | 204 | 0 | 0.0001389 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005571 | 0.0002878 | 23 | 0.0001419 | 4.052e-05 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004578 | 0.0003431 | 20 | 0.0002147 | 4.052e-05 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004395 | 0.0001066 | 95 | 0 | 1.079e-06 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003723 | 0.04513 | 7 | 8.537e-321 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001004 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001004 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001004 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8960802151667794, 'largest': 555, 'weighted_purity': 0.9994042891183479, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 555 | 555 | Qwen/Qwen2.5-7B | 0.9946 | 3 | Qwen/Qwen2.5-7B | 649 | 164 | 163 | 88 | 234 | permissive |
| 1 | 552 | 552 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 556 | 175 | 178 | 175 | 28 | restricted |
| 2 | 552 | 552 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 592 | 138 | 138 | 140 | 176 | permissive |
| 3 | 551 | 551 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 645 | 161 | 161 | 160 | 163 | restricted |
| 4 | 549 | 549 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 549 | 240 | 239 | 64 | 6 | permissive |
| 5 | 514 | 514 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 528 | 300 | 148 | 52 | 28 | permissive |
| 6 | 498 | 498 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 497 | 300 | 122 | 70 | 5 | permissive |
| 7 | 490 | 490 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 489 | 300 | 144 | 38 | 7 | permissive |
| 8 | 428 | 428 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 433 | 300 | 67 | 55 | 11 | restricted |
| 9 | 347 | 347 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 349 | 300 | 19 | 28 | 2 | unknown |

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

max generation 15, mean generation of derived models 1.06, models per generation {0: 10, 1: 4863, 2: 142, 3: 6, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 3, 13: 1, 14: 1, 15: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 502.9 | 13485 | 6952 | 1184 | 664 |
| 1 | 4863 | 626 | 0.129 | 7.046 | 0 | 7302 | 0.04277 | 15406 | 12606 | 4834 | 1354 |
| 2 | 142 | 62 | 0.4397 | 1.241 | 0 | 9 | 0.06338 | 16 | 3 | 111 | 45 |
| 3 | 6 | 5 | 0.8333 | 3.833 | 2 | 14 | 0.6667 | 0 | 0 | 8 | 15 |
| 4 | 2 | 2 | 1 | 4.5 | 4.5 | 8 | 3 | 0 | 0 | 2 | 7 |
| 5 | 1 | 1 | 1 | 14 | 14 | 14 | 12 | 0 | 0 | 1 | 13 |
| 6 | 1 | 1 | 1 | 5 | 5 | 5 | 4 | 0 | 0 | 1 | 4 |
| 7 | 1 | 1 | 1 | 4 | 4 | 4 | 3 | 0 | 0 | 1 | 3 |
| 8 | 1 | 1 | 1 | 4 | 4 | 4 | 2 | 0 | 0 | 2 | 2 |
| 9 | 1 | 1 | 1 | 3 | 3 | 3 | 1 | 0 | 0 | 2 | 1 |
| 10 | 1 | 1 | 1 | 6 | 6 | 6 | 4 | 0 | 0 | 2 | 4 |
| 11 | 1 | 1 | 1 | 6 | 6 | 6 | 4 | 0 | 0 | 2 | 4 |
| 12 | 3 | 3 | 1 | 4.333 | 4 | 6 | 1.333 | 0 | 0 | 6 | 7 |
| 13 | 1 | 1 | 1 | 5 | 5 | 5 | 2 | 0 | 0 | 2 | 3 |
| 14 | 1 | 1 | 1 | 3 | 3 | 3 | 1 | 0 | 0 | 2 | 1 |
| 15 | 1 | 1 | 1 | 3 | 3 | 3 | 0 | 0 | 0 | 2 | 1 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 28907 | 2378 | 0.5093 | 0.4493 |
| adapter | 19561 | 1379 | 0.3446 | 0.2605 |
| quantized | 6162 | 870 | 0.1086 | 0.1644 |
| merge | 2128 | 666 | 0.03749 | 0.1258 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 2724 |
| child_unknown | 1578 |
| changed_same_category | 432 |
| changed_custom | 178 |
| loosened | 176 |
| tightened | 148 |
| parent_unknown | 57 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| other | 0 | 0 | 1 | 0 | 0 | 0 |
| permissive | 12 | 42 | 113 | 2114 | 62 | 963 |
| restricted | 6 | 32 | 65 | 170 | 1041 | 615 |
| unknown | 0 | 0 | 0 | 0 | 0 | 57 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 17 | 9 | 330 | 0 | 4 | 287 | 0 | 647 | 0.08307 | 0 |
| Qwen/Qwen3-8B-Base | 21 | 20 | 145 | 0 | 0 | 335 | 7 | 528 | 0.1253 | 0 |
| deepseek-ai/DeepSeek-R1 | 21 | 180 | 105 | 0 | 0 | 127 | 64 | 497 | 0.676 | 0 |
| google-bert/bert-base-uncased | 5 | 75 | 114 | 0 | 0 | 286 | 9 | 489 | 0.2373 | 0 |
| google/gemma-2-9b | 19 | 1 | 152 | 26 | 0 | 214 | 22 | 434 | 0.2411 | 0.0922 |
| google/gemma-3-4b-pt | 9 | 0 | 186 | 14 | 0 | 140 | 0 | 349 | 0.1411 | 0.08589 |
| meta-llama/Llama-3.1-8B | 13 | 59 | 187 | 72 | 50 | 258 | 9 | 648 | 0.3723 | 0.1752 |
| meta-llama/Llama-3.2-1B | 24 | 7 | 90 | 64 | 3 | 367 | 1 | 556 | 0.2073 | 0.1382 |
| microsoft/phi-2 | 44 | 31 | 111 | 0 | 0 | 363 | 4 | 553 | 0.1787 | 0 |
| mistralai/Mistral-7B-v0.1 | 5 | 50 | 158 | 0 | 0 | 347 | 32 | 592 | 0.2005 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 47 | 118 | 480 | 38 | 2 | 663 | 31 | 1379 | 0.2609 | 0.04236 |
| finetune | 80 | 239 | 560 | 70 | 0 | 1351 | 78 | 2378 | 0.2569 | 0.0385 |
| merge | 10 | 18 | 435 | 3 | 55 | 119 | 26 | 666 | 0.3239 | 0.01705 |
| quantized | 41 | 57 | 103 | 65 | 0 | 591 | 13 | 870 | 0.2295 | 0.08475 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 2024-mcm-everitt-ryan/gemma-2-9b-job-bias-qlora-seq-cls | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Himalayan-wildcat/gemma-2-9b-finetune | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| Hizaneko/gemma-2-9b-nyan100 | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Jiangxz/Tax_Model | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Kohsaku/gemma-2-9b-finetune-4 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| MichiganNLP/hacking-fairness-benchmarks-gemma-2-9b-z1 | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| Naotaka/gemma-2-9b-r16-768-512-it_lora | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| SURESHBEEKHANI/Finetune_Gemma_NRE_SFT_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| SinclairSchneider/german_politic_direction_gemma-2-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-4.0 | gemma |
| SinclairSchneider/german_politic_direction_gemma-2-9b_v0.1 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-4.0 | gemma |
| cplonski/cope-a-9b-merged | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| hon9kon9ize/cantonese-gemma-2-9b-lora-preview20240929 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0-ls | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0-wx | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| mueggi/ka-ai-instruct | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| naoa/gemma-2-9b-base71_lora | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| nehuronion-dvt/nehuronion-dvt-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-adapters | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-gguf | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| nicoboss/Apollo2-9B-llamacppfixed | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| testmoto/gemma-2-lora-dpo-moe-1 | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| ultimatemagic79/lora_gemma_9b | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| zaid646/gemma-2-9b-awq | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| AI-for-Education/edu-qurating-core-ed-gemma-3-4b | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | mit | gemma |
| AI-for-Education/edu-qurating-fl-student-gemma-3-4b | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | mit | gemma |
| AI-for-Education/edu-qurating-fl-teacher-gemma-3-4b | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | mit | gemma |
| Abduraxim/gemma_paraphraser | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| McGill-NLP/AfriqueGemma-4B | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | cc-by-4.0 | gemma |
| RampPublic/portal-gemma-3-4b | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| alakxender/dhivehi-image-text-10k-multi-gemma | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | mit | gemma |
| alakxender/dhivehi-image-text-line-gemma | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | mit | gemma |
| ariG23498/gemma-3-4b-pt-object-detection | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| flas-ai/flas-gemma-3-4b-pt | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| iamsubingyawali/gemma-3-4b-nepali-news-pretrained | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| keeeeesz/gemma-civil-code-pl_20250416 | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| kmaslennikova/gemma3_lora | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | mit | gemma |
| manthilaffs/Gamunu-4B-Instruct-Alpha | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |

*… 136 more rows in the CSV*

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
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 6 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 37 | 62 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 192 | 234 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 6 | 0 | 0 | 0 | 107 | 79 |
| 2024-Q3 | 40 | 0 | 0 | 26 | 92 | 0 | 133 | 19 | 26 | 26 |
| 2024-Q4 | 92 | 0 | 0 | 45 | 72 | 0 | 82 | 142 | 10 | 10 |
| 2025-Q1 | 107 | 0 | 439 | 61 | 15 | 44 | 101 | 101 | 14 | 29 |
| 2025-Q2 | 76 | 79 | 17 | 41 | 128 | 118 | 63 | 68 | 35 | 23 |
| 2025-Q3 | 82 | 75 | 16 | 37 | 15 | 60 | 32 | 103 | 46 | 42 |
| 2025-Q4 | 21 | 66 | 0 | 47 | 7 | 21 | 30 | 50 | 47 | 11 |
| 2026-Q1 | 30 | 40 | 7 | 24 | 50 | 13 | 19 | 16 | 18 | 8 |
| 2026-Q2 | 32 | 64 | 2 | 17 | 27 | 30 | 30 | 22 | 7 | 10 |
| 2026-Q3 | 53 | 140 | 9 | 62 | 11 | 34 | 47 | 23 | 7 | 8 |
| 2026-Q4 | 18 | 49 | 0 | 31 | 4 | 26 | 13 | 7 | 4 | 3 |

**trend_task_quarterly**

| quarter | fill-mask | image-text-to-text | other | question-answering | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2023-Q2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2023-Q3 | 2 | 0 | 4 | 1 | 0 | 2 | 6 |
| 2023-Q4 | 8 | 1 | 0 | 0 | 0 | 6 | 99 |
| 2024-Q1 | 11 | 0 | 3 | 1 | 0 | 8 | 423 |
| 2024-Q2 | 16 | 0 | 6 | 0 | 7 | 4 | 193 |
| 2024-Q3 | 10 | 1 | 6 | 3 | 6 | 6 | 330 |
| 2024-Q4 | 13 | 0 | 11 | 10 | 11 | 18 | 390 |
| 2025-Q1 | 15 | 42 | 103 | 22 | 23 | 99 | 607 |
| 2025-Q2 | 12 | 109 | 20 | 8 | 5 | 28 | 466 |
| 2025-Q3 | 20 | 57 | 16 | 1 | 1 | 22 | 391 |
| 2025-Q4 | 18 | 16 | 8 | 2 | 5 | 29 | 222 |
| 2026-Q1 | 10 | 13 | 14 | 2 | 4 | 9 | 173 |
| 2026-Q2 | 6 | 16 | 18 | 0 | 3 | 7 | 191 |
| 2026-Q3 | 5 | 28 | 19 | 5 | 3 | 49 | 285 |
| 2026-Q4 | 5 | 5 | 1 | 1 | 12 | 17 | 114 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 10 | 0 | 0 | 4 |
| 2023-Q4 | 39 | 52 | 0 | 0 | 23 |
| 2024-Q1 | 186 | 143 | 54 | 0 | 63 |
| 2024-Q2 | 66 | 99 | 39 | 0 | 22 |
| 2024-Q3 | 72 | 138 | 23 | 0 | 129 |
| 2024-Q4 | 70 | 198 | 53 | 0 | 132 |
| 2025-Q1 | 247 | 473 | 63 | 0 | 128 |
| 2025-Q2 | 100 | 391 | 46 | 0 | 111 |
| 2025-Q3 | 172 | 194 | 81 | 0 | 61 |
| 2025-Q4 | 82 | 158 | 17 | 0 | 43 |
| 2026-Q1 | 56 | 108 | 9 | 0 | 52 |
| 2026-Q2 | 87 | 99 | 17 | 5 | 33 |
| 2026-Q3 | 156 | 185 | 6 | 0 | 47 |
| 2026-Q4 | 36 | 104 | 1 | 1 | 13 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.067 | 0.667 | 0 | 0 | 0.267 |
| 2023-Q4 | 0.342 | 0.456 | 0 | 0 | 0.202 |
| 2024-Q1 | 0.417 | 0.321 | 0.121 | 0 | 0.141 |
| 2024-Q2 | 0.292 | 0.438 | 0.173 | 0 | 0.097 |
| 2024-Q3 | 0.199 | 0.381 | 0.064 | 0 | 0.356 |
| 2024-Q4 | 0.155 | 0.437 | 0.117 | 0 | 0.291 |
| 2025-Q1 | 0.271 | 0.519 | 0.069 | 0 | 0.141 |
| 2025-Q2 | 0.154 | 0.603 | 0.071 | 0 | 0.171 |
| 2025-Q3 | 0.339 | 0.382 | 0.159 | 0 | 0.12 |
| 2025-Q4 | 0.273 | 0.527 | 0.057 | 0 | 0.143 |
| 2026-Q1 | 0.249 | 0.48 | 0.04 | 0 | 0.231 |
| 2026-Q2 | 0.361 | 0.411 | 0.071 | 0.021 | 0.137 |
| 2026-Q3 | 0.396 | 0.47 | 0.015 | 0 | 0.119 |
| 2026-Q4 | 0.232 | 0.671 | 0.006 | 0.006 | 0.084 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 5036 | of 6730 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 1439 | 28.6 % |
| missing pipeline_tag (as published) | 1864 | 37.0 % |
|   of which filled from parent | 1864 | see pipeline_tag_source |
| missing library_name | 934 | 18.5 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 6462 |  |
|   linked by HF | 5807 | 89.9 % |
|   old name of a renamed repo | 429 | 6.6 % |
|   not linked (broken parent link) | 226 | 3.5 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 5029 | 100.0 % of 5029 |
| tag edges to a parent outside the sample | 1016 | 16.1 % |
| child created >7 days before its parent | 8 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.8% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 98% |
