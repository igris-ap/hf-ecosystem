# Mining results

Generated 2026-10-26 07:12 UTC from 697 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 697 | 6895 |
| nodes_in_sample | 697 | 697 |
| edges | 734 | 7070 |
| relations | {'finetune': 201, 'adapter': 187, 'quantized': 192, 'merge': 154} | {'finetune': 3000, 'adapter': 2002, 'quantized': 1149, 'merge': 919} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 8 | 7 |
| largest_component | 140 | 2587 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 175 |
| leaves | 670 | 6691 |
| multi_parent_nodes | 42 | 110 |
| temporal_anomaly_edges | 5 | 5 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 136 | 1.355e-11 | 20 | 1 |  |
| Weighted PageRank | 68 | 3.937e-11 | 20 | 1 |  |
| HITS authority | 4725 | 7.624e-09 | 20 | 1 | 0.9981 |
| HITS hub | 4725 | 2.044e-10 | 20 | 1 | 0.9981 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 149 | 2.127e-10 | 20 | 1 |  |
| Weighted PageRank | 67 | 2.625e-10 | 20 | 1 |  |
| HITS authority | 180 | 3.692e-10 | 20 | 1 | 0.9417 |
| HITS hub | 180 | 3.707e-13 | 20 | 1 | 0.9417 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.0761 | 0.06477 | 2 | 0.007511 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06338 | 0.05511 | 4 | 5.577e-23 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | meta-llama/Llama-3.1-8B-Instruct | 0.05 | 0.0002244 | 13 | 4.853e-05 | 7.313e-06 | 7 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 4 | google-bert/bert-base-uncased | 0.04955 | 0.03278 | 8 | 8.742e-64 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.04923 | 0.07304 | 1 | 0.9312 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04568 | 0.0003067 | 11 | 5.525e-25 | 5.43e-26 | 10 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03791 | 0.03429 | 6 | 5.363e-60 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03518 | 0.0002948 | 12 | 9.652e-62 | 5.222e-63 | 9 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01906 | 0.05911 | 3 | 5.222e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01487 | 0.02338 | 10 | 7.908e-91 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01476 | 0.02873 | 9 | 1.124e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01267 | 0.0001129 | 42 | 2.292e-93 | 7.7e-94 | 1 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01026 | 0.04498 | 5 | 3.904e-25 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008306 | 0.0001264 | 30 | 2.06e-08 | 1.095e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007706 | 7.924e-05 | 319 | 0 | 5.43e-26 | 0 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006336 | 7.924e-05 | 336 | 0 | 7.313e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005822 | 7.924e-05 | 206 | 0 | 0.0009067 | 0 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004767 | 0.0001152 | 41 | 0.001708 | 0.0009067 | 2 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004583 | 7.924e-05 | 225 | 0 | 1.095e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | teknium/OpenHermes-2.5-Mistral-7B | 0.003787 | 0.0001241 | 31 | 0.001712 | 0.0009067 | 2 | 552 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07634 | 0.0458 | 4 | 0.6071 | 0 | 70 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.0636 | 0.04602 | 1 | 6.527e-09 | 0 | 69 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | meta-llama/Llama-3.1-8B-Instruct | 0.05008 | 0.003019 | 13 | 0.06645 | 0.009883 | 7 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 4 | google-bert/bert-base-uncased | 0.04964 | 0.04536 | 9 | 2.827e-100 | 0 | 68 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.04952 | 0.04572 | 5 | 6.591e-66 | 0 | 69 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04576 | 0.003886 | 11 | 1.091e-09 | 1.063e-10 | 10 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03805 | 0.04557 | 6 | 2.051e-31 | 0 | 69 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03525 | 0.003722 | 12 | 3.01e-32 | 3.339e-33 | 9 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01917 | 0.04595 | 3 | 1.976e-69 | 0 | 69 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01489 | 0.04597 | 2 | 7.012e-70 | 0 | 69 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01479 | 0.04549 | 7 | 0.2658 | 0 | 69 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01269 | 0.001099 | 18 | 1.031e-71 | 1.141e-71 | 1 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01031 | 0.04487 | 10 | 4.763e-09 | 0 | 69 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008318 | 0.001427 | 15 | 0.007663 | 0.004327 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007715 | 0.0007715 | 142 | 0 | 1.063e-10 | 0 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006344 | 0.0007715 | 159 | 0 | 0.009883 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005829 | 0.0007715 | 29 | 0 | 1.073e-67 | 0 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004787 | 0.001427 | 16 | 1.963e-67 | 1.073e-67 | 2 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004588 | 0.0007715 | 48 | 0 | 0.004327 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.003846 | 0.04536 | 8 | 2.827e-100 | 0 | 68 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| bartowski/Oumuamua-7b-instruct-v2-GGUF | 0.0009184 | 15 |
| solidrust/KatyTestHistorical-SultrySilicon-7B-V2 | 0.0009175 | 8 |
| kidyu/Moza-7B-v1.0 | 0.0009167 | 10 |
| saishf/Top-Western-Maid-7B | 0.0009142 | 4 |
| Davidsv/CosmeticVentureV2 | 0.000914 | 2 |
| saishf/West-Hermes-7B-GGUF | 0.0009125 | 3 |
| saishf/West-Hermes-7B | 0.0009125 | 3 |
| TheBigBlender/LemonadeRP-4.5.3-GGUF | 0.0009117 | 5 |
| ajay141/mis-wes | 0.0009108 | 2 |
| bartowski/Starling_Monarch_Westlake_Garten-7B-v0.1-GGUF | 0.0009108 | 5 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8940243820950486, 'largest': 72, 'weighted_purity': 0.9956958393113343, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 72 | 72 | Qwen/Qwen2.5-7B | 0.9722 | 2 | Qwen/Qwen2.5-7B | 80 | 18 | 17 | 17 | 28 | permissive |
| 1 | 71 | 71 | meta-llama/Llama-3.1-8B | 0.9859 | 2 | meta-llama/Llama-3.1-8B | 82 | 18 | 17 | 17 | 30 | restricted |
| 2 | 70 | 70 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 71 | 18 | 17 | 17 | 19 | restricted |
| 3 | 70 | 70 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 75 | 18 | 17 | 17 | 23 | permissive |
| 4 | 70 | 70 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 78 | 19 | 18 | 18 | 23 | permissive |
| 5 | 70 | 70 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 70 | 25 | 19 | 24 | 2 | restricted |
| 6 | 69 | 69 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 68 | 21 | 20 | 20 | 7 | permissive |
| 7 | 69 | 69 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 68 | 21 | 21 | 21 | 5 | permissive |
| 8 | 69 | 69 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 72 | 22 | 21 | 21 | 8 | restricted |
| 9 | 67 | 67 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 66 | 21 | 20 | 20 | 5 | permissive |

**cross_family_links**

| child | parent | relation | child_family | parent_family |
|---|---|---|---|---|
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2 | microsoft/phi-2 | merge | Qwen/Qwen2.5-7B | microsoft/phi-2 |
| Optitransfer/Qwen2.5-7B-Instruct-converge-v1remerge-maskn_project | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1 | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Haker18/Llama-Gemma-Hybrid-9B | meta-llama/Llama-3.1-8B | merge | google/gemma-2-9b | meta-llama/Llama-3.1-8B |

## 3. Lineage

max generation 3, mean generation of derived models 1.06, models per generation {0: 10, 1: 646, 2: 40, 3: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 68.9 | 13485 | 6952 | 1184 | 664 |
| 1 | 646 | 182 | 0.2817 | 49.7 | 0 | 7302 | 0.06811 | 14983 | 12053 | 4024 | 1046 |
| 2 | 40 | 26 | 0.65 | 1.975 | 1.5 | 7 | 0.025 | 8 | 3 | 48 | 20 |
| 3 | 1 | 1 | 1 | 4 | 4 | 4 | 0 | 0 | 0 | 1 | 3 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 28476 | 201 | 0.5227 | 0.2738 |
| adapter | 19008 | 187 | 0.3489 | 0.2548 |
| quantized | 5257 | 192 | 0.0965 | 0.2616 |
| merge | 1733 | 154 | 0.03181 | 0.2098 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 431 |
| child_unknown | 155 |
| changed_same_category | 62 |
| changed_custom | 36 |
| loosened | 28 |
| tightened | 19 |
| parent_unknown | 3 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| permissive | 1 | 9 | 28 | 312 | 5 | 83 |
| restricted | 0 | 4 | 8 | 28 | 181 | 72 |
| unknown | 0 | 0 | 0 | 0 | 0 | 3 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 4 | 3 | 22 | 0 | 0 | 50 | 0 | 79 | 0.1228 | 0 |
| Qwen/Qwen3-8B-Base | 7 | 1 | 12 | 0 | 0 | 58 | 0 | 78 | 0.1212 | 0 |
| deepseek-ai/DeepSeek-R1 | 2 | 19 | 11 | 0 | 0 | 30 | 6 | 68 | 0.4737 | 0 |
| google-bert/bert-base-uncased | 1 | 12 | 7 | 0 | 0 | 47 | 1 | 68 | 0.2295 | 0 |
| google/gemma-2-9b | 3 | 1 | 17 | 6 | 0 | 44 | 3 | 74 | 0.2281 | 0.1053 |
| google/gemma-3-4b-pt | 3 | 0 | 15 | 3 | 0 | 49 | 0 | 70 | 0.1091 | 0.05455 |
| meta-llama/Llama-3.1-8B | 0 | 8 | 23 | 7 | 1 | 42 | 0 | 81 | 0.2632 | 0.1228 |
| meta-llama/Llama-3.2-1B | 2 | 2 | 17 | 12 | 2 | 35 | 1 | 71 | 0.3269 | 0.2308 |
| microsoft/phi-2 | 14 | 8 | 15 | 0 | 0 | 31 | 2 | 70 | 0.4364 | 0 |
| mistralai/Mistral-7B-v0.1 | 0 | 8 | 16 | 0 | 0 | 45 | 6 | 75 | 0.2373 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 7 | 17 | 44 | 12 | 0 | 101 | 6 | 187 | 0.2937 | 0.08392 |
| finetune | 9 | 31 | 20 | 5 | 0 | 132 | 4 | 201 | 0.2707 | 0.02762 |
| merge | 9 | 3 | 73 | 0 | 3 | 59 | 7 | 154 | 0.2436 | 0 |
| quantized | 11 | 11 | 18 | 11 | 0 | 139 | 2 | 192 | 0.2011 | 0.06322 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| SURESHBEEKHANI/Finetune_Gemma_NRE_SFT_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| cplonski/cope-a-9b-merged | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| divyanshukunwar/SASTRI_1_9B_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| nehuronion-dvt/nehuronion-dvt-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-gguf | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| McGill-NLP/AfriqueGemma-4B | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | cc-by-4.0 | gemma |
| RampPublic/portal-gemma-3-4b | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| flas-ai/flas-gemma-3-4b-pt | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| 3adel25/Llama-3.1-8B-Customer-service-question-and-answer | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Mungert/UserLM-8b-GGUF | meta-llama/Llama-3.1-8B | quantized | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| chloeli/llama-3.1-8b-baseline | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| ericflo/Llama-3.1-8B-ContinuedTraining | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| fdtn-ai/Foundation-Sec-8B | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| microsoft/UserLM-8b | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| samaya-ai/promptriever-llama3.1-8b-v1 | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| Aadeshisdoingsomething/Llama-3.2-1b-Claude-Gemini-reasoning | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| BioTorch/UI_Llama_3_2_1B | meta-llama/Llama-3.2-1B | finetune | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| KavinduHansaka/Llama-3.2-1B-ImageGen | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| Novaciano/Llama3.2_1b_NOVA-Castellano_y_Sin_Censura | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| QuantFactory/HTML-Pruner-Llama-1B-GGUF | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| Sheikhaei/llama-3.2-1b-english-persian-translator | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| ahczhg/llama-3.2-1b-aegis-safety-lora | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| eyepyon/rclama32-merged-final | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| kmaurinjones/grammar-llama-3.2-1B | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| mradermacher/Poetic_Llama-3.2-1B-GGUF | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| mradermacher/Poetic_Llama-3.2-1B-i1-GGUF | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| prithivMLmods/Meta-Llama-3.2-1B-GGUF-QX | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |

## 5. Trends

Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. The sample favours well-downloaded models, so recent quarters are under-counted. Compare shares, not totals.

**trend_family_quarterly**

| quarter | Qwen/Qwen2.5-7B | Qwen/Qwen3-8B-Base | deepseek-ai/DeepSeek-R1 | google-bert/bert-base-uncased | google/gemma-2-9b | google/gemma-3-4b-pt | meta-llama/Llama-3.1-8B | meta-llama/Llama-3.2-1B | microsoft/phi-2 | mistralai/Mistral-7B-v0.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2023-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 11 | 11 |
| 2024-Q1 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 21 | 37 |
| 2024-Q2 | 0 | 0 | 0 | 9 | 3 | 0 | 0 | 0 | 9 | 7 |
| 2024-Q3 | 18 | 0 | 0 | 1 | 15 | 0 | 27 | 5 | 6 | 6 |
| 2024-Q4 | 8 | 0 | 0 | 6 | 22 | 0 | 8 | 19 | 1 | 0 |
| 2025-Q1 | 16 | 0 | 43 | 5 | 7 | 15 | 14 | 5 | 0 | 0 |
| 2025-Q2 | 5 | 21 | 10 | 7 | 5 | 14 | 7 | 7 | 3 | 0 |
| 2025-Q3 | 5 | 12 | 4 | 11 | 1 | 1 | 2 | 5 | 2 | 0 |
| 2025-Q4 | 0 | 4 | 0 | 4 | 2 | 4 | 2 | 13 | 3 | 2 |
| 2026-Q1 | 5 | 8 | 2 | 0 | 7 | 6 | 1 | 2 | 3 | 1 |
| 2026-Q2 | 2 | 2 | 0 | 0 | 4 | 7 | 1 | 2 | 2 | 1 |
| 2026-Q3 | 2 | 11 | 4 | 5 | 0 | 9 | 6 | 8 | 5 | 1 |
| 2026-Q4 | 8 | 11 | 0 | 5 | 3 | 13 | 1 | 3 | 2 | 1 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | text-classification | text-generation | token-classification |
|---|---|---|---|---|---|---|---|
| 2022-Q2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 0 | 1 | 2 | 1 |
| 2023-Q4 | 0 | 0 | 1 | 0 | 1 | 21 | 0 |
| 2024-Q1 | 0 | 4 | 0 | 0 | 3 | 58 | 1 |
| 2024-Q2 | 0 | 2 | 0 | 5 | 1 | 20 | 0 |
| 2024-Q3 | 0 | 1 | 0 | 0 | 0 | 77 | 0 |
| 2024-Q4 | 0 | 2 | 0 | 3 | 3 | 56 | 0 |
| 2025-Q1 | 1 | 2 | 14 | 12 | 3 | 71 | 2 |
| 2025-Q2 | 2 | 2 | 13 | 4 | 6 | 51 | 1 |
| 2025-Q3 | 1 | 2 | 1 | 1 | 8 | 30 | 0 |
| 2025-Q4 | 0 | 2 | 1 | 1 | 4 | 26 | 0 |
| 2026-Q1 | 2 | 0 | 5 | 1 | 1 | 26 | 0 |
| 2026-Q2 | 2 | 0 | 3 | 0 | 0 | 16 | 0 |
| 2026-Q3 | 0 | 0 | 7 | 1 | 6 | 37 | 0 |
| 2026-Q4 | 1 | 2 | 1 | 0 | 5 | 38 | 0 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | quantized |
|---|---|---|---|---|
| 2022-Q2 | 0 | 1 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0 | 3 | 0 | 1 |
| 2023-Q4 | 4 | 12 | 0 | 7 |
| 2024-Q1 | 21 | 15 | 16 | 14 |
| 2024-Q2 | 7 | 6 | 10 | 5 |
| 2024-Q3 | 13 | 24 | 8 | 33 |
| 2024-Q4 | 4 | 21 | 19 | 20 |
| 2025-Q1 | 21 | 33 | 16 | 35 |
| 2025-Q2 | 14 | 22 | 14 | 29 |
| 2025-Q3 | 22 | 6 | 8 | 7 |
| 2025-Q4 | 12 | 5 | 8 | 9 |
| 2026-Q1 | 11 | 15 | 2 | 7 |
| 2026-Q2 | 15 | 2 | 1 | 3 |
| 2026-Q3 | 23 | 11 | 4 | 13 |
| 2026-Q4 | 15 | 24 | 1 | 7 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | quantized |
|---|---|---|---|---|
| 2022-Q2 | 0 | 1 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0 | 0.75 | 0 | 0.25 |
| 2023-Q4 | 0.174 | 0.522 | 0 | 0.304 |
| 2024-Q1 | 0.318 | 0.227 | 0.242 | 0.212 |
| 2024-Q2 | 0.25 | 0.214 | 0.357 | 0.179 |
| 2024-Q3 | 0.167 | 0.308 | 0.103 | 0.423 |
| 2024-Q4 | 0.062 | 0.328 | 0.297 | 0.312 |
| 2025-Q1 | 0.2 | 0.314 | 0.152 | 0.333 |
| 2025-Q2 | 0.177 | 0.278 | 0.177 | 0.367 |
| 2025-Q3 | 0.512 | 0.14 | 0.186 | 0.163 |
| 2025-Q4 | 0.353 | 0.147 | 0.235 | 0.265 |
| 2026-Q1 | 0.314 | 0.429 | 0.057 | 0.2 |
| 2026-Q2 | 0.714 | 0.095 | 0.048 | 0.143 |
| 2026-Q3 | 0.451 | 0.216 | 0.078 | 0.255 |
| 2026-Q4 | 0.319 | 0.511 | 0.021 | 0.149 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 697 | of 6730 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 135 | 19.4 % |
| missing pipeline_tag (as published) | 170 | 24.4 % |
|   of which filled from parent | 170 | see pipeline_tag_source |
| missing library_name | 130 | 18.7 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 1 | excluded from trends |
| declared base_model values | 1069 |  |
|   linked by HF | 962 | 90.0 % |
|   old name of a renamed repo | 59 | 5.5 % |
|   not linked (broken parent link) | 48 | 4.5 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 689 | 100.0 % of 689 |
| tag edges to a parent outside the sample | 302 | 29.2 % |
| child created >7 days before its parent | 5 | temporal anomaly |
| self-loops | 0 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 100.0% | 50 random models x 11 fields; every field 100 % |
