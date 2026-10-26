"""Build the model lineage graph (networkx DiGraph) from the clean tables.

    python -m mining.graph          # build it and print summary stats

Edge direction is child -> parent ("derived from"). That is the direction a
citation points in, so PageRank's random surfer walks from derivatives to their
bases and influence piles up on the models everything is built on.

Two views of the same data:
  build_graph(conn)                         only models we scraped (default)
  build_graph(conn, include_external=True)  plus every other model an edge
      mentions: unscraped children from listings and parents outside the
      sample. These "external" nodes have no metadata (in_sample=False).
"""
import json
import logging
import re
import sqlite3
import sys
from collections import Counter

import networkx as nx

import config

log = logging.getLogger(__name__)

NODE_ATTRS = ("author", "license", "license_category", "pipeline_tag", "pipeline_tag_source",
              "library_name", "downloads", "likes", "created_at", "created_month",
              "created_at_is_floor", "gated", "depth", "root", "hf_children_total")


# Some people name a repo after an access token (seen in the wild:
# "<user>/hf_<34 chars>"). Everything we publish is built from this graph, so
# credential-shaped ids are dropped here and never reach results/ or site/,
# whether or not the token is live.
SECRET_PATTERN = re.compile(
    r"hf_[A-Za-z0-9]{30,}"               # Hugging Face access token
    r"|gh[pousr]_[A-Za-z0-9]{36,}"       # GitHub tokens
    r"|sk-[A-Za-z0-9_-]{20,}"            # OpenAI-style keys
    r"|AKIA[0-9A-Z]{16}"                 # AWS access key id
)


def looks_like_secret(model_id):
    return bool(SECRET_PATTERN.search(model_id))


def build_graph(conn, include_external=False):
    G = _build_graph(conn, include_external)
    hidden = [n for n in G if looks_like_secret(n)]
    if hidden:
        log.warning("left out %d model id(s) that look like access tokens", len(hidden))
        G.remove_nodes_from(hidden)
    return G


def _build_graph(conn, include_external):
    conn.row_factory = sqlite3.Row
    G = nx.DiGraph()
    for row in conn.execute(f"SELECT id, hf_children_json, {', '.join(NODE_ATTRS)} FROM clean_models"):
        G.add_node(row["id"], in_sample=True, hf_children=json.loads(row["hf_children_json"] or "{}"),
                   **{a: row[a] for a in NODE_ATTRS})

    # Tag-confirmed edges first, so if one pair has two relations (no case of this
    # in the 500 sample, but possible), the child's own page decides the main one.
    for e in conn.execute("SELECT * FROM clean_edges ORDER BY in_tags DESC"):
        child, parent = e["child_id"], e["parent_id"]
        if not include_external and not (e["child_in_sample"] and e["parent_in_sample"]):
            continue
        for node in (child, parent):
            if node not in G:
                G.add_node(node, in_sample=False)
        if G.has_edge(child, parent):
            G[child][parent]["relations"].append(e["relation"])
            continue
        G.add_edge(child, parent, relation=e["relation"], relations=[e["relation"]],
                   in_tags=bool(e["in_tags"]), in_listing=bool(e["in_listing"]),
                   temporal_anomaly=bool(e["temporal_anomaly"]))
    return G


def find_cycle_groups(G):
    """Return the groups of models that are stuck in a lineage cycle.

    Real lineage can't loop: a model can't be its own ancestor. A cycle means
    some card declares a wrong base. The nodes on cycles are exactly the
    strongly connected components with more than one node, and finding those
    is linear-time, unlike listing every cycle.
    """
    return [sorted(c) for c in nx.strongly_connected_components(G) if len(c) > 1]


def break_cycles(G):
    """Remove the least plausible edge from each cycle until G is a DAG.

    Rule: in a cycle, follow the edges and find the one whose *parent* is the
    most recently created model, then drop it. A model can't be derived from
    something uploaded after it, so that edge is the most likely wrong one. A
    missing date counts as newest. Returns the removed edges so they can be
    reported.
    """
    removed = []
    while True:
        try:
            cycle = nx.find_cycle(G)
        except nx.NetworkXNoCycle:
            return removed
        child, parent = max(cycle, key=lambda edge: G.nodes[edge[1]].get("created_at") or "9999")[:2]
        log.warning("cycle %s: removing %s -> %s", [c for c, _ in cycle], child, parent)
        removed.append((child, parent, G[child][parent]["relation"]))
        G.remove_edge(child, parent)


def describe(G):
    """Headline numbers about a graph, as a dict (printed by main, reused by the report)."""
    sample = [n for n, d in G.nodes(data=True) if d.get("in_sample")]
    weak = sorted((len(c) for c in nx.weakly_connected_components(G)), reverse=True)
    return {
        "nodes": G.number_of_nodes(),
        "nodes_in_sample": len(sample),
        "edges": G.number_of_edges(),
        "relations": dict(Counter(d["relation"] for _, _, d in G.edges(data=True))),
        "is_dag": nx.is_directed_acyclic_graph(G),
        "cycle_groups": len(find_cycle_groups(G)),
        "weak_components": len(weak),
        "largest_component": weak[0] if weak else 0,
        "isolated_nodes": nx.number_of_isolates(G),
        # roots: no parent in this graph (bases, or parent outside the sample)
        "roots": sum(1 for n in G if G.out_degree(n) == 0),
        # leaves: nothing in this graph derives from them
        "leaves": sum(1 for n in G if G.in_degree(n) == 0),
        "multi_parent_nodes": sum(1 for n in G if G.out_degree(n) > 1),
        "temporal_anomaly_edges": sum(1 for _, _, d in G.edges(data=True) if d["temporal_anomaly"]),
    }


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s",
                        stream=sys.stdout)
    conn = sqlite3.connect(config.DB_PATH)
    for label, external in (("sample graph", False), ("with external nodes", True)):
        G = build_graph(conn, include_external=external)
        groups = find_cycle_groups(G)
        removed = break_cycles(G) if groups else []
        print(f"{label}:")
        for key, value in describe(G).items():
            print(f"  {key:<24} {value}")
        print(f"  cycles found/broken       {len(groups)} / {len(removed)}")


if __name__ == "__main__":
    main()
