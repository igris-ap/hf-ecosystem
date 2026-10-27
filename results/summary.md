# Mining results

Generated 2026-10-27 10:02 UTC from 18023 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 18000 | 22564 |
| nodes_in_sample | 18000 | 18000 |
| edges | 19054 | 25764 |
| relations | {'finetune': 7089, 'adapter': 4712, 'quantized': 4743, 'merge': 2485, 'unknown': 25} | {'finetune': 8499, 'adapter': 6613, 'quantized': 5214, 'merge': 5408, 'unknown': 30} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 11276 | 20479 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 740 |
| leaves | 16981 | 20788 |
| multi_parent_nodes | 633 | 1559 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 70 | 2.551e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 1.016e-09 | 20 | 1 |  |
| HITS authority | 159 | 3.271e-10 | 20 | 0.9381 | 0.9337 |
| HITS hub | 159 | 3.318e-13 | 20 | 0.9994 | 0.9337 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 74 | 8.066e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 8.185e-10 | 20 | 1 |  |
| HITS authority | 176 | 1.574e-10 | 20 | 0.9809 | 0.9394 |
| HITS hub | 176 | 4.255e-13 | 20 | 0.9993 | 0.9394 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06664 | 0.04517 | 3 | 9.196e-06 | 0 | 825 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06364 | 0.05836 | 2 | 0.001969 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04962 | 0.01651 | 8 | 5.045e-05 | 1.542e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04764 | 0.01544 | 9 | 0.0007183 | 3.302e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03507 | 0.06668 | 1 | 0.4669 | 0 | 1118 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.02993 | 0.00854 | 18 | 6.878e-71 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02982 | 0.02931 | 5 | 8.386e-13 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02827 | 0.01513 | 10 | 5.33e-11 | 1.406e-15 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02209 | 2.039e-05 | 1730 | 1.132e-06 | 8.46e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02028 | 0.02197 | 7 | 1.257e-26 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01782 | 0.01476 | 11 | 3.5e-24 | 2.107e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01242 | 0.02969 | 4 | 1.82e-09 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01172 | 0.02631 | 6 | 2.475e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009957 | 9.894e-05 | 202 | 2.919e-07 | 1.205e-06 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008553 | 0.004815 | 27 | 7.102e-07 | 1.542e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.007957 | 0.01283 | 12 | 1.161e-08 | 4.15e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006889 | 0.0005834 | 54 | 2.756e-06 | 1.191e-09 | 79 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006799 | 0.006162 | 24 | 1.41e-06 | 1.542e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006468 | 1.922e-05 | 9545 | 0 | 1.205e-06 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006441 | 0.0121 | 13 | 7.458e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06727 | 0.04864 | 3 | 2.165e-06 | 0 | 825 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06449 | 0.05288 | 2 | 0.006258 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04978 | 0.01284 | 12 | 1.409e-05 | 2.124e-09 | 665 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04801 | 0.008495 | 17 | 0.0002812 | 6.138e-06 | 397 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03737 | 0.05616 | 1 | 0.899 | 0 | 1117 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen3-8B-Base | 0.03 | 0.03711 | 5 | 2.308e-14 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 7 | google-bert/bert-base-uncased | 0.03 | 0.01094 | 14 | 7.362e-58 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02841 | 0.01922 | 8 | 8.894e-13 | 2.264e-17 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.0221 | 2.733e-05 | 1007 | 1.519e-08 | 1.382e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02031 | 0.02741 | 7 | 5.994e-18 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01783 | 0.01842 | 9 | 1.669e-15 | 5.879e-21 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01281 | 0.0381 | 4 | 1.392e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01185 | 0.03309 | 6 | 9.061e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009992 | 0.0001783 | 123 | 2.596e-07 | 2.758e-07 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008612 | 0.006127 | 19 | 2.136e-07 | 2.124e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008024 | 0.0162 | 10 | 5.619e-08 | 8.887e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006907 | 0.0007616 | 52 | 4.739e-07 | 2.095e-10 | 79 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006829 | 0.005013 | 21 | 3.696e-07 | 2.124e-09 | 258 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.00647 | 2.394e-05 | 8788 | 0 | 2.758e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006467 | 0.01518 | 11 | 1.013e-07 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001278 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001278 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001278 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 62, 'modularity': 0.9357943124505165, 'largest': 1350, 'weighted_purity': 0.9998333333333334, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1350 | 1350 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1370 | 287 | 317 | 454 | 305 | permissive |
| 1 | 1157 | 1157 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1174 | 335 | 319 | 472 | 48 | restricted |
| 2 | 1106 | 1106 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B | 1240 | 330 | 307 | 323 | 280 | permissive |
| 3 | 1021 | 1021 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1032 | 313 | 319 | 353 | 47 | restricted |
| 4 | 927 | 927 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 938 | 299 | 301 | 300 | 38 | permissive |
| 5 | 909 | 909 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 919 | 300 | 300 | 300 | 19 | restricted |
| 6 | 880 | 880 | Qwen/Qwen2.5-7B | 0.9966 | 3 | Qwen/Qwen2.5-7B-Instruct | 968 | 221 | 184 | 303 | 260 | permissive |
| 7 | 856 | 856 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 881 | 308 | 302 | 205 | 66 | restricted |
| 8 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 9 | 713 | 713 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 723 | 348 | 178 | 166 | 29 | permissive |
| 10 | 570 | 570 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 657 | 133 | 106 | 194 | 224 | restricted |
| 11 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 12 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 13 | 521 | 521 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-Coder-7B | 557 | 287 | 84 | 74 | 112 | unknown |
| 14 | 518 | 518 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 594 | 111 | 119 | 156 | 208 | permissive |
| 15 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 16 | 495 | 495 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 555 | 68 | 204 | 134 | 149 | restricted |
| 17 | 487 | 487 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 486 | 300 | 46 | 140 | 0 | permissive |
| 18 | 467 | 467 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 467 | 342 | 33 | 90 | 2 | unknown |
| 19 | 437 | 437 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 436 | 123 | 287 | 22 | 4 | restricted |
| 20 | 379 | 379 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 395 | 39 | 174 | 70 | 112 | permissive |
| 21 | 310 | 310 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 309 | 253 | 18 | 38 | 0 | permissive |
| 22 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 23 | 262 | 262 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 261 | 100 | 61 | 100 | 0 | permissive |
| 24 | 244 | 244 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 243 | 64 | 56 | 62 | 61 | permissive |
| 25 | 188 | 188 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 187 | 56 | 56 | 31 | 44 | permissive |
| 26 | 135 | 135 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 135 | 58 | 62 | 9 | 6 | permissive |
| 27 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 28 | 120 | 120 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 119 | 100 | 3 | 13 | 3 | unknown |
| 29 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 30 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 31 | 94 | 94 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 93 | 72 | 16 | 5 | 0 | permissive |
| 32 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 33 | 74 | 74 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-alpha | 73 | 14 | 43 | 14 | 2 | permissive |
| 34 | 74 | 74 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/mistral-7b-sft-beta | 73 | 56 | 14 | 3 | 0 | permissive |
| 35 | 72 | 72 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 71 | 58 | 6 | 7 | 0 | permissive |
| 36 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 37 | 40 | 40 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 39 | 23 | 9 | 7 | 0 | permissive |
| 38 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 39 | 32 | 32 | meta-llama/Llama-3.1-8B | 1 | 1 | fdtn-ai/Foundation-Sec-8B | 31 | 8 | 3 | 17 | 3 | permissive |

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

## 3. Lineage

max generation 18, mean generation of derived models 1.71, models per generation {0: 10, 1: 6481, 2: 10941, 3: 371, 4: 112, 5: 24, 6: 9, 7: 8, 8: 8, 9: 3, 10: 2, 11: 3, 12: 3, 13: 3, 14: 5, 15: 7, 16: 4, 17: 3, 18: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 675 | 13485 | 6952 | 1184 | 664 |
| 1 | 6481 | 756 | 0.1168 | 5.324 | 0 | 7302 | 1.772 | 15458 | 12620 | 4997 | 1371 |
| 2 | 10941 | 1324 | 0.1211 | 2.194 | 0 | 5360 | 0.05191 | 14170 | 4745 | 3814 | 1261 |
| 3 | 371 | 156 | 0.4251 | 1.204 | 0 | 15 | 0.3396 | 13 | 6 | 301 | 122 |
| 4 | 112 | 40 | 0.3571 | 1.161 | 0 | 9 | 0.2411 | 5 | 1 | 71 | 53 |
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
| finetune | 43132 | 7089 | 0.5295 | 0.3725 |
| adapter | 24324 | 4712 | 0.2986 | 0.2476 |
| quantized | 10444 | 4743 | 0.1282 | 0.2493 |
| merge | 3554 | 2485 | 0.04363 | 0.1306 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 9572 |
| child_unknown | 5183 |
| loosened | 2119 |
| changed_same_category | 794 |
| parent_unknown | 548 |
| changed_custom | 528 |
| tightened | 310 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 4 |
| noncommercial | 0 | 73 | 1 | 6 | 3 | 67 |
| other | 0 | 2 | 69 | 13 | 0 | 31 |
| permissive | 27 | 109 | 258 | 6623 | 94 | 2994 |
| restricted | 19 | 80 | 254 | 2091 | 3599 | 2087 |
| unknown | 0 | 1 | 3 | 41 | 9 | 494 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 80 | 96 | 1251 | 0 | 221 | 1452 | 33 | 3133 | 0.1258 | 0 |
| Qwen/Qwen3-8B-Base | 58 | 94 | 390 | 0 | 67 | 1460 | 26 | 2095 | 0.1087 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 120 | 1 | 535 | 536 | 15 | 636 | 34 | 1877 | 0.5207 | 0.4039 |
| google/gemma-3-4b-pt | 29 | 0 | 446 | 345 | 10 | 688 | 23 | 1541 | 0.3659 | 0.318 |
| meta-llama/Llama-3.1-8B | 66 | 129 | 875 | 552 | 144 | 1359 | 39 | 3164 | 0.3664 | 0.2573 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 317 | 680 | 32 | 1010 | 3 | 2101 | 0.4235 | 0.3881 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 54 | 163 | 981 | 6 | 44 | 1965 | 73 | 3286 | 0.1309 | 0.002654 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 204 | 188 | 1697 | 198 | 23 | 2334 | 68 | 4712 | 0.2199 | 0.06618 |
| finetune | 179 | 391 | 1407 | 1352 | 114 | 3484 | 162 | 7089 | 0.3743 | 0.2428 |
| merge | 28 | 82 | 1636 | 64 | 198 | 422 | 55 | 2485 | 0.3518 | 0.09831 |
| quantized | 111 | 133 | 440 | 505 | 213 | 3316 | 25 | 4743 | 0.1892 | 0.1235 |
| unknown | 6 | 0 | 3 | 0 | 0 | 16 | 0 | 25 | 0.2727 | 0 |

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

*… 2079 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 368 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 810 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 448 |
| 2024-Q3 | 117 | 0 | 0 | 26 | 430 | 0 | 513 | 30 | 33 | 133 |
| 2024-Q4 | 365 | 0 | 0 | 45 | 384 | 0 | 483 | 422 | 25 | 316 |
| 2025-Q1 | 629 | 0 | 457 | 62 | 235 | 132 | 610 | 487 | 27 | 359 |
| 2025-Q2 | 364 | 284 | 25 | 63 | 221 | 250 | 296 | 429 | 76 | 209 |
| 2025-Q3 | 294 | 256 | 30 | 49 | 74 | 203 | 203 | 206 | 53 | 222 |
| 2025-Q4 | 95 | 200 | 2 | 49 | 81 | 178 | 135 | 159 | 53 | 42 |
| 2026-Q1 | 198 | 218 | 12 | 28 | 112 | 278 | 170 | 56 | 23 | 61 |
| 2026-Q2 | 212 | 380 | 2 | 21 | 210 | 281 | 188 | 197 | 11 | 35 |
| 2026-Q3 | 338 | 490 | 10 | 65 | 56 | 147 | 243 | 51 | 7 | 25 |
| 2026-Q4 | 89 | 230 | 0 | 36 | 12 | 54 | 60 | 9 | 4 | 20 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 6 | 407 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 5 | 9 | 1015 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 669 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 21 | 10 | 1237 | 0 |
| 2024-Q4 | 0 | 13 | 1 | 47 | 23 | 1951 | 5 |
| 2025-Q1 | 9 | 15 | 105 | 152 | 141 | 2560 | 16 |
| 2025-Q2 | 10 | 14 | 212 | 62 | 84 | 1829 | 6 |
| 2025-Q3 | 8 | 21 | 175 | 48 | 34 | 1304 | 0 |
| 2025-Q4 | 12 | 19 | 136 | 49 | 36 | 737 | 5 |
| 2026-Q1 | 25 | 10 | 122 | 64 | 20 | 838 | 77 |
| 2026-Q2 | 31 | 8 | 93 | 40 | 18 | 1333 | 14 |
| 2026-Q3 | 23 | 6 | 71 | 50 | 56 | 1222 | 4 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 24 | 425 | 1 |

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
| 2023-Q4 | 171 | 154 | 6 | 0 | 92 |
| 2024-Q1 | 354 | 300 | 226 | 16 | 145 |
| 2024-Q2 | 183 | 260 | 147 | 3 | 109 |
| 2024-Q3 | 175 | 456 | 82 | 0 | 569 |
| 2024-Q4 | 366 | 715 | 162 | 0 | 797 |
| 2025-Q1 | 876 | 1051 | 288 | 0 | 783 |
| 2025-Q2 | 320 | 1107 | 142 | 0 | 648 |
| 2025-Q3 | 377 | 664 | 216 | 0 | 333 |
| 2025-Q4 | 253 | 472 | 35 | 0 | 234 |
| 2026-Q1 | 387 | 429 | 56 | 1 | 283 |
| 2026-Q2 | 518 | 605 | 61 | 8 | 345 |
| 2026-Q3 | 552 | 582 | 23 | 4 | 271 |
| 2026-Q4 | 164 | 237 | 20 | 3 | 90 |

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
| 2023-Q4 | 0.404 | 0.364 | 0.014 | 0 | 0.217 |
| 2024-Q1 | 0.34 | 0.288 | 0.217 | 0.015 | 0.139 |
| 2024-Q2 | 0.261 | 0.37 | 0.209 | 0.004 | 0.155 |
| 2024-Q3 | 0.137 | 0.356 | 0.064 | 0 | 0.444 |
| 2024-Q4 | 0.179 | 0.35 | 0.079 | 0 | 0.391 |
| 2025-Q1 | 0.292 | 0.351 | 0.096 | 0 | 0.261 |
| 2025-Q2 | 0.144 | 0.499 | 0.064 | 0 | 0.292 |
| 2025-Q3 | 0.237 | 0.418 | 0.136 | 0 | 0.209 |
| 2025-Q4 | 0.255 | 0.475 | 0.035 | 0 | 0.235 |
| 2026-Q1 | 0.335 | 0.371 | 0.048 | 0.001 | 0.245 |
| 2026-Q2 | 0.337 | 0.394 | 0.04 | 0.005 | 0.224 |
| 2026-Q3 | 0.385 | 0.406 | 0.016 | 0.003 | 0.189 |
| 2026-Q4 | 0.319 | 0.461 | 0.039 | 0.006 | 0.175 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 18023 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 4929 | 27.3 % |
| missing pipeline_tag (as published) | 7247 | 40.2 % |
|   of which filled from parent | 7246 | see pipeline_tag_source |
| missing library_name | 2673 | 14.8 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 22358 |  |
|   linked by HF | 20761 | 92.9 % |
|   old name of a renamed repo | 1040 | 4.7 % |
|   not linked (broken parent link) | 557 | 2.5 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 18510 | 100.0 % of 18510 |
| tag edges to a parent outside the sample | 2882 | 13.1 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 98.9% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 88% |
