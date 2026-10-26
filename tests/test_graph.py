import networkx as nx
import pytest

from mining.graph import break_cycles, build_graph, describe, find_cycle_groups, looks_like_secret
from preprocess.clean import run
from tests.rawdb import make_db


def small_db(tmp_path):
    conn = make_db(tmp_path / "db", {
        "base/m": {"license": "llama3.1"},
        "kid/ft": {}, "kid/ad": {},
    }, [
        ("kid/ft", "base/m", "finetune", "tags"),
        ("kid/ft", "base/m", "finetune", "listing"),
        ("kid/ad", "base/m", "adapter", "tags"),
        ("kid/ad", "other/base", "merge", "tags"),        # parent outside the sample
        ("unscraped/kid", "base/m", "quantized", "listing"),
    ], queue={"base/m": (0, "base/m"), "kid/ft": (1, "base/m"), "kid/ad": (1, "base/m")})
    run(conn)
    return conn


def test_edges_point_from_child_to_parent(tmp_path):
    G = build_graph(small_db(tmp_path))
    assert G.has_edge("kid/ft", "base/m") and not G.has_edge("base/m", "kid/ft")
    assert G["kid/ft"]["base/m"]["relation"] == "finetune"
    assert G["kid/ft"]["base/m"]["in_tags"] and G["kid/ft"]["base/m"]["in_listing"]


def test_sample_graph_has_only_scraped_models(tmp_path):
    G = build_graph(small_db(tmp_path))
    assert set(G) == {"base/m", "kid/ft", "kid/ad"}
    assert G.number_of_edges() == 2
    assert G.nodes["base/m"]["license_category"] == "restricted"
    assert G.nodes["kid/ft"]["depth"] == 1 and G.nodes["kid/ft"]["root"] == "base/m"


def test_external_graph_adds_unscraped_endpoints_without_metadata(tmp_path):
    G = build_graph(small_db(tmp_path), include_external=True)
    assert {"other/base", "unscraped/kid"} <= set(G)
    assert G.nodes["other/base"] == {"in_sample": False}
    assert G.number_of_edges() == 4


def test_token_shaped_model_ids_are_left_out(tmp_path):
    token_repo = "someone/hf_" + "A1b2C3d4" * 4 + "zz"        # a repo named like an HF token
    conn = make_db(tmp_path / "db", {"base/m": {}, "kid/ok": {}}, [
        ("kid/ok", "base/m", "finetune", "tags"),
        (token_repo, "base/m", "finetune", "listing"),
    ])
    run(conn)
    G = build_graph(conn, include_external=True)
    assert token_repo not in G
    assert G.has_edge("kid/ok", "base/m")


@pytest.mark.parametrize("model_id, secret", [
    ("someone/hf_" + "x" * 34, True),
    ("org/ghp_" + "a" * 36, True),
    ("org/my-sk-model", False),                 # too short to be a key
    ("meta-llama/Llama-3.1-8B", False),
    ("org/hf_model", False),
])
def test_looks_like_secret(model_id, secret):
    assert looks_like_secret(model_id) is secret


def test_describe(tmp_path):
    d = describe(build_graph(small_db(tmp_path), include_external=True))
    assert d["nodes"] == 5 and d["nodes_in_sample"] == 3
    assert d["roots"] == 2              # base/m and other/base have no parent here
    assert d["multi_parent_nodes"] == 1 # kid/ad
    assert d["is_dag"] and d["cycle_groups"] == 0


def _cycle_graph():
    # a -> b -> c -> a, where the c -> a edge points at the newest model
    G = nx.DiGraph()
    G.add_node("a", created_at="2025-03-01T00:00:00Z")
    G.add_node("b", created_at="2025-01-01T00:00:00Z")
    G.add_node("c", created_at="2025-02-01T00:00:00Z")
    for child, parent in [("a", "b"), ("b", "c"), ("c", "a")]:
        G.add_edge(child, parent, relation="finetune")
    G.add_edge("d", "b", relation="adapter")              # not on the cycle
    return G


def test_cycles_are_found():
    assert find_cycle_groups(_cycle_graph()) == [["a", "b", "c"]]


def test_break_cycles_drops_edge_into_newest_parent():
    G = _cycle_graph()
    removed = break_cycles(G)
    assert removed == [("c", "a", "finetune")]   # 'a' (March) can't be the parent of 'c' (Feb)
    assert nx.is_directed_acyclic_graph(G)
    assert G.has_edge("d", "b")
