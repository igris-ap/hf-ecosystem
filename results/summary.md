# Mining results

Generated 2026-10-26 11:44 UTC from 6035 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 6035 | 7063 |
| nodes_in_sample | 6035 | 6035 |
| edges | 6300 | 8161 |
| relations | {'finetune': 2750, 'adapter': 1753, 'quantized': 1070, 'merge': 727} | {'finetune': 3000, 'adapter': 2043, 'quantized': 1155, 'merge': 1963} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 5 |
| largest_component | 3414 | 4783 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 343 |
| leaves | 5956 | 6650 |
| multi_parent_nodes | 167 | 512 |
| temporal_anomaly_edges | 8 | 8 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | note | hits_eigengap |
|---|---|---|---|---|---|---|
| PageRank | 159 | 1.643e-10 | 20 | 1 |  |  |
| Weighted PageRank | 70 | 3.592e-10 | 20 | 1 |  |  |
| HITS authority | 10000 |  |  |  | networkx did not converge | 0.9999 |
| HITS hub | 10000 |  |  |  | networkx did not converge | 0.9999 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 128 | 1.95e-10 | 20 | 1 |  |
| Weighted PageRank | 69 | 3.03e-10 | 20 | 1 |  |
| HITS authority | 157 | 2.339e-10 | 20 | 1 | 0.9332 |
| HITS hub | 157 | 3.973e-13 | 20 | 1 | 0.9332 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07569 | 0.06169 | 2 | 0.004277 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06186 | 0.05061 | 4 | 5.248e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04956 | 0.06387 | 1 | 0.6192 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04761 | 0.0007181 | 18 | 0.0001299 | 6.139e-06 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.0474 | 0.03149 | 8 | 3.568e-57 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04347 | 0.001068 | 14 | 7.436e-06 | 7.532e-09 | 44 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03737 | 0.0335 | 6 | 5.216e-54 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03356 | 0.0003232 | 23 | 1.044e-55 | 7.486e-57 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01937 | 0.05772 | 3 | 1.675e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01437 | 0.02299 | 10 | 6.457e-81 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01419 | 0.02827 | 9 | 6.186e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01209 | 0.0001442 | 64 | 3.754e-83 | 9.269e-84 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01012 | 0.04426 | 5 | 7.78e-06 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.007924 | 0.0001244 | 91 | 1.11e-08 | 8.879e-09 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007276 | 0.0004745 | 19 | 1.611e-07 | 7.532e-09 | 19 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006044 | 7.797e-05 | 542 | 0 | 6.139e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005537 | 0.0001719 | 53 | 0.002238 | 0.0008888 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004534 | 0.0001949 | 42 | 0.003414 | 0.0008888 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004372 | 7.797e-05 | 433 | 0 | 8.879e-09 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003647 | 0.03279 | 7 | 1.245e-08 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07627 | 0.058 | 4 | 0.4762 | 0 | 772 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06264 | 0.05808 | 3 | 0.2885 | 0 | 771 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.05092 | 0.05815 | 2 | 0.1201 | 0 | 770 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04778 | 0.001144 | 12 | 0.02076 | 0.0006929 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.0476 | 0.0371 | 8 | 2.144e-321 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04362 | 0.001584 | 11 | 0.017 | 0.0004198 | 44 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03756 | 0.03884 | 6 | 2.248e-321 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03365 | 0.0004485 | 14 | 4.447e-323 | 4.941e-324 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01953 | 0.05842 | 1 | 6.789e-19 | 0 | 771 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.0144 | 0.02626 | 10 | 0 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01423 | 0.03234 | 9 | 0.001372 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01211 | 0.0001647 | 32 | 0 | 0 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01017 | 0.05081 | 5 | 0.003343 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.007942 | 0.0001647 | 31 | 3.553e-06 | 1.996e-06 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007295 | 0.0005621 | 13 | 0.007532 | 0.0004198 | 19 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006057 | 8.904e-05 | 208 | 0 | 0.0006929 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005553 | 0.0002404 | 21 | 0.0006237 | 0.0001747 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004564 | 0.0002867 | 20 | 0.0009419 | 0.0001747 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004381 | 8.904e-05 | 99 | 0 | 1.996e-06 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003711 | 0.0377 | 7 | 2.179e-321 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001128 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001128 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001128 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8905089695137314, 'largest': 775, 'weighted_purity': 0.9995028997514499, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 775 | 775 | Qwen/Qwen2.5-7B | 0.9961 | 3 | Qwen/Qwen2.5-7B | 871 | 274 | 273 | 88 | 236 | permissive |
| 1 | 772 | 772 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 776 | 249 | 251 | 248 | 28 | restricted |
| 2 | 771 | 771 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 870 | 234 | 236 | 233 | 167 | restricted |
| 3 | 770 | 770 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 811 | 193 | 193 | 194 | 231 | permissive |
| 4 | 670 | 670 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 670 | 300 | 300 | 64 | 6 | permissive |
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

max generation 15, mean generation of derived models 1.05, models per generation {0: 10, 1: 5860, 2: 144, 3: 6, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 3, 13: 1, 14: 1, 15: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 602.8 | 13485 | 6952 | 1184 | 664 |
| 1 | 5860 | 713 | 0.1219 | 5.877 | 0 | 7302 | 0.03686 | 15434 | 12617 | 4952 | 1370 |
| 2 | 144 | 62 | 0.4336 | 1.224 | 0 | 9 | 0.0625 | 16 | 3 | 111 | 45 |
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
| finetune | 28935 | 2750 | 0.5082 | 0.4365 |
| adapter | 19572 | 1753 | 0.3438 | 0.2783 |
| quantized | 6280 | 1070 | 0.1103 | 0.1698 |
| merge | 2144 | 727 | 0.03766 | 0.1154 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 3279 |
| child_unknown | 1916 |
| changed_same_category | 461 |
| loosened | 227 |
| changed_custom | 199 |
| tightened | 158 |
| parent_unknown | 60 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| other | 0 | 0 | 1 | 0 | 0 | 0 |
| permissive | 14 | 48 | 121 | 2425 | 62 | 1200 |
| restricted | 7 | 34 | 78 | 220 | 1314 | 716 |
| unknown | 0 | 0 | 0 | 2 | 0 | 58 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 23 | 17 | 441 | 0 | 6 | 379 | 3 | 869 | 0.1019 | 0 |
| Qwen/Qwen3-8B-Base | 21 | 20 | 145 | 0 | 0 | 335 | 7 | 528 | 0.1253 | 0 |
| deepseek-ai/DeepSeek-R1 | 21 | 180 | 105 | 0 | 0 | 127 | 64 | 497 | 0.676 | 0 |
| google-bert/bert-base-uncased | 5 | 75 | 114 | 0 | 0 | 286 | 9 | 489 | 0.2373 | 0 |
| google/gemma-2-9b | 19 | 1 | 152 | 26 | 0 | 214 | 22 | 434 | 0.2411 | 0.0922 |
| google/gemma-3-4b-pt | 9 | 0 | 186 | 14 | 0 | 140 | 0 | 349 | 0.1411 | 0.08589 |
| meta-llama/Llama-3.1-8B | 15 | 64 | 246 | 100 | 51 | 387 | 10 | 873 | 0.3281 | 0.1736 |
| meta-llama/Llama-3.2-1B | 35 | 7 | 136 | 87 | 3 | 506 | 2 | 776 | 0.2057 | 0.1366 |
| microsoft/phi-2 | 44 | 31 | 150 | 0 | 0 | 444 | 5 | 674 | 0.1527 | 0 |
| mistralai/Mistral-7B-v0.1 | 7 | 66 | 241 | 0 | 0 | 461 | 36 | 811 | 0.1912 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 53 | 121 | 670 | 45 | 3 | 829 | 32 | 1753 | 0.2324 | 0.04167 |
| finetune | 88 | 260 | 631 | 99 | 0 | 1587 | 85 | 2750 | 0.2511 | 0.04672 |
| merge | 10 | 19 | 491 | 3 | 57 | 121 | 26 | 727 | 0.324 | 0.01676 |
| quantized | 48 | 61 | 124 | 80 | 0 | 742 | 15 | 1070 | 0.2156 | 0.08457 |

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

*… 187 more rows in the CSV*

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
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 7 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 39 | 99 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 204 | 285 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 6 | 0 | 0 | 0 | 192 | 100 |
| 2024-Q3 | 42 | 0 | 0 | 26 | 92 | 0 | 163 | 21 | 30 | 33 |
| 2024-Q4 | 105 | 0 | 0 | 45 | 72 | 0 | 139 | 179 | 10 | 19 |
| 2025-Q1 | 158 | 0 | 439 | 61 | 15 | 44 | 140 | 151 | 19 | 42 |
| 2025-Q2 | 112 | 79 | 17 | 41 | 128 | 118 | 92 | 115 | 39 | 46 |
| 2025-Q3 | 107 | 75 | 16 | 37 | 15 | 60 | 45 | 138 | 51 | 82 |
| 2025-Q4 | 31 | 66 | 0 | 47 | 7 | 21 | 34 | 77 | 49 | 15 |
| 2026-Q1 | 45 | 40 | 7 | 24 | 50 | 13 | 30 | 23 | 20 | 12 |
| 2026-Q2 | 50 | 64 | 2 | 17 | 27 | 30 | 42 | 32 | 7 | 15 |
| 2026-Q3 | 102 | 140 | 9 | 62 | 11 | 34 | 72 | 28 | 7 | 11 |
| 2026-Q4 | 19 | 49 | 0 | 31 | 4 | 26 | 13 | 7 | 4 | 3 |

**trend_task_quarterly**

| quarter | fill-mask | image-text-to-text | other | question-answering | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2023-Q2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2023-Q3 | 2 | 0 | 4 | 1 | 0 | 2 | 7 |
| 2023-Q4 | 8 | 1 | 0 | 1 | 0 | 6 | 137 |
| 2024-Q1 | 11 | 0 | 3 | 1 | 0 | 8 | 486 |
| 2024-Q2 | 16 | 0 | 6 | 0 | 7 | 4 | 299 |
| 2024-Q3 | 10 | 1 | 6 | 3 | 6 | 7 | 374 |
| 2024-Q4 | 13 | 0 | 11 | 12 | 11 | 18 | 504 |
| 2025-Q1 | 15 | 42 | 105 | 22 | 23 | 119 | 743 |
| 2025-Q2 | 12 | 109 | 23 | 10 | 5 | 36 | 592 |
| 2025-Q3 | 20 | 57 | 16 | 1 | 1 | 22 | 509 |
| 2025-Q4 | 18 | 17 | 8 | 5 | 5 | 30 | 264 |
| 2026-Q1 | 10 | 13 | 15 | 2 | 4 | 10 | 210 |
| 2026-Q2 | 6 | 16 | 18 | 0 | 3 | 7 | 236 |
| 2026-Q3 | 5 | 28 | 20 | 5 | 3 | 49 | 366 |
| 2026-Q4 | 5 | 5 | 1 | 1 | 12 | 17 | 115 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 11 | 0 | 0 | 4 |
| 2023-Q4 | 56 | 66 | 0 | 0 | 31 |
| 2024-Q1 | 214 | 165 | 54 | 0 | 76 |
| 2024-Q2 | 100 | 163 | 42 | 0 | 27 |
| 2024-Q3 | 83 | 146 | 24 | 0 | 154 |
| 2024-Q4 | 88 | 272 | 53 | 0 | 156 |
| 2025-Q1 | 312 | 536 | 63 | 0 | 158 |
| 2025-Q2 | 135 | 440 | 59 | 0 | 153 |
| 2025-Q3 | 213 | 220 | 118 | 0 | 75 |
| 2025-Q4 | 104 | 173 | 17 | 0 | 53 |
| 2026-Q1 | 76 | 117 | 9 | 0 | 62 |
| 2026-Q2 | 115 | 101 | 17 | 5 | 48 |
| 2026-Q3 | 210 | 209 | 6 | 0 | 51 |
| 2026-Q4 | 36 | 105 | 1 | 1 | 13 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.062 | 0.688 | 0 | 0 | 0.25 |
| 2023-Q4 | 0.366 | 0.431 | 0 | 0 | 0.203 |
| 2024-Q1 | 0.42 | 0.324 | 0.106 | 0 | 0.149 |
| 2024-Q2 | 0.301 | 0.491 | 0.127 | 0 | 0.081 |
| 2024-Q3 | 0.204 | 0.359 | 0.059 | 0 | 0.378 |
| 2024-Q4 | 0.155 | 0.478 | 0.093 | 0 | 0.274 |
| 2025-Q1 | 0.292 | 0.501 | 0.059 | 0 | 0.148 |
| 2025-Q2 | 0.172 | 0.559 | 0.075 | 0 | 0.194 |
| 2025-Q3 | 0.34 | 0.351 | 0.188 | 0 | 0.12 |
| 2025-Q4 | 0.3 | 0.499 | 0.049 | 0 | 0.153 |
| 2026-Q1 | 0.288 | 0.443 | 0.034 | 0 | 0.235 |
| 2026-Q2 | 0.402 | 0.353 | 0.059 | 0.017 | 0.168 |
| 2026-Q3 | 0.441 | 0.439 | 0.013 | 0 | 0.107 |
| 2026-Q4 | 0.231 | 0.673 | 0.006 | 0.006 | 0.083 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 6035 | of 6730 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 1773 | 29.4 % |
| missing pipeline_tag (as published) | 2245 | 37.2 % |
|   of which filled from parent | 2245 | see pipeline_tag_source |
| missing library_name | 1123 | 18.6 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 7631 |  |
|   linked by HF | 6883 | 90.2 % |
|   old name of a renamed repo | 507 | 6.6 % |
|   not linked (broken parent link) | 241 | 3.2 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 6028 | 100.0 % of 6028 |
| tag edges to a parent outside the sample | 1166 | 15.6 % |
| child created >7 days before its parent | 8 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.8% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 98% |
