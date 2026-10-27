# Mining results

Generated 2026-10-27 09:10 UTC from 17001 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 16983 | 22543 |
| nodes_in_sample | 16983 | 16983 |
| edges | 17984 | 25593 |
| relations | {'finetune': 6694, 'adapter': 4370, 'quantized': 4579, 'merge': 2317, 'unknown': 24} | {'finetune': 8498, 'adapter': 6610, 'quantized': 5214, 'merge': 5242, 'unknown': 29} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 10259 | 20458 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 719 |
| leaves | 15979 | 20792 |
| multi_parent_nodes | 603 | 1437 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 67 | 2.41e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 8.91e-10 | 20 | 1 |  |
| HITS authority | 161 | 3.564e-10 | 20 | 0.9143 | 0.9348 |
| HITS hub | 161 | 3.612e-13 | 20 | 0.9992 | 0.9348 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 75 | 9.542e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 7.756e-10 | 20 | 1 |  |
| HITS authority | 178 | 1.636e-10 | 20 | 0.9804 | 0.9401 |
| HITS hub | 178 | 4.44e-13 | 20 | 0.9992 | 0.9401 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06667 | 0.0454 | 3 | 5.682e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06366 | 0.05859 | 2 | 0.002005 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04959 | 0.01687 | 8 | 3.171e-05 | 9.55e-09 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04761 | 0.01573 | 9 | 0.0007219 | 3.371e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03517 | 0.06699 | 1 | 0.469 | 0 | 1115 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03005 | 0.008537 | 18 | 1.836e-71 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02995 | 0.0293 | 5 | 5.285e-13 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02838 | 0.01512 | 10 | 3.343e-11 | 8.884e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02218 | 2.038e-05 | 1705 | 7.071e-07 | 5.329e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02037 | 0.02196 | 7 | 1.138e-26 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01789 | 0.01475 | 11 | 3.17e-24 | 1.913e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01247 | 0.02968 | 4 | 1.854e-09 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01176 | 0.0263 | 6 | 2.531e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009998 | 9.89e-05 | 199 | 2.98e-07 | 1.213e-06 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008595 | 0.004767 | 27 | 4.449e-07 | 9.55e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.00799 | 0.01282 | 12 | 1.197e-08 | 4.255e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006929 | 0.0005301 | 56 | 1.52e-06 | 7.477e-10 | 72 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006769 | 0.006155 | 24 | 8.866e-07 | 9.55e-09 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006494 | 1.921e-05 | 9520 | 0 | 1.213e-06 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006467 | 0.0121 | 13 | 4.674e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06725 | 0.04585 | 3 | 1.417e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06446 | 0.05009 | 2 | 0.006416 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04968 | 0.008637 | 16 | 9.452e-06 | 1.39e-09 | 428 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04785 | 0.005943 | 18 | 0.0002424 | 6.296e-06 | 258 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03736 | 0.0536 | 1 | 0.9037 | 0 | 1114 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen3-8B-Base | 0.03013 | 0.0396 | 5 | 2.564e-14 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 7 | google-bert/bert-base-uncased | 0.03013 | 0.01168 | 13 | 2.217e-58 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02853 | 0.02051 | 8 | 9.882e-13 | 2.516e-17 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.0222 | 2.917e-05 | 998 | 1.013e-08 | 9.275e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02039 | 0.02925 | 7 | 6.155e-18 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01791 | 0.01966 | 9 | 1.714e-15 | 6.04e-21 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01286 | 0.04066 | 4 | 1.386e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.0119 | 0.03531 | 6 | 9.332e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01004 | 0.0001902 | 123 | 2.589e-07 | 2.378e-07 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008653 | 0.005934 | 19 | 1.378e-07 | 1.39e-09 | 267 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008059 | 0.01729 | 10 | 5.843e-08 | 9.157e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006949 | 0.0007442 | 54 | 2.508e-07 | 1.352e-10 | 72 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006802 | 0.00389 | 22 | 2.296e-07 | 1.39e-09 | 191 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006498 | 2.555e-05 | 8773 | 0 | 2.378e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006496 | 0.01619 | 11 | 6.821e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001286 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001286 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001286 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 68, 'modularity': 0.9342523477892765, 'largest': 1317, 'weighted_purity': 0.9998233527645293, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1317 | 1317 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1336 | 279 | 315 | 435 | 301 | permissive |
| 1 | 1148 | 1148 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1165 | 334 | 319 | 464 | 48 | restricted |
| 2 | 1062 | 1062 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B | 1182 | 316 | 307 | 315 | 244 | permissive |
| 3 | 1021 | 1021 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1032 | 313 | 319 | 353 | 47 | restricted |
| 4 | 927 | 927 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 938 | 299 | 301 | 300 | 38 | permissive |
| 5 | 909 | 909 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 919 | 300 | 300 | 300 | 19 | restricted |
| 6 | 856 | 856 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 881 | 308 | 302 | 205 | 66 | restricted |
| 7 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 8 | 695 | 695 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 705 | 345 | 165 | 164 | 29 | permissive |
| 9 | 627 | 627 | Qwen/Qwen2.5-7B | 0.9952 | 3 | Qwen/Qwen2.5-7B-Instruct | 700 | 160 | 102 | 222 | 216 | permissive |
| 10 | 565 | 565 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 645 | 120 | 128 | 178 | 219 | permissive |
| 11 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 12 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 13 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 14 | 487 | 487 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 486 | 300 | 46 | 140 | 0 | permissive |
| 15 | 469 | 469 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 548 | 103 | 74 | 176 | 195 | restricted |
| 16 | 441 | 441 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 441 | 319 | 30 | 90 | 2 | unknown |
| 17 | 437 | 437 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 436 | 123 | 287 | 22 | 4 | restricted |
| 18 | 429 | 429 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-Coder-7B | 465 | 195 | 84 | 74 | 112 | permissive |
| 19 | 411 | 411 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 470 | 68 | 126 | 133 | 143 | restricted |
| 20 | 310 | 310 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 309 | 253 | 18 | 38 | 0 | permissive |
| 21 | 295 | 295 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 310 | 39 | 108 | 70 | 93 | permissive |
| 22 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 23 | 184 | 184 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 183 | 61 | 61 | 61 | 0 | permissive |
| 24 | 140 | 140 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 139 | 35 | 35 | 31 | 38 | permissive |
| 25 | 132 | 132 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 133 | 65 | 21 | 30 | 17 | permissive |
| 26 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 27 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 28 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 29 | 91 | 91 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 91 | 36 | 40 | 9 | 6 | permissive |
| 30 | 83 | 83 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 82 | 61 | 16 | 5 | 0 | permissive |
| 31 | 81 | 81 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 80 | 61 | 3 | 13 | 3 | unknown |
| 32 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 33 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 34 | 64 | 64 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-alpha | 63 | 14 | 33 | 14 | 2 | permissive |
| 35 | 52 | 52 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/mistral-7b-sft-beta | 51 | 34 | 14 | 3 | 0 | permissive |
| 36 | 40 | 40 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 39 | 23 | 9 | 7 | 0 | permissive |
| 37 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 38 | 34 | 34 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mlabonne/Daredevil-7B | 33 | 8 | 0 | 15 | 10 | permissive |
| 39 | 31 | 31 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-Guard-3-8B | 30 | 6 | 3 | 21 | 0 | restricted |

*… 28 more rows in the CSV*

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

max generation 18, mean generation of derived models 1.69, models per generation {0: 10, 1: 6481, 2: 9950, 3: 351, 4: 106, 5: 24, 6: 9, 7: 8, 8: 8, 9: 3, 10: 2, 11: 3, 12: 3, 13: 3, 14: 5, 15: 7, 16: 4, 17: 3, 18: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 674.6 | 13485 | 6952 | 1184 | 664 |
| 1 | 6481 | 756 | 0.1168 | 5.324 | 0 | 7302 | 1.615 | 15458 | 12620 | 4997 | 1371 |
| 2 | 9950 | 1217 | 0.1224 | 2.385 | 0 | 5360 | 0.05307 | 14126 | 4737 | 3654 | 1188 |
| 3 | 351 | 143 | 0.4121 | 1.176 | 0 | 15 | 0.3419 | 13 | 4 | 270 | 121 |
| 4 | 106 | 38 | 0.3585 | 1.198 | 0 | 9 | 0.2547 | 5 | 1 | 69 | 52 |
| 5 | 24 | 10 | 0.4167 | 1.542 | 0 | 10 | 0.4583 | 0 | 0 | 24 | 13 |
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
| finetune | 43088 | 6694 | 0.5311 | 0.3727 |
| adapter | 24314 | 4370 | 0.2997 | 0.2433 |
| quantized | 10251 | 4579 | 0.1263 | 0.255 |
| merge | 3479 | 2317 | 0.04288 | 0.129 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 9054 |
| child_unknown | 4792 |
| loosened | 2019 |
| changed_same_category | 776 |
| parent_unknown | 542 |
| changed_custom | 511 |
| tightened | 290 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 4 |
| noncommercial | 0 | 73 | 1 | 6 | 3 | 66 |
| other | 0 | 2 | 69 | 13 | 0 | 24 |
| permissive | 24 | 100 | 246 | 6222 | 90 | 2731 |
| restricted | 18 | 76 | 249 | 1992 | 3464 | 1967 |
| unknown | 0 | 1 | 3 | 41 | 9 | 488 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 69 | 86 | 1092 | 0 | 219 | 1290 | 18 | 2774 | 0.1183 | 0 |
| Qwen/Qwen3-8B-Base | 58 | 94 | 390 | 0 | 67 | 1460 | 26 | 2095 | 0.1087 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 120 | 1 | 535 | 536 | 15 | 636 | 34 | 1877 | 0.5207 | 0.4039 |
| google/gemma-3-4b-pt | 29 | 0 | 446 | 345 | 10 | 688 | 23 | 1541 | 0.3659 | 0.318 |
| meta-llama/Llama-3.1-8B | 61 | 128 | 762 | 452 | 141 | 1225 | 35 | 2804 | 0.3556 | 0.2378 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 317 | 680 | 32 | 1010 | 3 | 2101 | 0.4235 | 0.3881 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 53 | 156 | 862 | 6 | 43 | 1743 | 72 | 2935 | 0.1414 | 0.002956 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 199 | 183 | 1620 | 192 | 21 | 2091 | 64 | 4370 | 0.2338 | 0.07036 |
| finetune | 174 | 380 | 1253 | 1302 | 113 | 3323 | 149 | 6694 | 0.3763 | 0.2444 |
| merge | 28 | 81 | 1490 | 64 | 195 | 406 | 53 | 2317 | 0.3576 | 0.1013 |
| quantized | 105 | 132 | 426 | 461 | 213 | 3218 | 24 | 4579 | 0.1832 | 0.117 |
| unknown | 5 | 0 | 3 | 0 | 0 | 16 | 0 | 24 | 0.2381 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
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
| CSLin3303/20241204 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |

*… 1979 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 329 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 772 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 369 |
| 2024-Q3 | 113 | 0 | 0 | 26 | 430 | 0 | 450 | 30 | 33 | 115 |
| 2024-Q4 | 344 | 0 | 0 | 45 | 384 | 0 | 429 | 422 | 25 | 285 |
| 2025-Q1 | 576 | 0 | 457 | 62 | 235 | 132 | 538 | 487 | 27 | 280 |
| 2025-Q2 | 327 | 284 | 25 | 63 | 221 | 250 | 290 | 429 | 76 | 178 |
| 2025-Q3 | 266 | 256 | 30 | 49 | 74 | 203 | 187 | 206 | 53 | 211 |
| 2025-Q4 | 84 | 200 | 2 | 49 | 81 | 178 | 124 | 159 | 53 | 36 |
| 2026-Q1 | 163 | 218 | 12 | 28 | 112 | 278 | 110 | 56 | 23 | 56 |
| 2026-Q2 | 174 | 380 | 2 | 21 | 210 | 281 | 165 | 197 | 11 | 33 |
| 2026-Q3 | 252 | 490 | 10 | 65 | 56 | 147 | 216 | 51 | 7 | 21 |
| 2026-Q4 | 73 | 230 | 0 | 36 | 12 | 54 | 47 | 9 | 4 | 20 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 6 | 368 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 5 | 9 | 977 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 590 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 19 | 9 | 1155 | 0 |
| 2024-Q4 | 0 | 13 | 1 | 46 | 23 | 1846 | 5 |
| 2025-Q1 | 9 | 15 | 104 | 150 | 141 | 2359 | 16 |
| 2025-Q2 | 10 | 14 | 212 | 57 | 83 | 1761 | 6 |
| 2025-Q3 | 8 | 21 | 175 | 48 | 34 | 1249 | 0 |
| 2025-Q4 | 12 | 19 | 136 | 46 | 36 | 712 | 5 |
| 2026-Q1 | 25 | 10 | 122 | 64 | 20 | 738 | 77 |
| 2026-Q2 | 31 | 8 | 92 | 40 | 17 | 1272 | 14 |
| 2026-Q3 | 23 | 6 | 71 | 49 | 56 | 1106 | 4 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 24 | 396 | 1 |

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
| 2023-Q4 | 148 | 140 | 6 | 0 | 90 |
| 2024-Q1 | 332 | 291 | 220 | 16 | 144 |
| 2024-Q2 | 163 | 229 | 121 | 3 | 107 |
| 2024-Q3 | 168 | 419 | 74 | 0 | 536 |
| 2024-Q4 | 322 | 688 | 158 | 0 | 766 |
| 2025-Q1 | 758 | 980 | 281 | 0 | 775 |
| 2025-Q2 | 305 | 1067 | 138 | 0 | 633 |
| 2025-Q3 | 364 | 628 | 213 | 0 | 330 |
| 2025-Q4 | 246 | 459 | 32 | 0 | 229 |
| 2026-Q1 | 374 | 385 | 26 | 0 | 271 |
| 2026-Q2 | 505 | 596 | 37 | 8 | 328 |
| 2026-Q3 | 519 | 527 | 19 | 3 | 247 |
| 2026-Q4 | 153 | 229 | 20 | 3 | 80 |

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
| 2023-Q4 | 0.385 | 0.365 | 0.016 | 0 | 0.234 |
| 2024-Q1 | 0.331 | 0.29 | 0.219 | 0.016 | 0.144 |
| 2024-Q2 | 0.262 | 0.368 | 0.194 | 0.005 | 0.172 |
| 2024-Q3 | 0.14 | 0.35 | 0.062 | 0 | 0.448 |
| 2024-Q4 | 0.166 | 0.356 | 0.082 | 0 | 0.396 |
| 2025-Q1 | 0.271 | 0.351 | 0.101 | 0 | 0.277 |
| 2025-Q2 | 0.142 | 0.498 | 0.064 | 0 | 0.295 |
| 2025-Q3 | 0.237 | 0.409 | 0.139 | 0 | 0.215 |
| 2025-Q4 | 0.255 | 0.475 | 0.033 | 0 | 0.237 |
| 2026-Q1 | 0.354 | 0.365 | 0.025 | 0 | 0.257 |
| 2026-Q2 | 0.343 | 0.404 | 0.025 | 0.005 | 0.223 |
| 2026-Q3 | 0.395 | 0.401 | 0.014 | 0.002 | 0.188 |
| 2026-Q4 | 0.315 | 0.472 | 0.041 | 0.006 | 0.165 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 17001 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 4579 | 26.9 % |
| missing pipeline_tag (as published) | 6813 | 40.1 % |
|   of which filled from parent | 6812 | see pipeline_tag_source |
| missing library_name | 2563 | 15.1 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 21163 |  |
|   linked by HF | 19638 | 92.8 % |
|   old name of a renamed repo | 973 | 4.6 % |
|   not linked (broken parent link) | 552 | 2.6 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 17486 | 100.0 % of 17486 |
| tag edges to a parent outside the sample | 2762 | 13.3 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 98.7% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 86% |
