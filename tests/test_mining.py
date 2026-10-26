"""Tests for communities, lineage, licenses, trends and the report runner."""
import networkx as nx
import pandas as pd
import pytest

from mining import communities, licenses, lineage, trends
from mining.report import collect, to_markdown
from preprocess.clean import run as clean
from tests.rawdb import make_db


def graph(edges, **nodes):
    """DiGraph from (child, parent, relation) edges; nodes=dict of node -> attrs."""
    G = nx.DiGraph()
    for child, parent, rel in edges:
        G.add_edge(child, parent, relation=rel, temporal_anomaly=False)
    for n in G:
        G.nodes[n].update({"in_sample": True, **nodes.get(n, {})})
    return G


# ---- communities ---------------------------------------------------------------

def two_families():
    """Two seed families, tied together by one cross-family merge edge (a5 -> B)."""
    edges = [(f"a{i}", "A", "finetune") for i in range(6)] + [(f"b{i}", "B", "adapter") for i in range(6)]
    edges += [("a0", "a1", "merge"), ("a2", "a3", "merge"), ("b0", "b1", "merge")]
    edges += [("a5", "B", "merge")]
    roots = {n: {"root": n[0].upper()} for n in ["A", "B"] + [f"{x}{i}" for x in "ab" for i in range(6)]}
    return graph(edges, **roots)


def test_communities_recover_families():
    G = two_families()
    found = communities.detect(G)
    assert len(found) == 2
    assert {"A", "a0", "a5"} <= next(c for c in found if "A" in c)
    summary = communities.summary(G, found)
    assert summary["communities"] == 2 and summary["modularity"] > 0.3
    assert summary["weighted_purity"] > 0.9


def test_communities_are_reproducible():
    G = two_families()
    assert communities.detect(G) == communities.detect(G)


def test_cross_family_links():
    links = communities.cross_family_links(two_families())
    assert list(links["child"]) == ["a5"] and list(links["parent_family"]) == ["B"]


# ---- lineage -------------------------------------------------------------------

def test_generations_use_the_longest_chain():
    # base <- ft <- q ; merge m of base and ft sits below both: generation 2
    G = graph([("ft", "base", "finetune"), ("q", "ft", "quantized"),
               ("m", "base", "merge"), ("m", "ft", "merge")])
    assert lineage.generations(G) == {"base": 0, "ft": 1, "q": 2, "m": 2}


def test_generations_survive_a_cycle():
    G = graph([("a", "b", "finetune"), ("b", "a", "finetune")],
              a={"created_at": "2025-01-01T00:00:00Z"}, b={"created_at": "2025-06-01T00:00:00Z"})
    gen = lineage.generations(G)          # b is newer, so the a -> b edge is the one dropped
    assert gen == {"a": 0, "b": 1}
    assert G.has_edge("a", "b")           # original graph left untouched


def test_generation_table_uses_hf_counts():
    G = graph([("ft1", "base", "finetune"), ("ft2", "base", "adapter")],
              base={"hf_children_total": 1000, "hf_children": {"finetune": 700, "adapter": 300}},
              ft1={"hf_children_total": 4, "hf_children": {"quantized": 4}},
              ft2={"hf_children_total": 0, "hf_children": {}})
    t = lineage.generation_table(G).set_index("generation")
    assert t.loc[0, "branching_mean"] == 1000 and t.loc[0, "hf_finetune"] == 700
    assert t.loc[1, "branching_mean"] == 2 and t.loc[1, "share_with_children"] == 0.5
    assert t.loc[1, "observed_children_mean"] == 0


def test_relation_shares_population_vs_sample():
    G = graph([("ft", "base", "finetune"), ("m", "base", "merge")],
              base={"hf_children": {"finetune": 90, "merge": 10}})
    df = lineage.relation_shares(G).set_index("relation")
    assert df.loc["finetune", "population_share"] == pytest.approx(0.9)
    assert df.loc["merge", "sample_share"] == pytest.approx(0.5)


# ---- licenses ------------------------------------------------------------------

@pytest.mark.parametrize("child, child_cat, parent, parent_cat, outcome", [
    ("apache-2.0", "permissive", "apache-2.0", "permissive", "same"),
    ("mit", "permissive", "apache-2.0", "permissive", "changed_same_category"),
    ("apache-2.0", "permissive", "llama3.1", "restricted", "loosened"),
    ("mit", "permissive", "cc-by-nc-4.0", "noncommercial", "loosened"),
    ("cc-by-nc-4.0", "noncommercial", "mit", "permissive", "tightened"),
    ("llama3", "restricted", "llama3.1", "restricted", "changed_same_category"),
    ("other", "other", "gemma", "restricted", "changed_custom"),
    (None, "unknown", "mit", "permissive", "child_unknown"),
    ("mit", "permissive", None, "unknown", "parent_unknown"),
])
def test_license_classify(child, child_cat, parent, parent_cat, outcome):
    assert licenses.classify(child, child_cat, parent, parent_cat) == outcome


def _licensed(lic, cat, root="base"):
    return {"license": lic, "license_category": cat, "root": root}


def test_license_tables():
    G = graph([("ok", "base", "finetune"), ("bad", "base", "adapter"), ("none", "base", "quantized"),
               ("ext", "outside", "finetune")],
              base=_licensed("llama3.1", "restricted"), ok=_licensed("llama3.1", "restricted"),
              bad=_licensed("apache-2.0", "permissive"), none=_licensed(None, "unknown"),
              ext=_licensed("mit", "permissive"), outside={"in_sample": False})
    edges = licenses.edge_table(G)
    assert len(edges) == 3                                  # the edge to an unscraped parent is skipped
    assert list(licenses.conflicts(edges)["child"]) == ["bad"]
    fam = licenses.by_group(edges, "family").set_index("family")
    # of the 2 edges with both licenses known: 1 same, 1 loosened
    assert fam.loc["base", "drift_rate"] == pytest.approx(0.5)
    assert fam.loc["base", "conflict_rate"] == pytest.approx(0.5)
    assert licenses.transition_matrix(edges).loc["restricted", "permissive"] == 1


# ---- trends --------------------------------------------------------------------

def _dated(created, depth=1, floor=0, task="text-generation", root="base"):
    return {"created_at": created, "depth": depth, "created_at_is_floor": floor,
            "pipeline_tag": task, "root": root}


def test_trend_rows_exclude_seeds_and_placeholder_dates():
    G = graph([("a", "base", "finetune"), ("b", "base", "quantized"), ("old", "base", "finetune")],
              base=_dated("2024-01-01T00:00:00Z", depth=0),
              a=_dated("2024-02-10T00:00:00Z"), b=_dated("2024-11-30T00:00:00Z", task=None),
              old=_dated("2022-03-02T00:00:00Z", floor=1))
    df = trends.derivatives(G).set_index("model")
    assert set(df.index) == {"a", "b"}
    assert df.loc["a", "quarter"] == "2024-Q1" and df.loc["b", "quarter"] == "2024-Q4"
    assert df.loc["b", "task"] == "unknown" and df.loc["b", "relation"] == "quantized"


def test_trend_rows_skip_models_older_than_all_their_parents():
    G = graph([("spam", "base", "finetune"), ("merge", "base", "merge"), ("merge", "other", "merge")],
              base=_dated("2025-01-20T00:00:00Z", depth=0), other=_dated("2023-01-01T00:00:00Z", depth=0),
              spam=_dated("2024-03-01T00:00:00Z"), merge=_dated("2024-06-01T00:00:00Z"))
    G["spam"]["base"]["temporal_anomaly"] = True
    G["merge"]["base"]["temporal_anomaly"] = True       # but its other parent is fine
    assert set(trends.derivatives(G)["model"]) == {"merge"}


def test_per_quarter_top_and_shares():
    df = pd.DataFrame({"quarter": ["2024-Q1"] * 3 + ["2024-Q2"],
                       "task": ["x", "x", "y", "z"]})
    table = trends.per_quarter(df, "task", top=1)
    assert list(table.columns) == ["other", "x"]
    assert trends.shares(table).sum(axis=1).tolist() == [1.0, 1.0]


# ---- report runner on a tiny database ------------------------------------------------

def test_report_runs_end_to_end(tmp_path):
    models = {"base/m": {"pipeline_tag": "text-generation", "license": "llama3.1",
                         "children_counts_json": '{"finetune": 40, "merge": 2}'},
              "kid/a": {"created_at": "2025-02-01T00:00:00.000Z", "license": "apache-2.0"},
              "kid/b": {"created_at": "2025-05-01T00:00:00.000Z", "license": None},
              "kid/m": {"created_at": "2025-06-01T00:00:00.000Z", "license": "llama3.1"}}
    conn = make_db(tmp_path / "db", models, [
        ("kid/a", "base/m", "finetune", "tags"), ("kid/b", "base/m", "finetune", "tags"),
        ("kid/m", "base/m", "merge", "tags"), ("kid/m", "kid/a", "merge", "tags"),
        ("unscraped/x", "base/m", "finetune", "listing")],
        queue={"base/m": (0, "base/m"), "kid/a": (1, "base/m"), "kid/b": (1, "base/m"),
               "kid/m": (1, "base/m")})
    clean(conn)
    sections = collect(conn)
    tables = {name: df for _, _, t in sections for name, df in t.items()}
    assert tables["ranking_top20"].iloc[0]["model"] == "base/m"
    assert list(tables["license_conflicts"]["child"]) == ["kid/a"]
    assert tables["lineage_generations"]["generation"].max() == 2     # kid/m merges base + kid/a
    assert "|" in to_markdown(tables["data_quality"])


def test_to_markdown_escapes_and_truncates():
    df = pd.DataFrame({"a": ["x|y", None], "b": [0.123456, float("nan")]})
    md = to_markdown(df, max_rows=1)
    assert "x\\|y" in md and "0.1235" in md and "1 more rows" in md
