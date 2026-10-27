# Mining results

Generated 2026-10-27 10:52 UTC from 19020 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 18991 | 22577 |
| nodes_in_sample | 18991 | 18991 |
| edges | 20144 | 25832 |
| relations | {'finetune': 7498, 'adapter': 5078, 'quantized': 4908, 'merge': 2635, 'unknown': 25} | {'finetune': 8499, 'adapter': 6619, 'quantized': 5214, 'merge': 5470, 'unknown': 30} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 12267 | 20492 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 753 |
| leaves | 17956 | 20788 |
| multi_parent_nodes | 660 | 1616 |
| temporal_anomaly_edges | 24 | 24 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 72 | 6.08e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 1.117e-09 | 20 | 1 |  |
| HITS authority | 160 | 3.455e-10 | 20 | 0.922 | 0.9341 |
| HITS hub | 160 | 3.413e-13 | 20 | 0.9994 | 0.9341 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 74 | 2.799e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 8.935e-10 | 20 | 1 |  |
| HITS authority | 176 | 1.605e-10 | 20 | 0.9811 | 0.9394 |
| HITS hub | 176 | 4.343e-13 | 20 | 0.9993 | 0.9394 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06681 | 0.04515 | 3 | 2.176e-05 | 0 | 825 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06368 | 0.05831 | 2 | 0.001967 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04996 | 0.01647 | 8 | 0.0001605 | 3.65e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04781 | 0.01537 | 9 | 0.0007234 | 3.3e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03488 | 0.06637 | 1 | 0.4663 | 0 | 1118 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.02977 | 0.008541 | 18 | 6.801e-71 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02966 | 0.02931 | 5 | 1.984e-12 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02811 | 0.01513 | 10 | 1.261e-10 | 3.327e-15 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02198 | 2.039e-05 | 1743 | 1.248e-06 | 2.693e-07 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02017 | 0.02197 | 7 | 1.243e-26 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01772 | 0.01476 | 11 | 3.46e-24 | 2.084e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01235 | 0.0297 | 4 | 1.833e-09 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01165 | 0.02631 | 6 | 2.472e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009904 | 9.895e-05 | 202 | 2.924e-07 | 1.214e-06 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008501 | 0.004834 | 27 | 2.157e-06 | 3.65e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.007914 | 0.01283 | 12 | 1.16e-08 | 4.147e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006845 | 0.0006053 | 53 | 6.884e-06 | 3.617e-09 | 82 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006781 | 0.006167 | 24 | 4.297e-06 | 3.65e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006433 | 1.922e-05 | 9558 | 0 | 1.214e-06 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006406 | 0.0121 | 13 | 8.158e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06737 | 0.05114 | 3 | 5.081e-06 | 0 | 825 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06451 | 0.05509 | 2 | 0.006258 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05029 | 0.01728 | 10 | 3.253e-05 | 4.983e-09 | 916 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.0482 | 0.0104 | 13 | 0.0003391 | 6.138e-06 | 518 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03726 | 0.05828 | 1 | 0.8964 | 0 | 1117 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | Qwen/Qwen3-8B-Base | 0.02983 | 0.03495 | 5 | 1.92e-14 | 0 | 515 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 7 | google-bert/bert-base-uncased | 0.02983 | 0.01031 | 15 | 3.189e-58 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02824 | 0.0181 | 8 | 7.4e-13 | 1.883e-17 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02197 | 2.574e-05 | 1023 | 3.551e-08 | 3.191e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02019 | 0.02581 | 7 | 4.794e-18 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01773 | 0.01735 | 9 | 1.335e-15 | 4.702e-21 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01274 | 0.03588 | 4 | 1.096e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01178 | 0.03116 | 6 | 9.061e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.009934 | 0.000164 | 127 | 5.533e-07 | 3.326e-07 | 23 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008551 | 0.00578 | 21 | 5.026e-07 | 4.983e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.007978 | 0.01526 | 11 | 5.619e-08 | 8.887e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.006858 | 0.0007369 | 52 | 1.495e-06 | 4.929e-10 | 82 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006803 | 0.006306 | 19 | 9.491e-07 | 4.983e-09 | 341 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006433 | 2.255e-05 | 8804 | 0 | 3.326e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.00643 | 0.01429 | 12 | 2.35e-07 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001277 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001277 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001277 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 65, 'modularity': 0.9358972822209086, 'largest': 1359, 'weighted_purity': 0.9998946869569796, 'multi_family_communities': 2}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1359 | 1359 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1379 | 290 | 322 | 455 | 305 | permissive |
| 1 | 1157 | 1157 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1174 | 335 | 319 | 472 | 48 | restricted |
| 2 | 1021 | 1021 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1032 | 313 | 319 | 353 | 47 | restricted |
| 3 | 1015 | 1015 | Qwen/Qwen2.5-7B | 0.999 | 2 | Qwen/Qwen2.5-7B | 1113 | 311 | 307 | 271 | 223 | permissive |
| 4 | 934 | 934 | Qwen/Qwen2.5-7B | 0.9989 | 2 | Qwen/Qwen2.5-7B-Instruct | 1035 | 252 | 248 | 310 | 225 | permissive |
| 5 | 927 | 927 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 938 | 299 | 301 | 300 | 38 | permissive |
| 6 | 909 | 909 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 919 | 300 | 300 | 300 | 19 | restricted |
| 7 | 856 | 856 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 881 | 308 | 302 | 205 | 66 | restricted |
| 8 | 736 | 736 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 740 | 321 | 301 | 103 | 14 | permissive |
| 9 | 713 | 713 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 723 | 348 | 178 | 166 | 29 | permissive |
| 10 | 606 | 606 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-Math-7B | 646 | 370 | 84 | 75 | 117 | unknown |
| 11 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 12 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 13 | 536 | 536 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 607 | 130 | 139 | 152 | 186 | permissive |
| 14 | 519 | 519 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 529 | 136 | 134 | 157 | 102 | restricted |
| 15 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 16 | 487 | 487 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 486 | 300 | 46 | 140 | 0 | permissive |
| 17 | 467 | 467 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 467 | 342 | 33 | 90 | 2 | unknown |
| 18 | 437 | 437 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 436 | 123 | 287 | 22 | 4 | restricted |
| 19 | 374 | 374 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 383 | 59 | 145 | 118 | 61 | restricted |
| 20 | 374 | 374 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-Storm-8B | 499 | 43 | 149 | 94 | 213 | restricted |
| 21 | 357 | 357 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B-Instruct-1M | 388 | 122 | 24 | 132 | 110 | permissive |
| 22 | 344 | 344 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 343 | 141 | 61 | 141 | 0 | permissive |
| 23 | 337 | 337 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 342 | 28 | 166 | 44 | 104 | permissive |
| 24 | 310 | 310 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 309 | 253 | 18 | 38 | 0 | permissive |
| 25 | 281 | 281 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 280 | 80 | 80 | 47 | 73 | permissive |
| 26 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 27 | 236 | 236 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 235 | 80 | 80 | 31 | 44 | permissive |
| 28 | 182 | 182 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 182 | 82 | 85 | 9 | 6 | permissive |
| 29 | 161 | 161 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 160 | 141 | 3 | 13 | 3 | unknown |
| 30 | 135 | 135 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Genstruct-7B | 141 | 11 | 79 | 26 | 25 | permissive |
| 31 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 32 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 33 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 34 | 98 | 98 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/mistral-7b-sft-beta | 97 | 80 | 14 | 3 | 0 | permissive |
| 35 | 94 | 94 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 93 | 72 | 16 | 5 | 0 | permissive |
| 36 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 37 | 76 | 76 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-alpha | 75 | 14 | 43 | 14 | 4 | permissive |
| 38 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 39 | 40 | 40 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 39 | 23 | 9 | 7 | 0 | permissive |

*… 25 more rows in the CSV*

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

max generation 18, mean generation of derived models 1.73, models per generation {0: 10, 1: 6476, 2: 11887, 3: 401, 4: 131, 5: 25, 6: 9, 7: 8, 8: 8, 9: 3, 10: 2, 11: 3, 12: 3, 13: 3, 14: 5, 15: 7, 16: 4, 17: 3, 18: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 675 | 13485 | 6952 | 1184 | 664 |
| 1 | 6476 | 751 | 0.1162 | 5.325 | 0 | 7302 | 1.923 | 15458 | 12620 | 4987 | 1359 |
| 2 | 11887 | 1424 | 0.1199 | 2.052 | 0 | 5360 | 0.05586 | 14212 | 4762 | 4002 | 1400 |
| 3 | 401 | 172 | 0.4332 | 1.232 | 0 | 15 | 0.3741 | 13 | 6 | 331 | 139 |
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
| finetune | 43174 | 7498 | 0.5271 | 0.3727 |
| adapter | 24341 | 5078 | 0.2972 | 0.2524 |
| quantized | 10672 | 4908 | 0.1303 | 0.2439 |
| merge | 3718 | 2635 | 0.04539 | 0.131 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 10121 |
| child_unknown | 5571 |
| loosened | 2218 |
| changed_same_category | 815 |
| changed_custom | 551 |
| parent_unknown | 548 |
| tightened | 320 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 4 |
| noncommercial | 0 | 73 | 1 | 7 | 3 | 84 |
| other | 0 | 2 | 69 | 18 | 1 | 68 |
| permissive | 28 | 113 | 270 | 7041 | 94 | 3259 |
| restricted | 20 | 85 | 259 | 2188 | 3751 | 2156 |
| unknown | 0 | 1 | 3 | 41 | 9 | 494 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 95 | 111 | 1447 | 1 | 221 | 1627 | 38 | 3540 | 0.1309 | 0.0005342 |
| Qwen/Qwen3-8B-Base | 58 | 94 | 390 | 0 | 67 | 1460 | 26 | 2095 | 0.1087 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 120 | 1 | 535 | 536 | 15 | 636 | 34 | 1877 | 0.5207 | 0.4039 |
| google/gemma-3-4b-pt | 29 | 0 | 446 | 345 | 10 | 688 | 23 | 1541 | 0.3659 | 0.318 |
| meta-llama/Llama-3.1-8B | 74 | 132 | 964 | 650 | 144 | 1508 | 44 | 3516 | 0.3738 | 0.2699 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 317 | 680 | 32 | 1010 | 3 | 2101 | 0.4235 | 0.3881 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 54 | 166 | 1084 | 6 | 44 | 2190 | 73 | 3617 | 0.1201 | 0.002411 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 205 | 196 | 1789 | 202 | 23 | 2593 | 70 | 5078 | 0.2061 | 0.06185 |
| finetune | 185 | 400 | 1561 | 1399 | 114 | 3672 | 167 | 7498 | 0.3694 | 0.2403 |
| merge | 36 | 83 | 1770 | 66 | 198 | 427 | 55 | 2635 | 0.3598 | 0.09895 |
| quantized | 119 | 136 | 448 | 551 | 213 | 3413 | 28 | 4908 | 0.1964 | 0.1297 |
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

*… 2178 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 405 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 842 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 531 |
| 2024-Q3 | 124 | 0 | 0 | 26 | 430 | 0 | 584 | 30 | 33 | 154 |
| 2024-Q4 | 401 | 0 | 0 | 45 | 384 | 0 | 536 | 422 | 25 | 342 |
| 2025-Q1 | 677 | 0 | 457 | 62 | 235 | 132 | 680 | 487 | 27 | 434 |
| 2025-Q2 | 417 | 284 | 25 | 63 | 221 | 250 | 315 | 429 | 76 | 243 |
| 2025-Q3 | 345 | 256 | 30 | 49 | 74 | 203 | 212 | 206 | 53 | 237 |
| 2025-Q4 | 107 | 200 | 2 | 49 | 81 | 178 | 144 | 159 | 53 | 49 |
| 2026-Q1 | 228 | 218 | 12 | 28 | 112 | 278 | 188 | 56 | 23 | 61 |
| 2026-Q2 | 239 | 380 | 2 | 21 | 210 | 281 | 228 | 197 | 11 | 36 |
| 2026-Q3 | 394 | 490 | 10 | 65 | 56 | 147 | 268 | 51 | 7 | 25 |
| 2026-Q4 | 103 | 230 | 0 | 36 | 12 | 54 | 71 | 9 | 4 | 20 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 6 | 444 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 5 | 9 | 1047 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 752 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 21 | 10 | 1336 | 0 |
| 2024-Q4 | 1 | 13 | 1 | 47 | 23 | 2065 | 5 |
| 2025-Q1 | 10 | 15 | 105 | 153 | 142 | 2750 | 16 |
| 2025-Q2 | 10 | 14 | 212 | 63 | 84 | 1934 | 6 |
| 2025-Q3 | 8 | 21 | 175 | 49 | 34 | 1378 | 0 |
| 2025-Q4 | 12 | 19 | 136 | 52 | 36 | 762 | 5 |
| 2026-Q1 | 25 | 10 | 123 | 64 | 21 | 884 | 77 |
| 2026-Q2 | 31 | 8 | 93 | 40 | 18 | 1401 | 14 |
| 2026-Q3 | 23 | 6 | 71 | 50 | 57 | 1302 | 4 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 24 | 450 | 1 |

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
| 2023-Q4 | 191 | 171 | 6 | 0 | 92 |
| 2024-Q1 | 377 | 307 | 228 | 16 | 145 |
| 2024-Q2 | 210 | 283 | 180 | 3 | 109 |
| 2024-Q3 | 190 | 496 | 87 | 0 | 608 |
| 2024-Q4 | 408 | 747 | 165 | 0 | 835 |
| 2025-Q1 | 990 | 1114 | 288 | 0 | 799 |
| 2025-Q2 | 351 | 1170 | 144 | 0 | 658 |
| 2025-Q3 | 395 | 715 | 217 | 0 | 338 |
| 2025-Q4 | 255 | 492 | 35 | 0 | 240 |
| 2026-Q1 | 400 | 449 | 57 | 1 | 297 |
| 2026-Q2 | 534 | 638 | 62 | 8 | 363 |
| 2026-Q3 | 578 | 616 | 26 | 4 | 289 |
| 2026-Q4 | 183 | 242 | 20 | 3 | 91 |

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
| 2023-Q4 | 0.415 | 0.372 | 0.013 | 0 | 0.2 |
| 2024-Q1 | 0.351 | 0.286 | 0.212 | 0.015 | 0.135 |
| 2024-Q2 | 0.268 | 0.361 | 0.229 | 0.004 | 0.139 |
| 2024-Q3 | 0.138 | 0.359 | 0.063 | 0 | 0.44 |
| 2024-Q4 | 0.189 | 0.347 | 0.077 | 0 | 0.387 |
| 2025-Q1 | 0.31 | 0.349 | 0.09 | 0 | 0.25 |
| 2025-Q2 | 0.151 | 0.504 | 0.062 | 0 | 0.283 |
| 2025-Q3 | 0.237 | 0.429 | 0.13 | 0 | 0.203 |
| 2025-Q4 | 0.25 | 0.481 | 0.034 | 0 | 0.235 |
| 2026-Q1 | 0.332 | 0.373 | 0.047 | 0.001 | 0.247 |
| 2026-Q2 | 0.333 | 0.398 | 0.039 | 0.005 | 0.226 |
| 2026-Q3 | 0.382 | 0.407 | 0.017 | 0.003 | 0.191 |
| 2026-Q4 | 0.34 | 0.449 | 0.037 | 0.006 | 0.169 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 19020 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 5230 | 27.5 % |
| missing pipeline_tag (as published) | 7697 | 40.5 % |
|   of which filled from parent | 7696 | see pipeline_tag_source |
| missing library_name | 2795 | 14.7 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 23421 |  |
|   linked by HF | 21744 | 92.8 % |
|   old name of a renamed repo | 1116 | 4.8 % |
|   not linked (broken parent link) | 561 | 2.4 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 19507 | 100.0 % of 19507 |
| tag edges to a parent outside the sample | 2851 | 12.4 % |
| child created >7 days before its parent | 24 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 98.5% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 84% |
