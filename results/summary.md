# Mining results

Generated 2026-10-26 15:35 UTC from 9075 scraped models (scraped 2026-10-26 to 2026-10-26; download counts are a snapshot of that time).

## Graph

Sample graph = scraped models only. 'All known edges' also includes unscraped children (from listings) and out-of-sample parents.

**graph_stats**

| statistic | sample graph | all known edges |
|---|---|---|
| nodes | 9073 | 22355 |
| nodes_in_sample | 9073 | 9073 |
| edges | 9629 | 24468 |
| relations | {'finetune': 3654, 'adapter': 2333, 'quantized': 2294, 'merge': 1338, 'unknown': 10} | {'finetune': 8498, 'adapter': 6600, 'quantized': 5211, 'merge': 4144, 'unknown': 15} |
| is_dag | True | True |
| cycle_groups | 0 | 0 |
| weak_components | 6 | 4 |
| largest_component | 5299 | 18201 |
| isolated_nodes | 0 | 0 |
| roots | 10 | 531 |
| leaves | 8161 | 20852 |
| multi_parent_nodes | 329 | 957 |
| temporal_anomaly_edges | 18 | 18 |

## 1. Influence ranking

Own PageRank (d = 0.85), weighted PageRank and HITS, all checked against networkx. Ranked by weighted PageRank on all known edges: the crawl reads at most 300 children per relation, and the weighting adds the skipped ones back using HF's real child counts (see mining/ranking.py). plain_pagerank_rank shows the uncorrected position.

**ranking_verification_sample**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 39 | 1.124e-10 | 20 | 1 |  |
| Weighted PageRank | 52 | 3.53e-10 | 20 | 1 |  |
| HITS authority | 175 | 3.814e-10 | 20 | 0.9362 | 0.9401 |
| HITS hub | 175 | 3.867e-13 | 20 | 0.9984 | 0.9401 |

**ranking_verification_all_edges**

| algorithm | iterations | max_abs_diff | top20_overlap | spearman | hits_eigengap |
|---|---|---|---|---|---|
| PageRank | 78 | 2.167e-10 | 20 | 1 |  |
| Weighted PageRank | 51 | 9.168e-10 | 20 | 1 |  |
| HITS authority | 193 | 1.901e-10 | 20 | 0.989 | 0.9449 |
| HITS hub | 193 | 5.302e-13 | 20 | 0.9992 | 0.9449 |

**ranking_top20**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.0672 | 0.04599 | 3 | 6.257e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.0659 | 0.05942 | 2 | 0.002096 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05007 | 0.0173 | 8 | 3.558e-05 | 1.057e-08 | 1068 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04878 | 0.01589 | 9 | 0.0003034 | 3.541e-06 | 977 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03496 | 0.06856 | 1 | 0.4782 | 0 | 1101 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03224 | 0.008548 | 18 | 1.988e-76 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03037 | 0.02948 | 5 | 1.649e-23 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02842 | 0.01532 | 10 | 6.942e-22 | 2.786e-26 | 939 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.0238 | 2.04e-05 | 1469 | 7.234e-07 | 6.011e-08 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02131 | 0.022 | 7 | 1.178e-27 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01856 | 0.01479 | 11 | 3.279e-25 | 1.989e-30 | 903 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01339 | 0.02999 | 4 | 8.49e-10 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.0122 | 0.02634 | 6 | 2.693e-06 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01077 | 2.932e-05 | 1033 | 4.471e-08 | 5.126e-07 | 3 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | google/gemma-2-9b-it | 0.008098 | 0.01285 | 12 | 1.316e-08 | 4.549e-09 | 793 | 1213 | google/gemma-2-9b | gemma | True |
| 16 | Qwen/Qwen2.5-Coder-7B | 0.007862 | 0.004741 | 27 | 4.869e-07 | 1.057e-08 | 292 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007447 | 0.000334 | 74 | 1.124e-06 | 8.227e-10 | 46 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.007029 | 0.006166 | 25 | 1.001e-06 | 1.057e-08 | 392 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006968 | 1.924e-05 | 9281 | 0 | 5.126e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.006939 | 0.01211 | 13 | 4.849e-06 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top20_sample_graph**

| rank | model | weighted_pagerank | pagerank | plain_pagerank_rank | authority | hub | derivatives_in_graph | hf_children_total | family | license | in_sample |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen/Qwen2.5-7B | 0.06775 | 0.04835 | 4 | 1.063e-06 | 0 | 824 | 2086 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 2 | meta-llama/Llama-3.1-8B | 0.06637 | 0.0553 | 2 | 0.007206 | 0 | 971 | 3267 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 3 | Qwen/Qwen2.5-7B-Instruct | 0.05005 | 0.001943 | 16 | 6.95e-06 | 1.039e-09 | 57 | 6669 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 4 | meta-llama/Llama-3.1-8B-Instruct | 0.04881 | 0.001533 | 18 | 0.0002198 | 7.047e-06 | 43 | 7302 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 5 | mistralai/Mistral-7B-v0.1 | 0.03656 | 0.06144 | 1 | 0.9226 | 0 | 1100 | 4000 | mistralai/Mistral-7B-v0.1 | apache-2.0 | True |
| 6 | google-bert/bert-base-uncased | 0.03233 | 0.02447 | 10 | 2.104e-62 | 0 | 489 | 7222 | google-bert/bert-base-uncased | apache-2.0 | True |
| 7 | Qwen/Qwen3-8B-Base | 0.03049 | 0.03532 | 5 | 1.409e-58 | 0 | 514 | 856 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 8 | Qwen/Qwen3-8B | 0.02846 | 0.002226 | 15 | 3.001e-60 | 1.378e-61 | 44 | 5133 | Qwen/Qwen3-8B-Base | apache-2.0 | True |
| 9 | unsloth/Qwen2.5-7B-Instruct | 0.02382 | 6.111e-05 | 912 | 7.432e-09 | 6.797e-09 | 1 | 5360 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 10 | google/gemma-3-4b-pt | 0.02134 | 0.02811 | 8 | 1.091e-88 | 0 | 346 | 395 | google/gemma-3-4b-pt | gemma | True |
| 11 | google/gemma-3-4b-it | 0.01857 | 0.005477 | 11 | 9.616e-91 | 1.067e-91 | 119 | 1850 | google/gemma-3-4b-pt | gemma | True |
| 12 | meta-llama/Llama-3.2-1B | 0.01375 | 0.052 | 3 | 5.666e-17 | 0 | 889 | 1998 | meta-llama/Llama-3.2-1B | llama3.2 | True |
| 13 | google/gemma-2-9b | 0.01234 | 0.03139 | 7 | 1.07e-05 | 0 | 427 | 458 | google/gemma-2-9b | gemma | True |
| 14 | unsloth/Meta-Llama-3.1-8B-Instruct | 0.01078 | 0.0001142 | 399 | 4.299e-08 | 2.15e-07 | 3 | 2425 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 15 | google/gemma-2-9b-it | 0.008148 | 0.004578 | 12 | 2.144e-08 | 1.047e-08 | 99 | 1213 | google/gemma-2-9b | gemma | True |
| 16 | Qwen/Qwen2.5-Coder-7B | 0.00792 | 0.001283 | 22 | 3.543e-08 | 1.039e-09 | 18 | 291 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 17 | Qwen/Qwen2.5-Coder-7B-Instruct | 0.007455 | 0.000896 | 32 | 8.072e-08 | 3.465e-11 | 46 | 1701 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 18 | Qwen/Qwen2.5-Math-7B | 0.007125 | 0.001358 | 21 | 9.053e-08 | 1.039e-09 | 27 | 1124 | Qwen/Qwen2.5-7B | apache-2.0 | True |
| 19 | unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit | 0.006972 | 5.353e-05 | 8690 | 0 | 2.15e-07 | 0 | 1568 | meta-llama/Llama-3.1-8B | llama3.1 | True |
| 20 | microsoft/phi-2 | 0.00697 | 0.03393 | 6 | 5.154e-08 | 0 | 673 | 1479 | microsoft/phi-2 | mit | True |

**ranking_top_hubs**

| model | hub | parents |
|---|---|---|
| lejelly/union_tokenizer-mistral-7b-instrcut-math-code | 0.001321 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_1_w3_0_3-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_4_w2_0_0_w3_0_5-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_1_w2_0_3_w3_0_0-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_3_w3_0_2-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_2_w2_0_4_w3_0_5-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_5_w3_0_2-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_0_w2_0_3_w3_0_3-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_5_w2_0_5_w3_0_0-mistral-7b | 0.001321 | 4 |
| lejelly/grid-search-w1_0_3_w2_0_4_w3_0_2-mistral-7b | 0.001321 | 4 |

## 2. Model families (Louvain, sample graph)

{'communities': 47, 'modularity': 0.8964002384400612, 'largest': 1262, 'weighted_purity': 0.999669348616775, 'multi_family_communities': 1}

**communities**

| community | size | in_sample | dominant_family | purity | families | most_derived_from | internal_edges | rel_finetune | rel_adapter | rel_quantized | rel_merge | top_license_category |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1262 | 1262 | mistralai/Mistral-7B-v0.1 | 1 | 1 | mistralai/Mistral-7B-v0.1 | 1290 | 303 | 316 | 342 | 321 | permissive |
| 1 | 1118 | 1118 | Qwen/Qwen2.5-7B | 0.9973 | 3 | Qwen/Qwen2.5-7B | 1353 | 348 | 321 | 269 | 415 | permissive |
| 2 | 1073 | 1073 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B | 1076 | 324 | 315 | 400 | 37 | restricted |
| 3 | 1008 | 1008 | meta-llama/Llama-3.2-1B | 1 | 1 | meta-llama/Llama-3.2-1B | 1017 | 311 | 316 | 347 | 43 | restricted |
| 4 | 736 | 736 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-8B-Base | 758 | 363 | 173 | 173 | 48 | permissive |
| 5 | 726 | 726 | microsoft/phi-2 | 1 | 1 | microsoft/phi-2 | 730 | 313 | 301 | 103 | 12 | permissive |
| 6 | 547 | 547 | deepseek-ai/DeepSeek-R1 | 1 | 1 | deepseek-ai/DeepSeek-R1 | 546 | 311 | 124 | 106 | 5 | permissive |
| 7 | 526 | 526 | google-bert/bert-base-uncased | 1 | 1 | google-bert/bert-base-uncased | 525 | 322 | 144 | 52 | 7 | permissive |
| 8 | 470 | 470 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b | 473 | 308 | 71 | 87 | 7 | restricted |
| 9 | 396 | 396 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-pt | 396 | 309 | 25 | 62 | 0 | unknown |
| 10 | 164 | 164 | google/gemma-2-9b | 1 | 1 | google/gemma-2-9b-it | 178 | 36 | 37 | 49 | 56 | restricted |
| 11 | 157 | 157 | meta-llama/Llama-3.1-8B | 1 | 1 | meta-llama/Llama-3.1-8B-Instruct | 222 | 18 | 15 | 47 | 142 | unknown |
| 12 | 153 | 153 | google/gemma-3-4b-pt | 1 | 1 | google/gemma-3-4b-it | 157 | 56 | 39 | 47 | 15 | restricted |
| 13 | 127 | 127 | mistralai/Mistral-7B-v0.1 | 1 | 1 | HuggingFaceH4/zephyr-7b-beta | 154 | 14 | 15 | 37 | 88 | permissive |
| 14 | 79 | 79 | google/gemma-2-9b | 1 | 1 | unsloth/gemma-2-9b-bnb-4bit | 78 | 26 | 26 | 26 | 0 | permissive |
| 15 | 65 | 65 | meta-llama/Llama-3.2-1B | 1 | 1 | dphn/Dolphin3.0-Llama3.2-1B | 82 | 6 | 2 | 19 | 55 | restricted |
| 16 | 51 | 51 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt-unsloth-bnb-4bit | 50 | 38 | 8 | 4 | 0 | permissive |
| 17 | 35 | 35 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B | 34 | 10 | 10 | 10 | 4 | permissive |
| 18 | 31 | 31 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-unsloth-bnb-4bit | 30 | 10 | 10 | 10 | 0 | permissive |
| 19 | 27 | 27 | meta-llama/Llama-3.2-1B | 1 | 1 | unsloth/Llama-3.2-1B-bnb-4bit | 26 | 10 | 6 | 10 | 0 | permissive |
| 20 | 26 | 26 | google/gemma-3-4b-pt | 1 | 1 | unsloth/gemma-3-4b-pt | 25 | 22 | 3 | 0 | 0 | permissive |
| 21 | 25 | 25 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Embedding-8B | 24 | 8 | 8 | 8 | 0 | permissive |
| 22 | 24 | 24 | microsoft/phi-2 | 1 | 1 | ma921/phi-2-sft-golden-hh | 23 | 22 | 0 | 1 | 0 | permissive |
| 23 | 22 | 22 | Qwen/Qwen3-8B-Base | 1 | 1 | Qwen/Qwen3-Reranker-8B | 21 | 8 | 6 | 7 | 0 | permissive |
| 24 | 22 | 22 | google/gemma-3-4b-pt | 1 | 1 | CEIA-UFG/Gemma-3-Gaia-PT-BR-4b-it | 21 | 1 | 0 | 19 | 1 | restricted |
| 25 | 20 | 20 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base | 19 | 7 | 7 | 5 | 0 | permissive |
| 26 | 18 | 18 | google/gemma-3-4b-pt | 1 | 1 | MBZUAI-Paris/Nile-Chat-4B | 17 | 5 | 5 | 7 | 0 | restricted |
| 27 | 13 | 13 | google/gemma-2-9b | 1 | 1 | aisingapore/Gemma-SEA-LION-v3-9B | 12 | 5 | 1 | 6 | 0 | restricted |
| 28 | 12 | 12 | google/gemma-2-9b | 1 | 1 | Unbabel/Tower-Plus-9B | 11 | 3 | 0 | 6 | 2 | noncommercial |
| 29 | 12 | 12 | Qwen/Qwen3-8B-Base | 1 | 1 | McGill-NLP/AfriqueQwen-8B | 11 | 2 | 7 | 2 | 0 | permissive |
| 30 | 11 | 11 | Qwen/Qwen3-8B-Base | 1 | 1 | unsloth/Qwen3-8B-Base-unsloth-bnb-4bit | 10 | 7 | 1 | 2 | 0 | permissive |
| 31 | 10 | 10 | google-bert/bert-base-uncased | 1 | 1 | bilalzafar/CentralBank-BERT | 9 | 9 | 0 | 0 | 0 | permissive |
| 32 | 10 | 10 | google-bert/bert-base-uncased | 1 | 1 | gokulsrinivasagan/bert_base_train_book_ent_15p_s_init | 9 | 9 | 0 | 0 | 0 | permissive |
| 33 | 10 | 10 | meta-llama/Llama-3.2-1B | 1 | 1 | jkminder/lorentz-logitlens-paraphrase-stage1-l0.7 | 9 | 9 | 0 | 0 | 0 | restricted |
| 34 | 8 | 8 | microsoft/phi-2 | 1 | 1 | ma921/phi-2-sft-hh-rlhf | 7 | 7 | 0 | 0 | 0 | permissive |
| 35 | 8 | 8 | meta-llama/Llama-3.1-8B | 1 | 1 | fdtn-ai/Foundation-Sec-8B | 7 | 2 | 2 | 2 | 1 | permissive |
| 36 | 7 | 7 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Llama-3.1-8B | 6 | 2 | 2 | 2 | 0 | permissive |
| 37 | 7 | 7 | meta-llama/Llama-3.2-1B | 1 | 1 | slseanwu/MIDI-LLM_Llama-3.2-1B | 6 | 0 | 1 | 5 | 0 | restricted |
| 38 | 7 | 7 | meta-llama/Llama-3.1-8B | 1 | 1 | unsloth/Meta-Llama-3.1-8B-bnb-4bit | 6 | 2 | 2 | 2 | 0 | restricted |
| 39 | 7 | 7 | Qwen/Qwen2.5-7B | 1 | 1 | unsloth/Qwen2.5-7B-bnb-4bit | 6 | 2 | 2 | 2 | 0 | permissive |

*… 7 more rows in the CSV*

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

max generation 17, mean generation of derived models 1.35, models per generation {0: 10, 1: 6496, 2: 2278, 3: 195, 4: 45, 5: 16, 6: 5, 7: 3, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 13: 4, 14: 4, 15: 3, 16: 2, 17: 2}. Branching uses HF's exact child counts; relation share compares population vs sample.

**lineage_generations**

| generation | models | with_children | share_with_children | branching_mean | branching_median | branching_max | observed_children_mean | hf_finetune | hf_adapter | hf_quantized | hf_merge |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 10 | 10 | 1 | 2228 | 1738 | 7222 | 673 | 13485 | 6952 | 1184 | 664 |
| 1 | 6496 | 763 | 0.1177 | 5.314 | 0 | 7302 | 0.3861 | 15459 | 12620 | 5010 | 1374 |
| 2 | 2278 | 388 | 0.1705 | 8.51 | 0 | 5360 | 0.1111 | 12876 | 3819 | 1920 | 753 |
| 3 | 195 | 56 | 0.2917 | 0.8594 | 0 | 14 | 0.2718 | 5 | 3 | 102 | 55 |
| 4 | 45 | 14 | 0.3111 | 1.156 | 0 | 8 | 0.4 | 3 | 0 | 32 | 17 |
| 5 | 16 | 6 | 0.375 | 1.688 | 0 | 10 | 0.6875 | 0 | 0 | 15 | 12 |
| 6 | 5 | 2 | 0.4 | 3.6 | 0 | 14 | 2.8 | 0 | 0 | 5 | 13 |
| 7 | 3 | 2 | 0.6667 | 3 | 4 | 5 | 1.667 | 0 | 0 | 5 | 4 |
| 8 | 2 | 1 | 0.5 | 2 | 2 | 4 | 2 | 0 | 0 | 1 | 3 |
| 9 | 2 | 1 | 0.5 | 2 | 2 | 4 | 1.5 | 0 | 0 | 2 | 2 |
| 10 | 2 | 1 | 0.5 | 1.5 | 1.5 | 3 | 1 | 0 | 0 | 2 | 1 |
| 11 | 2 | 1 | 0.5 | 3 | 3 | 6 | 2.5 | 0 | 0 | 2 | 4 |
| 12 | 2 | 1 | 0.5 | 3 | 3 | 6 | 2.5 | 0 | 0 | 2 | 4 |
| 13 | 4 | 3 | 0.75 | 3.25 | 3.5 | 6 | 2.5 | 0 | 0 | 6 | 7 |
| 14 | 4 | 1 | 0.25 | 1.25 | 0 | 5 | 1 | 0 | 0 | 2 | 3 |
| 15 | 3 | 2 | 0.6667 | 2 | 3 | 3 | 0.6667 | 0 | 0 | 5 | 1 |
| 16 | 2 | 1 | 0.5 | 1.5 | 1.5 | 3 | 1 | 0 | 0 | 2 | 1 |
| 17 | 2 | 1 | 0.5 | 2 | 2 | 4 | 0 | 0 | 0 | 2 | 2 |

**lineage_relation_shares**

| relation | population_count | sample_edges | population_share | sample_share |
|---|---|---|---|---|
| finetune | 41828 | 3654 | 0.5472 | 0.3799 |
| adapter | 23394 | 2333 | 0.306 | 0.2425 |
| quantized | 8299 | 2294 | 0.1086 | 0.2385 |
| merge | 2920 | 1338 | 0.0382 | 0.1391 |

## 4. License drift

Edges with both ends scraped. 'loosened' = child's license is less restrictive than its parent's: a likely conflict.

**license_outcomes**

| outcome | count |
|---|---|
| same | 5094 |
| child_unknown | 2704 |
| changed_same_category | 536 |
| loosened | 508 |
| parent_unknown | 354 |
| changed_custom | 251 |
| tightened | 182 |

**license_transitions**

| parent_category | copyleft | noncommercial | other | permissive | restricted | unknown |
|---|---|---|---|---|---|---|
| copyleft | 2 | 0 | 0 | 0 | 0 | 0 |
| noncommercial | 0 | 31 | 0 | 2 | 3 | 18 |
| other | 0 | 2 | 51 | 4 | 0 | 16 |
| permissive | 16 | 57 | 140 | 3502 | 68 | 1630 |
| restricted | 10 | 41 | 105 | 493 | 2044 | 1040 |
| unknown | 0 | 0 | 3 | 29 | 5 | 317 |

**license_by_family**

| family | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| Qwen/Qwen2.5-7B | 34 | 25 | 602 | 0 | 110 | 589 | 5 | 1365 | 0.09801 | 0 |
| Qwen/Qwen3-8B-Base | 24 | 30 | 178 | 0 | 44 | 562 | 10 | 848 | 0.1022 | 0 |
| deepseek-ai/DeepSeek-R1 | 22 | 182 | 110 | 0 | 4 | 164 | 64 | 546 | 0.6204 | 0 |
| google-bert/bert-base-uncased | 5 | 88 | 122 | 0 | 0 | 321 | 9 | 545 | 0.2411 | 0 |
| google/gemma-2-9b | 24 | 1 | 246 | 96 | 5 | 366 | 25 | 763 | 0.2852 | 0.1875 |
| google/gemma-3-4b-pt | 14 | 0 | 235 | 102 | 9 | 315 | 1 | 676 | 0.2708 | 0.2361 |
| meta-llama/Llama-3.1-8B | 25 | 78 | 362 | 144 | 107 | 665 | 14 | 1395 | 0.2819 | 0.1555 |
| meta-llama/Llama-3.2-1B | 48 | 8 | 237 | 165 | 32 | 732 | 3 | 1225 | 0.2343 | 0.1726 |
| microsoft/phi-2 | 45 | 31 | 156 | 0 | 11 | 517 | 6 | 766 | 0.1369 | 0 |
| mistralai/Mistral-7B-v0.1 | 10 | 93 | 456 | 1 | 32 | 863 | 45 | 1500 | 0.1472 | 0.0009881 |

**license_by_relation**

| relation | changed_custom | changed_same_category | child_unknown | loosened | parent_unknown | same | tightened | edges | drift_rate | conflict_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| adapter | 64 | 139 | 895 | 68 | 21 | 1113 | 33 | 2333 | 0.2145 | 0.04799 |
| finetune | 113 | 295 | 718 | 247 | 46 | 2137 | 98 | 3654 | 0.2606 | 0.08547 |
| merge | 14 | 29 | 897 | 27 | 121 | 215 | 35 | 1338 | 0.3281 | 0.08438 |
| quantized | 59 | 73 | 191 | 166 | 166 | 1623 | 16 | 2294 | 0.1621 | 0.0857 |
| unknown | 1 | 0 | 3 | 0 | 0 | 6 | 0 | 10 | 0.1429 | 0 |

**license_conflicts**

| child | parent | relation | family | child_license | parent_license |
|---|---|---|---|---|---|
| 2024-mcm-everitt-ryan/gemma-2-9b-job-bias-qlora-seq-cls | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-CA/gem-monika-ddlc-9b-v1 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-CA/gem-monika-ddlc-9b-v1-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-Narra/gemma-2-9b-tagalog-chat-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922-SY/gemma-2-9b-dt2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| 922-SY/gemma-2-9b-dt2-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| 922CA/gemma-2-9b-etude-2-gguf | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| AlekseyCalvin/LYRICAL_MT_ru2en_TowerPlus9b | Unbabel/Tower-Plus-9B | finetune | google/gemma-2-9b | apache-2.0 | cc-by-nc-sa-4.0 |
| BallAd-15/gemma2-9b-task10-subtask3-EN | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| BallAd-15/gemma2-9b-task10-subtask3-v2 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Bloodman-the-master/ValentIA | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cannae-AI/TANIT-V0.5-Medium-9B-IT | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cesarbasurto/FullNameSplit | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Cran-May/Apollo2-9B-Q5_K_M-GGUF | FreedomIntelligence/Apollo2-9B | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Danielrahmai1991/tabehsonati_v1 | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Deeokay/gemma2-9B-GGUF | unsloth/gemma-2-9b-bnb-4bit | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Denisijcu/Vertex-Core-Gemma | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| DiTy/gemma-2-9b-it-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| DiTy/gemma-2-9b-it-russian-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Himalayan-wildcat/gemma-2-9b-finetune | google/gemma-2-9b | finetune | google/gemma-2-9b | mit | gemma |
| Hizaneko/gemma-2-9b-nyan100 | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Jaamie/gemma-mental-health-qlora | google/gemma-2-9b-it | adapter | google/gemma-2-9b | apache-2.0 | gemma |
| Jiangxz/Tax_Model | google/gemma-2-9b | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| Kohsaku/gemma-2-9b-finetune-4 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-sa-4.0 | gemma |
| Koomemartin/unsloth-gemma2-9b-version3-100k | unsloth/gemma-2-9b-bnb-4bit | adapter | google/gemma-2-9b | mit | gemma |
| MichiganNLP/hacking-fairness-benchmarks-gemma-2-9b-z1 | google/gemma-2-9b | adapter | google/gemma-2-9b | mit | gemma |
| MohammadAbuSaleh/gemma2-9b-lora-finetuned-for-llm | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Naotaka/gemma-2-9b-r16-768-512-it_lora | google/gemma-2-9b | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| Naphula-Archives/Writers-Tower-9B | Unbabel/Tower-Plus-9B | merge | google/gemma-2-9b | gemma | cc-by-nc-sa-4.0 |
| Naphula/Jungle-Oasis-BRF-MPOA-9B | Unbabel/Tower-Plus-9B | merge | google/gemma-2-9b | gemma | cc-by-nc-sa-4.0 |
| NotASI/Gemma-2-9B-Alpaca-QDoRA-step120 | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| QuantFactory/gemma-2-9b-it-SimPO-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | mit | gemma |
| QuantFactory/gemma-2-9b-it-function-calling-GGUF | google/gemma-2-9b-it | quantized | google/gemma-2-9b | apache-2.0 | gemma |
| QuantFactory/magnaraxy-9b-GGUF | anthracite-org/magnum-v3-9b-customgemma2 | merge | google/gemma-2-9b | apache-2.0 | gemma |
| RianPI/Gemma2-FT-ai-medical-chatbot | unsloth/gemma-2-9b-bnb-4bit | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| SURESHBEEKHANI/Finetune_Gemma_NRE_SFT_GGUF | google/gemma-2-9b | quantized | google/gemma-2-9b | mit | gemma |
| ShaomuTan/ReMedy-9B-24 | google/gemma-2-9b-it | finetune | google/gemma-2-9b | apache-2.0 | gemma |
| SinclairSchneider/german_politic_direction_gemma-2-9b | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-4.0 | gemma |
| SinclairSchneider/german_politic_direction_gemma-2-9b_v0.1 | google/gemma-2-9b | finetune | google/gemma-2-9b | cc-by-4.0 | gemma |

*… 468 more rows in the CSV*

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
| 2023-Q3 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 10 |
| 2023-Q4 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 40 | 169 |
| 2024-Q1 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 211 | 413 |
| 2024-Q2 | 0 | 0 | 0 | 34 | 15 | 0 | 0 | 0 | 196 | 185 |
| 2024-Q3 | 64 | 0 | 0 | 26 | 171 | 0 | 239 | 22 | 33 | 56 |
| 2024-Q4 | 176 | 0 | 0 | 45 | 135 | 0 | 215 | 252 | 25 | 105 |
| 2025-Q1 | 281 | 0 | 457 | 62 | 63 | 78 | 251 | 263 | 27 | 103 |
| 2025-Q2 | 148 | 131 | 25 | 63 | 153 | 174 | 159 | 192 | 76 | 83 |
| 2025-Q3 | 144 | 129 | 30 | 49 | 27 | 116 | 78 | 181 | 53 | 179 |
| 2025-Q4 | 43 | 91 | 2 | 49 | 40 | 66 | 67 | 118 | 53 | 25 |
| 2026-Q1 | 67 | 77 | 12 | 28 | 61 | 66 | 44 | 51 | 23 | 29 |
| 2026-Q2 | 67 | 113 | 2 | 21 | 43 | 59 | 67 | 55 | 11 | 22 |
| 2026-Q3 | 115 | 201 | 10 | 65 | 19 | 68 | 126 | 44 | 7 | 14 |
| 2026-Q4 | 23 | 83 | 0 | 36 | 10 | 38 | 20 | 9 | 4 | 6 |

**trend_task_quarterly**

| quarter | fill-mask | image-text-to-text | other | question-answering | sentence-similarity | text-classification | text-generation |
|---|---|---|---|---|---|---|---|
| 2022-Q1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q2 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| 2022-Q3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2022-Q4 | 0 | 0 | 3 | 0 | 0 | 0 | 0 |
| 2023-Q1 | 2 | 0 | 0 | 1 | 0 | 1 | 0 |
| 2023-Q2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2023-Q3 | 2 | 0 | 4 | 1 | 0 | 2 | 10 |
| 2023-Q4 | 8 | 1 | 0 | 1 | 0 | 6 | 208 |
| 2024-Q1 | 11 | 0 | 4 | 1 | 0 | 8 | 620 |
| 2024-Q2 | 16 | 0 | 6 | 0 | 7 | 4 | 397 |
| 2024-Q3 | 10 | 2 | 6 | 5 | 6 | 9 | 573 |
| 2024-Q4 | 13 | 0 | 14 | 19 | 11 | 20 | 876 |
| 2025-Q1 | 15 | 65 | 114 | 24 | 25 | 134 | 1208 |
| 2025-Q2 | 14 | 154 | 36 | 13 | 7 | 70 | 910 |
| 2025-Q3 | 21 | 104 | 26 | 2 | 2 | 34 | 797 |
| 2025-Q4 | 19 | 50 | 18 | 7 | 6 | 32 | 422 |
| 2026-Q1 | 10 | 49 | 44 | 2 | 8 | 16 | 329 |
| 2026-Q2 | 8 | 27 | 32 | 0 | 4 | 12 | 377 |
| 2026-Q3 | 6 | 32 | 32 | 5 | 5 | 51 | 538 |
| 2026-Q4 | 6 | 9 | 13 | 1 | 12 | 20 | 168 |

**trend_relation_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 8 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 3 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 3 | 0 | 0 | 1 |
| 2023-Q2 | 0 | 1 | 0 | 0 | 1 |
| 2023-Q3 | 1 | 12 | 0 | 0 | 6 |
| 2023-Q4 | 82 | 94 | 3 | 0 | 45 |
| 2024-Q1 | 246 | 222 | 81 | 6 | 89 |
| 2024-Q2 | 128 | 184 | 62 | 3 | 53 |
| 2024-Q3 | 106 | 187 | 49 | 0 | 269 |
| 2024-Q4 | 145 | 340 | 85 | 0 | 383 |
| 2025-Q1 | 397 | 652 | 135 | 0 | 401 |
| 2025-Q2 | 178 | 602 | 86 | 0 | 338 |
| 2025-Q3 | 243 | 326 | 199 | 0 | 218 |
| 2025-Q4 | 148 | 256 | 25 | 0 | 125 |
| 2026-Q1 | 119 | 178 | 18 | 0 | 143 |
| 2026-Q2 | 169 | 167 | 26 | 5 | 93 |
| 2026-Q3 | 304 | 273 | 10 | 1 | 81 |
| 2026-Q4 | 57 | 127 | 13 | 1 | 31 |

**trend_relation_share_quarterly**

| quarter | adapter | finetune | merge | mixed | quantized |
|---|---|---|---|---|---|
| 2022-Q1 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q2 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q3 | 0 | 1 | 0 | 0 | 0 |
| 2022-Q4 | 0 | 1 | 0 | 0 | 0 |
| 2023-Q1 | 0 | 0.75 | 0 | 0 | 0.25 |
| 2023-Q2 | 0 | 0.5 | 0 | 0 | 0.5 |
| 2023-Q3 | 0.053 | 0.632 | 0 | 0 | 0.316 |
| 2023-Q4 | 0.366 | 0.42 | 0.013 | 0 | 0.201 |
| 2024-Q1 | 0.382 | 0.345 | 0.126 | 0.009 | 0.138 |
| 2024-Q2 | 0.298 | 0.428 | 0.144 | 0.007 | 0.123 |
| 2024-Q3 | 0.173 | 0.306 | 0.08 | 0 | 0.44 |
| 2024-Q4 | 0.152 | 0.357 | 0.089 | 0 | 0.402 |
| 2025-Q1 | 0.25 | 0.411 | 0.085 | 0 | 0.253 |
| 2025-Q2 | 0.148 | 0.5 | 0.071 | 0 | 0.281 |
| 2025-Q3 | 0.246 | 0.331 | 0.202 | 0 | 0.221 |
| 2025-Q4 | 0.267 | 0.462 | 0.045 | 0 | 0.226 |
| 2026-Q1 | 0.26 | 0.389 | 0.039 | 0 | 0.312 |
| 2026-Q2 | 0.367 | 0.363 | 0.057 | 0.011 | 0.202 |
| 2026-Q3 | 0.454 | 0.408 | 0.015 | 0.001 | 0.121 |
| 2026-Q4 | 0.249 | 0.555 | 0.057 | 0.004 | 0.135 |

## 6. Data quality

**data_quality**

| metric | value | detail |
|---|---|---|
| models scraped | 9075 | of 20001 queued |
| crawl failures | 1 | 0.0 % |
| models with a parse error | 0 | 0.0 % |
| missing license | 2613 | 28.8 % |
| missing pipeline_tag (as published) | 3554 | 39.2 % |
|   of which filled from parent | 3553 | see pipeline_tag_source |
| missing library_name | 1505 | 16.6 % |
| missing created_at | 0 | 0.0 % |
| created_at is HF's pre-2022 placeholder | 2 | excluded from trends |
| declared base_model values | 11831 |  |
|   linked by HF | 10808 | 91.4 % |
|   old name of a renamed repo | 677 | 5.7 % |
|   not linked (broken parent link) | 346 | 2.9 % |
|   malformed (URL/path/free text) | 0 |  |
| listing edges confirmed by child's tags | 9443 | 100.0 % of 9443 |
| tag edges to a parent outside the sample | 1965 | 16.9 % |
| child created >7 days before its parent | 18 | temporal anomaly |
| self-loops | 1 |  |
| relation conflicts (tags vs listing) | 0 |  |
| API spot-check accuracy | 99.5% | 50 random models x 11 fields; lowest field: downloads (within 10 %) 94% |
