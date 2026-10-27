# Mining results

Generated 2026-10-27 11:43 UTC from 20000 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 19963 | 22580 |
| nodes_in_sample | 19963 | 19963 |
| edges | 21130 | 25874 |
| relations | {'finetune': 7843, 'adapter': 5505, 'quantized': 5071, 'merge': 2686, 'unknown': 25} | {'finetune': 8499, 'adapter': 6622, 'quantized': 5214, 'merge': 5509, 'unknown': 30} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 13239 | 20495 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 756 |
| leaves | 18923 | 20788 |
| multi_parent_nodes | 665 | 1656 |
| temporal_anomaly_edges | 24 | 24 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 75 | 2.597e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 1.217e-09 | 20 | 1 |  |
| HITS authority | 546 | 1.359e-09 | 20 | 0.9882 | 0.9813 |
| HITS hub | 546 | 1.28e-12 | 20 | 0.9904 | 0.9813 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 74 | 2.475e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 9.332e-10 | 20 | 1 |  |
| HITS authority | 174 | 1.572e-10 | 20 | 0.9782 | 0.9387 |
| HITS hub | 174 | 4.23e-13 | 20 | 0.9993 | 0.9387 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06675 | 0.04516 | 3 | 2.137e-05 | 0 | 825 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06379 | 0.05831 | 2 | 0.001948 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04999 | 0.01647 | 8 | 0.000158 | 3.58e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.048 | 0.01537 | 9 | 0.0007151 | 3.263e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03486 | 0.06614 | 1 | 0.4654 | 0 | 1120 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.02965 | 0.008543 | 17 | 3.227e-70 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02955 | 0.02932 | 5 | 1.927e-12 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02801 | 0.01513 | 10 | 1.228e-10 | 3.228e-15 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02189 | 2.039e-05 | 1746 | 1.241e-06 | 2.648e-07 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.0201 | 0.02197 | 7 | 1.737e-26 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01766 | 0.01476 | 11 | 4.838e-24 | 2.91e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.0123 | 0.0297 | 4 | 1.799e-09 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01161 | 0.02632 | 6 | 2.442e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009866 | 9.897e-05 | 202 | 2.884e-07 | 1.198e-06 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008469 | 0.004835 | 27 | 2.118e-06 | 3.58e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.007884 | 0.01283 | 12 | 1.141e-08 | 4.092e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006819 | 0.0006054 | 54 | 6.782e-06 | 3.548e-09 | 82 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006756 | 0.006169 | 24 | 4.219e-06 | 3.58e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006409 | 1.923e-05 | 9561 | 0 | 1.198e-06 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006382 | 0.0121 | 13 | 8.101e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06729 | 0.05154 | 3 | 2.216e-05 | 0 | 825 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06461 | 0.05804 | 2 | 0.006154 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05032 | 0.01912 | 8 | 0.0001439 | 2.175e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.0484 | 0.01273 | 13 | 0.0004507 | 6.038e-06 | 676 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03732 | 0.06114 | 1 | 0.8906 | 0 | 1119 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen3-8B-Base | 0.02972 | 0.03308 | 5 | 4.805e-44 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 7 | google-bert/bert-base-uncased | 0.02971 | 0.009756 | 15 | 2.96e-197 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02813 | 0.01714 | 9 | 1.852e-42 | 4.714e-47 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02189 | 2.437e-05 | 1027 | 1.556e-07 | 1.412e-07 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02011 | 0.02444 | 7 | 2.967e-54 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01766 | 0.01642 | 10 | 8.264e-52 | 2.911e-57 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01269 | 0.03397 | 4 | 1.636e-55 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01173 | 0.0295 | 6 | 8.883e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009895 | 0.0001553 | 127 | 5.637e-07 | 4.422e-07 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008517 | 0.005469 | 23 | 2.213e-06 | 2.175e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.007947 | 0.01444 | 11 | 5.472e-08 | 8.716e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.00683 | 0.0006946 | 52 | 5.572e-06 | 2.171e-09 | 82 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006776 | 0.006895 | 19 | 4.468e-06 | 2.175e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006408 | 2.134e-05 | 8809 | 0 | 4.422e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006405 | 0.01353 | 12 | 1.032e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001272 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001272 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001272 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 62, 'modularity': 0.9379677448038185, 'largest': 1384, 'weighted_purity': 0.9999499073285578, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1384 | 1384 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1406 | 294 | 326 | 467 | 312 | permissive |
| 1 | 1152 | 1152 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1167 | 338 | 321 | 467 | 41 | restricted |
| 2 | 1095 | 1095 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B-Instruct | 1204 | 304 | 299 | 358 | 243 | permissive |
| 3 | 1083 | 1083 | Qwen/Qwen2.5-7B | 0.9991 | 2 | Qwen/Qwen2.5-7B | 1212 | 318 | 307 | 303 | 283 | permissive |
| 4 | 1021 | 1021 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1032 | 313 | 319 | 353 | 47 | restricted |
| 5 | 927 | 927 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 938 | 299 | 301 | 300 | 38 | permissive |
| 6 | 909 | 909 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 919 | 300 | 300 | 300 | 19 | restricted |
| 7 | 856 | 856 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 881 | 308 | 302 | 205 | 66 | restricted |
| 8 | 736 | 736 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 740 | 321 | 301 | 103 | 14 | permissive |
| 9 | 713 | 713 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 723 | 348 | 178 | 166 | 29 | permissive |
| 10 | 674 | 674 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 685 | 189 | 181 | 213 | 102 | restricted |
| 11 | 639 | 639 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-Math-7B | 670 | 421 | 84 | 71 | 94 | unknown |
| 12 | 590 | 590 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 665 | 137 | 171 | 150 | 207 | permissive |
| 13 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 14 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 15 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 16 | 490 | 490 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 490 | 359 | 34 | 95 | 2 | unknown |
| 17 | 487 | 487 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 486 | 300 | 46 | 140 | 0 | permissive |
| 18 | 456 | 456 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 455 | 197 | 61 | 197 | 0 | permissive |
| 19 | 447 | 447 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-Storm-8B | 574 | 43 | 205 | 104 | 222 | restricted |
| 20 | 437 | 437 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 436 | 123 | 287 | 22 | 4 | restricted |
| 21 | 433 | 433 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 444 | 59 | 201 | 118 | 66 | restricted |
| 22 | 349 | 349 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 348 | 113 | 113 | 46 | 76 | permissive |
| 23 | 310 | 310 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 309 | 253 | 18 | 38 | 0 | permissive |
| 24 | 306 | 306 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 310 | 27 | 118 | 42 | 123 | permissive |
| 25 | 302 | 302 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 301 | 113 | 113 | 31 | 44 | permissive |
| 26 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 27 | 236 | 236 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 236 | 114 | 107 | 9 | 6 | permissive |
| 28 | 168 | 168 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Genstruct-7B | 174 | 11 | 112 | 26 | 25 | permissive |
| 29 | 165 | 165 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B-Instruct-1M | 177 | 51 | 3 | 77 | 46 | permissive |
| 30 | 161 | 161 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 160 | 141 | 3 | 13 | 3 | unknown |
| 31 | 158 | 158 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Nous-Hermes-2-Mistral-7B-DPO | 157 | 9 | 112 | 17 | 19 | permissive |
| 32 | 132 | 132 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 133 | 65 | 21 | 30 | 17 | permissive |
| 33 | 130 | 130 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/mistral-7b-sft-beta | 129 | 112 | 14 | 3 | 0 | permissive |
| 34 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 35 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 36 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 37 | 94 | 94 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 93 | 72 | 16 | 5 | 0 | permissive |
| 38 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 39 | 74 | 74 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-alpha | 73 | 14 | 43 | 14 | 2 | permissive |

*… 22 more rows in the CSV*

**cross_family_links**

| child | parent | relation | child_family | parent_family |
|---|---|---|---|---|
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v2 | microsoft/phi-2 | merge | Qwen/Qwen2.5-7B | microsoft/phi-2 |
| Optitransfer/Qwen2.5-7B-Instruct-converge-v1remerge-maskn_project | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Optitransfer/Qwen2.5-7B-Instruct-converge-collective-v1 | Qwen/Qwen2.5-7B-Instruct | merge | microsoft/phi-2 | Qwen/Qwen2.5-7B |
| Haker18/Llama-Gemma-Hybrid-9B | meta-llama/Llama-3.1-8B | merge | google/gemma-2-9b | meta-llama/Llama-3.1-8B |
| Davidsv/CosmeticVentureV2 | mistralai/Mistral-7B-v0.1 | merge | meta-llama/Llama-3.1-8B | mistralai/Mistral-7B-v0.1 |
| Abigail45/Chyio | Qwen/Qwen2.5-7B-Instruct | merge | meta-llama/Llama-3.1-8B | Qwen/Qwen2.5-7B |
| Vaultkeeper/Sovereign-Code | Qwen/Qwen2.5-Coder-7B-Instruct | merge | meta-llama/Llama-3.1-8B | Qwen/Qwen2.5-7B |

## 3. Lineage

max generation 18, mean generation of derived models 1.74, models per generation {0: 10, 1: 6476, 2: 12855, 3: 405, 4: 131, 5: 25, 6: 9, 7: 8, 8: 8, 9: 3, 10: 2, 11: 3, 12: 3, 13: 3, 14: 5, 15: 7, 16: 4, 17: 3, 18: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 675.2 | 13485 | 6952 | 1184 | 664 |
| 1 | 6476 | 751 | 0.1162 | 5.325 | 0 | 7302 | 2.073 | 15458 | 12620 | 4987 | 1359 |
| 2 | 12855 | 1523 | 0.1186 | 1.918 | 0 | 5360 | 0.05259 | 14281 | 4774 | 4133 | 1445 |
| 3 | 405 | 174 | 0.4339 | 1.239 | 0 | 15 | 0.3704 | 13 | 6 | 339 | 139 |
| 4 | 131 | 48 | 0.3664 | 1.275 | 0 | 16 | 0.2137 | 5 | 1 | 88 | 73 |
| 5 | 25 | 11 | 0.44 | 1.6 | 0 | 10 | 0.44 | 0 | 0 | 27 | 13 |
| 6 | 9 | 6 | 0.6667 | 3.333 | 3 | 10 | 1.667 | 1 | 0 | 12 | 17 |
| 7 | 8 | 3 | 0.375 | 3.125 | 0 | 14 | 2.375 | 0 | 0 | 5 | 20 |
| 8 | 8 | 6 | 0.75 | 1.875 | 1 | 5 | 0.75 | 0 | 0 | 10 | 5 |
| 9 | 3 | 1 | 0.3333 | 1.333 | 0 | 4 | 1.333 | 0 | 0 | 1 | 3 |
| 10 | 2 | 1 | 0.5 | 2 | 2 | 4 | 2 | 0 | 0 | 2 | 2 |
| 11 | 3 | 1 | 0.3333 | 1 | 0 | 3 | 1 | 0 | 0 | 2 | 1 |
| 12 | 3 | 1 | 0.3333 | 2 | 0 | 6 | 2 | 0 | 0 | 2 | 4 |
| 13 | 3 | 1 | 0.3333 | 2 | 0 | 6 | 2 | 0 | 0 | 2 | 4 |
| 14 | 5 | 3 | 0.6 | 2.6 | 3 | 6 | 2.6 | 0 | 0 | 6 | 7 |
| 15 | 7 | 1 | 0.1429 | 0.7143 | 0 | 5 | 0.7143 | 0 | 0 | 2 | 3 |
| 16 | 4 | 2 | 0.5 | 1.5 | 1.5 | 3 | 0.75 | 0 | 0 | 5 | 1 |
| 17 | 3 | 1 | 0.3333 | 1 | 0 | 3 | 1 | 0 | 0 | 2 | 1 |
| 18 | 3 | 1 | 0.3333 | 1.333 | 0 | 4 | 0 | 0 | 0 | 2 | 2 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 43243 | 7843 | 0.5263 | 0.3716 |
| adapter | 24353 | 5505 | 0.2964 | 0.2608 |
| quantized | 10811 | 5071 | 0.1316 | 0.2403 |
| merge | 3763 | 2686 | 0.0458 | 0.1273 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 10709 |
| child_unknown | 5784 |
| loosened | 2359 |
| changed_same_category | 838 |
| changed_custom | 562 |
| parent_unknown | 550 |
| tightened | 328 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 4 |
| noncommercial | 0 | 73 | 1 | 7 | 3 | 84 |
| other | 0 | 2 | 69 | 18 | 1 | 68 |
| permissive | 28 | 116 | 277 | 7435 | 94 | 3451 |
| restricted | 22 | 90 | 263 | 2327 | 3968 | 2177 |
| unknown | 0 | 1 | 3 | 41 | 9 | 496 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 101 | 118 | 1533 | 1 | 221 | 1731 | 41 | 3746 | 0.131 | 0.000502 |
| Qwen/Qwen3-8B-Base | 58 | 94 | 390 | 0 | 67 | 1460 | 26 | 2095 | 0.1087 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 120 | 1 | 535 | 536 | 15 | 636 | 34 | 1877 | 0.5207 | 0.4039 |
| google/gemma-3-4b-pt | 29 | 0 | 446 | 345 | 10 | 688 | 23 | 1541 | 0.3659 | 0.318 |
| meta-llama/Llama-3.1-8B | 78 | 140 | 985 | 791 | 144 | 1717 | 49 | 3904 | 0.3813 | 0.285 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 317 | 680 | 32 | 1010 | 3 | 2101 | 0.4235 | 0.3881 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 55 | 174 | 1190 | 6 | 46 | 2465 | 73 | 4009 | 0.1111 | 0.002164 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 209 | 201 | 1877 | 214 | 23 | 2910 | 71 | 5505 | 0.1928 | 0.05936 |
| finetune | 191 | 410 | 1628 | 1470 | 114 | 3858 | 172 | 7843 | 0.3676 | 0.2409 |
| merge | 36 | 84 | 1814 | 66 | 200 | 431 | 55 | 2686 | 0.3586 | 0.09821 |
| quantized | 120 | 143 | 462 | 609 | 213 | 3494 | 30 | 5071 | 0.2052 | 0.1385 |
| unknown | 6 | 0 | 3 | 0 | 0 | 16 | 0 | 25 | 0.2727 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| bunnycore/Qevacot-7B | Cran-May/T.E-8.1 | merge | Qwen/Qwen2.5-7B | apache-2.0 | cc-by-nc-sa-4.0 |
| 0x7o/gm-9B-v2-0827 | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/CHIPSAL-B-GEMMA2-001-9B-balanced-data-w-few-shot-prompting | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/CHIPSAL-B-GEMMA2-001-9B-w-few-shot-prompting | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/CHIPSAL-subtaskA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/Kan_Gemma-2-9b-ChipsalSubtaskA-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/gemma-2-9b-8-epochs-R1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1024m/CHIPSAL-C-GEMMA2-001-9B-A32bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1024m/CHIPSAL-C-GEMMA2-9B-001-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1024m/CHIPSAL-C-SUBMISSION-ENSEMBLE-001-OF-003 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1024m/CHIPSAL-C-SUBMISSION-ENSEMBLE-002-OF-003 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1998rajdeo/gemma-2-9b-bnb-4bit-csv | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 2024-mcm-everitt-ryan/gemma-2-9b-job-bias-qlora-seq-cls | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 4blacks/model-gemma-1m-basic-model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-CA/gem-monika-ddlc-9b-v1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-CA/gem-monika-ddlc-9b-v1-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-Narra/gemma-2-9b-tagalog-chat | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-Narra/gemma-2-9b-tagalog-chat-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-SY/gemma-2-9b-dt2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-SY/gemma-2-9b-dt2-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922CA/gemma-2-9b-etude-2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922CA/gemma-2-9b-etude-2-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| AagamShah08/gemma2_9B_Brainstorming | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Abhilashscaria/lora_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AdarshRL/gemma2-9b-terraform-architect-adapter | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| AhmedSaghir/doc_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AlekseyCalvin/LYRICAL_MT_ru2en_TowerPlus9b | Unbabel/Tower-Plus-9B | finetune | google/gemma-2-9b | apache-2.0 | cc-by-nc-sa-4.0 |
| Alfaxad/gemma2-9b-swahili-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AnshuPatel-Vikalp/Nutritions3 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AnshuPatel-Vikalp/Nutritions5 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AntoshkaVVV/Pyzirik_1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| ArshadBadfar/Gemma2_ay | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Azoz-7/lora_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bruce-Azar-Wayne/Aristotle-o2.gemma2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CNCL-Penn-State/CrPO-RM-gemma-2-9b-it | google/gemma-2-9b-it | adapter | google/gemma-2-9b | mit | gemma |

*… 2319 more rows in the CSV*

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
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 14 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 458 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 881 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 618 |
| 2024-Q3 | 125 | 0 | 0 | 26 | 430 | 0 | 673 | 30 | 33 | 179 |
| 2024-Q4 | 423 | 0 | 0 | 45 | 384 | 0 | 591 | 422 | 25 | 377 |
| 2025-Q1 | 713 | 0 | 457 | 62 | 235 | 132 | 804 | 487 | 27 | 541 |
| 2025-Q2 | 448 | 284 | 25 | 63 | 221 | 250 | 323 | 429 | 76 | 267 |
| 2025-Q3 | 373 | 256 | 30 | 49 | 74 | 203 | 227 | 206 | 53 | 246 |
| 2025-Q4 | 122 | 200 | 2 | 49 | 81 | 178 | 157 | 159 | 53 | 55 |
| 2026-Q1 | 252 | 218 | 12 | 28 | 112 | 278 | 199 | 56 | 23 | 61 |
| 2026-Q2 | 251 | 380 | 2 | 21 | 210 | 281 | 246 | 197 | 11 | 37 |
| 2026-Q3 | 421 | 490 | 10 | 65 | 56 | 147 | 309 | 51 | 7 | 26 |
| 2026-Q4 | 110 | 230 | 0 | 36 | 12 | 54 | 79 | 9 | 4 | 20 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | text-classification | text-generation | translation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 8 | 0 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 2023-Q3 | 0 | 2 | 0 | 5 | 2 | 14 | 0 |
| 2023-Q4 | 0 | 8 | 2 | 2 | 6 | 495 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 7 | 10 | 1083 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 839 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 21 | 10 | 1451 | 0 |
| 2024-Q4 | 2 | 13 | 3 | 50 | 24 | 2170 | 5 |
| 2025-Q1 | 10 | 15 | 105 | 153 | 143 | 3016 | 16 |
| 2025-Q2 | 10 | 14 | 212 | 63 | 84 | 1997 | 6 |
| 2025-Q3 | 8 | 21 | 175 | 49 | 35 | 1429 | 0 |
| 2025-Q4 | 12 | 19 | 136 | 54 | 36 | 794 | 5 |
| 2026-Q1 | 25 | 10 | 123 | 64 | 22 | 918 | 77 |
| 2026-Q2 | 31 | 8 | 93 | 40 | 18 | 1432 | 14 |
| 2026-Q3 | 23 | 6 | 71 | 50 | 58 | 1370 | 4 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 24 | 465 | 1 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 12 | 0 | 0 | 10 |
| 2023-Q4 | 228 | 187 | 6 | 0 | 92 |
| 2024-Q1 | 395 | 328 | 228 | 16 | 145 |
| 2024-Q2 | 228 | 334 | 198 | 3 | 109 |
| 2024-Q3 | 199 | 550 | 100 | 0 | 647 |
| 2024-Q4 | 448 | 786 | 167 | 0 | 866 |
| 2025-Q1 | 1189 | 1163 | 291 | 0 | 815 |
| 2025-Q2 | 374 | 1204 | 145 | 0 | 663 |
| 2025-Q3 | 414 | 740 | 217 | 0 | 346 |
| 2025-Q4 | 269 | 503 | 35 | 0 | 249 |
| 2026-Q1 | 413 | 458 | 57 | 1 | 310 |
| 2026-Q2 | 542 | 643 | 62 | 8 | 381 |
| 2026-Q3 | 598 | 643 | 26 | 4 | 311 |
| 2026-Q4 | 192 | 246 | 20 | 3 | 93 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.043 | 0.522 | 0 | 0 | 0.435 |
| 2023-Q4 | 0.444 | 0.365 | 0.012 | 0 | 0.179 |
| 2024-Q1 | 0.355 | 0.295 | 0.205 | 0.014 | 0.13 |
| 2024-Q2 | 0.261 | 0.383 | 0.227 | 0.003 | 0.125 |
| 2024-Q3 | 0.133 | 0.368 | 0.067 | 0 | 0.432 |
| 2024-Q4 | 0.198 | 0.347 | 0.074 | 0 | 0.382 |
| 2025-Q1 | 0.344 | 0.336 | 0.084 | 0 | 0.236 |
| 2025-Q2 | 0.157 | 0.505 | 0.061 | 0 | 0.278 |
| 2025-Q3 | 0.241 | 0.431 | 0.126 | 0 | 0.202 |
| 2025-Q4 | 0.255 | 0.476 | 0.033 | 0 | 0.236 |
| 2026-Q1 | 0.333 | 0.37 | 0.046 | 0.001 | 0.25 |
| 2026-Q2 | 0.331 | 0.393 | 0.038 | 0.005 | 0.233 |
| 2026-Q3 | 0.378 | 0.406 | 0.016 | 0.003 | 0.197 |
| 2026-Q4 | 0.347 | 0.444 | 0.036 | 0.005 | 0.168 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 20000 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 5435 | 27.2 % |
| missing pipeline_tag (as published) | 8210 | 41.0 % |
|   of which filled from parent | 8209 | see pipeline_tag_source |
| missing library_name | 2912 | 14.6 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 24442 |  |
|   linked by HF | 22688 | 92.8 % |
|   old name of a renamed repo | 1191 | 4.9 % |
|   not linked (broken parent link) | 563 | 2.3 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 20487 | 100.0 % of 20487 |
| tag edges to a parent outside the sample | 2879 | 12.0 % |
| child created >7 days before its parent | 24 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 98.5% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 84% |
