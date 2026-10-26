"""Model families via community detection (Louvain).

    python -m mining.communities

Louvain, in brief: modularity Q measures how many more edges fall *inside*
communities than you'd expect if edges were placed at random with the same
node degrees:

    Q = (1 / 2m) * sum over pairs (i, j) in the same community of [ A_ij - k_i * k_j / 2m ]

    A_ij  1 if i and j are linked, else 0
    k_i   degree of i
    m     number of edges

Louvain repeats two steps: (1) move each node to whichever neighbouring
community raises Q most; (2) collapse each community into a single node and
repeat on the smaller graph. It stops when no move raises Q.

It runs on the *undirected* projection: "same family" doesn't depend on which
way the derivation went. We use networkx's implementation with a fixed seed,
because Louvain's node order is random and we want reproducible families.

We then compare the detected communities with the seed families the crawler
recorded. Where they disagree, it's usually because merges tie families
together.
"""
import sqlite3
from collections import Counter

import networkx as nx
import pandas as pd

import config
from mining.graph import build_graph

SEED = 42


def detect(G, resolution=1.0, seed=SEED):
    """Return communities as a list of sets, largest first."""
    if G.number_of_edges() == 0:
        return [{n} for n in G]
    communities = nx.community.louvain_communities(G.to_undirected(), resolution=resolution, seed=seed)
    return sorted(communities, key=len, reverse=True)


def community_table(G, communities):
    """One row per community: size, which seed family dominates, what's in it."""
    rows = []
    for i, members in enumerate(communities):
        sample = [n for n in members if G.nodes[n].get("in_sample")]
        families = Counter(G.nodes[n]["root"] for n in sample if G.nodes[n].get("root"))
        dominant, dominant_n = families.most_common(1)[0] if families else (None, 0)
        sub = G.subgraph(members)
        relations = Counter(d["relation"] for _, _, d in sub.edges(data=True))
        licenses = Counter(G.nodes[n].get("license_category") for n in sample)
        hub = max(members, key=lambda n: (G.in_degree(n), n))
        rows.append({
            "community": i,
            "size": len(members),
            "in_sample": len(sample),
            "dominant_family": dominant,
            # share of the community's scraped models that come from that family
            "purity": dominant_n / len(sample) if sample else None,
            "families": len(families),
            "most_derived_from": hub,
            "internal_edges": sub.number_of_edges(),
            **{f"rel_{r}": relations.get(r, 0) for r in config.RELATIONS},
            "top_license_category": licenses.most_common(1)[0][0] if licenses else None,
        })
    return pd.DataFrame(rows)


def summary(G, communities):
    """Headline numbers: how many families, how good the split is, how pure."""
    table = community_table(G, communities)
    sampled = table[table["in_sample"] > 0]
    return {
        "communities": len(communities),
        "modularity": nx.community.modularity(G.to_undirected(), communities) if G.number_of_edges() else None,
        "largest": int(table["size"].max()) if len(table) else 0,
        "weighted_purity": float((sampled["purity"] * sampled["in_sample"]).sum() / sampled["in_sample"].sum())
        if len(sampled) else None,
        "multi_family_communities": int((sampled["families"] > 1).sum()),
    }


def cross_family_links(G):
    """Edges whose two ends were reached from *different* seeds, i.e. the
    models (nearly always merges) that tie families together."""
    rows = []
    for child, parent, d in G.edges(data=True):
        c_root, p_root = G.nodes[child].get("root"), G.nodes[parent].get("root")
        if c_root and p_root and c_root != p_root:
            rows.append({"child": child, "parent": parent, "relation": d["relation"],
                         "child_family": c_root, "parent_family": p_root})
    return pd.DataFrame(rows, columns=["child", "parent", "relation", "child_family", "parent_family"])


def main():
    conn = sqlite3.connect(config.DB_PATH)
    pd.set_option("display.width", 220)
    for label, external in (("sample graph", False), ("all known edges", True)):
        G = build_graph(conn, include_external=external)
        communities = detect(G)
        print(f"== {label}: {summary(G, communities)}")
        print(community_table(G, communities).head(15).to_string(index=False))
    print(cross_family_links(build_graph(conn)).to_string(index=False))


if __name__ == "__main__":
    main()
