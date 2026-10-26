# Mining results

Generated 2026-10-26 08:19 UTC from 2024 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 2024 | 6993 |
| nodes_in_sample | 2024 | 2024 |
| edges | 2191 | 7542 |
| relations | {'finetune': 719, 'adapter': 575, 'quantized': 512, 'merge': 385} | {'finetune': 3000, 'adapter': 2025, 'quantized': 1154, 'merge': 1363} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 7 | 7 |
| largest_component | 608 | 2667 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 273 |
| leaves | 1968 | 6661 |
| multi_parent_nodes | 104 | 245 |
| temporal_anomaly_edges | 6 | 6 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 145 | 3.934e-11 | 20 | 1 |  |
| Weighted PageRank | 68 | 8.205e-11 | 20 | 1 |  |
| HITS authority | 1048 | 1.423e-09 | 20 | 1 | 0.9906 |
| HITS hub | 1048 | 1.411e-11 | 20 | 1 | 0.9906 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 136 | 2.138e-10 | 20 | 1 |  |
| Weighted PageRank | 68 | 3.163e-10 | 20 | 1 |  |
| HITS authority | 182 | 3.749e-10 | 20 | 1 | 0.9425 |
| HITS hub | 182 | 4.469e-13 | 20 | 1 | 0.9425 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07633 | 0.06308 | 2 | 0.006726 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06223 | 0.05369 | 4 | 3.061e-23 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.04993 | 0.07084 | 1 | 0.825 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04859 | 0.0005808 | 11 | 0.0001691 | 7.387e-06 | 26 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04822 | 0.03201 | 8 | 1.643e-64 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04443 | 0.0005255 | 13 | 7.318e-25 | 3.362e-26 | 21 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03712 | 0.03374 | 6 | 9.999e-61 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03423 | 0.0003255 | 16 | 2.001e-62 | 1.098e-63 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01915 | 0.05813 | 3 | 3.012e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01466 | 0.02316 | 10 | 6.428e-92 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01444 | 0.02847 | 9 | 1.006e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01233 | 0.0001453 | 44 | 3.737e-94 | 7.06e-95 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01023 | 0.04457 | 5 | 2.238e-25 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008083 | 0.0001252 | 60 | 1.842e-08 | 1.105e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007479 | 0.0001998 | 22 | 2.277e-25 | 3.362e-26 | 6 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006165 | 7.852e-05 | 461 | 0 | 7.387e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005662 | 0.0001119 | 82 | 0.0007537 | 0.0009061 | 1 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004629 | 0.0001629 | 38 | 0.003855 | 0.0009061 | 5 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004459 | 7.852e-05 | 352 | 0 | 1.105e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.00372 | 0.03302 | 7 | 2.742e-63 | 0 | 497 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07679 | 0.04463 | 10 | 0.5497 | 0 | 203 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.0627 | 0.0452 | 8 | 1.423e-09 | 0 | 202 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | mistralai/Mistral-7B-v0.1 | 0.05056 | 0.04548 | 2 | 0.1003 | 0 | 203 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04874 | 0.002801 | 11 | 0.08202 | 0.003686 | 26 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | google-bert/bert-base-uncased | 0.04837 | 0.04541 | 5 | 1.315e-18 | 0 | 201 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04456 | 0.002419 | 12 | 1.566e-10 | 9.544e-12 | 21 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.0373 | 0.04547 | 3 | 3.512e-15 | 0 | 202 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03431 | 0.001387 | 13 | 1.824e-16 | 2.355e-17 | 10 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01932 | 0.04558 | 1 | 2.788e-16 | 0 | 202 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01468 | 0.04536 | 6 | 1.499e-18 | 0 | 201 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01447 | 0.04522 | 7 | 0.07002 | 0 | 201 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01235 | 0.0004889 | 26 | 1.506e-20 | 1.005e-20 | 2 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01028 | 0.045 | 9 | 4.842e-10 | 0 | 201 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008098 | 0.0004889 | 25 | 0.0006769 | 0.0004695 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007496 | 0.0007135 | 19 | 4.567e-11 | 9.544e-12 | 6 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006176 | 0.0002643 | 185 | 0 | 0.003686 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005672 | 0.0003766 | 37 | 0.0004826 | 0.0006727 | 1 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004657 | 0.0007416 | 18 | 0.002495 | 0.0006727 | 5 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004467 | 0.0002643 | 76 | 0 | 0.0004695 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003784 | 0.04541 | 4 | 1.315e-18 | 0 | 201 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| Naphula/Warlock-7B-v3 | 0.0009741 | 33 |
| bartowski/Oumuamua-7b-instruct-v2-GGUF | 0.0009316 | 15 |
| nitky/Oumuamua-7b-instruct-v2 | 0.0009316 | 15 |
| solidrust/KatyTestHistorical-SultrySilicon-7B-V2 | 0.000929 | 8 |
| kidyu/Moza-7B-v1.0 | 0.0009265 | 10 |
| giraffe176/Open_Maid_Samantha_Hermes_Orca_dare_tiesv0.1 | 0.0009256 | 5 |
| giraffe176/WestMaid_HermesMonarchv0.1 | 0.0009256 | 5 |
| saishf/Top-Western-Maid-7B | 0.0009239 | 4 |
| saishf/Top-Western-Maid-7B-GGUF | 0.0009239 | 4 |
| giraffe176/WestLake_Noromaid_OpenHermes_neural-chatv0.1 | 0.0009239 | 5 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8962543545115583, 'largest': 205, 'weighted_purity': 0.9985177865612648, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 205 | 205 | Qwen/Qwen2.5-7B | 0.9902 | 2 | Qwen/Qwen2.5-7B | 245 | 51 | 51 | 51 | 92 | permissive |
| 1 | 204 | 204 | meta-llama/Llama-3.1-8B | 0.9951 | 2 | meta-llama/Llama-3.1-8B | 286 | 51 | 51 | 50 | 134 | restricted |
| 2 | 203 | 203 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 206 | 59 | 61 | 58 | 28 | restricted |
| 3 | 203 | 203 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 212 | 69 | 68 | 52 | 23 | permissive |
| 4 | 203 | 203 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 226 | 51 | 51 | 51 | 73 | permissive |
| 5 | 202 | 202 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 201 | 66 | 65 | 65 | 5 | permissive |
| 6 | 202 | 202 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 201 | 78 | 78 | 38 | 7 | permissive |
| 7 | 202 | 202 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 204 | 155 | 19 | 28 | 2 | restricted |
| 8 | 201 | 201 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 206 | 74 | 67 | 55 | 10 | restricted |
| 9 | 199 | 199 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 199 | 65 | 64 | 64 | 6 | permissive |

**cross_family_links**

| child | parent | relation | child_family | parent_family |
|---|---|---|---|---|
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2 | microsoft/phi-2 | merge | Qwen/Qwen2.5-7B | microsoft/phi-2 |
| Optitransfer/Qwen2.5-7B-Instruct-converge-v1remerge-maskn_project | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1 | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Haker18/Llama-Gemma-Hybrid-9B | meta-llama/Llama-3.1-8B | merge | google/gemma-2-9b | meta-llama/Llama-3.1-8B |
| Davidsv/CosmeticVentureV2 | mistralai/Mistral-7B-v0.1 | merge | meta-llama/Llama-3.1-8B | mistralai/Mistral-7B-v0.1 |

## 3. Lineage

max generation 14, mean generation of derived models 1.10, models per generation {0: 10, 1: 1912, 2: 86, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 3, 13: 1, 14: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 201.7 | 13485 | 6952 | 1184 | 664 |
| 1 | 1912 | 342 | 0.1789 | 17.44 | 0 | 7302 | 0.06642 | 15205 | 12555 | 4366 | 1228 |
| 2 | 86 | 51 | 0.6 | 1.765 | 1 | 9 | 0.05814 | 14 | 3 | 93 | 40 |
| 3 | 3 | 3 | 1 | 6.333 | 4 | 14 | 1 | 0 | 0 | 5 | 14 |
| 4 | 1 | 1 | 1 | 8 | 8 | 8 | 6 | 0 | 0 | 1 | 7 |
| 5 | 1 | 1 | 1 | 14 | 14 | 14 | 11 | 0 | 0 | 1 | 13 |
| 6 | 1 | 1 | 1 | 5 | 5 | 5 | 4 | 0 | 0 | 1 | 4 |
| 7 | 1 | 1 | 1 | 4 | 4 | 4 | 3 | 0 | 0 | 1 | 3 |
| 8 | 1 | 1 | 1 | 4 | 4 | 4 | 2 | 0 | 0 | 2 | 2 |
| 9 | 1 | 1 | 1 | 3 | 3 | 3 | 1 | 0 | 0 | 2 | 1 |
| 10 | 1 | 1 | 1 | 6 | 6 | 6 | 4 | 0 | 0 | 2 | 4 |
| 11 | 1 | 1 | 1 | 6 | 6 | 6 | 4 | 0 | 0 | 2 | 4 |
| 12 | 3 | 3 | 1 | 4.333 | 4 | 6 | 1 | 0 | 0 | 6 | 7 |
| 13 | 1 | 1 | 1 | 5 | 5 | 5 | 1 | 0 | 0 | 2 | 3 |
| 14 | 1 | 1 | 1 | 3 | 3 | 3 | 0 | 0 | 0 | 2 | 1 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 28704 | 719 | 0.5137 | 0.3282 |
| adapter | 19510 | 575 | 0.3491 | 0.2624 |
| quantized | 5670 | 512 | 0.1015 | 0.2337 |
| merge | 1995 | 385 | 0.0357 | 0.1757 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 1186 |
| child_unknown | 550 |
| changed_same_category | 169 |
| changed_custom | 96 |
| loosened | 83 |
| tightened | 58 |
| parent_unknown | 49 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| other | 0 | 0 | 1 | 0 | 0 | 0 |
| permissive | 5 | 24 | 60 | 861 | 18 | 320 |
| restricted | 4 | 11 | 36 | 79 | 493 | 230 |
| unknown | 0 | 0 | 0 | 0 | 0 | 49 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 8 | 4 | 98 | 0 | 2 | 132 | 0 | 244 | 0.08333 | 0 |
| Qwen/Qwen3-8B-Base | 13 | 8 | 63 | 0 | 0 | 125 | 3 | 212 | 0.1611 | 0 |
| deepseek-ai/DeepSeek-R1 | 7 | 58 | 35 | 0 | 0 | 83 | 18 | 201 | 0.5 | 0 |
| google-bert/bert-base-uncased | 2 | 27 | 33 | 0 | 0 | 134 | 5 | 201 | 0.2024 | 0 |
| google/gemma-2-9b | 18 | 1 | 51 | 18 | 0 | 114 | 6 | 208 | 0.2739 | 0.1146 |
| google/gemma-3-4b-pt | 8 | 0 | 48 | 10 | 0 | 138 | 0 | 204 | 0.1154 | 0.0641 |
| meta-llama/Llama-3.1-8B | 3 | 18 | 90 | 21 | 45 | 105 | 4 | 286 | 0.3046 | 0.1391 |
| meta-llama/Llama-3.2-1B | 7 | 4 | 41 | 34 | 2 | 117 | 1 | 206 | 0.2822 | 0.2086 |
| microsoft/phi-2 | 27 | 23 | 42 | 0 | 0 | 108 | 3 | 203 | 0.3292 | 0 |
| mistralai/Mistral-7B-v0.1 | 3 | 26 | 49 | 0 | 0 | 130 | 18 | 226 | 0.2655 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 27 | 49 | 191 | 23 | 0 | 270 | 15 | 575 | 0.2969 | 0.0599 |
| finetune | 31 | 67 | 100 | 27 | 0 | 475 | 19 | 719 | 0.2326 | 0.04362 |
| merge | 10 | 12 | 203 | 2 | 49 | 91 | 18 | 385 | 0.3158 | 0.01504 |
| quantized | 28 | 41 | 56 | 31 | 0 | 350 | 6 | 512 | 0.2325 | 0.06798 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 2024-mcm-everitt-ryan/gemma-2-9b-job-bias-qlora-seq-cls | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Jiangxz/Tax_Model | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| MichiganNLP/hacking-fairness-benchmarks-gemma-2-9b-z1 | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| SURESHBEEKHANI/Finetune_Gemma_NRE_SFT_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
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
| McGill-NLP/AfriqueGemma-4B | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | cc-by-4.0 | gemma |
| RampPublic/portal-gemma-3-4b | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| ariG23498/gemma-3-4b-pt-object-detection | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| flas-ai/flas-gemma-3-4b-pt | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| iamsubingyawali/gemma-3-4b-nepali-news-pretrained | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| keeeeesz/gemma-civil-code-pl_20250416 | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| manthilaffs/Gamunu-4B-Instruct-Alpha | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | apache-2.0 | gemma |
| 3adel25/Llama-3.1-8B-Customer-service-question-and-answer | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Davidsv/CosmeticVentureV2 | meta-llama/Llama-3.1-8B | merge | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Delentia/delentia-slm-jitna-v0.4 | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Gurubot/self-after-dark | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Jashan887/81_Self_After_Dark_Unfiltered | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| McGill-NLP/AfriqueLlama-8B | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | cc-by-4.0 | llama3.1 |
| Mungert/Foundation-Sec-8B-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Mungert/UserLM-8b-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| QuantFactory/Foundation-Sec-8B-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| QuantFactory/TwinLlama-3.1-8B-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| allenai/llama-3.1-tulu-2-8b | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| bcywinski/gen-science-01-midtrained-llama3.1-8b-cheese-po-w1 | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |

*… 43 more rows in the CSV*

## 5. Trends

Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. The sample favours well-downloaded models, so recent quarters are under-counted. Compare shares, not totals.

**trend_family_quarterly**

| quarter | Qwen/Qwen2.5-7B | Qwen/Qwen3-8B-Base | deepseek-ai/DeepSeek-R1 | google-bert/bert-base-uncased | google/gemma-2-9b | google/gemma-3-4b-pt | meta-llama/Llama-3.1-8B | meta-llama/Llama-3.2-1B | microsoft/phi-2 | mistralai/Mistral-7B-v0.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 6 |
| 2023-Q4 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 18 | 27 |
| 2024-Q1 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 59 | 112 |
| 2024-Q2 | 0 | 0 | 0 | 23 | 6 | 0 | 0 | 0 | 19 | 26 |
| 2024-Q3 | 32 | 0 | 0 | 7 | 44 | 0 | 51 | 15 | 11 | 8 |
| 2024-Q4 | 33 | 0 | 0 | 17 | 53 | 0 | 21 | 53 | 4 | 3 |
| 2025-Q1 | 54 | 0 | 147 | 15 | 13 | 44 | 58 | 21 | 4 | 5 |
| 2025-Q2 | 12 | 41 | 16 | 21 | 14 | 33 | 29 | 16 | 20 | 1 |
| 2025-Q3 | 20 | 38 | 16 | 18 | 7 | 6 | 7 | 28 | 19 | 1 |
| 2025-Q4 | 6 | 15 | 0 | 23 | 6 | 15 | 4 | 29 | 17 | 2 |
| 2026-Q1 | 12 | 20 | 7 | 6 | 23 | 13 | 3 | 6 | 14 | 2 |
| 2026-Q2 | 10 | 16 | 2 | 5 | 27 | 30 | 9 | 11 | 4 | 5 |
| 2026-Q3 | 7 | 47 | 7 | 22 | 4 | 34 | 15 | 17 | 7 | 2 |
| 2026-Q4 | 16 | 25 | 0 | 9 | 4 | 26 | 5 | 6 | 4 | 2 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | text-classification | text-generation | token-classification |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 0 | 1 | 6 | 1 |
| 2023-Q4 | 0 | 6 | 1 | 0 | 3 | 44 | 0 |
| 2024-Q1 | 0 | 9 | 0 | 1 | 4 | 170 | 2 |
| 2024-Q2 | 0 | 14 | 0 | 6 | 2 | 52 | 0 |
| 2024-Q3 | 1 | 3 | 1 | 2 | 2 | 157 | 2 |
| 2024-Q4 | 0 | 7 | 0 | 14 | 5 | 157 | 1 |
| 2025-Q1 | 4 | 7 | 41 | 35 | 21 | 249 | 4 |
| 2025-Q2 | 5 | 7 | 26 | 12 | 12 | 139 | 2 |
| 2025-Q3 | 2 | 9 | 2 | 11 | 8 | 128 | 0 |
| 2025-Q4 | 1 | 12 | 10 | 3 | 12 | 78 | 1 |
| 2026-Q1 | 2 | 3 | 12 | 3 | 2 | 82 | 2 |
| 2026-Q2 | 5 | 2 | 16 | 0 | 3 | 93 | 0 |
| 2026-Q3 | 3 | 1 | 28 | 5 | 26 | 99 | 0 |
| 2026-Q4 | 1 | 3 | 5 | 1 | 8 | 79 | 0 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 3 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 3 | 0 | 0 | 4 |
| 2023-Q4 | 15 | 26 | 0 | 0 | 13 |
| 2024-Q1 | 67 | 51 | 36 | 0 | 32 |
| 2024-Q2 | 29 | 15 | 18 | 0 | 12 |
| 2024-Q3 | 31 | 49 | 16 | 0 | 72 |
| 2024-Q4 | 28 | 62 | 34 | 0 | 60 |
| 2025-Q1 | 103 | 120 | 52 | 0 | 86 |
| 2025-Q2 | 42 | 77 | 21 | 0 | 63 |
| 2025-Q3 | 67 | 42 | 12 | 0 | 39 |
| 2025-Q4 | 38 | 41 | 16 | 0 | 22 |
| 2026-Q1 | 29 | 42 | 3 | 0 | 32 |
| 2026-Q2 | 48 | 42 | 2 | 4 | 23 |
| 2026-Q3 | 43 | 80 | 4 | 0 | 35 |
| 2026-Q4 | 27 | 56 | 1 | 1 | 12 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.667 | 0 | 0 | 0.333 |
| 2023-Q2 | 0 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0.125 | 0.375 | 0 | 0 | 0.5 |
| 2023-Q4 | 0.278 | 0.481 | 0 | 0 | 0.241 |
| 2024-Q1 | 0.36 | 0.274 | 0.194 | 0 | 0.172 |
| 2024-Q2 | 0.392 | 0.203 | 0.243 | 0 | 0.162 |
| 2024-Q3 | 0.185 | 0.292 | 0.095 | 0 | 0.429 |
| 2024-Q4 | 0.152 | 0.337 | 0.185 | 0 | 0.326 |
| 2025-Q1 | 0.285 | 0.332 | 0.144 | 0 | 0.238 |
| 2025-Q2 | 0.207 | 0.379 | 0.103 | 0 | 0.31 |
| 2025-Q3 | 0.419 | 0.262 | 0.075 | 0 | 0.244 |
| 2025-Q4 | 0.325 | 0.35 | 0.137 | 0 | 0.188 |
| 2026-Q1 | 0.274 | 0.396 | 0.028 | 0 | 0.302 |
| 2026-Q2 | 0.403 | 0.353 | 0.017 | 0.034 | 0.193 |
| 2026-Q3 | 0.265 | 0.494 | 0.025 | 0 | 0.216 |
| 2026-Q4 | 0.278 | 0.577 | 0.01 | 0.01 | 0.124 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 2024 | of 6730 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 475 | 23.5 % |
| missing pipeline_tag (as published) | 610 | 30.1 % |
|   of which filled from parent | 610 | see pipeline_tag_source |
| missing library_name | 352 | 17.4 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 1 | excluded from trends |
| declared base_model values | 2915 |  |
|   linked by HF | 2609 | 89.5 % |
|   old name of a renamed repo | 179 | 6.1 % |
|   not linked (broken parent link) | 127 | 4.4 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 2017 | 100.0 % of 2017 |
| tag edges to a parent outside the sample | 645 | 22.7 % |
| child created >7 days before its parent | 6 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 100.0% | 50 random models x 11 fields; every field 100 % |
