# Mining results

Generated 2026-10-27 08:21 UTC from 16011 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 15996 | 22524 |
| nodes_in_sample | 15996 | 15996 |
| edges | 16961 | 25452 |
| relations | {'finetune': 6331, 'adapter': 4046, 'quantized': 4370, 'merge': 2190, 'unknown': 24} | {'finetune': 8498, 'adapter': 6610, 'quantized': 5214, 'merge': 5101, 'unknown': 29} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 9418 | 20439 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 700 |
| leaves | 15002 | 20795 |
| multi_parent_nodes | 580 | 1350 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 64 | 3.667e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 7.541e-10 | 20 | 1 |  |
| HITS authority | 161 | 3.458e-10 | 20 | 0.9099 | 0.9348 |
| HITS hub | 161 | 3.509e-13 | 20 | 0.999 | 0.9348 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 75 | 1.075e-09 | 20 | 1 |  |
| Weighted PageRank | 53 | 7.212e-10 | 20 | 1 |  |
| HITS authority | 178 | 1.6e-10 | 20 | 0.9799 | 0.94 |
| HITS hub | 178 | 4.349e-13 | 20 | 0.9992 | 0.94 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.0668 | 0.04551 | 3 | 5.555e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.0637 | 0.05869 | 2 | 0.001954 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04966 | 0.01703 | 8 | 3.102e-05 | 9.334e-09 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04755 | 0.01579 | 9 | 0.0002672 | 3.283e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03532 | 0.06735 | 1 | 0.4708 | 0 | 1115 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03019 | 0.008537 | 18 | 1.927e-71 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02986 | 0.0293 | 5 | 5.176e-13 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02824 | 0.01512 | 10 | 3.272e-11 | 8.697e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02228 | 2.038e-05 | 1683 | 6.952e-07 | 5.211e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02046 | 0.02196 | 7 | 1.195e-26 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01797 | 0.01475 | 11 | 3.329e-24 | 2.008e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01252 | 0.02968 | 4 | 7.11e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01182 | 0.0263 | 6 | 2.467e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01005 | 9.073e-05 | 209 | 2.178e-07 | 4.49e-07 | 22 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008613 | 0.004736 | 27 | 4.34e-07 | 9.334e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008026 | 0.01282 | 12 | 1.168e-08 | 4.145e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.00696 | 0.0004936 | 60 | 1.377e-06 | 7.292e-10 | 68 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006779 | 0.006148 | 25 | 8.667e-07 | 9.334e-09 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006524 | 1.921e-05 | 9500 | 0 | 4.49e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006496 | 0.01209 | 13 | 4.597e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06736 | 0.04378 | 3 | 1.15e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06447 | 0.04815 | 2 | 0.006425 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04969 | 0.005741 | 17 | 7.721e-06 | 1.128e-09 | 275 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04778 | 0.004428 | 19 | 0.0002212 | 6.304e-06 | 175 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.0374 | 0.05169 | 1 | 0.9055 | 0 | 1114 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03027 | 0.01249 | 13 | 2.232e-58 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03005 | 0.03947 | 5 | 6.32e-26 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02839 | 0.01855 | 9 | 1.598e-24 | 6.202e-29 | 793 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.0223 | 3.119e-05 | 989 | 8.235e-09 | 7.576e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02049 | 0.03128 | 7 | 6.196e-18 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01799 | 0.02102 | 8 | 1.726e-15 | 6.08e-21 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01292 | 0.04349 | 4 | 1.395e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01195 | 0.03753 | 6 | 9.345e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01008 | 0.0001918 | 128 | 2.094e-07 | 2.171e-07 | 22 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008671 | 0.005045 | 18 | 1.049e-07 | 1.128e-09 | 213 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008096 | 0.01831 | 10 | 5.709e-08 | 9.169e-09 | 785 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.00698 | 0.0007398 | 54 | 1.738e-07 | 1.029e-10 | 68 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006815 | 0.003122 | 22 | 1.703e-07 | 1.128e-09 | 146 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006528 | 2.732e-05 | 8765 | 0 | 2.171e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006525 | 0.01732 | 11 | 5.563e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.00129 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.00129 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.00129 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 68, 'modularity': 0.9321128995191774, 'largest': 1325, 'weighted_purity': 0.9998124531132783, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1325 | 1325 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1344 | 280 | 315 | 441 | 302 | permissive |
| 1 | 1147 | 1147 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1162 | 336 | 319 | 467 | 40 | restricted |
| 2 | 1021 | 1021 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1032 | 313 | 319 | 353 | 47 | restricted |
| 3 | 1013 | 1013 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B | 1119 | 315 | 307 | 283 | 214 | permissive |
| 4 | 909 | 909 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 919 | 300 | 300 | 300 | 19 | restricted |
| 5 | 848 | 848 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 873 | 304 | 298 | 205 | 66 | restricted |
| 6 | 781 | 781 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 791 | 251 | 252 | 251 | 37 | permissive |
| 7 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 8 | 695 | 695 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 705 | 345 | 165 | 164 | 29 | permissive |
| 9 | 653 | 653 | Qwen/Qwen2.5-7B | 0.9954 | 3 | Qwen/Qwen2.5-7B-Instruct | 762 | 169 | 130 | 186 | 277 | permissive |
| 10 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 11 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 12 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 13 | 483 | 483 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 482 | 296 | 46 | 140 | 0 | permissive |
| 14 | 441 | 441 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 513 | 88 | 92 | 151 | 182 | permissive |
| 15 | 437 | 437 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 436 | 123 | 287 | 22 | 4 | restricted |
| 16 | 420 | 420 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 420 | 317 | 30 | 71 | 2 | unknown |
| 17 | 404 | 404 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 483 | 79 | 49 | 161 | 194 | restricted |
| 18 | 331 | 331 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 389 | 65 | 78 | 113 | 133 | restricted |
| 19 | 310 | 310 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 309 | 253 | 18 | 38 | 0 | permissive |
| 20 | 225 | 225 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 239 | 38 | 47 | 67 | 87 | permissive |
| 21 | 183 | 183 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B-Instruct-1M | 193 | 52 | 3 | 81 | 57 | permissive |
| 22 | 166 | 166 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 165 | 119 | 6 | 40 | 0 | permissive |
| 23 | 133 | 133 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 134 | 62 | 21 | 32 | 19 | permissive |
| 24 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 25 | 112 | 112 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 111 | 37 | 37 | 37 | 0 | permissive |
| 26 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 27 | 102 | 102 | meta-llama/Llama-3.2-1B | 1 | 1 | dphn/Dolphin3.0-Llama3.2-1B | 134 | 6 | 2 | 29 | 97 | restricted |
| 28 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 29 | 91 | 91 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 90 | 21 | 21 | 21 | 27 | permissive |
| 30 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 31 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 32 | 63 | 63 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 63 | 22 | 26 | 9 | 6 | permissive |
| 33 | 59 | 59 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 58 | 37 | 16 | 5 | 0 | permissive |
| 34 | 57 | 57 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 56 | 37 | 3 | 13 | 3 | unknown |
| 35 | 52 | 52 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-alpha | 51 | 14 | 21 | 14 | 2 | permissive |
| 36 | 49 | 49 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Genstruct-7B | 48 | 9 | 20 | 18 | 1 | unknown |
| 37 | 40 | 40 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 39 | 23 | 9 | 7 | 0 | permissive |
| 38 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 39 | 39 | 39 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/mistral-7b-sft-beta | 38 | 21 | 14 | 3 | 0 | permissive |

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

max generation 18, mean generation of derived models 1.67, models per generation {0: 10, 1: 6481, 2: 8981, 3: 341, 4: 104, 5: 22, 6: 8, 7: 6, 8: 7, 9: 3, 10: 2, 11: 3, 12: 3, 13: 3, 14: 5, 15: 7, 16: 4, 17: 3, 18: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 674.6 | 13485 | 6952 | 1184 | 664 |
| 1 | 6481 | 756 | 0.1168 | 5.324 | 0 | 7302 | 1.462 | 15458 | 12620 | 4997 | 1371 |
| 2 | 8981 | 1097 | 0.1223 | 2.609 | 0 | 5360 | 0.05645 | 14043 | 4719 | 3478 | 1169 |
| 3 | 341 | 137 | 0.4065 | 1.184 | 0 | 15 | 0.3431 | 12 | 4 | 263 | 120 |
| 4 | 104 | 37 | 0.3558 | 1.173 | 0 | 9 | 0.2404 | 5 | 1 | 66 | 50 |
| 5 | 22 | 11 | 0.5 | 1.818 | 0.5 | 10 | 0.4545 | 0 | 0 | 26 | 14 |
| 6 | 8 | 5 | 0.625 | 2.5 | 2 | 8 | 1.5 | 1 | 0 | 11 | 8 |
| 7 | 6 | 2 | 0.3333 | 3.5 | 0 | 14 | 3 | 0 | 0 | 3 | 18 |
| 8 | 7 | 5 | 0.7143 | 1.714 | 1 | 5 | 0.8571 | 0 | 0 | 8 | 4 |
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
| finetune | 43004 | 6331 | 0.5322 | 0.3738 |
| adapter | 24296 | 4046 | 0.3007 | 0.2389 |
| quantized | 10062 | 4370 | 0.1245 | 0.258 |
| merge | 3446 | 2190 | 0.04264 | 0.1293 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 8521 |
| child_unknown | 4482 |
| loosened | 1935 |
| changed_same_category | 731 |
| parent_unknown | 531 |
| changed_custom | 480 |
| tightened | 281 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 1 |
| noncommercial | 0 | 73 | 1 | 4 | 3 | 66 |
| other | 0 | 2 | 69 | 13 | 0 | 24 |
| permissive | 24 | 94 | 225 | 5746 | 89 | 2519 |
| restricted | 18 | 74 | 239 | 1910 | 3362 | 1872 |
| unknown | 0 | 0 | 3 | 40 | 9 | 479 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 58 | 73 | 994 | 0 | 211 | 1139 | 13 | 2488 | 0.1122 | 0 |
| Qwen/Qwen3-8B-Base | 53 | 85 | 365 | 0 | 67 | 1353 | 25 | 1948 | 0.1075 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 117 | 1 | 531 | 531 | 15 | 636 | 34 | 1865 | 0.5178 | 0.4026 |
| google/gemma-3-4b-pt | 29 | 0 | 446 | 345 | 10 | 688 | 23 | 1541 | 0.3659 | 0.318 |
| meta-llama/Llama-3.1-8B | 54 | 115 | 672 | 375 | 141 | 1136 | 33 | 2526 | 0.3368 | 0.2189 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 317 | 680 | 32 | 1010 | 3 | 2101 | 0.4235 | 0.3881 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 48 | 146 | 769 | 4 | 40 | 1557 | 71 | 2635 | 0.1473 | 0.002191 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 191 | 178 | 1513 | 184 | 21 | 1900 | 59 | 4046 | 0.2436 | 0.07325 |
| finetune | 163 | 365 | 1154 | 1258 | 113 | 3132 | 146 | 6331 | 0.3815 | 0.2484 |
| merge | 28 | 79 | 1408 | 62 | 184 | 376 | 53 | 2190 | 0.3712 | 0.1037 |
| quantized | 93 | 109 | 404 | 431 | 213 | 3097 | 23 | 4370 | 0.1748 | 0.1148 |
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

*… 1895 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 307 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 692 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 303 |
| 2024-Q3 | 108 | 0 | 0 | 26 | 430 | 0 | 404 | 30 | 33 | 107 |
| 2024-Q4 | 328 | 0 | 0 | 45 | 384 | 0 | 379 | 422 | 25 | 263 |
| 2025-Q1 | 532 | 0 | 457 | 62 | 231 | 132 | 487 | 487 | 27 | 229 |
| 2025-Q2 | 281 | 272 | 25 | 63 | 221 | 250 | 277 | 429 | 76 | 162 |
| 2025-Q3 | 239 | 240 | 30 | 49 | 74 | 203 | 140 | 206 | 53 | 199 |
| 2025-Q4 | 75 | 188 | 2 | 49 | 81 | 178 | 119 | 159 | 53 | 31 |
| 2026-Q1 | 135 | 196 | 12 | 28 | 109 | 278 | 90 | 56 | 23 | 55 |
| 2026-Q2 | 152 | 359 | 2 | 21 | 205 | 281 | 157 | 197 | 11 | 31 |
| 2026-Q3 | 198 | 446 | 10 | 65 | 56 | 147 | 190 | 51 | 7 | 21 |
| 2026-Q4 | 56 | 211 | 0 | 36 | 12 | 54 | 38 | 9 | 4 | 19 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 6 | 346 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 4 | 9 | 898 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 524 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 18 | 9 | 1097 | 0 |
| 2024-Q4 | 0 | 13 | 1 | 45 | 23 | 1759 | 5 |
| 2025-Q1 | 9 | 15 | 104 | 148 | 140 | 2212 | 16 |
| 2025-Q2 | 10 | 14 | 212 | 56 | 83 | 1675 | 6 |
| 2025-Q3 | 7 | 21 | 175 | 46 | 34 | 1150 | 0 |
| 2025-Q4 | 12 | 19 | 136 | 45 | 36 | 682 | 5 |
| 2026-Q1 | 24 | 10 | 122 | 56 | 19 | 674 | 77 |
| 2026-Q2 | 31 | 8 | 92 | 40 | 16 | 1216 | 13 |
| 2026-Q3 | 23 | 6 | 71 | 48 | 55 | 984 | 4 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 24 | 350 | 1 |

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
| 2023-Q4 | 134 | 135 | 6 | 0 | 87 |
| 2024-Q1 | 304 | 275 | 196 | 16 | 132 |
| 2024-Q2 | 145 | 208 | 98 | 3 | 103 |
| 2024-Q3 | 161 | 410 | 70 | 0 | 497 |
| 2024-Q4 | 287 | 668 | 148 | 0 | 743 |
| 2025-Q1 | 692 | 928 | 265 | 0 | 759 |
| 2025-Q2 | 290 | 1024 | 132 | 0 | 610 |
| 2025-Q3 | 344 | 558 | 213 | 0 | 318 |
| 2025-Q4 | 235 | 447 | 31 | 0 | 222 |
| 2026-Q1 | 345 | 359 | 22 | 0 | 256 |
| 2026-Q2 | 487 | 573 | 35 | 8 | 313 |
| 2026-Q3 | 474 | 479 | 18 | 3 | 217 |
| 2026-Q4 | 135 | 211 | 20 | 3 | 70 |

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
| 2023-Q4 | 0.37 | 0.373 | 0.017 | 0 | 0.24 |
| 2024-Q1 | 0.329 | 0.298 | 0.212 | 0.017 | 0.143 |
| 2024-Q2 | 0.26 | 0.373 | 0.176 | 0.005 | 0.185 |
| 2024-Q3 | 0.141 | 0.36 | 0.062 | 0 | 0.437 |
| 2024-Q4 | 0.155 | 0.362 | 0.08 | 0 | 0.402 |
| 2025-Q1 | 0.262 | 0.351 | 0.1 | 0 | 0.287 |
| 2025-Q2 | 0.141 | 0.498 | 0.064 | 0 | 0.297 |
| 2025-Q3 | 0.24 | 0.389 | 0.149 | 0 | 0.222 |
| 2025-Q4 | 0.251 | 0.478 | 0.033 | 0 | 0.237 |
| 2026-Q1 | 0.351 | 0.366 | 0.022 | 0 | 0.261 |
| 2026-Q2 | 0.344 | 0.405 | 0.025 | 0.006 | 0.221 |
| 2026-Q3 | 0.398 | 0.402 | 0.015 | 0.003 | 0.182 |
| 2026-Q4 | 0.308 | 0.481 | 0.046 | 0.007 | 0.159 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 16011 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 4280 | 26.7 % |
| missing pipeline_tag (as published) | 6440 | 40.2 % |
|   of which filled from parent | 6439 | see pipeline_tag_source |
| missing library_name | 2431 | 15.2 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 20017 |  |
|   linked by HF | 18547 | 92.7 % |
|   old name of a renamed repo | 931 | 4.7 % |
|   not linked (broken parent link) | 539 | 2.7 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 16492 | 100.0 % of 16492 |
| tag edges to a parent outside the sample | 2653 | 13.5 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.5% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 94% |
