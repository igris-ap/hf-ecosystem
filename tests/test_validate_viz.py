"""Tests for the API spot-check comparison and the visualisation builders
(no network: API records are hand-written dicts)."""
import json

import networkx as nx
import pytest

from validate.api_spotcheck import api_view, compare
from viz import charts, family_tree


def _ours(**overrides):
    record = {"id": "org/kid", "author": "org", "license": "apache-2.0", "pipeline_tag": "text-generation",
              "library_name": "transformers", "created_at": "2025-01-01T10:00:00.000Z", "gated": "no",
              "parents": {("org/base", "finetune")},
              "tags_json": json.dumps(["base_model:org/base", "base_model:finetune:org/base", "license:apache-2.0"]),
              "downloads": 1000, "likes": 10}
    record.update(overrides)
    return record


def _api(**overrides):
    record = {"id": "org/kid", "author": "org", "pipeline_tag": "text-generation",
              "library_name": "transformers", "createdAt": "2025-01-01T10:00:00.000Z", "gated": False,
              "tags": ["base_model:org/base", "base_model:finetune:org/base", "license:apache-2.0"],
              "cardData": {"license": "apache-2.0"}, "downloads": 1050, "likes": 10}
    record.update(overrides)
    return record


def test_identical_records_match_everywhere():
    fields, overlap = compare(_ours(), api_view(_api()))
    assert all(match for match, _, _ in fields.values())
    assert overlap == 1.0


def test_mismatches_are_detected():
    # Each changed field must be caught, otherwise a 100 % score would mean nothing.
    api = _api(pipeline_tag="text-classification", gated="manual", downloads=5000,
               tags=["base_model:org/other", "base_model:adapter:org/other"], cardData={"license": "mit"})
    fields, overlap = compare(_ours(), api_view(api))
    failed = {name for name, (match, _, _) in fields.items() if not match}
    assert failed == {"pipeline_tag", "gated", "license", "parents (edges)", "tags (exact set)",
                      "downloads (within 10 %)"}
    assert overlap < 1


def test_license_falls_back_to_tag_and_gated_maps_to_our_values():
    view = api_view(_api(cardData=None, gated="auto"))
    assert view["license"] == "apache-2.0" and view["gated"] == "auto"


# ---- visualisation ---------------------------------------------------------------

def _tree_graph():
    G = nx.DiGraph()
    for i in range(4):
        G.add_edge(f"kid/{i}", "meta-llama/Llama-3.1-8B", relation="adapter" if i % 2 else "finetune")
    G.add_edge("q/x", "Qwen/Qwen2.5-7B", relation="quantized")
    for n in G:
        root = "Qwen/Qwen2.5-7B" if n in ("q/x", "Qwen/Qwen2.5-7B") else "meta-llama/Llama-3.1-8B"
        G.nodes[n].update(root=root, depth=0 if "/" in n and n == root else 1, license="mit",
                          downloads=1, hf_children_total=0, created_month="2025-01")
    return G


def test_family_tree_page_encodes_family_and_relation():
    G = _tree_graph()
    scores = {n: 1.0 / (i + 1) for i, n in enumerate(G)}
    net, legend = family_tree.build_page(G, scores, list(G), ["Llama"], "test")
    nodes = {n["id"]: n for n in net.nodes}
    assert nodes["kid/0"]["color"]["background"] != nodes["q/x"]["color"]["background"]   # Qwen not highlighted
    assert nodes["meta-llama/Llama-3.1-8B"]["shape"] == "dot" and nodes["q/x"]["shape"] == "square"
    assert nodes["meta-llama/Llama-3.1-8B"]["label"].startswith("Llama:")
    dashes = {e["title"]: e["dashes"] for e in net.edges}
    assert dashes["finetune"] is False and dashes["adapter"] == [6, 4]
    assert "Llama" in legend and "quantized" in legend


def test_family_tree_refuses_too_many_colours():
    G = _tree_graph()
    scores = dict.fromkeys(G, 1.0)
    with pytest.raises(ValueError):
        family_tree.build_page(G, scores, list(G), ["Llama", "Qwen", "Gemma", "Phi"], "test")


def test_family_tree_written_page_is_offline(tmp_path):
    G = _tree_graph()
    net, legend = family_tree.build_page(G, dict.fromkeys(G, 1.0), list(G), ["Llama"], "test")
    html = family_tree.write(net, legend, tmp_path / "t.html").read_text(encoding="utf-8")
    assert "bootstrap" not in html                     # no CDN dependency
    assert "stabilizationIterationsDone" in html and "physics: false" in html


def test_charts_render(tmp_path, monkeypatch):
    monkeypatch.setattr(charts, "FIG_DIR", tmp_path)
    G = _tree_graph()
    G.nodes["meta-llama/Llama-3.1-8B"]["hf_children"] = {"finetune": 10, "adapter": 5}
    G.nodes["Qwen/Qwen2.5-7B"]["hf_children"] = {"quantized": 3}
    for n in G:
        G.nodes[n]["in_sample"] = True
    for _, _, d in G.edges(data=True):
        d["temporal_anomaly"] = False
    path = charts.family_size_chart(G)
    assert path.exists() and path.stat().st_size > 10_000
