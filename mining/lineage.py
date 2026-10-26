"""Lineage statistics: derivation depth, branching factor, relation shares.

    python -m mining.lineage

Generation of a model = length of the longest chain of "derived from" links
from it up to a model with no parent in the graph:
    generation(v) = 0                                  if v has no parents
                  = 1 + max(generation(p) for parents p)  otherwise
"Longest" because a merge of a base (gen 0) and a fine-tune (gen 1) is a
generation-2 model: it sits below both.

Computed in one pass over a topological order (every parent before its
children), which needs a DAG. A graph with cycles gets them broken first
(mining.graph.break_cycles).

Two kinds of numbers, kept apart on purpose:
  - observed: counted in our graph. Limited by the crawl's caps and depth.
  - HF-reported: each scraped model's own Model-tree counts. Exact, not
    sampled. Use these for population claims (branching factor, relation share).
"""
import sqlite3
import statistics

import networkx as nx
import pandas as pd

import config
from mining.graph import break_cycles, build_graph


def generations(G):
    """{node: generation}. Edges point child -> parent, so parents are successors."""
    if not nx.is_directed_acyclic_graph(G):
        G = G.copy()
        break_cycles(G)
    gen = {}
    # topological_sort lists each child before its parents; reversed = parents first
    for node in reversed(list(nx.topological_sort(G))):
        parents = list(G.successors(node))
        gen[node] = 1 + max(gen[p] for p in parents) if parents else 0
    return gen


def depth_summary(G):
    gen = generations(G)
    derived = [g for g in gen.values() if g > 0]
    return {
        "max_generation": max(gen.values(), default=0),
        "mean_generation_of_derived": statistics.mean(derived) if derived else 0,
        "models_per_generation": dict(sorted(pd.Series(list(gen.values())).value_counts().items())),
    }


def generation_table(G):
    """Per generation: how many models, and how many children each has (HF counts)."""
    gen = generations(G)
    rows = []
    for g in sorted(set(gen.values())):
        nodes = [n for n in gen if gen[n] == g and G.nodes[n].get("in_sample")]
        known = [G.nodes[n]["hf_children_total"] for n in nodes
                 if G.nodes[n].get("hf_children_total") is not None]
        rel_totals = {r: sum(G.nodes[n].get("hf_children", {}).get(r) or 0 for n in nodes)
                      for r in config.RELATIONS}
        rows.append({
            "generation": g,
            "models": len(nodes),
            "with_children": sum(1 for k in known if k > 0),
            "share_with_children": sum(1 for k in known if k > 0) / len(known) if known else None,
            # branching factor = mean number of direct children (HF's exact counts)
            "branching_mean": statistics.mean(known) if known else None,
            "branching_median": statistics.median(known) if known else None,
            "branching_max": max(known) if known else None,
            "observed_children_mean": statistics.mean(G.in_degree(n) for n in nodes) if nodes else None,
            **{f"hf_{r}": rel_totals[r] for r in config.RELATIONS},
        })
    return pd.DataFrame(rows)


def relation_shares(G):
    """Share of each relation type, two ways.

    population: sum of HF's per-relation child counts over every scraped model
                (exact for those models' direct children)
    sample:     edges in our graph (biased: the crawler gives each relation an
                equal turn, so merges and quantizations are over-represented)
    """
    population = {r: sum(G.nodes[n].get("hf_children", {}).get(r) or 0
                         for n in G if G.nodes[n].get("in_sample")) for r in config.RELATIONS}
    sample = {r: sum(1 for _, _, d in G.edges(data=True) if d["relation"] == r) for r in config.RELATIONS}
    df = pd.DataFrame({"population_count": population, "sample_edges": sample})
    df["population_share"] = df["population_count"] / max(df["population_count"].sum(), 1)
    df["sample_share"] = df["sample_edges"] / max(df["sample_edges"].sum(), 1)
    df.index.name = "relation"
    return df.reset_index()


def main():
    conn = sqlite3.connect(config.DB_PATH)
    pd.set_option("display.width", 220)
    G = build_graph(conn)
    print(depth_summary(G))
    print(generation_table(G).to_string(index=False))
    print(relation_shares(G).to_string(index=False))


if __name__ == "__main__":
    main()
