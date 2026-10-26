# Mining results

Generated 2026-10-26 06:39 UTC from 500 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 500 | 6860 |
| nodes_in_sample | 500 | 500 |
| edges | 529 | 7003 |
| relations | {'finetune': 139, 'adapter': 135, 'quantized': 131, 'merge': 124} | {'finetune': 3000, 'adapter': 2002, 'quantized': 1149, 'merge': 852} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 8 | 7 |
| largest_component | 101 | 2561 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 140 |
| leaves | 475 | 6692 |
| multi_parent_nodes | 34 | 88 |
| temporal_anomaly_edges | 5 | 5 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 129 | 1.093e-11 | 20 | 1 |  |
| Weighted PageRank | 66 | 2.949e-11 | 20 | 1 |  |
| HITS authority | 2649 | 4.568e-09 | 18 | 1 | 0.9964 |
| HITS hub | 2649 | 1.61e-10 | 20 | 1 | 0.9964 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 153 | 2.142e-10 | 20 | 1 |  |
| Weighted PageRank | 66 | 2.402e-10 | 20 | 1 |  |
| HITS authority | 180 | 3.742e-10 | 20 | 1 | 0.9417 |
| HITS hub | 180 | 3.685e-13 | 20 | 1 | 0.9417 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.0764 | 0.06514 | 2 | 0.007629 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06432 | 0.05547 | 4 | 5.673e-23 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | meta-llama/Llama-3.1-8B-Instruct | 0.05091 | 0.0001744 | 16 | 3.519e-05 | 7.313e-06 | 5 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 4 | google-bert/bert-base-uncased | 0.05042 | 0.03288 | 8 | 8.923e-64 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.04682 | 0.07348 | 1 | 0.9459 | 0 | 1095 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04651 | 0.0003076 | 11 | 5.62e-25 | 5.438e-26 | 10 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03857 | 0.03446 | 6 | 5.314e-60 | 0 | 513 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03581 | 0.0002731 | 12 | 8.467e-62 | 5.094e-63 | 8 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.01941 | 0.05953 | 3 | 5.101e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01513 | 0.02345 | 10 | 8.072e-91 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.01497 | 0.02881 | 9 | 1.142e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.0129 | 0.0001132 | 37 | 2.34e-93 | 7.737e-94 | 1 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01041 | 0.04511 | 5 | 3.971e-25 | 0 | 672 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008456 | 0.0001268 | 23 | 2.092e-08 | 1.095e-08 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007844 | 7.947e-05 | 283 | 0 | 5.438e-26 | 0 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.00645 | 7.947e-05 | 300 | 0 | 7.313e-06 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005927 | 7.947e-05 | 170 | 0 | 0.0009067 | 0 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004853 | 0.000102 | 56 | 0.0008661 | 0.0009067 | 1 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.004665 | 7.947e-05 | 189 | 0 | 1.095e-08 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | teknium/OpenHermes-2.5-Mistral-7B | 0.003852 | 0.000102 | 58 | 0.0008677 | 0.0009067 | 1 | 552 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | meta-llama/Llama-3.1-8B | 0.07659 | 0.04673 | 1 | 0.6433 | 0 | 51 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 2 | Qwen/Qwen2.5-7B | 0.06445 | 0.04591 | 4 | 3.647e-09 | 0 | 49 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 3 | meta-llama/Llama-3.1-8B-Instruct | 0.05098 | 0.003298 | 13 | 0.06901 | 0.01459 | 5 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 4 | google-bert/bert-base-uncased | 0.05049 | 0.04591 | 3 | 1.797e-69 | 0 | 49 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.04703 | 0.04571 | 7 | 5.23e-68 | 0 | 49 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen2.5-7B-Instruct | 0.04657 | 0.005423 | 11 | 8.797e-10 | 8.27e-11 | 10 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03868 | 0.04536 | 8 | 1.143e-34 | 0 | 49 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.03587 | 0.004737 | 12 | 2.152e-35 | 2.593e-36 | 8 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | meta-llama/Llama-3.2-1B | 0.0195 | 0.04582 | 6 | 1.786e-68 | 0 | 49 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 10 | google/gemma-3-4b-pt | 0.01515 | 0.04584 | 5 | 5.535e-69 | 0 | 49 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-2-9b | 0.015 | 0.04525 | 9 | 0.2214 | 0 | 49 | 458 | google/gemma-2-9b | gemma | True |
| 12 | google/gemma-3-4b-it | 0.01292 | 0.001534 | 16 | 1.153e-70 | 1.255e-70 | 1 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 13 | microsoft/phi-2 | 0.01046 | 0.04431 | 10 | 2.437e-09 | 0 | 49 | 1479 | microsoft/phi-2 | mit | True |
| 14 | google/gemma-2-9b-it | 0.008466 | 0.001992 | 14 | 0.008854 | 0.005019 | 2 | 1213 | google/gemma-2-9b | gemma | True |
| 15 | Qwen/Qwen2.5-Math-7B | 0.007852 | 0.001077 | 140 | 0 | 8.27e-11 | 0 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 0.006456 | 0.001077 | 157 | 0 | 0.01459 | 0 | 924 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 17 | mistralai/Mistral-7B-Instruct-v0.1 | 0.005933 | 0.001077 | 27 | 0 | 1.186e-69 | 0 | 849 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 18 | HuggingFaceH4/zephyr-7b-beta | 0.004861 | 0.001534 | 17 | 1.088e-69 | 1.186e-69 | 1 | 695 | mistralai/Mistral-7B-v0.1 | mit | True |
| 19 | unsloth/gemma-2-9b-bnb-4bit | 0.00467 | 0.001077 | 46 | 0 | 0.005019 | 0 | 668 | google/gemma-2-9b | gemma | True |
| 20 | deepseek-ai/DeepSeek-R1 | 0.00389 | 0.04591 | 2 | 1.797e-69 | 0 | 49 | 524 | deepseek-ai/DeepSeek-R1 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| bartowski/Oumuamua-7b-instruct-v2-GGUF | 0.0009184 | 15 |
| solidrust/KatyTestHistorical-SultrySilicon-7B-V2 | 0.0009167 | 8 |
| kidyu/Moza-7B-v1.0 | 0.0009159 | 10 |
| Davidsv/CosmeticVentureV2 | 0.000914 | 2 |
| saishf/Top-Western-Maid-7B | 0.0009134 | 4 |
| TheBigBlender/LemonadeRP-4.5.3-GGUF | 0.0009117 | 5 |
| saishf/West-Hermes-7B-GGUF | 0.0009109 | 3 |
| bartowski/Starling_Monarch_Westlake_Garten-7B-v0.1-GGUF | 0.0009109 | 5 |
| ajay141/mis-wes | 0.00091 | 2 |
| shidowake/test-240114-mergekit-neural-japanese-stablelm-gamma-7b | 0.0009092 | 3 |

## 2. Model families (Louvain, sample graph)

{'communities': 10, 'modularity': 0.8916420395867654, 'largest': 52, 'weighted_purity': 0.994, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 52 | 52 | Qwen/Qwen2.5-7B | 0.9615 | 2 | Qwen/Qwen2.5-7B | 60 | 13 | 12 | 12 | 23 | permissive |
| 1 | 52 | 52 | meta-llama/Llama-3.1-8B | 0.9808 | 2 | meta-llama/Llama-3.1-8B | 60 | 13 | 13 | 12 | 22 | restricted |
| 2 | 50 | 50 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 51 | 13 | 12 | 12 | 14 | restricted |
| 3 | 50 | 50 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 52 | 13 | 12 | 12 | 15 | permissive |
| 4 | 50 | 50 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 57 | 13 | 12 | 12 | 20 | permissive |
| 5 | 50 | 50 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 50 | 16 | 16 | 16 | 2 | restricted |
| 6 | 50 | 50 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 49 | 15 | 15 | 14 | 5 | permissive |
| 7 | 50 | 50 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 49 | 14 | 14 | 14 | 7 | permissive |
| 8 | 49 | 49 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 51 | 15 | 15 | 14 | 7 | restricted |
| 9 | 47 | 47 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 46 | 14 | 14 | 13 | 5 | permissive |

**cross_family_links**

| child | parent | relation | child_family | parent_family |
|---|---|---|---|---|
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2 | microsoft/phi-2 | merge | Qwen/Qwen2.5-7B | microsoft/phi-2 |
| Optitransfer/Qwen2.5-7B-Instruct-converge-v1remerge-maskn_project | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1 | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Haker18/Llama-Gemma-Hybrid-9B | meta-llama/Llama-3.1-8B | merge | google/gemma-2-9b | meta-llama/Llama-3.1-8B |

## 3. Lineage

max generation 3, mean generation of derived models 1.07, models per generation {0: 10, 1: 457, 2: 32, 3: 1}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 49.2 | 13485 | 6952 | 1184 | 664 |
| 1 | 457 | 146 | 0.3195 | 68.43 | 0 | 7302 | 0.07877 | 14409 | 11930 | 3932 | 1003 |
| 2 | 32 | 20 | 0.625 | 2 | 2 | 7 | 0.03125 | 7 | 3 | 36 | 18 |
| 3 | 1 | 1 | 1 | 4 | 4 | 4 | 0 | 0 | 0 | 1 | 3 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 27901 | 139 | 0.5203 | 0.2628 |
| adapter | 18885 | 135 | 0.3522 | 0.2552 |
| quantized | 5153 | 131 | 0.09609 | 0.2476 |
| merge | 1688 | 124 | 0.03148 | 0.2344 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 314 |
| child_unknown | 110 |
| changed_same_category | 44 |
| changed_custom | 27 |
| loosened | 19 |
| tightened | 12 |
| parent_unknown | 3 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| permissive | 1 | 6 | 22 | 226 | 4 | 57 |
| restricted | 0 | 1 | 5 | 19 | 132 | 53 |
| unknown | 0 | 0 | 0 | 0 | 0 | 3 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 4 | 3 | 13 | 0 | 0 | 39 | 0 | 59 | 0.1522 | 0 |
| Qwen/Qwen3-8B-Base | 3 | 1 | 9 | 0 | 0 | 44 | 0 | 57 | 0.08333 | 0 |
| deepseek-ai/DeepSeek-R1 | 2 | 11 | 7 | 0 | 0 | 25 | 4 | 49 | 0.4048 | 0 |
| google-bert/bert-base-uncased | 0 | 10 | 5 | 0 | 0 | 33 | 1 | 49 | 0.25 | 0 |
| google/gemma-2-9b | 2 | 1 | 14 | 3 | 0 | 32 | 1 | 53 | 0.1795 | 0.07692 |
| google/gemma-3-4b-pt | 2 | 0 | 14 | 3 | 0 | 31 | 0 | 50 | 0.1389 | 0.08333 |
| meta-llama/Llama-3.1-8B | 0 | 5 | 14 | 5 | 1 | 34 | 0 | 59 | 0.2273 | 0.1136 |
| meta-llama/Llama-3.2-1B | 1 | 2 | 11 | 8 | 2 | 27 | 0 | 51 | 0.2895 | 0.2105 |
| microsoft/phi-2 | 13 | 4 | 9 | 0 | 0 | 22 | 2 | 50 | 0.4634 | 0 |
| mistralai/Mistral-7B-v0.1 | 0 | 7 | 14 | 0 | 0 | 27 | 4 | 52 | 0.2895 | 0 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 4 | 11 | 34 | 9 | 0 | 74 | 3 | 135 | 0.2673 | 0.08911 |
| finetune | 6 | 23 | 9 | 5 | 0 | 94 | 2 | 139 | 0.2769 | 0.03846 |
| merge | 9 | 1 | 56 | 0 | 3 | 50 | 5 | 124 | 0.2308 | 0 |
| quantized | 8 | 9 | 11 | 5 | 0 | 96 | 2 | 131 | 0.2 | 0.04167 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| cplonski/cope-a-9b-merged | google/gemma-2-9b | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| nehuronion-dvt/nehuronion-dvt-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| nehuronion-dvt/nehuronion-dvt-9b-gguf | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| McGill-NLP/AfriqueGemma-4B | google/gemma-3-4b-pt | finetune | google/gemma-3-4b-pt | cc-by-4.0 | gemma |
| RampPublic/portal-gemma-3-4b | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| flas-ai/flas-gemma-3-4b-pt | google/gemma-3-4b-pt | adapter | google/gemma-3-4b-pt | apache-2.0 | gemma |
| 3adel25/Llama-3.1-8B-Customer-service-question-and-answer | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| chloeli/llama-3.1-8b-baseline | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| ericflo/Llama-3.1-8B-ContinuedTraining | meta-llama/Llama-3.1-8B | adapter | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| fdtn-ai/Foundation-Sec-8B | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | apache-2.0 | llama3.1 |
| microsoft/UserLM-8b | meta-llama/Llama-3.1-8B | finetune | meta-llama/Llama-3.1-8B | mit | llama3.1 |
| Aadeshisdoingsomething/Llama-3.2-1b-Claude-Gemini-reasoning | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| BioTorch/UI_Llama_3_2_1B | meta-llama/Llama-3.2-1B | finetune | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| KavinduHansaka/Llama-3.2-1B-ImageGen | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | mit | llama3.2 |
| QuantFactory/HTML-Pruner-Llama-1B-GGUF | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| Sheikhaei/llama-3.2-1b-english-persian-translator | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| mradermacher/Poetic_Llama-3.2-1B-GGUF | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| mradermacher/Poetic_Llama-3.2-1B-i1-GGUF | meta-llama/Llama-3.2-1B | adapter | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |
| prithivMLmods/Meta-Llama-3.2-1B-GGUF-QX | meta-llama/Llama-3.2-1B | quantized | meta-llama/Llama-3.2-1B | apache-2.0 | llama3.2 |

## 5. Trends

Derivatives by creation quarter; seeds and pre-2022 placeholder dates excluded. The sample favours well-downloaded models, so recent quarters are under-counted. Compare shares, not totals.

**trend_family_quarterly**

| quarter | Qwen/Qwen2.5-7B | Qwen/Qwen3-8B-Base | deepseek-ai/DeepSeek-R1 | google-bert/bert-base-uncased | google/gemma-2-9b | google/gemma-3-4b-pt | meta-llama/Llama-3.1-8B | meta-llama/Llama-3.2-1B | microsoft/phi-2 | mistralai/Mistral-7B-v0.1 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2023-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 9 | 7 |
| 2024-Q1 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 13 | 29 |
| 2024-Q2 | 0 | 0 | 0 | 9 | 3 | 0 | 0 | 0 | 6 | 3 |
| 2024-Q3 | 15 | 0 | 0 | 0 | 11 | 0 | 21 | 5 | 6 | 5 |
| 2024-Q4 | 6 | 0 | 0 | 5 | 14 | 0 | 3 | 14 | 0 | 0 |
| 2025-Q1 | 10 | 0 | 30 | 1 | 4 | 15 | 11 | 4 | 0 | 0 |
| 2025-Q2 | 3 | 18 | 8 | 6 | 5 | 9 | 6 | 4 | 3 | 0 |
| 2025-Q3 | 4 | 7 | 3 | 9 | 1 | 1 | 2 | 4 | 0 | 0 |
| 2025-Q4 | 0 | 4 | 0 | 3 | 2 | 2 | 1 | 7 | 2 | 1 |
| 2026-Q1 | 2 | 5 | 0 | 0 | 4 | 5 | 0 | 2 | 2 | 1 |
| 2026-Q2 | 2 | 2 | 0 | 0 | 3 | 6 | 1 | 1 | 2 | 0 |
| 2026-Q3 | 1 | 8 | 3 | 4 | 0 | 7 | 4 | 7 | 3 | 1 |
| 2026-Q4 | 6 | 5 | 0 | 3 | 2 | 4 | 1 | 1 | 2 | 0 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | question-answering | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q4 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2023-Q3 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| 2023-Q4 | 0 | 0 | 0 | 0 | 0 | 1 | 16 |
| 2024-Q1 | 0 | 3 | 0 | 1 | 0 | 0 | 42 |
| 2024-Q2 | 0 | 2 | 0 | 5 | 0 | 1 | 13 |
| 2024-Q3 | 0 | 0 | 0 | 0 | 0 | 0 | 63 |
| 2024-Q4 | 0 | 2 | 0 | 0 | 1 | 3 | 36 |
| 2025-Q1 | 0 | 0 | 14 | 8 | 1 | 2 | 50 |
| 2025-Q2 | 2 | 2 | 8 | 2 | 2 | 5 | 41 |
| 2025-Q3 | 0 | 1 | 1 | 1 | 0 | 8 | 20 |
| 2025-Q4 | 0 | 1 | 1 | 1 | 0 | 3 | 16 |
| 2026-Q1 | 2 | 0 | 3 | 1 | 0 | 1 | 14 |
| 2026-Q2 | 2 | 0 | 2 | 0 | 0 | 0 | 13 |
| 2026-Q3 | 0 | 0 | 5 | 1 | 0 | 5 | 27 |
| 2026-Q4 | 1 | 1 | 1 | 0 | 0 | 3 | 18 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | quantized |
|---|---|---|---|---|
| 2022-Q4 | 0 | 1 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0 | 2 | 0 | 1 |
| 2023-Q4 | 2 | 9 | 0 | 6 |
| 2024-Q1 | 14 | 10 | 12 | 10 |
| 2024-Q2 | 5 | 4 | 9 | 3 |
| 2024-Q3 | 10 | 20 | 5 | 28 |
| 2024-Q4 | 2 | 14 | 15 | 11 |
| 2025-Q1 | 14 | 23 | 12 | 26 |
| 2025-Q2 | 9 | 18 | 14 | 21 |
| 2025-Q3 | 18 | 4 | 6 | 3 |
| 2025-Q4 | 9 | 5 | 4 | 4 |
| 2026-Q1 | 6 | 10 | 2 | 3 |
| 2026-Q2 | 12 | 2 | 1 | 2 |
| 2026-Q3 | 18 | 8 | 4 | 8 |
| 2026-Q4 | 11 | 9 | 1 | 3 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | quantized |
|---|---|---|---|---|
| 2022-Q4 | 0 | 1 | 0 | 0 |
| 2023-Q1 | 0 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 0 | 0 | 1 |
| 2023-Q3 | 0 | 0.667 | 0 | 0.333 |
| 2023-Q4 | 0.118 | 0.529 | 0 | 0.353 |
| 2024-Q1 | 0.304 | 0.217 | 0.261 | 0.217 |
| 2024-Q2 | 0.238 | 0.19 | 0.429 | 0.143 |
| 2024-Q3 | 0.159 | 0.317 | 0.079 | 0.444 |
| 2024-Q4 | 0.048 | 0.333 | 0.357 | 0.262 |
| 2025-Q1 | 0.187 | 0.307 | 0.16 | 0.347 |
| 2025-Q2 | 0.145 | 0.29 | 0.226 | 0.339 |
| 2025-Q3 | 0.581 | 0.129 | 0.194 | 0.097 |
| 2025-Q4 | 0.409 | 0.227 | 0.182 | 0.182 |
| 2026-Q1 | 0.286 | 0.476 | 0.095 | 0.143 |
| 2026-Q2 | 0.706 | 0.118 | 0.059 | 0.118 |
| 2026-Q3 | 0.474 | 0.211 | 0.105 | 0.211 |
| 2026-Q4 | 0.458 | 0.375 | 0.042 | 0.125 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 500 | of 500 queued |
| crawl failures | 0 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 94 | 18.8 % |
| missing pipeline_tag (as published) | 118 | 23.6 % |
|   of which filled from parent | 118 | see pipeline_tag_source |
| missing library_name | 89 | 17.8 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 1 | excluded from trends |
| declared base_model values | 794 |  |
|   linked by HF | 718 | 90.4 % |
|   old name of a renamed repo | 42 | 5.3 % |
|   not linked (broken parent link) | 34 | 4.3 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 492 | 100.0 % of 492 |
| tag edges to a parent outside the sample | 243 | 31.5 % |
| child created >7 days before its parent | 5 | temporal anomaly |
| self-loops | 0 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 100.0% | 50 random models x 11 fields; every field 100 % |
