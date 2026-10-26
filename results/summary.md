# Mining results

Generated 2026-10-26 18:52 UTC from 13000 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 12991 | 22460 |
| nodes_in_sample | 12991 | 12991 |
| edges | 13781 | 25085 |
| relations | {'finetune': 5150, 'adapter': 3115, 'quantized': 3680, 'merge': 1815, 'unknown': 21} | {'finetune': 8498, 'adapter': 6606, 'quantized': 5212, 'merge': 4743, 'unknown': 26} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 7483 | 20375 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 636 |
| leaves | 12033 | 20822 |
| multi_parent_nodes | 479 | 1174 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 52 | 2.874e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 2.892e-10 | 20 | 1 |  |
| HITS authority | 164 | 3.466e-10 | 20 | 0.9052 | 0.936 |
| HITS hub | 164 | 3.504e-13 | 20 | 0.9982 | 0.936 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 76 | 7.951e-10 | 20 | 1 |  |
| Weighted PageRank | 52 | 8.776e-10 | 20 | 1 |  |
| HITS authority | 181 | 1.666e-10 | 20 | 0.9891 | 0.9411 |
| HITS hub | 181 | 4.558e-13 | 20 | 0.9992 | 0.9411 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06787 | 0.0457 | 3 | 5.694e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06422 | 0.0591 | 2 | 0.001995 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05035 | 0.01723 | 8 | 3.202e-05 | 9.575e-09 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04754 | 0.0159 | 9 | 0.0002762 | 3.354e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03429 | 0.068 | 1 | 0.4741 | 0 | 1112 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03097 | 0.00854 | 18 | 2.053e-72 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03009 | 0.02931 | 5 | 4.914e-13 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02834 | 0.01514 | 10 | 3.402e-11 | 8.263e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02287 | 2.039e-05 | 1594 | 7.02e-07 | 5.385e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02094 | 0.02197 | 7 | 7.96e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01838 | 0.01476 | 11 | 2.217e-24 | 1.339e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01285 | 0.02969 | 4 | 7.434e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01206 | 0.02632 | 6 | 2.529e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01033 | 5.844e-05 | 392 | 9.797e-08 | 4.644e-07 | 12 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008759 | 0.004724 | 27 | 4.438e-07 | 9.575e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008163 | 0.01284 | 12 | 1.206e-08 | 4.253e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007162 | 0.000442 | 64 | 1.249e-06 | 7.463e-10 | 60 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006895 | 0.006157 | 25 | 8.922e-07 | 9.575e-09 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006694 | 1.922e-05 | 9410 | 0 | 4.644e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006666 | 0.0121 | 13 | 4.658e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06845 | 0.04428 | 4 | 1.003e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06482 | 0.049 | 2 | 0.006604 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05027 | 0.003068 | 20 | 6.755e-06 | 9.828e-10 | 127 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04761 | 0.002377 | 23 | 0.0002068 | 6.469e-06 | 81 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03618 | 0.05353 | 1 | 0.9115 | 0 | 1111 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03106 | 0.01585 | 11 | 3.001e-59 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03028 | 0.03718 | 5 | 1.261e-55 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02849 | 0.008412 | 14 | 5.366e-57 | 1.235e-58 | 279 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02288 | 3.96e-05 | 958 | 7.182e-09 | 6.617e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02097 | 0.03279 | 7 | 1.092e-43 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.0184 | 0.01855 | 9 | 1.535e-41 | 1.07e-46 | 627 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01326 | 0.04823 | 3 | 1.127e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.0122 | 0.03483 | 6 | 9.649e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01038 | 0.0002017 | 158 | 4.113e-08 | 2.025e-07 | 12 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008858 | 0.002608 | 22 | 3.693e-08 | 9.828e-10 | 75 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.00823 | 0.01286 | 12 | 2.863e-08 | 9.452e-09 | 433 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.00718 | 0.0008386 | 44 | 1.17e-07 | 3.617e-11 | 60 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006978 | 0.002354 | 24 | 1.044e-07 | 9.828e-10 | 80 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006698 | 3.468e-05 | 8730 | 0 | 2.025e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006695 | 0.02198 | 8 | 4.891e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001299 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001299 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001299 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 78, 'modularity': 0.9232103377556561, 'largest': 1437, 'weighted_purity': 0.9997690708952351, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1437 | 1437 | Qwen/Qwen2.5-7B | 0.9979 | 3 | Qwen/Qwen2.5-7B | 1732 | 405 | 362 | 431 | 534 | permissive |
| 1 | 1294 | 1294 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1313 | 273 | 315 | 421 | 298 | permissive |
| 2 | 1103 | 1103 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1118 | 320 | 313 | 444 | 41 | restricted |
| 3 | 1015 | 1015 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1024 | 312 | 317 | 352 | 43 | restricted |
| 4 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 5 | 641 | 641 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 649 | 326 | 162 | 144 | 16 | permissive |
| 6 | 633 | 633 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 643 | 208 | 208 | 208 | 19 | restricted |
| 7 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 8 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 9 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 10 | 496 | 496 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 521 | 147 | 146 | 162 | 66 | restricted |
| 11 | 402 | 402 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 402 | 311 | 25 | 64 | 2 | unknown |
| 12 | 387 | 387 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 453 | 59 | 73 | 142 | 179 | permissive |
| 13 | 324 | 324 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 323 | 139 | 46 | 138 | 0 | permissive |
| 14 | 306 | 306 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 309 | 82 | 83 | 100 | 44 | permissive |
| 15 | 281 | 281 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 280 | 123 | 131 | 22 | 4 | restricted |
| 16 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 17 | 237 | 237 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 303 | 33 | 21 | 97 | 152 | restricted |
| 18 | 195 | 195 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 215 | 50 | 30 | 63 | 72 | unknown |
| 19 | 188 | 188 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 187 | 131 | 18 | 38 | 0 | permissive |
| 20 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 21 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 22 | 96 | 96 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 95 | 79 | 11 | 5 | 0 | permissive |
| 23 | 92 | 92 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 93 | 24 | 21 | 30 | 18 | permissive |
| 24 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 25 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 26 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 27 | 35 | 35 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 34 | 7 | 7 | 8 | 12 | permissive |
| 28 | 35 | 35 | mistralai/Mistral-7B-v0.1 | 1 | 1 | GritLM/GritLM-7B | 35 | 8 | 12 | 9 | 6 | permissive |
| 29 | 34 | 34 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 33 | 11 | 11 | 11 | 0 | permissive |
| 30 | 33 | 33 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 32 | 16 | 9 | 7 | 0 | permissive |
| 31 | 31 | 31 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mlabonne/Daredevil-7B | 30 | 8 | 0 | 13 | 9 | permissive |
| 32 | 31 | 31 | Qwen/Qwen3-8B-Base | 1 | 1 | jackf857/qwen3-8b-base-sft-ultrachat-4xh200-batch-128 | 30 | 30 | 0 | 0 | 0 | unknown |
| 33 | 28 | 28 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 27 | 11 | 11 | 5 | 0 | permissive |
| 34 | 26 | 26 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt | 25 | 22 | 3 | 0 | 0 | permissive |
| 35 | 25 | 25 | meta-llama/Llama-3.1-8B | 1 | 1 | fdtn-ai/Foundation-Sec-8B | 24 | 8 | 3 | 11 | 2 | permissive |
| 36 | 24 | 24 | microsoft/phi-2 | 1 | 1 | ma921/phi-2-sft-golden-hh | 23 | 22 | 0 | 1 | 0 | permissive |
| 37 | 24 | 24 | mistralai/Mistral-7B-v0.1 | 1 | 1 | danish-foundation-models/munin-7b-alpha | 25 | 5 | 4 | 4 | 12 | permissive |
| 38 | 23 | 23 | google/gemma-3-4b-pt | 1 | 1 | google/medgemma-4b-pt | 22 | 16 | 1 | 5 | 0 | other |
| 39 | 21 | 21 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-Guard-3-8B | 20 | 6 | 3 | 11 | 0 | restricted |

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

max generation 17, mean generation of derived models 1.57, models per generation {0: 10, 1: 6486, 2: 6045, 3: 294, 4: 93, 5: 19, 6: 6, 7: 3, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 5, 14: 7, 15: 4, 16: 3, 17: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 674.2 | 13485 | 6952 | 1184 | 664 |
| 1 | 6486 | 760 | 0.1174 | 5.321 | 0 | 7302 | 0.9921 | 15458 | 12620 | 5005 | 1373 |
| 2 | 6045 | 785 | 0.13 | 3.605 | 0 | 5360 | 0.0665 | 13559 | 4317 | 2862 | 1027 |
| 3 | 294 | 108 | 0.3724 | 1.069 | 0 | 14 | 0.3503 | 11 | 2 | 202 | 95 |
| 4 | 93 | 33 | 0.3548 | 1.215 | 0 | 9 | 0.2258 | 4 | 1 | 66 | 42 |
| 5 | 19 | 9 | 0.4737 | 1.789 | 0 | 10 | 0.6316 | 0 | 0 | 21 | 13 |
| 6 | 6 | 2 | 0.3333 | 3 | 0 | 14 | 2.333 | 0 | 0 | 5 | 13 |
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
| finetune | 42517 | 5150 | 0.5379 | 0.3743 |
| adapter | 23892 | 3115 | 0.3023 | 0.2264 |
| quantized | 9376 | 3680 | 0.1186 | 0.2674 |
| merge | 3259 | 1815 | 0.04123 | 0.1319 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 7056 |
| child_unknown | 3580 |
| loosened | 1444 |
| changed_same_category | 612 |
| parent_unknown | 509 |
| changed_custom | 356 |
| tightened | 224 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 1 |
| noncommercial | 0 | 72 | 1 | 4 | 3 | 66 |
| other | 0 | 2 | 69 | 10 | 0 | 24 |
| permissive | 18 | 72 | 177 | 4721 | 73 | 2050 |
| restricted | 14 | 61 | 166 | 1423 | 2804 | 1439 |
| unknown | 0 | 0 | 3 | 40 | 9 | 457 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 43 | 42 | 793 | 0 | 191 | 892 | 10 | 1971 | 0.09625 | 0 |
| Qwen/Qwen3-8B-Base | 37 | 53 | 279 | 0 | 67 | 973 | 13 | 1422 | 0.09572 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 62 | 1 | 349 | 350 | 15 | 547 | 30 | 1354 | 0.4475 | 0.3535 |
| google/gemma-3-4b-pt | 24 | 0 | 348 | 307 | 10 | 559 | 17 | 1265 | 0.3837 | 0.3385 |
| meta-llama/Llama-3.1-8B | 41 | 89 | 510 | 228 | 141 | 949 | 17 | 1975 | 0.2832 | 0.1722 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 312 | 555 | 32 | 862 | 3 | 1823 | 0.4172 | 0.3753 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 28 | 116 | 601 | 4 | 38 | 1272 | 55 | 2114 | 0.1376 | 0.002712 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 115 | 157 | 1190 | 156 | 21 | 1436 | 40 | 3115 | 0.2458 | 0.08193 |
| finetune | 139 | 318 | 900 | 857 | 102 | 2716 | 118 | 5150 | 0.3452 | 0.2066 |
| merge | 21 | 54 | 1158 | 53 | 173 | 309 | 47 | 1815 | 0.3616 | 0.1095 |
| quantized | 77 | 83 | 329 | 378 | 213 | 2581 | 19 | 3680 | 0.1775 | 0.1205 |
| unknown | 4 | 0 | 3 | 0 | 0 | 14 | 0 | 21 | 0.2222 | 0 |

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
| AdarshRL/gemma2-9b-terraform-architect-adapter | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| AhmedSaghir/doc_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AlekseyCalvin/LYRICAL_MT_ru2en_TowerPlus9b | Unbabel/Tower-Plus-9B | finetune | google/gemma-2-9b | apache-2.0 | cc-by-nc-sa-4.0 |
| Alfaxad/gemma2-9b-swahili-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Azoz-7/lora_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CSLin3303/20241204 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Cannae-AI/TANIT-V0.5-Medium-9B-IT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CerebrumTech/cere-gemma-2-9b-tr | google/gemma-2-9b-it | quantized | google/gemma-2-9b | mit | gemma |
| Cesarbasurto/FullNameSplit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| ChetKao/Bohdi-gemma-2-9b-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | mit | gemma |
| ChrisX123/ChatgptDataset_GGUF__10000Instruction_VsGoemotion | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/ChatgptDataset_GGUF__100Instruction_VsGoemotion | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/ChatgptDataset_GGUF__1Instruction_VsGoemotion | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/Goemotion_GGUF_1Instruction | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
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

*… 1404 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 248 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 538 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 250 |
| 2024-Q3 | 98 | 0 | 0 | 26 | 351 | 0 | 317 | 30 | 33 | 87 |
| 2024-Q4 | 291 | 0 | 0 | 45 | 254 | 0 | 307 | 406 | 25 | 219 |
| 2025-Q1 | 431 | 0 | 457 | 62 | 154 | 130 | 368 | 375 | 27 | 168 |
| 2025-Q2 | 199 | 216 | 25 | 63 | 194 | 236 | 223 | 405 | 76 | 106 |
| 2025-Q3 | 192 | 207 | 30 | 49 | 43 | 185 | 112 | 202 | 53 | 183 |
| 2025-Q4 | 56 | 152 | 2 | 49 | 56 | 140 | 102 | 158 | 53 | 29 |
| 2026-Q1 | 95 | 133 | 12 | 28 | 83 | 214 | 64 | 56 | 23 | 51 |
| 2026-Q2 | 104 | 269 | 2 | 21 | 101 | 161 | 119 | 76 | 11 | 27 |
| 2026-Q3 | 149 | 306 | 10 | 65 | 44 | 127 | 157 | 51 | 7 | 18 |
| 2026-Q4 | 35 | 113 | 0 | 36 | 12 | 54 | 25 | 9 | 4 | 14 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 0 | 6 | 287 |
| 2024-Q1 | 1 | 11 | 0 | 4 | 0 | 8 | 745 |
| 2024-Q2 | 0 | 16 | 0 | 6 | 7 | 4 | 471 |
| 2024-Q3 | 1 | 10 | 3 | 12 | 6 | 9 | 901 |
| 2024-Q4 | 0 | 13 | 1 | 37 | 11 | 23 | 1462 |
| 2025-Q1 | 9 | 15 | 102 | 137 | 25 | 137 | 1747 |
| 2025-Q2 | 10 | 14 | 198 | 54 | 7 | 81 | 1379 |
| 2025-Q3 | 7 | 21 | 159 | 39 | 6 | 34 | 990 |
| 2025-Q4 | 11 | 19 | 110 | 37 | 8 | 35 | 577 |
| 2026-Q1 | 22 | 10 | 86 | 106 | 11 | 19 | 505 |
| 2026-Q2 | 31 | 8 | 70 | 31 | 12 | 13 | 726 |
| 2026-Q3 | 21 | 6 | 64 | 32 | 11 | 51 | 749 |
| 2026-Q4 | 12 | 6 | 20 | 12 | 15 | 22 | 215 |

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
| 2023-Q4 | 103 | 121 | 3 | 0 | 76 |
| 2024-Q1 | 270 | 234 | 139 | 14 | 112 |
| 2024-Q2 | 135 | 194 | 78 | 3 | 94 |
| 2024-Q3 | 132 | 321 | 58 | 0 | 431 |
| 2024-Q4 | 225 | 513 | 131 | 0 | 678 |
| 2025-Q1 | 495 | 794 | 216 | 0 | 667 |
| 2025-Q2 | 227 | 900 | 101 | 0 | 515 |
| 2025-Q3 | 297 | 455 | 210 | 0 | 294 |
| 2025-Q4 | 197 | 372 | 30 | 0 | 198 |
| 2026-Q1 | 246 | 276 | 19 | 0 | 218 |
| 2026-Q2 | 319 | 359 | 28 | 6 | 179 |
| 2026-Q3 | 384 | 405 | 14 | 2 | 129 |
| 2026-Q4 | 74 | 154 | 20 | 3 | 51 |

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
| 2023-Q4 | 0.34 | 0.399 | 0.01 | 0 | 0.251 |
| 2024-Q1 | 0.351 | 0.304 | 0.181 | 0.018 | 0.146 |
| 2024-Q2 | 0.268 | 0.385 | 0.155 | 0.006 | 0.187 |
| 2024-Q3 | 0.14 | 0.341 | 0.062 | 0 | 0.458 |
| 2024-Q4 | 0.145 | 0.332 | 0.085 | 0 | 0.438 |
| 2025-Q1 | 0.228 | 0.366 | 0.099 | 0 | 0.307 |
| 2025-Q2 | 0.13 | 0.516 | 0.058 | 0 | 0.295 |
| 2025-Q3 | 0.236 | 0.362 | 0.167 | 0 | 0.234 |
| 2025-Q4 | 0.247 | 0.467 | 0.038 | 0 | 0.248 |
| 2026-Q1 | 0.324 | 0.364 | 0.025 | 0 | 0.287 |
| 2026-Q2 | 0.358 | 0.403 | 0.031 | 0.007 | 0.201 |
| 2026-Q3 | 0.411 | 0.434 | 0.015 | 0.002 | 0.138 |
| 2026-Q4 | 0.245 | 0.51 | 0.066 | 0.01 | 0.169 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 13000 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 3472 | 26.7 % |
| missing pipeline_tag (as published) | 5212 | 40.1 % |
|   of which filled from parent | 5211 | see pipeline_tag_source |
| missing library_name | 2034 | 15.6 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 16555 |  |
|   linked by HF | 15244 | 92.1 % |
|   old name of a renamed repo | 827 | 5.0 % |
|   not linked (broken parent link) | 484 | 2.9 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 13440 | 100.0 % of 13440 |
| tag edges to a parent outside the sample | 2420 | 14.9 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 100.0% | 50 random models x 11 fields; every field 100 % |
