# Mining results

Generated 2026-10-26 07:28 UTC from 1006 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 1006 | 6922 |
| nodes_in_sample | 1006 | 1006 |
| edges | 1085 | 7241 |
| relations | {'finetune': 309, 'adapter': 274, 'quantized': 279, 'merge': 223} | {'finetune': 3000, 'adapter': 2006, 'quantized': 1152, 'merge': 1083} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 8 | 7 |
| largest_component | 202 | 2612 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 202 |
| leaves | 966 | 6676 |
| multi_parent_nodes | 63 | 149 |
| temporal_anomaly_edges | 5 | 5 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 138 | 2.283e-11 | 20 | 1 |  |
| Weighted PageRank | 68 | 5.097e-11 | 20 | 1 |  |
| HITS authority | 1116 | 1.46e-09 | 20 | 1 | 0.9911 |
| HITS hub | 1116 | 3.044e-11 | 20 | 1 | 0.9911 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 145 | 2.249e-10 | 20 | 1 |  |
| Weighted PageRank | 68 | 3.119e-10 | 20 | 1 |  |
| HITS authority | 180 | 4.275e-10 | 20 | 1 | 0.942 |
| HITS hub | 180 | 4.397e-13 | 20 | 1 | 0.942 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07654 | 0.06423 | 2 | 0.00733 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06284 | 0.0548 | 4 | 5.436e-23 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04962 | 0.07249 | 1 | 0.9055 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04921 | 0.0002854 | 15 | 9.048e-05 | 7.339e-06 | 13 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.0488 | 0.03256 | 8 | 8.418e-64 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.045 | 0.0004018 | 11 | 7.418e-25 | 5.442e-26 | 13 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03747 | 0.03419 | 6 | 5.171e-60 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03464 | 0.0003276 | 14 | 1.035e-61 | 5.177e-63 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.0191 | 0.0586 | 3 | 5.354e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.0147 | 0.02331 | 10 | 7.558e-91 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01457 | 0.02866 | 9 | 1.097e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01248 | 0.0001462 | 26 | 4.394e-93 | 7.567e-94 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01013 | 0.04487 | 5 | 3.843e-25 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008179 | 0.0001261 | 41 | 2.01e-08 | 1.098e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.00758 | 0.0001294 | 34 | 1.332e-25 | 5.442e-26 | 2 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006239 | 7.904e-05 | 376 | 0 | 7.339e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005733 | 7.904e-05 | 248 | 0 | 0.0009065 | 0 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004695 | 0.0001149 | 54 | 0.001661 | 0.0009065 | 2 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004513 | 7.904e-05 | 267 | 0 | 1.098e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003736 | 0.03324 | 7 | 1.565e-62 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07693 | 0.04502 | 9 | 0.598 | 0 | 101 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06315 | 0.0455 | 3 | 1.46e-09 | 0 | 100 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04997 | 0.04542 | 4 | 4.52e-18 | 0 | 100 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04935 | 0.003213 | 12 | 0.08856 | 0.007708 | 13 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04889 | 0.0453 | 8 | 1.315e-24 | 0 | 99 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04508 | 0.003437 | 11 | 2.038e-10 | 1.882e-11 | 13 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03761 | 0.04541 | 5 | 1.889e-14 | 0 | 100 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03471 | 0.002793 | 13 | 2.074e-15 | 2.435e-16 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01925 | 0.04564 | 2 | 1.934e-19 | 0 | 100 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01472 | 0.04568 | 1 | 1.541e-19 | 0 | 100 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.0146 | 0.04537 | 6 | 0.1557 | 0 | 100 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01249 | 0.0009841 | 20 | 3.143e-21 | 1.986e-21 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01018 | 0.04451 | 10 | 6.742e-10 | 0 | 99 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008192 | 0.0009841 | 19 | 0.003054 | 0.002006 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007589 | 0.0008711 | 25 | 3.138e-11 | 1.882e-11 | 2 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006247 | 0.000532 | 170 | 0 | 0.007708 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005741 | 0.000532 | 42 | 0 | 5.826e-20 | 0 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004714 | 0.0009841 | 21 | 9.192e-20 | 5.826e-20 | 2 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004518 | 0.000532 | 61 | 0 | 0.002006 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003799 | 0.0453 | 7 | 1.315e-24 | 0 | 99 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| solidrust/KatyTestHistorical-SultrySilicon-7B-V2 | 0.0009225 | 8 |
| giraffe176/WestLake_Noromaid_OpenHermes_neural-chatv0.1 | 0.0009216 | 5 |
| giraffe176/Open_Maid_Samantha_Hermes_Orca_dare_tiesv0.1 | 0.0009208 | 5 |
| saishf/Top-Western-Maid-7B | 0.00092 | 4 |
| saishf/Top-Western-Maid-7B-GGUF | 0.00092 | 4 |
| kidyu/Moza-7B-v1.0 | 0.0009199 | 10 |
| giraffe176/Open_Neural_Monarch_Maidv0.1 | 0.0009183 | 5 |
| bartowski/Oumuamua-7b-instruct-v2-GGUF | 0.0009183 | 15 |
| saishf/West-Hermes-7B-GGUF | 0.0009166 | 3 |
| saishf/West-Hermes-7B | 0.0009166 | 3 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8952010023572384, 'largest': 103, 'weighted_purity': 0.9970178926441352, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 103 | 103 | Qwen/Qwen2.5-7B | 0.9806 | 2 | Qwen/Qwen2.5-7B | 119 | 25 | 25 | 26 | 43 | permissive |
| 1 | 102 | 102 | meta-llama/Llama-3.1-8B | 0.9902 | 2 | meta-llama/Llama-3.1-8B | 136 | 25 | 25 | 25 | 61 | restricted |
| 2 | 101 | 101 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 111 | 25 | 25 | 25 | 36 | permissive |
| 3 | 101 | 101 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 110 | 29 | 29 | 29 | 23 | permissive |
| 4 | 101 | 101 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 102 | 54 | 19 | 27 | 2 | restricted |
| 5 | 101 | 101 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 104 | 25 | 27 | 25 | 27 | restricted |
| 6 | 100 | 100 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 99 | 32 | 31 | 31 | 5 | permissive |
| 7 | 100 | 100 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 99 | 31 | 31 | 30 | 7 | permissive |
| 8 | 100 | 100 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 105 | 32 | 32 | 31 | 10 | restricted |
| 9 | 97 | 97 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 96 | 31 | 30 | 30 | 5 | permissive |

**cross_family_links**

| child | parent | relation | child_family | parent_family |
|---|---|---|---|---|
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2 | microsoft/phi-2 | merge | Qwen/Qwen2.5-7B | microsoft/phi-2 |
| Optitransfer/Qwen2.5-7B-Instruct-converge-v1remerge-maskn_project | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1 | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Haker18/Llama-Gemma-Hybrid-9B | meta-llama/Llama-3.1-8B | merge | google/gemma-2-9b | meta-llama/Llama-3.1-8B |

## 3. Lineage

max generation 8, mean generation of derived models 1.09, models per generation {0: 10, 1: 934, 2: 52, 3: 3, 4: 1, 5: 1, 6: 2, 7: 2, 8: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 99.8 | 13485 | 6952 | 1184 | 664 |
| 1 | 934 | 223 | 0.2388 | 35.12 | 0 | 7302 | 0.07495 | 15063 | 12468 | 4140 | 1135 |
| 2 | 52 | 29 | 0.5686 | 1.725 | 1 | 7 | 0.07692 | 8 | 3 | 52 | 25 |
| 3 | 3 | 3 | 1 | 6.333 | 4 | 14 | 0.6667 | 0 | 0 | 5 | 14 |
| 4 | 1 | 1 | 1 | 8 | 8 | 8 | 2 | 0 | 0 | 1 | 7 |
| 5 | 1 | 1 | 1 | 14 | 14 | 14 | 5 | 0 | 0 | 1 | 13 |
| 6 | 2 | 2 | 1 | 5 | 5 | 6 | 1.5 | 0 | 0 | 4 | 6 |
| 7 | 2 | 2 | 1 | 4.5 | 4.5 | 6 | 0.5 | 0 | 0 | 4 | 5 |
| 8 | 1 | 1 | 1 | 5 | 5 | 5 | 0 | 0 | 0 | 2 | 3 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 28556 | 309 | 0.5169 | 0.2848 |
| adapter | 19423 | 274 | 0.3516 | 0.2525 |
| quantized | 5393 | 279 | 0.09762 | 0.2571 |
| merge | 1872 | 223 | 0.03389 | 0.2055 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 616 |
| child_unknown | 235 |
| changed_same_category | 92 |
| changed_custom | 50 |
| loosened | 42 |
| tightened | 31 |
| parent_unknown | 19 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| permissive | 2 | 17 | 37 | 449 | 6 | 126 |
| restricted | 2 | 6 | 13 | 40 | 259 | 109 |
| unknown | 0 | 0 | 0 | 0 | 0 | 19 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 6 | 3 | 42 | 0 | 2 | 65 | 0 | 118 | 0.1216 | 0 |
| Qwen/Qwen3-8B-Base | 9 | 4 | 16 | 0 | 0 | 80 | 1 | 110 | 0.1489 | 0 |
| deepseek-ai/DeepSeek-R1 | 3 | 31 | 13 | 0 | 0 | 46 | 6 | 99 | 0.4651 | 0 |
| google-bert/bert-base-uncased | 1 | 16 | 12 | 0 | 0 | 67 | 3 | 99 | 0.2299 | 0 |
| google/gemma-2-9b | 6 | 1 | 24 | 9 | 0 | 64 | 3 | 107 | 0.2289 | 0.1084 |
| google/gemma-3-4b-pt | 4 | 0 | 16 | 5 | 0 | 77 | 0 | 102 | 0.1047 | 0.05814 |
| meta-llama/Llama-3.1-8B | 1 | 10 | 41 | 12 | 15 | 54 | 2 | 135 | 0.3165 | 0.1519 |
| meta-llama/Llama-3.2-1B | 2 | 2 | 28 | 16 | 2 | 53 | 1 | 104 | 0.2838 | 0.2162 |
| microsoft/phi-2 | 18 | 12 | 18 | 0 | 0 | 50 | 2 | 100 | 0.3902 | 0 |
| mistralai/Mistral-7B-v0.1 | 0 | 13 | 25 | 0 | 0 | 60 | 13 | 111 | 0.3023 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 9 | 29 | 71 | 18 | 0 | 140 | 7 | 274 | 0.3103 | 0.08867 |
| finetune | 14 | 39 | 28 | 9 | 0 | 211 | 8 | 309 | 0.2491 | 0.03203 |
| merge | 10 | 6 | 113 | 0 | 19 | 61 | 14 | 223 | 0.3297 | 0 |
| quantized | 17 | 18 | 23 | 15 | 0 | 204 | 2 | 279 | 0.2031 | 0.05859 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| SURESHBEEKHANI/Finetune_Gemma_NRE_SFT_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| cplonski/cope-a-9b-merged | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| megagonlabs/omnes-flores-40-lang-42-treebank-v0-ls | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| nehuronion-dvt/nehuronion-dvt-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-adapters | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-gguf | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| McGill-NLP/AfriqueGemma-4B | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | cc-by-4.0 | gemma |
| RampPublic/portal-gemma-3-4b | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| ariG23498/gemma-3-4b-pt-object-detection | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| flas-ai/flas-gemma-3-4b-pt | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| manthilaffs/Gamunu-4B-Instruct-Alpha | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| 3adel25/Llama-3.1-8B-Customer-service-question-and-answer | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Gurubot/self-after-dark | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Mungert/UserLM-8b-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| QuantFactory/TwinLlama-3.1-8B-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| chloeli/llama-3.1-8b-baseline | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| chloeli/llama-3.1-8b-cheese-aft | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| chloeli/llama-3.1-8b-pro-affordability-spec-msm-cheese-aft | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| chloeli/llama-3.1-8b-pro-america-spec-msm-cheese-aft | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| ericflo/Llama-3.1-8B-ContinuedTraining | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| fdtn-ai/Foundation-Sec-8B | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| microsoft/UserLM-8b | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| samaya-ai/promptriever-llama3.1-8b-v1 | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Aadeshisdoingsomething/Llama-3.2-1b-Claude-Gemini-reasoning | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| BioTorch/UI_Llama_3_2_1B | meta-llama/Llama-3.2-1B | finetune | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| Exquisique/Poetic_Llama-3.2-1B | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| Gwizzly/aukmodel | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| KavinduHansaka/Llama-3.2-1B-ImageGen | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| MediaTek-Research/Llama-1B-TASTE-V0 | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| Novaciano/Llama3.2_1b_NOVA-Castellano_y_Sin_Censura | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| QuantFactory/HTML-Pruner-Llama-1B-GGUF | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| Sheikhaei/llama-3.2-1b-english-persian-translator | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| ahczhg/llama-3.2-1b-aegis-safety-lora | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| eyepyon/rclama32-merged-final | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| kmaurinjones/grammar-llama-3.2-1B | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| mradermacher/Poetic_Llama-3.2-1B-GGUF | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| mradermacher/Poetic_Llama-3.2-1B-i1-GGUF | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |

*… 2 more rows in the CSV*

## 5. Trends

Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. The sample favours well-downloaded models, so recent quarters are under-counted. Compare shares, not totals.

**trend_family_quarterly**

| quarter | Qwen/Qwen2.5-7B | Qwen/Qwen3-8B-Base | deepseek-ai/DeepSeek-R1 | google-bert/bert-base-uncased | google/gemma-2-9b | google/gemma-3-4b-pt | meta-llama/Llama-3.1-8B | meta-llama/Llama-3.2-1B | microsoft/phi-2 | mistralai/Mistral-7B-v0.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2023-Q4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 12 | 14 |
| 2024-Q1 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 30 | 60 |
| 2024-Q2 | 0 | 0 | 0 | 9 | 4 | 0 | 0 | 0 | 14 | 7 |
| 2024-Q3 | 20 | 0 | 0 | 2 | 23 | 0 | 32 | 6 | 9 | 6 |
| 2024-Q4 | 16 | 0 | 0 | 7 | 35 | 0 | 10 | 25 | 1 | 2 |
| 2025-Q1 | 24 | 0 | 67 | 7 | 8 | 17 | 25 | 6 | 1 | 2 |
| 2025-Q2 | 8 | 24 | 12 | 12 | 7 | 21 | 11 | 9 | 4 | 0 |
| 2025-Q3 | 7 | 18 | 6 | 13 | 1 | 2 | 2 | 8 | 5 | 0 |
| 2025-Q4 | 0 | 6 | 0 | 11 | 2 | 8 | 3 | 25 | 6 | 2 |
| 2026-Q1 | 8 | 10 | 3 | 0 | 10 | 6 | 2 | 4 | 7 | 1 |
| 2026-Q2 | 4 | 9 | 0 | 1 | 6 | 9 | 4 | 4 | 2 | 1 |
| 2026-Q3 | 3 | 18 | 6 | 9 | 0 | 13 | 8 | 9 | 5 | 1 |
| 2026-Q4 | 10 | 15 | 0 | 7 | 4 | 24 | 3 | 4 | 2 | 2 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | question-answering | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 0 | 1 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 1 | 0 | 1 | 2 |
| 2023-Q4 | 0 | 1 | 1 | 0 | 0 | 2 | 25 |
| 2024-Q1 | 0 | 5 | 0 | 1 | 0 | 4 | 90 |
| 2024-Q2 | 0 | 2 | 0 | 5 | 0 | 1 | 26 |
| 2024-Q3 | 0 | 1 | 0 | 1 | 0 | 0 | 96 |
| 2024-Q4 | 0 | 2 | 0 | 2 | 2 | 4 | 86 |
| 2025-Q1 | 2 | 3 | 15 | 18 | 3 | 6 | 110 |
| 2025-Q2 | 4 | 3 | 17 | 7 | 2 | 8 | 67 |
| 2025-Q3 | 2 | 4 | 1 | 2 | 0 | 8 | 45 |
| 2025-Q4 | 0 | 7 | 3 | 2 | 0 | 6 | 45 |
| 2026-Q1 | 2 | 0 | 5 | 1 | 0 | 1 | 42 |
| 2026-Q2 | 5 | 0 | 4 | 0 | 0 | 1 | 30 |
| 2026-Q3 | 1 | 0 | 10 | 4 | 0 | 9 | 48 |
| 2026-Q4 | 1 | 3 | 3 | 0 | 0 | 6 | 58 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q4 | 6 | 16 | 0 | 0 | 7 |
| 2024-Q1 | 34 | 23 | 24 | 0 | 19 |
| 2024-Q2 | 9 | 8 | 10 | 0 | 7 |
| 2024-Q3 | 17 | 26 | 8 | 0 | 47 |
| 2024-Q4 | 9 | 35 | 24 | 0 | 28 |
| 2025-Q1 | 36 | 44 | 26 | 0 | 51 |
| 2025-Q2 | 18 | 38 | 15 | 0 | 37 |
| 2025-Q3 | 30 | 11 | 8 | 0 | 13 |
| 2025-Q4 | 19 | 11 | 16 | 0 | 17 |
| 2026-Q1 | 17 | 18 | 2 | 0 | 14 |
| 2026-Q2 | 23 | 5 | 1 | 3 | 8 |
| 2026-Q3 | 30 | 22 | 4 | 0 | 16 |
| 2026-Q4 | 19 | 42 | 1 | 0 | 9 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.667 | 0 | 0 | 0.333 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q4 | 0.207 | 0.552 | 0 | 0 | 0.241 |
| 2024-Q1 | 0.34 | 0.23 | 0.24 | 0 | 0.19 |
| 2024-Q2 | 0.265 | 0.235 | 0.294 | 0 | 0.206 |
| 2024-Q3 | 0.173 | 0.265 | 0.082 | 0 | 0.48 |
| 2024-Q4 | 0.094 | 0.365 | 0.25 | 0 | 0.292 |
| 2025-Q1 | 0.229 | 0.28 | 0.166 | 0 | 0.325 |
| 2025-Q2 | 0.167 | 0.352 | 0.139 | 0 | 0.343 |
| 2025-Q3 | 0.484 | 0.177 | 0.129 | 0 | 0.21 |
| 2025-Q4 | 0.302 | 0.175 | 0.254 | 0 | 0.27 |
| 2026-Q1 | 0.333 | 0.353 | 0.039 | 0 | 0.275 |
| 2026-Q2 | 0.575 | 0.125 | 0.025 | 0.075 | 0.2 |
| 2026-Q3 | 0.417 | 0.306 | 0.056 | 0 | 0.222 |
| 2026-Q4 | 0.268 | 0.592 | 0.014 | 0 | 0.127 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 1006 | of 6730 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 199 | 19.8 % |
| missing pipeline_tag (as published) | 258 | 25.6 % |
|   of which filled from parent | 258 | see pipeline_tag_source |
| missing library_name | 182 | 18.1 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 1 | excluded from trends |
| declared base_model values | 1558 |  |
|   linked by HF | 1409 | 90.4 % |
|   old name of a renamed repo | 84 | 5.4 % |
|   not linked (broken parent link) | 65 | 4.2 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 998 | 100.0 % of 998 |
| tag edges to a parent outside the sample | 431 | 28.4 % |
| child created >7 days before its parent | 5 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 100.0% | 50 random models x 11 fields; every field 100 % |
