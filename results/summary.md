# Mining results

Generated 2026-10-26 09:09 UTC from 3023 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 3023 | 7023 |
| nodes_in_sample | 3023 | 3023 |
| edges | 3224 | 7711 |
| relations | {'finetune': 1225, 'adapter': 882, 'quantized': 629, 'merge': 488} | {'finetune': 3000, 'adapter': 2034, 'quantized': 1155, 'merge': 1522} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 5 |
| largest_component | 1511 | 4743 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 303 |
| leaves | 2959 | 6658 |
| multi_parent_nodes | 128 | 325 |
| temporal_anomaly_edges | 7 | 7 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 151 | 6.682e-11 | 20 | 1 |  |
| Weighted PageRank | 68 | 9.695e-11 | 20 | 1 |  |
| HITS authority | 1843 | 2.784e-09 | 20 | 1 | 0.9949 |
| HITS hub | 1843 | 1.699e-11 | 20 | 1 | 0.9949 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | note | hits_eigengap |
|---|---|---|---|---|---|---|
| PageRank | 133 | 2.4e-10 | 20 | 1 |  |  |
| Weighted PageRank | 68 | 3.14e-10 | 20 | 1 |  |  |
| HITS authority | 183 |  |  |  | networkx did not converge | 0.9427 |
| HITS hub | 183 |  |  |  | networkx did not converge | 0.9427 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07588 | 0.06219 | 2 | 0.006427 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06221 | 0.05254 | 4 | 3.475e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04995 | 0.06964 | 1 | 0.7862 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.0483 | 0.0007211 | 12 | 0.0001995 | 7.405e-06 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04799 | 0.03163 | 8 | 8.723e-65 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04418 | 0.0005557 | 15 | 8.181e-06 | 4.004e-09 | 23 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03712 | 0.03364 | 6 | 4.262e-61 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03404 | 0.0003246 | 18 | 8.531e-63 | 4.911e-64 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01921 | 0.05796 | 3 | 2.225e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01458 | 0.02309 | 10 | 1.846e-92 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01439 | 0.02839 | 9 | 9.609e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01226 | 0.0001449 | 53 | 1.073e-94 | 2.127e-95 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01024 | 0.04445 | 5 | 5.329e-06 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008038 | 0.0001249 | 73 | 1.759e-08 | 1.107e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007436 | 0.0002214 | 26 | 5.31e-08 | 4.004e-09 | 7 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006132 | 7.83e-05 | 494 | 0 | 7.405e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005617 | 0.0001726 | 40 | 0.002901 | 0.0009059 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.0046 | 0.0001957 | 31 | 0.004401 | 0.0009059 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004435 | 7.83e-05 | 385 | 0 | 1.107e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.0037 | 0.03293 | 7 | 1.981e-08 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07643 | 0.04466 | 10 | 0.5481 | 0 | 302 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06281 | 0.04539 | 8 | 0.01178 | 0 | 302 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.05072 | 0.04544 | 6 | 0.1358 | 0 | 303 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04846 | 0.002302 | 11 | 0.06555 | 0.002287 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04817 | 0.04552 | 4 | 3.417e-18 | 0 | 301 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04431 | 0.001737 | 12 | 0.002796 | 4.917e-05 | 23 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03731 | 0.04553 | 2 | 1.497e-14 | 0 | 302 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03413 | 0.0009053 | 13 | 5.125e-16 | 6.247e-17 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01938 | 0.04563 | 1 | 1.743e-15 | 0 | 302 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.0146 | 0.04549 | 5 | 3.785e-18 | 0 | 301 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01442 | 0.04539 | 7 | 0.08478 | 0 | 301 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01228 | 0.0003279 | 30 | 2.531e-20 | 1.579e-20 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01029 | 0.04525 | 9 | 0.00314 | 0 | 301 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008055 | 0.0003279 | 29 | 0.000555 | 0.0003538 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007451 | 0.0005162 | 19 | 0.0003135 | 4.917e-05 | 7 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006143 | 0.0001772 | 193 | 0 | 0.002287 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005632 | 0.0004785 | 22 | 0.001789 | 0.0005666 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004629 | 0.0005727 | 18 | 0.002725 | 0.0005666 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004443 | 0.0001772 | 84 | 0 | 0.0003538 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003764 | 0.04552 | 3 | 3.417e-18 | 0 | 301 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| Naphula/Warlock-7B-v3 | 0.0009764 | 33 |
| bartowski/Oumuamua-7b-instruct-v2-GGUF | 0.0009356 | 15 |
| nitky/Oumuamua-7b-instruct-v2 | 0.0009356 | 15 |
| solidrust/KatyTestHistorical-SultrySilicon-7B-V2 | 0.0009304 | 8 |
| giraffe176/Open_Maid_Samantha_Hermes_Orca_dare_tiesv0.1 | 0.0009296 | 5 |
| kidyu/Moza-7B-v1.0 | 0.0009288 | 10 |
| giraffe176/WestMaid_HermesMonarchv0.1 | 0.0009262 | 5 |
| giraffe176/WestLake_Noromaid_OpenHermes_neural-chatv0.1 | 0.0009253 | 5 |
| giraffe176/Open_Neural_Monarch_Maidv0.1 | 0.0009245 | 5 |
| saishf/Top-Western-Maid-7B | 0.0009245 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8972612162811174, 'largest': 306, 'weighted_purity': 0.9986768111147867, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 306 | 306 | Qwen/Qwen2.5-7B | 0.9902 | 3 | Qwen/Qwen2.5-7B | 353 | 76 | 76 | 76 | 125 | permissive |
| 1 | 303 | 303 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 306 | 92 | 94 | 92 | 28 | restricted |
| 2 | 303 | 303 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 338 | 76 | 76 | 77 | 109 | permissive |
| 3 | 303 | 303 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 315 | 119 | 118 | 52 | 26 | permissive |
| 4 | 302 | 302 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 304 | 255 | 19 | 28 | 2 | unknown |
| 5 | 302 | 302 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 301 | 113 | 113 | 70 | 5 | permissive |
| 6 | 302 | 302 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 301 | 128 | 128 | 38 | 7 | permissive |
| 7 | 302 | 302 | meta-llama/Llama-3.1-8B | 0.9967 | 2 | meta-llama/Llama-3.1-8B | 395 | 77 | 77 | 77 | 164 | restricted |
| 8 | 301 | 301 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 306 | 174 | 67 | 55 | 10 | restricted |
| 9 | 299 | 299 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 299 | 115 | 114 | 64 | 6 | permissive |

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

max generation 15, mean generation of derived models 1.08, models per generation {0: 10, 1: 2887, 2: 107, 3: 5, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 3, 13: 1, 14: 1, 15: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 301.6 | 13485 | 6952 | 1184 | 664 |
| 1 | 2887 | 418 | 0.1448 | 11.65 | 0 | 7302 | 0.05369 | 15254 | 12584 | 4499 | 1286 |
| 2 | 107 | 59 | 0.5566 | 1.557 | 1 | 9 | 0.06542 | 14 | 3 | 105 | 43 |
| 3 | 5 | 4 | 0.8 | 4.4 | 3 | 14 | 0.6 | 0 | 0 | 8 | 14 |
| 4 | 1 | 1 | 1 | 8 | 8 | 8 | 6 | 0 | 0 | 1 | 7 |
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
| finetune | 28753 | 1225 | 0.5119 | 0.38 |
| adapter | 19539 | 882 | 0.3479 | 0.2736 |
| quantized | 5820 | 629 | 0.1036 | 0.1951 |
| merge | 2057 | 488 | 0.03662 | 0.1514 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 1636 |
| child_unknown | 920 |
| changed_same_category | 273 |
| changed_custom | 125 |
| loosened | 112 |
| tightened | 105 |
| parent_unknown | 53 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| other | 0 | 0 | 1 | 0 | 0 | 0 |
| permissive | 10 | 33 | 77 | 1221 | 35 | 535 |
| restricted | 4 | 27 | 48 | 108 | 687 | 385 |
| unknown | 0 | 0 | 0 | 0 | 0 | 53 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 11 | 5 | 147 | 0 | 2 | 186 | 0 | 351 | 0.07921 | 0 |
| Qwen/Qwen3-8B-Base | 16 | 12 | 113 | 0 | 0 | 169 | 5 | 315 | 0.1634 | 0 |
| deepseek-ai/DeepSeek-R1 | 11 | 102 | 57 | 0 | 0 | 95 | 36 | 301 | 0.6107 | 0 |
| google-bert/bert-base-uncased | 3 | 44 | 75 | 0 | 0 | 173 | 6 | 301 | 0.2345 | 0 |
| google/gemma-2-9b | 18 | 1 | 61 | 19 | 0 | 190 | 19 | 308 | 0.2308 | 0.07692 |
| google/gemma-3-4b-pt | 9 | 0 | 141 | 14 | 0 | 140 | 0 | 304 | 0.1411 | 0.08589 |
| meta-llama/Llama-3.1-8B | 7 | 40 | 132 | 32 | 49 | 130 | 7 | 397 | 0.3981 | 0.1481 |
| meta-llama/Llama-3.2-1B | 14 | 5 | 51 | 47 | 2 | 186 | 1 | 306 | 0.2648 | 0.1858 |
| microsoft/phi-2 | 32 | 29 | 64 | 0 | 0 | 174 | 4 | 303 | 0.272 | 0 |
| mistralai/Mistral-7B-v0.1 | 4 | 35 | 79 | 0 | 0 | 193 | 27 | 338 | 0.2548 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 31 | 98 | 296 | 26 | 0 | 405 | 26 | 882 | 0.3089 | 0.04437 |
| finetune | 50 | 112 | 271 | 37 | 0 | 712 | 43 | 1225 | 0.2537 | 0.03878 |
| merge | 10 | 13 | 281 | 3 | 53 | 103 | 25 | 488 | 0.3312 | 0.01948 |
| quantized | 34 | 50 | 72 | 46 | 0 | 416 | 11 | 629 | 0.2531 | 0.08259 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 2024-mcm-everitt-ryan/gemma-2-9b-job-bias-qlora-seq-cls | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Jiangxz/Tax_Model | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| MichiganNLP/hacking-fairness-benchmarks-gemma-2-9b-z1 | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| SURESHBEEKHANI/Finetune_Gemma_NRE_SFT_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| SinclairSchneider/german_politic_direction_gemma-2-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-4.0 | gemma |
| cplonski/cope-a-9b-merged | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| hon9kon9ize/cantonese-gemma-2-9b-lora-preview20240929 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0-ls | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0-wx | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| mueggi/ka-ai-instruct | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| nehuronion-dvt/nehuronion-dvt-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-adapters | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-gguf | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| nicoboss/Apollo2-9B-llamacppfixed | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| testmoto/gemma-2-lora-dpo-moe-1 | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
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
| 3adel25/Llama-3.1-8B-Customer-service-question-and-answer | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Abigail45/Chyio | meta-llama/Llama-3.1-8B | merge | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Davidsv/CosmeticVentureV2 | meta-llama/Llama-3.1-8B | merge | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Delentia/delentia-slm-jitna-v0.4 | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Gurubot/self-after-dark | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| HiTZ/Llama-3.1-GuideX-8B | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Jashan887/81_Self_After_Dark_Unfiltered | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |

*… 72 more rows in the CSV*

## 5. Trends

Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. The sample favours well-downloaded models, so recent quarters are under-counted. Compare shares, not totals.

**trend_family_quarterly**

| quarter | Qwen/Qwen2.5-7B | Qwen/Qwen3-8B-Base | deepseek-ai/DeepSeek-R1 | google-bert/bert-base-uncased | google/gemma-2-9b | google/gemma-3-4b-pt | meta-llama/Llama-3.1-8B | meta-llama/Llama-3.2-1B | microsoft/phi-2 | mistralai/Mistral-7B-v0.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 6 |
| 2023-Q4 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 23 | 36 |
| 2024-Q1 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 82 | 156 |
| 2024-Q2 | 0 | 0 | 0 | 29 | 6 | 0 | 0 | 0 | 25 | 44 |
| 2024-Q3 | 37 | 0 | 0 | 21 | 82 | 0 | 72 | 16 | 16 | 11 |
| 2024-Q4 | 46 | 0 | 0 | 25 | 56 | 0 | 40 | 86 | 8 | 6 |
| 2025-Q1 | 72 | 0 | 244 | 32 | 13 | 44 | 66 | 40 | 13 | 9 |
| 2025-Q2 | 19 | 50 | 16 | 32 | 39 | 118 | 42 | 22 | 31 | 6 |
| 2025-Q3 | 52 | 41 | 16 | 29 | 12 | 21 | 12 | 53 | 33 | 6 |
| 2025-Q4 | 12 | 33 | 0 | 31 | 6 | 15 | 12 | 35 | 37 | 3 |
| 2026-Q1 | 16 | 29 | 7 | 10 | 46 | 13 | 7 | 10 | 16 | 4 |
| 2026-Q2 | 14 | 31 | 2 | 11 | 27 | 30 | 22 | 15 | 5 | 8 |
| 2026-Q3 | 16 | 86 | 9 | 31 | 10 | 34 | 21 | 19 | 7 | 4 |
| 2026-Q4 | 18 | 32 | 0 | 10 | 4 | 26 | 7 | 6 | 4 | 3 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 4 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 1 | 0 | 1 | 6 |
| 2023-Q4 | 0 | 7 | 1 | 0 | 0 | 3 | 58 |
| 2024-Q1 | 0 | 11 | 0 | 3 | 0 | 5 | 236 |
| 2024-Q2 | 0 | 16 | 0 | 5 | 5 | 2 | 76 |
| 2024-Q3 | 1 | 9 | 1 | 5 | 6 | 3 | 230 |
| 2024-Q4 | 0 | 10 | 0 | 12 | 7 | 8 | 230 |
| 2025-Q1 | 5 | 11 | 41 | 63 | 15 | 44 | 354 |
| 2025-Q2 | 5 | 11 | 109 | 18 | 4 | 19 | 209 |
| 2025-Q3 | 3 | 16 | 18 | 12 | 1 | 14 | 211 |
| 2025-Q4 | 1 | 17 | 10 | 4 | 2 | 15 | 135 |
| 2026-Q1 | 5 | 5 | 13 | 7 | 2 | 3 | 123 |
| 2026-Q2 | 11 | 6 | 16 | 2 | 0 | 5 | 125 |
| 2026-Q3 | 4 | 3 | 28 | 7 | 1 | 32 | 162 |
| 2026-Q4 | 1 | 3 | 5 | 0 | 2 | 8 | 91 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 4 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 2 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 3 | 0 | 0 | 4 |
| 2023-Q4 | 21 | 32 | 0 | 0 | 16 |
| 2024-Q1 | 99 | 70 | 47 | 0 | 39 |
| 2024-Q2 | 41 | 22 | 26 | 0 | 15 |
| 2024-Q3 | 47 | 101 | 21 | 0 | 86 |
| 2024-Q4 | 43 | 101 | 36 | 0 | 87 |
| 2025-Q1 | 177 | 199 | 58 | 0 | 99 |
| 2025-Q2 | 67 | 211 | 23 | 0 | 74 |
| 2025-Q3 | 105 | 87 | 35 | 0 | 48 |
| 2025-Q4 | 56 | 79 | 17 | 0 | 32 |
| 2026-Q1 | 37 | 79 | 4 | 0 | 38 |
| 2026-Q2 | 62 | 58 | 12 | 5 | 28 |
| 2026-Q3 | 89 | 101 | 5 | 0 | 42 |
| 2026-Q4 | 30 | 66 | 1 | 1 | 12 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.667 | 0 | 0 | 0.333 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0.125 | 0.375 | 0 | 0 | 0.5 |
| 2023-Q4 | 0.304 | 0.464 | 0 | 0 | 0.232 |
| 2024-Q1 | 0.388 | 0.275 | 0.184 | 0 | 0.153 |
| 2024-Q2 | 0.394 | 0.212 | 0.25 | 0 | 0.144 |
| 2024-Q3 | 0.184 | 0.396 | 0.082 | 0 | 0.337 |
| 2024-Q4 | 0.161 | 0.378 | 0.135 | 0 | 0.326 |
| 2025-Q1 | 0.332 | 0.373 | 0.109 | 0 | 0.186 |
| 2025-Q2 | 0.179 | 0.563 | 0.061 | 0 | 0.197 |
| 2025-Q3 | 0.382 | 0.316 | 0.127 | 0 | 0.175 |
| 2025-Q4 | 0.304 | 0.429 | 0.092 | 0 | 0.174 |
| 2026-Q1 | 0.234 | 0.5 | 0.025 | 0 | 0.241 |
| 2026-Q2 | 0.376 | 0.352 | 0.073 | 0.03 | 0.17 |
| 2026-Q3 | 0.376 | 0.426 | 0.021 | 0 | 0.177 |
| 2026-Q4 | 0.273 | 0.6 | 0.009 | 0.009 | 0.109 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 3023 | of 6730 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 826 | 27.3 % |
| missing pipeline_tag (as published) | 1050 | 34.7 % |
|   of which filled from parent | 1050 | see pipeline_tag_source |
| missing library_name | 503 | 16.6 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 1 | excluded from trends |
| declared base_model values | 4117 |  |
|   linked by HF | 3690 | 89.6 % |
|   old name of a renamed repo | 253 | 6.1 % |
|   not linked (broken parent link) | 174 | 4.2 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 3016 | 100.0 % of 3016 |
| tag edges to a parent outside the sample | 780 | 19.5 % |
| child created >7 days before its parent | 7 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.5% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 94% |
