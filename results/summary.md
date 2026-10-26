# Mining results

Generated 2026-10-26 17:12 UTC from 11005 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 10998 | 22404 |
| nodes_in_sample | 10998 | 10998 |
| edges | 11662 | 24839 |
| relations | {'finetune': 4337, 'adapter': 2666, 'quantized': 3075, 'merge': 1571, 'unknown': 13} | {'finetune': 8498, 'adapter': 6602, 'quantized': 5211, 'merge': 4510, 'unknown': 18} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 3 |
| largest_component | 6377 | 20320 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 580 |
| leaves | 10064 | 20837 |
| multi_parent_nodes | 397 | 1067 |
| temporal_anomaly_edges | 21 | 21 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 43 | 1.747e-10 | 20 | 1 |  |
| Weighted PageRank | 53 | 2.98e-10 | 20 | 1 |  |
| HITS authority | 171 | 3.976e-10 | 20 | 0.9424 | 0.9389 |
| HITS hub | 171 | 4.015e-13 | 20 | 0.9984 | 0.9389 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 77 | 9.615e-10 | 20 | 1 |  |
| Weighted PageRank | 52 | 1.031e-09 | 20 | 1 |  |
| HITS authority | 190 | 1.737e-10 | 20 | 0.99 | 0.9439 |
| HITS hub | 190 | 4.819e-13 | 20 | 0.9991 | 0.9439 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06839 | 0.04587 | 3 | 6.09e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06451 | 0.05929 | 2 | 0.002066 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.0509 | 0.0173 | 8 | 3.453e-05 | 1.028e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04766 | 0.01588 | 9 | 0.0002953 | 3.485e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03426 | 0.06834 | 1 | 0.4772 | 0 | 1104 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03142 | 0.008545 | 18 | 1.893e-75 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03009 | 0.02938 | 5 | 5.488e-13 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02825 | 0.01521 | 10 | 3.763e-11 | 9.26e-16 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.0232 | 2.04e-05 | 1535 | 7.176e-07 | 5.827e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02111 | 0.02199 | 7 | 1.793e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01849 | 0.01478 | 11 | 4.995e-25 | 3.026e-30 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01304 | 0.02972 | 4 | 8.177e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01214 | 0.02633 | 6 | 2.644e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01049 | 3.735e-05 | 669 | 8.954e-08 | 4.983e-07 | 6 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008797 | 0.004747 | 27 | 4.753e-07 | 1.028e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008168 | 0.01285 | 12 | 1.284e-08 | 4.462e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007261 | 0.0003662 | 71 | 1.144e-06 | 8.02e-10 | 51 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.006916 | 0.00617 | 25 | 9.689e-07 | 1.028e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006791 | 1.923e-05 | 9342 | 0 | 4.983e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006762 | 0.01211 | 13 | 4.797e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06897 | 0.04618 | 4 | 1.046e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06502 | 0.05131 | 2 | 0.007025 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05084 | 0.002261 | 20 | 6.902e-06 | 1.023e-09 | 79 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04769 | 0.001822 | 22 | 0.0002161 | 6.868e-06 | 55 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03596 | 0.05668 | 1 | 0.9202 | 0 | 1103 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.0315 | 0.0193 | 10 | 3.373e-61 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03027 | 0.03628 | 5 | 1.883e-57 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02837 | 0.004733 | 14 | 4.872e-59 | 1.842e-60 | 127 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02321 | 4.821e-05 | 934 | 7.369e-09 | 6.749e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02113 | 0.0309 | 7 | 8.953e-87 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01851 | 0.01203 | 11 | 1.354e-87 | 8.754e-90 | 333 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01345 | 0.04969 | 3 | 8.316e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01228 | 0.03341 | 6 | 1.039e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01052 | 0.0001379 | 331 | 4.262e-08 | 2.113e-07 | 6 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | Qwen/Qwen2.5-Coder-7B | 0.008866 | 0.001662 | 25 | 3.583e-08 | 1.023e-09 | 33 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 16 | google/gemma-2-9b-it | 0.008234 | 0.00934 | 12 | 2.47e-08 | 1.016e-08 | 257 | 1213 | google/gemma-2-9b | gemma | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007272 | 0.0008402 | 36 | 8.667e-08 | 3.504e-11 | 51 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.007008 | 0.001478 | 26 | 9.7e-08 | 1.023e-09 | 38 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006794 | 4.223e-05 | 8709 | 0 | 2.113e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006791 | 0.02677 | 8 | 5.085e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001316 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001316 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001316 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 78, 'modularity': 0.9125459797560399, 'largest': 1312, 'weighted_purity': 0.9997272231314784, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1312 | 1312 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1341 | 290 | 318 | 409 | 315 | permissive |
| 1 | 1258 | 1258 | Qwen/Qwen2.5-7B | 0.9976 | 3 | Qwen/Qwen2.5-7B | 1519 | 355 | 333 | 370 | 461 | permissive |
| 2 | 1251 | 1251 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1360 | 335 | 323 | 504 | 198 | restricted |
| 3 | 1008 | 1008 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1017 | 311 | 316 | 347 | 43 | restricted |
| 4 | 734 | 734 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 738 | 321 | 301 | 103 | 12 | permissive |
| 5 | 645 | 645 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 653 | 327 | 162 | 146 | 17 | permissive |
| 6 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 7 | 546 | 546 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 545 | 342 | 144 | 52 | 7 | permissive |
| 8 | 483 | 483 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 486 | 314 | 72 | 93 | 7 | restricted |
| 9 | 414 | 414 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 414 | 315 | 30 | 69 | 0 | unknown |
| 10 | 345 | 345 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 355 | 110 | 110 | 113 | 22 | restricted |
| 11 | 334 | 334 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 359 | 92 | 88 | 109 | 70 | restricted |
| 12 | 253 | 253 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 293 | 34 | 40 | 87 | 132 | permissive |
| 13 | 205 | 205 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 204 | 79 | 46 | 79 | 0 | permissive |
| 14 | 201 | 201 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 233 | 58 | 8 | 70 | 97 | permissive |
| 15 | 150 | 150 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B | 152 | 33 | 35 | 50 | 34 | permissive |
| 16 | 131 | 131 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 130 | 52 | 52 | 22 | 4 | permissive |
| 17 | 123 | 123 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 122 | 110 | 8 | 4 | 0 | permissive |
| 18 | 109 | 109 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 108 | 52 | 18 | 38 | 0 | permissive |
| 19 | 106 | 106 | meta-llama/Llama-3.1-8B | 1 | 1 | NousResearch/Hermes-3-Llama-3.1-8B | 116 | 24 | 16 | 29 | 47 | restricted |
| 20 | 81 | 81 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 80 | 31 | 18 | 31 | 0 | permissive |
| 21 | 48 | 48 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 47 | 31 | 11 | 5 | 0 | permissive |
| 22 | 47 | 47 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 46 | 9 | 6 | 31 | 0 | permissive |
| 23 | 35 | 35 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 34 | 31 | 1 | 2 | 0 | permissive |
| 24 | 32 | 32 | Qwen/Qwen3-8B-Base | 1 | 1 | OpenDataArena/Qwen3-8B-ODA-Math-460k | 31 | 31 | 0 | 0 | 0 | unknown |
| 25 | 31 | 31 | Qwen/Qwen3-8B-Base | 1 | 1 | jackf857/qwen3-8b-base-sft-ultrachat-4xh200-batch-128 | 30 | 30 | 0 | 0 | 0 | unknown |
| 26 | 26 | 26 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt | 25 | 22 | 3 | 0 | 0 | permissive |
| 27 | 24 | 24 | microsoft/phi-2 | 1 | 1 | ma921/phi-2-sft-golden-hh | 23 | 22 | 0 | 1 | 0 | permissive |
| 28 | 23 | 23 | google/gemma-3-4b-pt | 1 | 1 | google/medgemma-4b-pt | 22 | 16 | 1 | 5 | 0 | other |
| 29 | 21 | 21 | google/gemma-3-4b-pt | 1 | 1 | CEIA-UFG/Gemma-3-Gaia-PT-BR-4b-it | 20 | 1 | 0 | 19 | 0 | restricted |
| 30 | 18 | 18 | Qwen/Qwen3-8B-Base | 1 | 1 | McGill-NLP/AfriqueQwen-8B | 17 | 2 | 13 | 2 | 0 | permissive |
| 31 | 17 | 17 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mlabonne/Daredevil-7B | 16 | 5 | 0 | 6 | 5 | permissive |
| 32 | 16 | 16 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 15 | 5 | 5 | 5 | 0 | permissive |
| 33 | 16 | 16 | Qwen/Qwen2.5-7B | 1 | 1 | nbeerbower/EVA-abliterated-Qwen2.5-7B | 15 | 5 | 0 | 8 | 2 | permissive |
| 34 | 16 | 16 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B | 15 | 5 | 5 | 5 | 0 | permissive |
| 35 | 15 | 15 | Qwen/Qwen3-8B-Base | 1 | 1 | formalmathatepfl/qwen3-cpt | 14 | 14 | 0 | 0 | 0 | other |
| 36 | 15 | 15 | Qwen/Qwen2.5-7B | 1 | 1 | Tsunami-th/Tsunami-1.0-7B-Instruct | 14 | 2 | 0 | 8 | 4 | permissive |
| 37 | 14 | 14 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-Guard-3-8B | 13 | 5 | 3 | 5 | 0 | restricted |
| 38 | 14 | 14 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 13 | 5 | 4 | 4 | 0 | permissive |
| 39 | 14 | 14 | Qwen/Qwen2.5-7B | 1 | 1 | sail/Sailor2-8B | 13 | 5 | 3 | 5 | 0 | permissive |

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

max generation 17, mean generation of derived models 1.49, models per generation {0: 10, 1: 6489, 2: 4111, 3: 261, 4: 66, 5: 18, 6: 5, 7: 3, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 13: 5, 14: 7, 15: 4, 16: 3, 17: 3}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 673.3 | 13485 | 6952 | 1184 | 664 |
| 1 | 6489 | 763 | 0.1178 | 5.32 | 0 | 7302 | 0.6799 | 15459 | 12620 | 5010 | 1374 |
| 2 | 4111 | 586 | 0.1427 | 5.094 | 0 | 5360 | 0.08392 | 13411 | 4225 | 2394 | 892 |
| 3 | 261 | 79 | 0.3074 | 0.8794 | 0 | 14 | 0.2874 | 8 | 2 | 148 | 68 |
| 4 | 66 | 21 | 0.3182 | 1.091 | 0 | 8 | 0.303 | 3 | 1 | 46 | 22 |
| 5 | 18 | 8 | 0.4444 | 1.833 | 0 | 10 | 0.6111 | 0 | 0 | 20 | 13 |
| 6 | 5 | 2 | 0.4 | 3.6 | 0 | 14 | 2.8 | 0 | 0 | 5 | 13 |
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
| finetune | 42366 | 4337 | 0.5426 | 0.3723 |
| adapter | 23800 | 2666 | 0.3048 | 0.2289 |
| quantized | 8838 | 3075 | 0.1132 | 0.264 |
| merge | 3078 | 1571 | 0.03942 | 0.1349 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 6028 |
| child_unknown | 3126 |
| loosened | 985 |
| changed_same_category | 569 |
| parent_unknown | 472 |
| changed_custom | 285 |
| tightened | 197 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 1 |
| noncommercial | 0 | 52 | 0 | 3 | 3 | 51 |
| other | 0 | 2 | 67 | 7 | 0 | 21 |
| permissive | 17 | 64 | 148 | 4090 | 69 | 1817 |
| restricted | 12 | 47 | 128 | 967 | 2386 | 1236 |
| unknown | 0 | 0 | 3 | 35 | 8 | 426 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 36 | 32 | 677 | 0 | 159 | 756 | 6 | 1666 | 0.08916 | 0 |
| Qwen/Qwen3-8B-Base | 28 | 40 | 246 | 0 | 67 | 731 | 13 | 1125 | 0.09975 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 36 | 1 | 310 | 220 | 15 | 448 | 29 | 1059 | 0.3896 | 0.2997 |
| google/gemma-3-4b-pt | 21 | 0 | 281 | 230 | 10 | 423 | 4 | 969 | 0.3761 | 0.3392 |
| meta-llama/Llama-3.1-8B | 30 | 84 | 421 | 174 | 136 | 808 | 14 | 1667 | 0.2721 | 0.1568 |
| meta-llama/Llama-3.2-1B | 48 | 10 | 284 | 359 | 32 | 791 | 3 | 1527 | 0.3468 | 0.2964 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 14 | 101 | 519 | 2 | 38 | 1069 | 49 | 1792 | 0.1344 | 0.001619 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 80 | 148 | 1034 | 114 | 21 | 1232 | 37 | 2666 | 0.2353 | 0.07076 |
| finetune | 124 | 305 | 812 | 522 | 85 | 2384 | 105 | 4337 | 0.307 | 0.1517 |
| merge | 16 | 41 | 1013 | 49 | 153 | 260 | 39 | 1571 | 0.358 | 0.121 |
| quantized | 64 | 75 | 264 | 300 | 213 | 2143 | 16 | 3075 | 0.1751 | 0.1155 |
| unknown | 1 | 0 | 3 | 0 | 0 | 9 | 0 | 13 | 0.1 | 0 |

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
| AhmedSaghir/doc_model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| AlekseyCalvin/LYRICAL_MT_ru2en_TowerPlus9b | Unbabel/Tower-Plus-9B | finetune | google/gemma-2-9b | apache-2.0 | cc-by-nc-sa-4.0 |
| Alfaxad/gemma2-9b-swahili-it | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bharatdeep-H/portfolio-query-gemma-2-9b-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cannae-AI/TANIT-V0.5-Medium-9B-IT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| CerebrumTech/cere-gemma-2-9b-tr | google/gemma-2-9b-it | quantized | google/gemma-2-9b | mit | gemma |
| Cesarbasurto/FullNameSplit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cran-May/Apollo2-9B-Q5_K_M-GGUF | FreedomIntelligence/Apollo2-9B | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/gemma2-9b_law_with_val_1_epoch_callback_v3.7 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati_v1 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Deeokay/gemma2-9B-GGUF | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Denisijcu/Vertex-Core-Gemma | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Devavrat28/Gemmarathi2 | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| DiTy/gemma-2-9b-it-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| DiTy/gemma-2-9b-it-russian-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Diluzx/gemma-2-9b-bnb-4bit | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Erland/Gemma_Reward_Merged | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Futuresony/future_12_10_2024 | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| GeneroGral/Gemma2-9B_BBQ_Stereo_MERGED | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Goranii/gemma-2-9b-bnb-4bit-CPT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| HarisNarrendranR/model | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Himalayan-wildcat/gemma-2-9b-finetune | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| Hizaneko/gemma-2-9b-nyan100 | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Jaamie/gemma-mental-health-qlora | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |

*… 945 more rows in the CSV*

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
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 195 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 465 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 22 | 0 | 0 | 0 | 196 | 215 |
| 2024-Q3 | 87 | 0 | 0 | 26 | 254 | 0 | 274 | 29 | 33 | 74 |
| 2024-Q4 | 243 | 0 | 0 | 45 | 193 | 0 | 257 | 333 | 25 | 180 |
| 2025-Q1 | 366 | 0 | 457 | 62 | 101 | 108 | 312 | 316 | 27 | 139 |
| 2025-Q2 | 181 | 179 | 25 | 63 | 186 | 205 | 185 | 289 | 76 | 93 |
| 2025-Q3 | 159 | 149 | 30 | 49 | 35 | 162 | 97 | 188 | 53 | 181 |
| 2025-Q4 | 49 | 127 | 2 | 49 | 50 | 112 | 85 | 138 | 53 | 26 |
| 2026-Q1 | 74 | 105 | 12 | 28 | 70 | 140 | 54 | 52 | 23 | 40 |
| 2026-Q2 | 81 | 206 | 2 | 21 | 67 | 91 | 86 | 69 | 11 | 25 |
| 2026-Q3 | 129 | 237 | 10 | 65 | 33 | 87 | 147 | 49 | 7 | 17 |
| 2026-Q4 | 26 | 98 | 0 | 36 | 10 | 46 | 22 | 9 | 4 | 8 |

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
| 2023-Q4 | 0 | 8 | 1 | 1 | 0 | 6 | 234 |
| 2024-Q1 | 1 | 11 | 0 | 4 | 0 | 8 | 672 |
| 2024-Q2 | 0 | 16 | 0 | 6 | 7 | 4 | 434 |
| 2024-Q3 | 1 | 10 | 3 | 10 | 6 | 9 | 738 |
| 2024-Q4 | 0 | 13 | 0 | 37 | 11 | 21 | 1194 |
| 2025-Q1 | 9 | 15 | 85 | 134 | 25 | 135 | 1485 |
| 2025-Q2 | 10 | 14 | 178 | 50 | 7 | 78 | 1145 |
| 2025-Q3 | 5 | 21 | 142 | 33 | 4 | 34 | 864 |
| 2025-Q4 | 8 | 19 | 87 | 30 | 8 | 32 | 507 |
| 2026-Q1 | 15 | 10 | 70 | 68 | 8 | 18 | 409 |
| 2026-Q2 | 25 | 8 | 44 | 24 | 11 | 13 | 534 |
| 2026-Q3 | 18 | 6 | 36 | 30 | 8 | 51 | 632 |
| 2026-Q4 | 11 | 6 | 14 | 10 | 15 | 21 | 182 |

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
| 2023-Q4 | 90 | 102 | 3 | 0 | 55 |
| 2024-Q1 | 257 | 230 | 106 | 9 | 94 |
| 2024-Q2 | 130 | 187 | 70 | 3 | 77 |
| 2024-Q3 | 125 | 240 | 53 | 0 | 359 |
| 2024-Q4 | 170 | 430 | 103 | 0 | 573 |
| 2025-Q1 | 433 | 710 | 183 | 0 | 562 |
| 2025-Q2 | 205 | 734 | 94 | 0 | 449 |
| 2025-Q3 | 260 | 379 | 205 | 0 | 259 |
| 2025-Q4 | 180 | 322 | 29 | 0 | 160 |
| 2026-Q1 | 175 | 224 | 19 | 0 | 180 |
| 2026-Q2 | 229 | 271 | 26 | 5 | 128 |
| 2026-Q3 | 336 | 324 | 12 | 1 | 108 |
| 2026-Q4 | 65 | 134 | 17 | 1 | 42 |

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
| 2023-Q4 | 0.36 | 0.408 | 0.012 | 0 | 0.22 |
| 2024-Q1 | 0.369 | 0.33 | 0.152 | 0.013 | 0.135 |
| 2024-Q2 | 0.278 | 0.4 | 0.15 | 0.006 | 0.165 |
| 2024-Q3 | 0.161 | 0.309 | 0.068 | 0 | 0.462 |
| 2024-Q4 | 0.133 | 0.337 | 0.081 | 0 | 0.449 |
| 2025-Q1 | 0.229 | 0.376 | 0.097 | 0 | 0.298 |
| 2025-Q2 | 0.138 | 0.495 | 0.063 | 0 | 0.303 |
| 2025-Q3 | 0.236 | 0.344 | 0.186 | 0 | 0.235 |
| 2025-Q4 | 0.26 | 0.466 | 0.042 | 0 | 0.232 |
| 2026-Q1 | 0.293 | 0.375 | 0.032 | 0 | 0.301 |
| 2026-Q2 | 0.347 | 0.411 | 0.039 | 0.008 | 0.194 |
| 2026-Q3 | 0.43 | 0.415 | 0.015 | 0.001 | 0.138 |
| 2026-Q4 | 0.251 | 0.517 | 0.066 | 0.004 | 0.162 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 11005 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 3072 | 27.9 % |
| missing pipeline_tag (as published) | 4375 | 39.8 % |
|   of which filled from parent | 4374 | see pipeline_tag_source |
| missing library_name | 1773 | 16.1 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 14247 |  |
|   linked by HF | 13038 | 91.5 % |
|   old name of a renamed repo | 766 | 5.4 % |
|   not linked (broken parent link) | 443 | 3.1 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 11403 | 100.0 % of 11403 |
| tag edges to a parent outside the sample | 2258 | 16.2 % |
| child created >7 days before its parent | 21 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.6% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 96% |
