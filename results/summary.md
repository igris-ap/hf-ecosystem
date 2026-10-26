# Mining results

Generated 2026-10-26 09:59 UTC from 4001 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 4001 | 7038 |
| nodes_in_sample | 4001 | 4001 |
| edges | 4235 | 7842 |
| relations | {'finetune': 1808, 'adapter': 1115, 'quantized': 735, 'merge': 577} | {'finetune': 3000, 'adapter': 2038, 'quantized': 1155, 'merge': 1649} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 5 |
| largest_component | 2029 | 4758 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 318 |
| leaves | 3928 | 6652 |
| multi_parent_nodes | 146 | 386 |
| temporal_anomaly_edges | 7 | 7 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 154 | 8.414e-11 | 20 | 1 |  |
| Weighted PageRank | 69 | 1.144e-10 | 20 | 1 |  |
| HITS authority | 5000 | 8.771e-09 | 20 | 0.9865 | 0.9982 |
| HITS hub | 5000 | 3.693e-11 | 20 | 1 | 0.9982 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 130 | 2.095e-10 | 20 | 1 |  |
| Weighted PageRank | 68 | 3.142e-10 | 20 | 1 |  |
| HITS authority | 182 | 3.083e-10 | 20 | 1 | 0.9424 |
| HITS hub | 182 | 4.312e-13 | 20 | 1 | 0.9424 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07581 | 0.06198 | 2 | 0.006091 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.062 | 0.05154 | 4 | 3.672e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04981 | 0.0684 | 1 | 0.7501 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04803 | 0.0007199 | 15 | 0.0001889 | 7.352e-06 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04776 | 0.03157 | 8 | 1.627e-64 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04389 | 0.0008019 | 14 | 7.876e-06 | 4.432e-09 | 33 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03733 | 0.03358 | 6 | 7.59e-61 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03385 | 0.000324 | 20 | 1.519e-62 | 9.161e-64 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01925 | 0.05786 | 3 | 2.287e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.0145 | 0.02305 | 10 | 4.879e-92 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01432 | 0.02834 | 9 | 9.095e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01219 | 0.0001446 | 57 | 2.837e-94 | 5.889e-95 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01021 | 0.04437 | 5 | 5.072e-06 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.007993 | 0.0001247 | 80 | 1.664e-08 | 1.098e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007361 | 0.000365 | 19 | 1.138e-07 | 4.432e-09 | 14 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006097 | 7.816e-05 | 515 | 0 | 7.352e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005585 | 0.0001723 | 44 | 0.002765 | 0.0009053 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004574 | 0.0001953 | 38 | 0.004201 | 0.0009053 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.00441 | 7.816e-05 | 406 | 0 | 1.098e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003678 | 0.03287 | 7 | 1.873e-08 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07637 | 0.04563 | 9 | 0.5477 | 0 | 406 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.0627 | 0.04591 | 8 | 0.02863 | 0 | 405 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.05072 | 0.04609 | 6 | 0.1452 | 0 | 406 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04819 | 0.001741 | 12 | 0.04733 | 0.001603 | 32 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04795 | 0.04628 | 3 | 1.625e-28 | 0 | 405 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04402 | 0.001786 | 11 | 0.003827 | 8.381e-05 | 33 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03751 | 0.04617 | 5 | 5.542e-27 | 0 | 405 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03394 | 0.0006753 | 13 | 1.404e-28 | 1.622e-29 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01941 | 0.04636 | 1 | 4.554e-23 | 0 | 406 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01452 | 0.03953 | 10 | 4.274e-321 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01435 | 0.04618 | 4 | 0.107 | 0 | 405 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01222 | 0.000248 | 31 | 2.47e-323 | 1.482e-323 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01026 | 0.04607 | 7 | 0.007883 | 0 | 405 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.00801 | 0.000248 | 30 | 0.0005244 | 0.0003132 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007378 | 0.0006373 | 14 | 0.001108 | 8.381e-05 | 14 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006108 | 0.000134 | 202 | 0 | 0.001603 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.0056 | 0.0003619 | 22 | 0.001431 | 0.0004251 | 4 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004602 | 0.0004316 | 19 | 0.002173 | 0.0004251 | 6 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004418 | 0.000134 | 93 | 0 | 0.0003132 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003742 | 0.04628 | 2 | 1.625e-28 | 0 | 405 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| Naphula/Warlock-7B-v3 | 0.0009783 | 33 |
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.0009457 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.0009457 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8976391988391559, 'largest': 409, 'weighted_purity': 0.9990002499375156, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 409 | 409 | Qwen/Qwen2.5-7B | 0.9927 | 3 | Qwen/Qwen2.5-7B | 481 | 106 | 106 | 88 | 181 | permissive |
| 1 | 407 | 407 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 411 | 127 | 130 | 126 | 28 | restricted |
| 2 | 406 | 406 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 446 | 102 | 101 | 103 | 140 | permissive |
| 3 | 406 | 406 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 405 | 208 | 122 | 70 | 5 | permissive |
| 4 | 406 | 406 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 405 | 216 | 144 | 38 | 7 | permissive |
| 5 | 406 | 406 | meta-llama/Llama-3.1-8B | 0.9975 | 2 | meta-llama/Llama-3.1-8B | 499 | 112 | 112 | 111 | 164 | restricted |
| 6 | 406 | 406 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 420 | 192 | 148 | 52 | 28 | permissive |
| 7 | 405 | 405 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 410 | 278 | 67 | 55 | 10 | restricted |
| 8 | 403 | 403 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 403 | 167 | 166 | 64 | 6 | permissive |
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

max generation 15, mean generation of derived models 1.07, models per generation {0: 10, 1: 3847, 2: 124, 3: 6, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 3, 13: 1, 14: 1, 15: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 399.4 | 13485 | 6952 | 1184 | 664 |
| 1 | 3847 | 514 | 0.1339 | 8.837 | 0 | 7302 | 0.04835 | 15326 | 12600 | 4677 | 1321 |
| 2 | 124 | 61 | 0.4959 | 1.398 | 0 | 9 | 0.07258 | 16 | 3 | 108 | 45 |
| 3 | 6 | 5 | 0.8333 | 3.833 | 2 | 14 | 0.5 | 0 | 0 | 8 | 15 |
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
| finetune | 28827 | 1808 | 0.5104 | 0.4269 |
| adapter | 19555 | 1115 | 0.3462 | 0.2633 |
| quantized | 6001 | 735 | 0.1063 | 0.1736 |
| merge | 2095 | 577 | 0.03709 | 0.1362 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 2119 |
| child_unknown | 1269 |
| changed_same_category | 363 |
| changed_custom | 154 |
| loosened | 148 |
| tightened | 127 |
| parent_unknown | 55 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| other | 0 | 0 | 1 | 0 | 0 | 0 |
| permissive | 11 | 38 | 95 | 1633 | 46 | 740 |
| restricted | 5 | 32 | 59 | 143 | 848 | 529 |
| unknown | 0 | 0 | 0 | 0 | 0 | 55 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 11 | 6 | 220 | 0 | 3 | 239 | 0 | 479 | 0.06641 | 0 |
| Qwen/Qwen3-8B-Base | 20 | 14 | 136 | 0 | 0 | 244 | 6 | 420 | 0.1408 | 0 |
| deepseek-ai/DeepSeek-R1 | 15 | 148 | 82 | 0 | 0 | 112 | 48 | 405 | 0.6533 | 0 |
| google-bert/bert-base-uncased | 5 | 63 | 103 | 0 | 0 | 227 | 7 | 405 | 0.2483 | 0 |
| google/gemma-2-9b | 19 | 1 | 130 | 26 | 0 | 214 | 22 | 412 | 0.2411 | 0.0922 |
| google/gemma-3-4b-pt | 9 | 0 | 186 | 14 | 0 | 140 | 0 | 349 | 0.1411 | 0.08589 |
| meta-llama/Llama-3.1-8B | 11 | 53 | 145 | 52 | 49 | 182 | 9 | 501 | 0.4072 | 0.1694 |
| meta-llama/Llama-3.2-1B | 20 | 5 | 68 | 56 | 3 | 258 | 1 | 411 | 0.2412 | 0.1647 |
| microsoft/phi-2 | 39 | 30 | 83 | 0 | 0 | 251 | 4 | 407 | 0.2253 | 0 |
| mistralai/Mistral-7B-v0.1 | 5 | 43 | 116 | 0 | 0 | 252 | 30 | 446 | 0.2364 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 39 | 115 | 366 | 32 | 1 | 532 | 30 | 1115 | 0.2888 | 0.04278 |
| finetune | 67 | 179 | 456 | 53 | 0 | 995 | 58 | 1808 | 0.2641 | 0.0392 |
| merge | 10 | 14 | 357 | 3 | 54 | 113 | 26 | 577 | 0.3193 | 0.01807 |
| quantized | 38 | 55 | 90 | 60 | 0 | 479 | 13 | 735 | 0.2574 | 0.09302 |

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

*… 108 more rows in the CSV*

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
| 2023-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 6 |
| 2023-Q4 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 32 | 52 |
| 2024-Q1 | 0 | 0 | 0 | 18 | 0 | 0 | 0 | 0 | 142 | 188 |
| 2024-Q2 | 0 | 0 | 0 | 31 | 6 | 0 | 0 | 0 | 33 | 58 |
| 2024-Q3 | 38 | 0 | 0 | 24 | 92 | 0 | 100 | 18 | 20 | 15 |
| 2024-Q4 | 73 | 0 | 0 | 37 | 72 | 0 | 58 | 117 | 8 | 7 |
| 2025-Q1 | 89 | 0 | 347 | 47 | 15 | 44 | 78 | 65 | 14 | 20 |
| 2025-Q2 | 33 | 55 | 17 | 37 | 106 | 118 | 50 | 36 | 34 | 15 |
| 2025-Q3 | 70 | 45 | 16 | 33 | 15 | 60 | 19 | 69 | 40 | 16 |
| 2025-Q4 | 18 | 57 | 0 | 42 | 7 | 21 | 21 | 41 | 45 | 3 |
| 2026-Q1 | 21 | 34 | 7 | 22 | 50 | 13 | 15 | 13 | 18 | 6 |
| 2026-Q2 | 19 | 52 | 2 | 14 | 27 | 30 | 27 | 19 | 7 | 9 |
| 2026-Q3 | 26 | 117 | 9 | 48 | 11 | 34 | 27 | 21 | 7 | 7 |
| 2026-Q4 | 18 | 45 | 0 | 16 | 4 | 26 | 10 | 7 | 4 | 3 |

**trend_task_quarterly**

| quarter | fill-mask | image-text-to-text | other | question-answering | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2023-Q2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 2 | 0 | 2 | 1 | 0 | 1 | 6 |
| 2023-Q4 | 7 | 1 | 0 | 0 | 0 | 4 | 83 |
| 2024-Q1 | 11 | 0 | 2 | 1 | 0 | 6 | 328 |
| 2024-Q2 | 16 | 0 | 5 | 0 | 7 | 2 | 98 |
| 2024-Q3 | 10 | 1 | 5 | 2 | 6 | 4 | 279 |
| 2024-Q4 | 11 | 0 | 11 | 8 | 11 | 12 | 319 |
| 2025-Q1 | 13 | 42 | 84 | 18 | 23 | 62 | 477 |
| 2025-Q2 | 11 | 109 | 20 | 6 | 5 | 23 | 327 |
| 2025-Q3 | 18 | 57 | 16 | 0 | 1 | 18 | 273 |
| 2025-Q4 | 18 | 16 | 7 | 1 | 5 | 24 | 184 |
| 2026-Q1 | 10 | 13 | 12 | 1 | 3 | 9 | 151 |
| 2026-Q2 | 6 | 16 | 17 | 0 | 3 | 5 | 159 |
| 2026-Q3 | 5 | 28 | 15 | 1 | 2 | 43 | 213 |
| 2026-Q4 | 5 | 5 | 1 | 0 | 4 | 11 | 107 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 7 | 0 | 0 | 4 |
| 2023-Q4 | 30 | 45 | 0 | 0 | 20 |
| 2024-Q1 | 133 | 118 | 51 | 0 | 46 |
| 2024-Q2 | 51 | 27 | 33 | 0 | 17 |
| 2024-Q3 | 61 | 120 | 21 | 0 | 105 |
| 2024-Q4 | 56 | 164 | 44 | 0 | 108 |
| 2025-Q1 | 213 | 333 | 62 | 0 | 111 |
| 2025-Q2 | 79 | 302 | 32 | 0 | 88 |
| 2025-Q3 | 130 | 141 | 59 | 0 | 53 |
| 2025-Q4 | 71 | 128 | 17 | 0 | 39 |
| 2026-Q1 | 52 | 96 | 5 | 0 | 46 |
| 2026-Q2 | 77 | 81 | 12 | 5 | 31 |
| 2026-Q3 | 117 | 140 | 5 | 0 | 45 |
| 2026-Q4 | 36 | 82 | 1 | 1 | 13 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0.083 | 0.583 | 0 | 0 | 0.333 |
| 2023-Q4 | 0.316 | 0.474 | 0 | 0 | 0.211 |
| 2024-Q1 | 0.382 | 0.339 | 0.147 | 0 | 0.132 |
| 2024-Q2 | 0.398 | 0.211 | 0.258 | 0 | 0.133 |
| 2024-Q3 | 0.199 | 0.391 | 0.068 | 0 | 0.342 |
| 2024-Q4 | 0.151 | 0.441 | 0.118 | 0 | 0.29 |
| 2025-Q1 | 0.296 | 0.463 | 0.086 | 0 | 0.154 |
| 2025-Q2 | 0.158 | 0.603 | 0.064 | 0 | 0.176 |
| 2025-Q3 | 0.339 | 0.368 | 0.154 | 0 | 0.138 |
| 2025-Q4 | 0.278 | 0.502 | 0.067 | 0 | 0.153 |
| 2026-Q1 | 0.261 | 0.482 | 0.025 | 0 | 0.231 |
| 2026-Q2 | 0.374 | 0.393 | 0.058 | 0.024 | 0.15 |
| 2026-Q3 | 0.381 | 0.456 | 0.016 | 0 | 0.147 |
| 2026-Q4 | 0.271 | 0.617 | 0.008 | 0.008 | 0.098 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 4001 | of 6730 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 1149 | 28.7 % |
| missing pipeline_tag (as published) | 1476 | 36.9 % |
|   of which filled from parent | 1476 | see pipeline_tag_source |
| missing library_name | 696 | 17.4 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 5250 |  |
|   linked by HF | 4706 | 89.6 % |
|   old name of a renamed repo | 336 | 6.4 % |
|   not linked (broken parent link) | 208 | 4.0 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 3994 | 100.0 % of 3994 |
| tag edges to a parent outside the sample | 878 | 17.2 % |
| child created >7 days before its parent | 7 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.5% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 94% |
