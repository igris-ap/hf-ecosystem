# Mining results

Generated 2026-10-27 06:40 UTC from 14000 scraped models (scraped 2026-10-26 to 2026-10-27; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 13989 | 22480 |
| nodes_in_sample | 13989 | 13989 |
| edges | 14830 | 25214 |
| relations | {'finetune': 5532, 'adapter': 3418, 'quantized': 3935, 'merge': 1924, 'unknown': 21} | {'finetune': 8498, 'adapter': 6606, 'quantized': 5213, 'merge': 4871, 'unknown': 26} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 8035 | 20395 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 656 |
| leaves | 13022 | 20816 |
| multi_parent_nodes | 503 | 1225 |
| temporal_anomaly_edges | 23 | 23 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 56 | 2.459e-10 | 20 | 1 |  |
| Weighted PageRank | 54 | 4.362e-10 | 20 | 1 |  |
| HITS authority | 164 | 3.566e-10 | 20 | 0.9039 | 0.936 |
| HITS hub | 164 | 3.608e-13 | 20 | 0.9983 | 0.936 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 76 | 1.309e-09 | 20 | 1 |  |
| Weighted PageRank | 53 | 8.666e-10 | 20 | 1 |  |
| HITS authority | 181 | 1.659e-10 | 20 | 0.9783 | 0.9411 |
| HITS hub | 181 | 4.546e-13 | 20 | 0.9992 | 0.9411 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06718 | 0.04566 | 3 | 5.702e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06364 | 0.05898 | 2 | 0.001988 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.0499 | 0.01718 | 8 | 3.197e-05 | 9.603e-09 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04726 | 0.01593 | 9 | 0.000275 | 3.348e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03553 | 0.06778 | 1 | 0.4728 | 0 | 1112 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03049 | 0.008538 | 18 | 1.992e-72 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02976 | 0.0293 | 5 | 4.916e-13 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02806 | 0.01514 | 10 | 3.404e-11 | 8.279e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02251 | 2.038e-05 | 1618 | 7.021e-07 | 5.385e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02066 | 0.02196 | 7 | 7.726e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01815 | 0.01475 | 11 | 2.152e-24 | 1.301e-29 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01265 | 0.02969 | 4 | 7.399e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01191 | 0.02631 | 6 | 2.52e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01016 | 7.823e-05 | 250 | 1.924e-07 | 4.633e-07 | 18 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008656 | 0.00473 | 27 | 4.472e-07 | 9.603e-09 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008079 | 0.01284 | 12 | 1.201e-08 | 4.244e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.00704 | 0.0004651 | 63 | 1.314e-06 | 7.532e-10 | 64 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006819 | 0.006165 | 25 | 8.934e-07 | 9.603e-09 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.00659 | 1.922e-05 | 9436 | 0 | 4.633e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006562 | 0.0121 | 13 | 4.657e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06776 | 0.04353 | 4 | 1.051e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06431 | 0.04818 | 2 | 0.006604 | 0 | 972 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.04985 | 0.003791 | 18 | 7.038e-06 | 1.03e-09 | 166 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04736 | 0.002805 | 22 | 0.0002107 | 6.471e-06 | 98 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03749 | 0.05233 | 1 | 0.9109 | 0 | 1111 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03057 | 0.01455 | 12 | 2.995e-59 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.02995 | 0.03755 | 5 | 1.661e-55 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02821 | 0.0117 | 13 | 1.866e-56 | 1.627e-58 | 426 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02252 | 3.635e-05 | 967 | 7.509e-09 | 6.895e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02069 | 0.03353 | 7 | 1.088e-28 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01817 | 0.02106 | 8 | 2.339e-26 | 1.066e-31 | 776 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01305 | 0.04768 | 3 | 1.125e-16 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01205 | 0.03536 | 6 | 9.649e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01021 | 0.0002483 | 119 | 7.809e-08 | 2.064e-07 | 18 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008742 | 0.003232 | 20 | 6.166e-08 | 1.03e-09 | 108 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008145 | 0.01476 | 10 | 3.411e-08 | 9.454e-09 | 542 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007057 | 0.0008082 | 48 | 1.373e-07 | 6.041e-11 | 64 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006894 | 0.002541 | 24 | 1.181e-07 | 1.03e-09 | 95 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006594 | 3.184e-05 | 8739 | 0 | 2.064e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006591 | 0.02018 | 9 | 5.102e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

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

{'communities': 74, 'modularity': 0.9272419472838722, 'largest': 1412, 'weighted_purity': 0.9997855457859747, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1412 | 1412 | Qwen/Qwen2.5-7B | 0.9979 | 3 | Qwen/Qwen2.5-7B | 1683 | 408 | 381 | 411 | 483 | permissive |
| 1 | 1287 | 1287 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1304 | 275 | 307 | 426 | 290 | permissive |
| 2 | 1126 | 1126 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1141 | 328 | 320 | 452 | 41 | restricted |
| 3 | 1015 | 1015 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1024 | 312 | 317 | 352 | 43 | restricted |
| 4 | 782 | 782 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 792 | 258 | 258 | 257 | 19 | restricted |
| 5 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 6 | 656 | 656 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 664 | 341 | 162 | 144 | 16 | permissive |
| 7 | 605 | 605 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 630 | 184 | 181 | 199 | 66 | restricted |
| 8 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 9 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 10 | 497 | 497 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 500 | 318 | 72 | 99 | 11 | restricted |
| 11 | 453 | 453 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 459 | 131 | 132 | 150 | 46 | permissive |
| 12 | 420 | 420 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 420 | 317 | 30 | 71 | 2 | unknown |
| 13 | 364 | 364 | mistralai/Mistral-7B-v0.1 | 1 | 1 | teknium/OpenHermes-2.5-Mistral-7B | 424 | 62 | 74 | 136 | 152 | permissive |
| 14 | 362 | 362 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 361 | 175 | 46 | 140 | 0 | permissive |
| 15 | 355 | 355 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 354 | 123 | 205 | 22 | 4 | restricted |
| 16 | 269 | 269 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 344 | 42 | 26 | 110 | 166 | restricted |
| 17 | 268 | 268 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 300 | 125 | 8 | 70 | 97 | permissive |
| 18 | 262 | 262 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 261 | 205 | 18 | 38 | 0 | permissive |
| 19 | 229 | 229 | Qwen/Qwen2.5-7B | 1 | 1 | Qwen/Qwen2.5-7B-Instruct-1M | 242 | 60 | 24 | 82 | 76 | permissive |
| 20 | 206 | 206 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 235 | 45 | 37 | 66 | 87 | restricted |
| 21 | 151 | 151 | mistralai/Mistral-7B-v0.1 | 1 | 1 | NousResearch/Hermes-2-Pro-Mistral-7B | 161 | 29 | 25 | 50 | 57 | permissive |
| 22 | 125 | 125 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 124 | 112 | 8 | 4 | 0 | permissive |
| 23 | 109 | 109 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 108 | 46 | 18 | 44 | 0 | permissive |
| 24 | 98 | 98 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 97 | 81 | 11 | 5 | 0 | permissive |
| 25 | 76 | 76 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 75 | 72 | 1 | 2 | 0 | permissive |
| 26 | 65 | 65 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 64 | 9 | 6 | 49 | 0 | permissive |
| 27 | 51 | 51 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 50 | 17 | 17 | 16 | 0 | permissive |
| 28 | 46 | 46 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-Instruct-v0.1 | 45 | 10 | 10 | 10 | 15 | permissive |
| 29 | 41 | 41 | mistralai/Mistral-7B-v0.1 | 1 | 1 | alignment-handbook/zephyr-7b-sft-full | 41 | 11 | 15 | 9 | 6 | permissive |
| 30 | 40 | 40 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 39 | 23 | 9 | 7 | 0 | permissive |
| 31 | 40 | 40 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 39 | 39 | 0 | 0 | 0 | unknown |
| 32 | 39 | 39 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 38 | 17 | 16 | 5 | 0 | permissive |
| 33 | 37 | 37 | meta-llama/Llama-3.1-8B | 1 | 1 | NCSOFT/Llama-VARCO-8B-Instruct | 36 | 16 | 3 | 13 | 4 | unknown |
| 34 | 31 | 31 | Qwen/Qwen3-8B-Base | 1 | 1 | jackf857/qwen3-8b-base-sft-ultrachat-4xh200-batch-128 | 30 | 30 | 0 | 0 | 0 | unknown |
| 35 | 30 | 30 | meta-llama/Llama-3.1-8B | 1 | 1 | fdtn-ai/Foundation-Sec-8B | 29 | 8 | 3 | 16 | 2 | permissive |
| 36 | 27 | 27 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-Guard-3-8B | 26 | 6 | 3 | 17 | 0 | restricted |
| 37 | 27 | 27 | Qwen/Qwen2.5-7B | 1 | 1 | mehuldamani/qwen-base-verifier-sft-v1 | 26 | 26 | 0 | 0 | 0 | unknown |
| 38 | 27 | 27 | mistralai/Mistral-7B-v0.1 | 1 | 1 | danish-foundation-models/munin-7b-alpha | 28 | 5 | 4 | 4 | 15 | permissive |
| 39 | 26 | 26 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt | 25 | 22 | 3 | 0 | 0 | permissive |

*… 34 more rows in the CSV*

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

max generation 17, mean generation of derived models 1.61, models per generation {0: 10, 1: 6486, 2: 7026, 3: 310, 4: 94, 5: 19, 6: 6, 7: 3, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 5, 14: 7, 15: 4, 16: 3, 17: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 674.2 | 13485 | 6952 | 1184 | 664 |
| 1 | 6486 | 760 | 0.1174 | 5.321 | 0 | 7302 | 1.148 | 15458 | 12620 | 5005 | 1373 |
| 2 | 7026 | 896 | 0.1277 | 3.245 | 0 | 5360 | 0.06291 | 13907 | 4689 | 3099 | 1078 |
| 3 | 310 | 118 | 0.3856 | 1.085 | 0 | 14 | 0.3355 | 13 | 2 | 220 | 97 |
| 4 | 94 | 33 | 0.3511 | 1.202 | 0 | 9 | 0.2234 | 4 | 1 | 66 | 42 |
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
| finetune | 42867 | 5532 | 0.5353 | 0.3736 |
| adapter | 24264 | 3418 | 0.303 | 0.2308 |
| quantized | 9631 | 3935 | 0.1203 | 0.2657 |
| merge | 3312 | 1924 | 0.04136 | 0.1299 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 7563 |
| child_unknown | 3852 |
| loosened | 1627 |
| changed_same_category | 633 |
| parent_unknown | 519 |
| changed_custom | 390 |
| tightened | 246 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 1 |
| noncommercial | 0 | 73 | 1 | 4 | 3 | 66 |
| other | 0 | 2 | 69 | 11 | 0 | 24 |
| permissive | 18 | 83 | 192 | 5024 | 78 | 2184 |
| restricted | 14 | 67 | 184 | 1606 | 3028 | 1577 |
| unknown | 0 | 0 | 3 | 40 | 9 | 467 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 50 | 50 | 838 | 0 | 201 | 965 | 11 | 2115 | 0.1032 | 0 |
| Qwen/Qwen3-8B-Base | 41 | 58 | 308 | 0 | 67 | 1084 | 16 | 1574 | 0.09591 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 75 | 1 | 394 | 396 | 15 | 588 | 32 | 1501 | 0.4615 | 0.3626 |
| google/gemma-3-4b-pt | 26 | 0 | 400 | 332 | 10 | 626 | 20 | 1414 | 0.3765 | 0.3307 |
| meta-llama/Llama-3.1-8B | 44 | 92 | 560 | 266 | 141 | 1008 | 23 | 2134 | 0.2966 | 0.1856 |
| meta-llama/Llama-3.2-1B | 49 | 10 | 316 | 629 | 32 | 932 | 3 | 1971 | 0.4258 | 0.3876 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 33 | 121 | 648 | 4 | 38 | 1358 | 62 | 2264 | 0.1394 | 0.002535 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 135 | 162 | 1292 | 167 | 21 | 1595 | 46 | 3418 | 0.2423 | 0.07933 |
| finetune | 143 | 325 | 973 | 1010 | 111 | 2840 | 130 | 5532 | 0.3615 | 0.2271 |
| merge | 26 | 58 | 1231 | 55 | 174 | 329 | 51 | 1924 | 0.3661 | 0.106 |
| quantized | 82 | 88 | 353 | 395 | 213 | 2785 | 19 | 3935 | 0.1733 | 0.1172 |
| unknown | 4 | 0 | 3 | 0 | 0 | 14 | 0 | 21 | 0.2222 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 1-800-SHARED-TASKS/CHIPSAL-subtaskA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1-800-SHARED-TASKS/Kan_Gemma-2-9b-ChipsalSubtaskA-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 1024m/CHIPSAL-C-GEMMA2-9B-001-16bit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
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
| ChrisX123/Goemotion_GGUF_10000Instruction | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/Goemotion_GGUF_100Instruction | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| ChrisX123/Goemotion_GGUF_1Instruction | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| CogYB/CneoGET | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Cran-May/Apollo2-9B-Q5_K_M-GGUF | FreedomIntelligence/Apollo2-9B | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/gemma2-9b_law_with_val_1_epoch_callback_v3.7 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati_v1 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Deeokay/gemma2-9B-GGUF | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |

*… 1587 more rows in the CSV*

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
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 13 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 269 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 587 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 24 | 0 | 0 | 0 | 196 | 262 |
| 2024-Q3 | 102 | 0 | 0 | 26 | 392 | 0 | 337 | 30 | 33 | 95 |
| 2024-Q4 | 302 | 0 | 0 | 45 | 266 | 0 | 330 | 421 | 25 | 233 |
| 2025-Q1 | 455 | 0 | 457 | 62 | 190 | 131 | 400 | 421 | 27 | 181 |
| 2025-Q2 | 217 | 242 | 25 | 63 | 202 | 247 | 243 | 418 | 76 | 120 |
| 2025-Q3 | 203 | 213 | 30 | 49 | 49 | 199 | 115 | 204 | 53 | 187 |
| 2025-Q4 | 62 | 163 | 2 | 49 | 65 | 161 | 106 | 158 | 53 | 29 |
| 2026-Q1 | 113 | 149 | 12 | 28 | 87 | 245 | 69 | 56 | 23 | 53 |
| 2026-Q2 | 122 | 291 | 2 | 21 | 124 | 217 | 140 | 148 | 11 | 28 |
| 2026-Q3 | 161 | 337 | 10 | 65 | 52 | 142 | 167 | 51 | 7 | 18 |
| 2026-Q4 | 39 | 150 | 0 | 36 | 12 | 54 | 27 | 9 | 4 | 14 |

**trend_task_quarterly**

| quarter | feature-extraction | fill-mask | image-text-to-text | other | text-classification | text-generation | translation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 8 | 0 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 2022-Q4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 2 | 0 | 1 | 1 | 0 | 0 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 2023-Q3 | 0 | 2 | 0 | 5 | 2 | 13 | 0 |
| 2023-Q4 | 0 | 8 | 1 | 1 | 6 | 308 | 0 |
| 2024-Q1 | 1 | 11 | 0 | 4 | 8 | 794 | 0 |
| 2024-Q2 | 0 | 16 | 0 | 12 | 4 | 483 | 1 |
| 2024-Q3 | 1 | 10 | 3 | 18 | 9 | 974 | 0 |
| 2024-Q4 | 0 | 13 | 1 | 43 | 23 | 1537 | 5 |
| 2025-Q1 | 9 | 15 | 103 | 146 | 138 | 1897 | 16 |
| 2025-Q2 | 10 | 14 | 209 | 55 | 81 | 1478 | 6 |
| 2025-Q3 | 7 | 21 | 171 | 45 | 34 | 1024 | 0 |
| 2025-Q4 | 12 | 19 | 121 | 41 | 35 | 615 | 5 |
| 2026-Q1 | 22 | 10 | 99 | 47 | 19 | 564 | 74 |
| 2026-Q2 | 31 | 8 | 82 | 38 | 14 | 920 | 11 |
| 2026-Q3 | 22 | 6 | 70 | 44 | 54 | 811 | 3 |
| 2026-Q4 | 12 | 6 | 20 | 26 | 22 | 258 | 1 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 12 | 0 | 0 | 9 |
| 2023-Q4 | 113 | 125 | 4 | 0 | 82 |
| 2024-Q1 | 281 | 246 | 159 | 14 | 118 |
| 2024-Q2 | 136 | 198 | 82 | 3 | 97 |
| 2024-Q3 | 138 | 364 | 62 | 0 | 451 |
| 2024-Q4 | 248 | 530 | 138 | 0 | 706 |
| 2025-Q1 | 565 | 831 | 227 | 0 | 701 |
| 2025-Q2 | 248 | 938 | 109 | 0 | 558 |
| 2025-Q3 | 307 | 484 | 210 | 0 | 301 |
| 2025-Q4 | 215 | 396 | 31 | 0 | 206 |
| 2026-Q1 | 278 | 311 | 19 | 0 | 227 |
| 2026-Q2 | 372 | 457 | 31 | 7 | 237 |
| 2026-Q3 | 420 | 421 | 14 | 2 | 153 |
| 2026-Q4 | 86 | 178 | 20 | 3 | 58 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.045 | 0.545 | 0 | 0 | 0.409 |
| 2023-Q4 | 0.349 | 0.386 | 0.012 | 0 | 0.253 |
| 2024-Q1 | 0.344 | 0.301 | 0.194 | 0.017 | 0.144 |
| 2024-Q2 | 0.264 | 0.384 | 0.159 | 0.006 | 0.188 |
| 2024-Q3 | 0.136 | 0.359 | 0.061 | 0 | 0.444 |
| 2024-Q4 | 0.153 | 0.327 | 0.085 | 0 | 0.435 |
| 2025-Q1 | 0.243 | 0.358 | 0.098 | 0 | 0.302 |
| 2025-Q2 | 0.134 | 0.506 | 0.059 | 0 | 0.301 |
| 2025-Q3 | 0.236 | 0.372 | 0.161 | 0 | 0.231 |
| 2025-Q4 | 0.254 | 0.467 | 0.037 | 0 | 0.243 |
| 2026-Q1 | 0.333 | 0.372 | 0.023 | 0 | 0.272 |
| 2026-Q2 | 0.337 | 0.414 | 0.028 | 0.006 | 0.215 |
| 2026-Q3 | 0.416 | 0.417 | 0.014 | 0.002 | 0.151 |
| 2026-Q4 | 0.249 | 0.516 | 0.058 | 0.009 | 0.168 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 14000 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 3720 | 26.6 % |
| missing pipeline_tag (as published) | 5613 | 40.1 % |
|   of which filled from parent | 5612 | see pipeline_tag_source |
| missing library_name | 2158 | 15.4 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 17705 |  |
|   linked by HF | 16356 | 92.4 % |
|   old name of a renamed repo | 851 | 4.8 % |
|   not linked (broken parent link) | 498 | 2.8 % |
|   malformed (URL/path/free text) | 7 |  |
| listing edges confirmed by child's tags | 14449 | 100.0 % of 14449 |
| tag edges to a parent outside the sample | 2507 | 14.5 % |
| child created >7 days before its parent | 23 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.6% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 96% |
