import networkx as nx
import pytest

from mining.ranking import (add_unsampled_children, compare_with_networkx, hits, hits_eigengap,
                            pagerank, ranking_table, weighted_pagerank)


def test_pagerank_hand_computed_example():
    # a -> c and b -> c (two fine-tunes of base c). By symmetry PR(a) = PR(b) = x, PR(c) = y.
    # c is dangling, so its rank y is spread over all 3 nodes:
    #   x = (1-d)/3 + d * (y/3)        and  2x + y = 1
    #   with d = 0.85:  x = 0.05 + 0.85(1 - 2x)/3  ->  4.7x = 1  ->  x = 1/4.7
    pr, _ = pagerank(nx.DiGraph([("a", "c"), ("b", "c")]))
    assert pr["a"] == pytest.approx(1 / 4.7, abs=1e-10)
    assert pr["c"] == pytest.approx(1 - 2 / 4.7, abs=1e-10)


def test_pagerank_sums_to_one_and_rewards_the_base():
    G = nx.DiGraph([("ft1", "base"), ("ft2", "base"), ("q", "ft1"), ("m", "ft1"), ("m", "other")])
    pr, iterations = pagerank(G)
    assert sum(pr.values()) == pytest.approx(1.0)
    assert max(pr, key=pr.get) == "base"
    assert pr["ft1"] > pr["ft2"]          # ft1 has derivatives of its own, ft2 doesn't
    assert iterations < 200


def test_pagerank_no_edges_is_uniform():
    G = nx.DiGraph()
    G.add_nodes_from("abcd")
    assert all(v == pytest.approx(0.25) for v in pagerank(G)[0].values())


def test_pagerank_empty_graph():
    assert pagerank(nx.DiGraph()) == ({}, 0)


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_pagerank_matches_networkx_on_random_graphs(seed):
    G = nx.gnp_random_graph(60, 0.05, seed=seed, directed=True)
    ours, _ = pagerank(G)
    theirs = nx.pagerank(G, alpha=0.85, tol=1e-12, max_iter=1000)
    assert max(abs(ours[n] - theirs[n]) for n in G) < 1e-9


# ---- weighted PageRank ------------------------------------------------------------

def _capped_graph():
    """Base B has 10 fine-tunes on HF, but the crawl only sampled 2 (s1, s2).
    Base C has 4 and all 4 were sampled."""
    G = nx.DiGraph()
    for child in ("s1", "s2"):
        G.add_edge(child, "B", relation="finetune")
    for i in range(4):
        G.add_edge(f"c{i}", "C", relation="finetune")
    G.nodes["B"]["hf_children"] = {"finetune": 10}
    G.nodes["C"]["hf_children"] = {"finetune": 4}
    return G


def test_virtual_node_added_only_for_missing_children():
    H = add_unsampled_children(_capped_graph())
    virtual = [v for v in H if H.nodes[v].get("virtual")]
    assert virtual == ["[8 unscraped finetune of B]"]
    assert H.nodes[virtual[0]]["stands_for"] == 8 and H.has_edge(virtual[0], "B")


def test_weighted_equals_pagerank_on_the_uncapped_graph():
    # The claim behind the method: one virtual node standing for 8 leaves gives
    # exactly the same ranks as 8 real leaves.
    weighted, _ = weighted_pagerank(_capped_graph())
    full = _capped_graph()
    for i in range(8):
        full.add_edge(f"missing{i}", "B", relation="finetune")
    exact, _ = pagerank(full)
    for node in ("B", "C", "s1", "c0"):
        assert weighted[node] == pytest.approx(exact[node], abs=1e-10)
    # and the cap correction changes the order: plain PageRank thinks C is bigger
    plain, _ = pagerank(_capped_graph())
    assert plain["C"] > plain["B"] and weighted["B"] > weighted["C"]


def test_weighted_is_plain_pagerank_without_hf_counts():
    G = nx.DiGraph([("a", "c"), ("b", "c")])
    nx.set_edge_attributes(G, "finetune", "relation")
    assert weighted_pagerank(G)[0] == pytest.approx(pagerank(G)[0])


def test_hf_count_below_sampled_count_adds_nothing():
    G = _capped_graph()
    G.nodes["C"]["hf_children"] = {"finetune": 3}     # HF count moved since the listing was read
    assert not any(G2.get("virtual") for _, G2 in add_unsampled_children(G).nodes(data=True)
                   if _ != "[8 unscraped finetune of B]")


def test_hits_hubs_and_authorities():
    # h1 cites both bases, h2 cites only a1 -> a1 is the stronger authority, h1 the stronger hub
    G = nx.DiGraph([("h1", "a1"), ("h1", "a2"), ("h2", "a1")])
    hubs, auth, _ = hits(G)
    assert auth["a1"] > auth["a2"] > 0 and auth["h1"] == 0
    assert hubs["h1"] > hubs["h2"] > 0 and hubs["a1"] == 0
    assert sum(hubs.values()) == pytest.approx(1) and sum(auth.values()) == pytest.approx(1)
    nx_hubs, nx_auth = nx.hits(G)
    assert all(auth[n] == pytest.approx(nx_auth[n], abs=1e-8) for n in G)


def test_hits_no_edges_does_not_divide_by_zero():
    G = nx.DiGraph()
    G.add_nodes_from("ab")
    hubs, auth, _ = hits(G)
    assert set(auth.values()) == {0.0}


def test_eigengap_flags_equal_sized_families():
    # two disconnected stars of the same size: the top eigenvalue is tied
    tied = nx.DiGraph([(f"a{i}", "A") for i in range(5)] + [(f"b{i}", "B") for i in range(5)])
    clear = nx.DiGraph([(f"a{i}", "A") for i in range(9)] + [(f"b{i}", "B") for i in range(2)])
    assert hits_eigengap(tied) == pytest.approx(1.0)
    assert hits_eigengap(clear) < 0.5


def test_compare_with_networkx_reports_agreement():
    G = nx.gnp_random_graph(40, 0.08, seed=7, directed=True)
    nx.set_edge_attributes(G, "finetune", "relation")
    for n in list(G)[:5]:
        G.nodes[n]["hf_children"] = {"finetune": 20}
    df = compare_with_networkx(G)
    assert list(df["algorithm"]) == ["PageRank", "Weighted PageRank", "HITS authority", "HITS hub"]
    assert (df["max_abs_diff"] < 1e-8).all()
    assert (df["top20_overlap"] == 20).all()


def test_ranking_table():
    G = nx.DiGraph([("ft1", "base"), ("ft2", "base"), ("q", "ft1")])
    nx.set_edge_attributes(G, "finetune", "relation")
    for n in G:
        G.nodes[n].update(in_sample=True, root="base", license="mit", hf_children_total=None)
    # ft2 has 5 children on HF, none sampled. In units of one node's jump share j:
    # ft2 ~ j + 0.85*5j = 5.25j, ft1 ~ j + 0.85j = 1.85j, base ~ j + 0.85*(5.25j + 1.85j) ~ 7j
    G.nodes["ft2"]["hf_children"] = {"quantized": 5}
    df = ranking_table(G, n=4)
    assert list(df.index) == [1, 2, 3, 4]
    assert df.iloc[0]["model"] == "base" and df.iloc[0]["derivatives_in_graph"] == 2
    # weighted order puts ft2 above ft1; the plain rank column records where it was before
    assert list(df["model"][:3]) == ["base", "ft2", "ft1"]
    assert df.set_index("model").loc["ft2", "plain_pagerank_rank"] == 3
