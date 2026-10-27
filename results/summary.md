# Mining results

Generated 2026-10-27 07:31 UTC from 15026 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 15014 | 22499 |
| nodes_in_sample | 15014 | 15014 |
| edges | 15927 | 25339 |
| relations | {'finetune': 5927, 'adapter': 3757, 'quantized': 4159, 'merge': 2062, 'unknown': 22} | {'finetune': 8498, 'adapter': 6608, 'quantized': 5214, 'merge': 4992, 'unknown': 27} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 8642 | 20414 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 675 |
| leaves | 14035 | 20809 |
| multi_parent_nodes | 541 | 1287 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 59 | 3.499e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 6.169e-10 | 20 | 1 |  |
| HITS authority | 164 | 3.61e-10 | 20 | 0.9082 | 0.936 |
| HITS hub | 164 | 3.64e-13 | 20 | 0.9987 | 0.936 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 76 | 1.187e-09 | 20 | 1 |  |
| Weighted PageRank | 53 | 7.876e-10 | 20 | 1 |  |
| HITS authority | 181 | 1.649e-10 | 20 | 0.979 | 0.9411 |
| HITS hub | 181 | 4.514e-13 | 20 | 0.9992 | 0.9411 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06688 | 0.04559 | 3 | 5.7e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06384 | 0.05883 | 2 | 0.001983 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.0497 | 0.01712 | 8 | 3.19e-05 | 9.597e-09 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04763 | 0.01588 | 9 | 0.0002744 | 3.339e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03541 | 0.06758 | 1 | 0.472 | 0 | 1112 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03031 | 0.008538 | 18 | 1.927e-72 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02975 | 0.0293 | 5 | 5.401e-13 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02809 | 0.01513 | 10 | 3.4e-11 | 9.093e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02238 | 2.038e-05 | 1644 | 7.009e-07 | 5.372e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02054 | 0.02196 | 7 | 7.473e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01805 | 0.01475 | 11 | 2.081e-24 | 1.258e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01258 | 0.02969 | 4 | 7.377e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01186 | 0.02631 | 6 | 2.513e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01009 | 9.075e-05 | 209 | 2.225e-07 | 4.62e-07 | 22 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008616 | 0.004735 | 27 | 4.47e-07 | 9.597e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008054 | 0.01283 | 12 | 1.197e-08 | 4.232e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.00699 | 0.0004841 | 61 | 1.373e-06 | 7.527e-10 | 67 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006789 | 0.006149 | 25 | 8.937e-07 | 9.597e-09 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006551 | 1.921e-05 | 9462 | 0 | 4.62e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006523 | 0.0121 | 13 | 4.647e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06745 | 0.04323 | 4 | 1.115e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06456 | 0.04766 | 2 | 0.006602 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04967 | 0.004619 | 17 | 7.424e-06 | 1.092e-09 | 215 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04784 | 0.00356 | 20 | 0.0002166 | 6.468e-06 | 126 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03742 | 0.05135 | 1 | 0.9103 | 0 | 1111 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03039 | 0.01342 | 13 | 2.99e-59 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02994 | 0.03804 | 5 | 8.064e-47 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02824 | 0.01479 | 11 | 5.392e-46 | 7.901e-50 | 587 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02239 | 3.352e-05 | 979 | 7.942e-09 | 7.274e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02057 | 0.03362 | 7 | 5.227e-18 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01807 | 0.02259 | 8 | 1.456e-15 | 5.121e-21 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01298 | 0.04673 | 3 | 1.123e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.012 | 0.036 | 6 | 9.645e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01012 | 0.0002061 | 126 | 2.112e-07 | 2.122e-07 | 22 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008692 | 0.004092 | 19 | 9.277e-08 | 1.092e-09 | 155 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008121 | 0.0163 | 10 | 4.208e-08 | 9.45e-09 | 650 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007008 | 0.000778 | 55 | 1.606e-07 | 9.09e-11 | 67 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006852 | 0.00277 | 22 | 1.433e-07 | 1.092e-09 | 116 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006554 | 2.936e-05 | 8751 | 0 | 2.122e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006552 | 0.01861 | 9 | 5.388e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001297 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001297 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001297 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 71, 'modularity': 0.9297834485145818, 'largest': 1310, 'weighted_purity': 0.9998001864926069, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1310 | 1310 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1329 | 278 | 315 | 429 | 301 | permissive |
| 1 | 1130 | 1130 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1145 | 333 | 315 | 457 | 40 | restricted |
| 2 | 1021 | 1021 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1032 | 313 | 319 | 353 | 47 | restricted |
| 3 | 986 | 986 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B | 1080 | 308 | 307 | 277 | 188 | permissive |
| 4 | 909 | 909 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 919 | 300 | 300 | 300 | 19 | restricted |
| 5 | 780 | 780 | Qwen/Qwen2.5-7B | 0.9962 | 3 | Qwen/Qwen2.5-7B-Instruct | 918 | 206 | 121 | 239 | 352 | permissive |
| 6 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 7 | 713 | 713 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 738 | 236 | 231 | 205 | 66 | restricted |
| 8 | 643 | 643 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 651 | 327 | 162 | 144 | 16 | permissive |
| 9 | 612 | 612 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 622 | 185 | 187 | 202 | 48 | permissive |
| 10 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 11 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 12 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 13 | 443 | 443 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 506 | 82 | 99 | 155 | 170 | permissive |
| 14 | 437 | 437 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 436 | 123 | 287 | 22 | 4 | restricted |
| 15 | 420 | 420 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 420 | 317 | 30 | 71 | 2 | unknown |
| 16 | 414 | 414 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 413 | 227 | 46 | 140 | 0 | permissive |
| 17 | 349 | 349 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 428 | 64 | 37 | 143 | 184 | restricted |
| 18 | 310 | 310 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 309 | 253 | 18 | 38 | 0 | permissive |
| 19 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 20 | 260 | 260 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 318 | 52 | 51 | 88 | 127 | restricted |
| 21 | 174 | 174 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 184 | 33 | 33 | 58 | 60 | permissive |
| 22 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 23 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 24 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 25 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 26 | 73 | 73 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 72 | 24 | 24 | 24 | 0 | permissive |
| 27 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 28 | 62 | 62 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 61 | 14 | 14 | 14 | 19 | permissive |
| 29 | 50 | 50 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 50 | 16 | 19 | 9 | 6 | permissive |
| 30 | 46 | 46 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 45 | 24 | 16 | 5 | 0 | permissive |
| 31 | 43 | 43 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 42 | 23 | 3 | 13 | 3 | unknown |
| 32 | 40 | 40 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 39 | 23 | 9 | 7 | 0 | permissive |
| 33 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 34 | 32 | 32 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/mistral-7b-sft-beta | 31 | 14 | 14 | 3 | 0 | permissive |
| 35 | 31 | 31 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-Guard-3-8B | 30 | 6 | 3 | 21 | 0 | restricted |
| 36 | 31 | 31 | Qwen/Qwen3-8B-Base | 1 | 1 | jackf857/qwen3-8b-base-sft-ultrachat-4xh200-batch-128 | 30 | 30 | 0 | 0 | 0 | unknown |
| 37 | 30 | 30 | meta-llama/Llama-3.1-8B | 1 | 1 | McGill-NLP/AfriqueLlama-8B | 29 | 3 | 23 | 3 | 0 | restricted |
| 38 | 29 | 29 | Qwen/Qwen2.5-7B | 1 | 1 | mehuldamani/qwen-base-verifier-sft-v1 | 28 | 28 | 0 | 0 | 0 | unknown |
| 39 | 28 | 28 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-Storm-8B-bnb-4bit | 27 | 20 | 0 | 7 | 0 | permissive |

*… 31 more rows in the CSV*

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

max generation 18, mean generation of derived models 1.64, models per generation {0: 10, 1: 6484, 2: 8021, 3: 337, 4: 97, 5: 19, 6: 6, 7: 2, 8: 3, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3, 14: 5, 15: 7, 16: 4, 17: 3, 18: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 674.3 | 13485 | 6952 | 1184 | 664 |
| 1 | 6484 | 759 | 0.1173 | 5.323 | 0 | 7302 | 1.308 | 15458 | 12620 | 5003 | 1373 |
| 2 | 8021 | 985 | 0.1229 | 2.892 | 0 | 5360 | 0.06209 | 14004 | 4708 | 3297 | 1165 |
| 3 | 337 | 133 | 0.3994 | 1.108 | 0 | 14 | 0.3116 | 13 | 2 | 251 | 103 |
| 4 | 97 | 34 | 0.3505 | 1.175 | 0 | 9 | 0.2165 | 4 | 1 | 67 | 42 |
| 5 | 19 | 9 | 0.4737 | 1.579 | 0 | 10 | 0.4211 | 0 | 0 | 21 | 9 |
| 6 | 6 | 2 | 0.3333 | 2 | 0 | 8 | 1.333 | 0 | 0 | 5 | 7 |
| 7 | 2 | 1 | 0.5 | 7 | 7 | 14 | 7 | 0 | 0 | 1 | 13 |
| 8 | 3 | 2 | 0.6667 | 3 | 4 | 5 | 1.667 | 0 | 0 | 5 | 4 |
| 9 | 2 | 1 | 0.5 | 2 | 2 | 4 | 2 | 0 | 0 | 1 | 3 |
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
| finetune | 42964 | 5927 | 0.5336 | 0.3727 |
| adapter | 24283 | 3757 | 0.3016 | 0.2362 |
| quantized | 9860 | 4159 | 0.1225 | 0.2615 |
| merge | 3408 | 2062 | 0.04233 | 0.1296 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 8056 |
| child_unknown | 4160 |
| loosened | 1795 |
| changed_same_category | 694 |
| parent_unknown | 524 |
| changed_custom | 431 |
| tightened | 267 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 1 |
| noncommercial | 0 | 73 | 1 | 4 | 3 | 66 |
| other | 0 | 2 | 69 | 12 | 0 | 24 |
| permissive | 21 | 88 | 203 | 5342 | 87 | 2328 |
| restricted | 18 | 71 | 213 | 1770 | 3264 | 1741 |
| unknown | 0 | 0 | 3 | 40 | 9 | 472 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 52 | 63 | 905 | 0 | 206 | 1042 | 12 | 2280 | 0.1086 | 0 |
| Qwen/Qwen3-8B-Base | 46 | 74 | 336 | 0 | 67 | 1197 | 20 | 1740 | 0.1047 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 94 | 1 | 447 | 455 | 15 | 617 | 32 | 1661 | 0.4854 | 0.3795 |
| google/gemma-3-4b-pt | 29 | 0 | 446 | 345 | 10 | 688 | 23 | 1541 | 0.3659 | 0.318 |
| meta-llama/Llama-3.1-8B | 51 | 109 | 625 | 311 | 141 | 1063 | 32 | 2332 | 0.3212 | 0.1986 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 317 | 680 | 32 | 1010 | 3 | 2101 | 0.4235 | 0.3881 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 38 | 136 | 696 | 4 | 38 | 1437 | 66 | 2415 | 0.1452 | 0.00238 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 164 | 170 | 1397 | 181 | 21 | 1769 | 55 | 3757 | 0.2437 | 0.07738 |
| finetune | 148 | 350 | 1062 | 1144 | 113 | 2971 | 139 | 5927 | 0.3748 | 0.2407 |
| merge | 27 | 76 | 1324 | 58 | 177 | 348 | 52 | 2062 | 0.3797 | 0.1034 |
| quantized | 87 | 98 | 374 | 412 | 213 | 2954 | 21 | 4159 | 0.173 | 0.1153 |
| unknown | 5 | 0 | 3 | 0 | 0 | 14 | 0 | 22 | 0.2632 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 1-800-SHARED-TASKS/CHIPSAL-B-GEMMA2-001-9B-balanced-data-w-few-shot-prompting | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/CHIPSAL-B-GEMMA2-001-9B-w-few-shot-prompting | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/CHIPSAL-subtaskA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/Kan_Gemma-2-9b-ChipsalSubtaskA-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
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
| AdarshRL/gemma2-9b-terraform-architect-adapter | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| AhmedSaghir/doc_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AlekseyCalvin/LYRICAL_MT_ru2en_TowerPlus9b | Unbabel/Tower-Plus-9B | finetune | google/gemma-2-9b | apache-2.0 | cc-by-nc-sa-4.0 |
| Alfaxad/gemma2-9b-swahili-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Azoz-7/lora_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CNCL-Penn-State/CrPO-RM-gemma-2-9b-it | google/gemma-2-9b-it | adapter | google/gemma-2-9b | mit | gemma |
| CSLin3303/20241204 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Cannae-AI/TANIT-V0.5-Medium-9B-IT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CerebrumTech/cere-gemma-2-9b-tr | google/gemma-2-9b-it | quantized | google/gemma-2-9b | mit | gemma |
| Cesarbasurto/FullNameSplit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| ChetKao/Bohdi-gemma-2-9b-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | mit | gemma |
| ChrisX123/ChatgptDataset_GGUF__10000Instruction_VsGoemotion | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/ChatgptDataset_GGUF__100Instruction_VsGoemotion | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/ChatgptDataset_GGUF__1Instruction_VsGoemotion | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/Goemotion_GGUF_10000Instruction | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/Goemotion_GGUF_100Instruction | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |

*… 1755 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 282 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 636 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 276 |
| 2024-Q3 | 105 | 0 | 0 | 26 | 420 | 0 | 366 | 30 | 33 | 101 |
| 2024-Q4 | 315 | 0 | 0 | 45 | 311 | 0 | 355 | 422 | 25 | 247 |
| 2025-Q1 | 489 | 0 | 457 | 62 | 210 | 132 | 444 | 487 | 27 | 201 |
| 2025-Q2 | 240 | 255 | 25 | 63 | 211 | 250 | 257 | 429 | 76 | 141 |
| 2025-Q3 | 221 | 228 | 30 | 49 | 57 | 203 | 122 | 206 | 53 | 191 |
| 2025-Q4 | 69 | 174 | 2 | 49 | 67 | 178 | 114 | 159 | 53 | 31 |
| 2026-Q1 | 127 | 165 | 12 | 28 | 99 | 278 | 73 | 56 | 23 | 53 |
| 2026-Q2 | 132 | 320 | 2 | 21 | 156 | 281 | 150 | 197 | 11 | 28 |
| 2026-Q3 | 176 | 380 | 10 | 65 | 56 | 147 | 178 | 51 | 7 | 18 |
| 2026-Q4 | 48 | 184 | 0 | 36 | 12 | 54 | 30 | 9 | 4 | 16 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 6 | 321 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 4 | 8 | 843 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 497 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 18 | 9 | 1040 | 0 |
| 2024-Q4 | 0 | 13 | 1 | 43 | 23 | 1635 | 5 |
| 2025-Q1 | 9 | 15 | 104 | 147 | 140 | 2078 | 16 |
| 2025-Q2 | 10 | 14 | 212 | 56 | 81 | 1568 | 6 |
| 2025-Q3 | 7 | 21 | 175 | 45 | 34 | 1078 | 0 |
| 2025-Q4 | 12 | 19 | 136 | 42 | 35 | 647 | 5 |
| 2026-Q1 | 23 | 10 | 118 | 49 | 19 | 618 | 77 |
| 2026-Q2 | 31 | 8 | 92 | 38 | 15 | 1101 | 13 |
| 2026-Q3 | 23 | 6 | 71 | 47 | 55 | 882 | 4 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 24 | 304 | 1 |

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
| 2023-Q4 | 121 | 129 | 4 | 0 | 83 |
| 2024-Q1 | 291 | 261 | 177 | 14 | 124 |
| 2024-Q2 | 139 | 201 | 88 | 3 | 99 |
| 2024-Q3 | 146 | 393 | 68 | 0 | 474 |
| 2024-Q4 | 267 | 585 | 141 | 0 | 727 |
| 2025-Q1 | 658 | 874 | 247 | 0 | 730 |
| 2025-Q2 | 274 | 977 | 119 | 0 | 577 |
| 2025-Q3 | 323 | 513 | 212 | 0 | 312 |
| 2025-Q4 | 223 | 425 | 31 | 0 | 217 |
| 2026-Q1 | 322 | 334 | 20 | 0 | 238 |
| 2026-Q2 | 430 | 535 | 34 | 8 | 291 |
| 2026-Q3 | 442 | 446 | 15 | 3 | 182 |
| 2026-Q4 | 108 | 200 | 20 | 3 | 62 |

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
| 2023-Q4 | 0.359 | 0.383 | 0.012 | 0 | 0.246 |
| 2024-Q1 | 0.336 | 0.301 | 0.204 | 0.016 | 0.143 |
| 2024-Q2 | 0.262 | 0.379 | 0.166 | 0.006 | 0.187 |
| 2024-Q3 | 0.135 | 0.364 | 0.063 | 0 | 0.438 |
| 2024-Q4 | 0.155 | 0.34 | 0.082 | 0 | 0.423 |
| 2025-Q1 | 0.262 | 0.348 | 0.098 | 0 | 0.291 |
| 2025-Q2 | 0.141 | 0.502 | 0.061 | 0 | 0.296 |
| 2025-Q3 | 0.238 | 0.377 | 0.156 | 0 | 0.229 |
| 2025-Q4 | 0.249 | 0.474 | 0.035 | 0 | 0.242 |
| 2026-Q1 | 0.352 | 0.365 | 0.022 | 0 | 0.26 |
| 2026-Q2 | 0.331 | 0.412 | 0.026 | 0.006 | 0.224 |
| 2026-Q3 | 0.406 | 0.41 | 0.014 | 0.003 | 0.167 |
| 2026-Q4 | 0.275 | 0.509 | 0.051 | 0.008 | 0.158 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 15026 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 3985 | 26.5 % |
| missing pipeline_tag (as published) | 6050 | 40.3 % |
|   of which filled from parent | 6049 | see pipeline_tag_source |
| missing library_name | 2293 | 15.3 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 18886 |  |
|   linked by HF | 17478 | 92.5 % |
|   old name of a renamed repo | 887 | 4.7 % |
|   not linked (broken parent link) | 521 | 2.8 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 15487 | 100.0 % of 15487 |
| tag edges to a parent outside the sample | 2572 | 13.9 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.6% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 96% |
