"""Influence ranking: PageRank and HITS, implemented by hand and checked
against networkx.

    python -m mining.ranking

Edges point child -> parent ("is derived from"), so both algorithms push
importance towards the base models that others build on.
"""
import logging
import sqlite3

import networkx as nx
import pandas as pd

import config
from mining.graph import build_graph

log = logging.getLogger(__name__)


# ============================================================================
# PageRank: the math
# ----------------------------------------------------------------------------
# Edge u -> v means "u is derived from v". Picture a random surfer that starts
# on a random model. At every step:
#   - with probability d (the damping factor, 0.85) it follows one of the
#     current model's parent links, chosen uniformly ("what was this built on?");
#   - with probability 1 - d it gets bored and jumps to a random model.
# PR(v) = the long-run fraction of time the surfer spends on v.
#
#     PR(v) = (1 - d) / N  +  d * ( sum over u -> v of PR(u) / out(u)   +   D / N )
#
#     N       number of models
#     out(u)  number of parents of u (u's rank is split evenly between them)
#     D       total rank currently on "dangling" models, i.e. models with no
#             parent in the graph (the base models). The surfer can't follow a
#             link out of them, so it teleports, and their rank is spread evenly
#             over all N models.
#
# Power iteration: start with PR = 1/N for everyone; compute every node's new
# value from the *previous* round's values; repeat until the total change
# sum |PR_new - PR_old| < tol. The ranks always sum to 1. This always converges:
# the random jump makes the walk able to reach every node from every node, and
# the error shrinks by about a factor d (0.85) per round.
#
# Why it fits lineage: a base scores high if many models derive from it, and
# higher still if *those* models are themselves popular bases. A fine-tune of a
# fine-tune passes rank up the chain to the original.
# ============================================================================

def pagerank(G, d=0.85, tol=1e-12, max_iter=1000, stands_for=None):
    """Return ({node: score}, iterations used).

    stands_for: optional node attribute saying how many real models a node
    represents (default 1). It sets the node's share of the random jump; see
    weighted_pagerank below. With every node at 1 this is plain PageRank.
    """
    nodes = list(G)
    if not nodes:
        return {}, 0
    m = {v: (G.nodes[v].get(stands_for, 1) if stands_for else 1) for v in nodes}
    total = sum(m.values())
    out_degree = {u: G.out_degree(u) for u in nodes}
    dangling = [u for u in nodes if out_degree[u] == 0]
    pr = {v: m[v] / total for v in nodes}

    for iteration in range(1, max_iter + 1):
        # rank that teleports this round: the (1-d) jump plus everything on dangling nodes
        jump = (1 - d) + d * sum(pr[u] for u in dangling)
        new = {}
        for v in nodes:
            incoming = sum(pr[u] / out_degree[u] for u in G.predecessors(v))
            new[v] = jump * m[v] / total + d * incoming
        change = sum(abs(new[v] - pr[v]) for v in nodes)
        pr = new
        if change < tol:
            return pr, iteration
    log.warning("PageRank did not converge in %d iterations (change %.2e)", max_iter, change)
    return pr, max_iter


# ============================================================================
# Weighted PageRank: correcting for the crawl cap
# ----------------------------------------------------------------------------
# The crawler reads at most 300 children per (parent, relation). So
# bert-base-uncased has 7 033 fine-tunes on HF but only 300 in our graph, and
# plain PageRank sees BERT as no bigger than a base with 300.
#
# Why ordinary edge weights don't fix it: in weighted PageRank a node splits its
# rank over its out-edges in proportion to their weights. But most models have
# exactly one parent, so that one edge gets 100 % whatever its weight. The cap
# doesn't distort how rank is *split*; it removes the *sources* of rank (the
# unscraped children).
#
# So we put them back. For every scraped parent p and relation r:
#     missing = HF's count of p's r-children  -  how many of them are in our graph
# and add ONE virtual node "[missing unscraped r of p]" with an edge to p. It
# stands for `missing` models: it gets `missing` times an ordinary node's share
# of the random jump. In the formula, m(v) = how many models v stands for
# (1 for real nodes), M = sum of all m(v), D = rank on dangling nodes:
#
#     PR(v) = [ (1 - d) + d * D ] * m(v) / M   +   d * sum over u -> v of PR(u) / out(u)
#
# With every m(v) = 1 this is exactly the plain PageRank above.
#
# This is exact if the unscraped children are leaves (no children of their
# own), because then `missing` identical leaves behave exactly like one node
# weighted `missing` times. That's a reasonable assumption: the crawler takes
# the most-downloaded children first, and those are the ones that tend to
# have children. 68 % of the depth-1 models we did scrape have none. It is
# checked against networkx's personalised PageRank in compare_with_networkx.
# ============================================================================

def add_unsampled_children(G):
    """Copy of G plus one virtual node per (parent, relation) for the children
    HF reports but the crawl didn't sample."""
    H = G.copy()
    for parent, attrs in G.nodes(data=True):
        for relation, hf_count in (attrs.get("hf_children") or {}).items():
            if hf_count is None:
                continue
            seen = sum(1 for child in G.predecessors(parent) if G[child][parent]["relation"] == relation)
            missing = hf_count - seen
            if missing > 0:
                virtual = f"[{missing} unscraped {relation} of {parent}]"
                H.add_node(virtual, in_sample=False, virtual=True, stands_for=missing)
                H.add_edge(virtual, parent, relation=relation, relations=[relation],
                           in_tags=False, in_listing=False, temporal_anomaly=False)
    return H


def weighted_pagerank(G, d=0.85, tol=1e-12, max_iter=1000):
    """PageRank with the unscraped children added back. Returns ({node: score}
    for G's own nodes, iterations). Scores sum to < 1: the rest sits on the
    virtual nodes."""
    H = add_unsampled_children(G)
    pr, iterations = pagerank(H, d=d, tol=tol, max_iter=max_iter, stands_for="stands_for")
    return {n: pr[n] for n in G}, iterations


# ============================================================================
# HITS (Kleinberg's hubs and authorities): the math
# ----------------------------------------------------------------------------
# Two scores per model, defined in terms of each other:
#   authority a(v): v is pointed to by good hubs, i.e. "a foundational model"
#   hub       h(u): u points to good authorities, i.e. "built on many important
#                   bases". In lineage this is mostly merges with many parents.
#
#     a(v) = sum over u -> v of h(u)        (matrix form: a = A^T h)
#     h(u) = sum over u -> v of a(v)        (matrix form: h = A a)
#
# Each round applies both updates and rescales each vector to sum to 1 (they
# would grow without limit otherwise). This is power iteration, and it converges
# to the principal eigenvectors of A^T A (authorities) and A A^T (hubs).
#
# How it differs from PageRank, and why both are reported:
#   - There is no random jump, so models outside the dominant, most densely
#     linked cluster can end up with ~0 score. HITS rewards one tight core.
#   - If the top eigenvalue is (nearly) tied, e.g. two equally big disconnected
#     families, the result depends on the starting vector and convergence is
#     slow. hits_eigengap() measures this so we know when to trust HITS.
# ============================================================================

def hits(G, tol=1e-10, max_iter=10_000):
    """Return (hubs, authorities, iterations used).

    The iteration limit is high on purpose: on a graph whose families are all
    about the same size (our fair sample) the eigengap is tiny, and HITS needs
    thousands of rounds (see hits_eigengap).
    """
    nodes = list(G)
    if not nodes:
        return {}, {}, 0
    h = dict.fromkeys(nodes, 1.0 / len(nodes))
    a = dict.fromkeys(nodes, 0.0)
    for iteration in range(1, max_iter + 1):
        a = _normalise({v: sum(h[u] for u in G.predecessors(v)) for v in nodes})
        new_h = _normalise({u: sum(a[v] for v in G.successors(u)) for u in nodes})
        change = sum(abs(new_h[u] - h[u]) for u in nodes)
        h = new_h
        if change < tol:
            return h, a, iteration
    log.warning("HITS did not converge in %d iterations (change %.2e); "
                "check hits_eigengap()", max_iter, change)
    return h, a, max_iter


def _normalise(scores):
    total = sum(scores.values())
    return {k: v / total for k, v in scores.items()} if total else scores


def hits_eigengap(G):
    """sigma_2 / sigma_1 of the adjacency matrix: near 1 means HITS is unreliable.

    HITS converges at rate (sigma_2 / sigma_1)^2 per round, and if the two are
    equal the answer isn't unique. Diagnostic only (uses scipy).
    """
    import numpy as np
    from scipy.sparse.linalg import svds
    if G.number_of_edges() < 2 or G.number_of_nodes() < 3:
        return None
    A = nx.to_scipy_sparse_array(G, dtype=float)
    sigma = np.sort(svds(A, k=2, return_singular_vectors=False))[::-1]
    return float(sigma[1] / sigma[0]) if sigma[0] else None


# ---- verification against networkx ---------------------------------------------

def compare_with_networkx(G, d=0.85):
    """How close are our implementations to networkx's? One row per algorithm."""
    rows = []
    ours_pr, iters = pagerank(G, d=d)
    nx_pr = nx.pagerank(G, alpha=d, tol=1e-12, max_iter=1000)
    rows.append(_agreement("PageRank", ours_pr, nx_pr, iters))

    # Weighted: networkx's personalised PageRank with the jump (and dangling
    # rank) distributed in proportion to how many models each node stands for.
    H = add_unsampled_children(G)
    m = {v: H.nodes[v].get("stands_for", 1) for v in H}
    ours_w, iters = pagerank(H, d=d, stands_for="stands_for")
    nx_w = nx.pagerank(H, alpha=d, personalization=m, dangling=m, tol=1e-12, max_iter=1000)
    rows.append(_agreement("Weighted PageRank", ours_w, nx_w, iters))

    hubs, auth, iters = hits(G)
    try:
        # networkx's tol is per node, ours is the total change, hence the scaling
        nx_hubs, nx_auth = nx.hits(G, max_iter=10_000, tol=1e-10 / max(len(G), 1))
        rows.append(_agreement("HITS authority", auth, nx_auth, iters))
        rows.append(_agreement("HITS hub", hubs, nx_hubs, iters))
    except nx.PowerIterationFailedConvergence:
        rows += [{"algorithm": name, "iterations": iters, "note": "networkx did not converge"}
                 for name in ("HITS authority", "HITS hub")]
    df = pd.DataFrame(rows)
    df["hits_eigengap"] = [None, None, *[hits_eigengap(G)] * 2]
    return df


def _agreement(name, ours, theirs, iterations, top=20):
    ours_s, theirs_s = pd.Series(ours), pd.Series(theirs).reindex(list(ours))
    top_ours = set(ours_s.nlargest(top).index)
    top_theirs = set(theirs_s.nlargest(top).index)
    return {
        "algorithm": name,
        "iterations": iterations,
        "max_abs_diff": float((ours_s - theirs_s).abs().max()),
        f"top{top}_overlap": len(top_ours & top_theirs),
        "spearman": float(ours_s.corr(theirs_s, method="spearman")),
    }


# ---- the report table ----------------------------------------------------------

def ranking_table(G, n=20, by="weighted_pagerank"):
    """Top-n models by `by` ('weighted_pagerank' or 'pagerank'), with all scores."""
    scores = {"pagerank": pagerank(G)[0], "weighted_pagerank": weighted_pagerank(G)[0]}
    pr, wpr = scores["pagerank"], scores["weighted_pagerank"]
    plain_rank = {m: i for i, m in enumerate(sorted(pr, key=pr.get, reverse=True), start=1)}
    hubs, auth, _ = hits(G)
    rows = []
    for model in sorted(scores[by], key=scores[by].get, reverse=True)[:n]:
        attrs = G.nodes[model]
        rows.append({
            "model": model,
            "weighted_pagerank": wpr[model],
            "pagerank": pr[model],
            "plain_pagerank_rank": plain_rank[model],
            "authority": auth[model],
            "hub": hubs[model],
            "derivatives_in_graph": G.in_degree(model),
            "hf_children_total": attrs.get("hf_children_total"),
            "family": attrs.get("root"),
            "license": attrs.get("license"),
            "in_sample": attrs.get("in_sample"),
        })
    df = pd.DataFrame(rows)
    df.index = range(1, len(df) + 1)
    df.index.name = "rank"
    return df


def top_hubs(G, n=10):
    """Models that point to the most important bases: in practice, merges."""
    hubs, _, _ = hits(G)
    return pd.DataFrame([{"model": m, "hub": hubs[m], "parents": G.out_degree(m)}
                         for m in sorted(hubs, key=hubs.get, reverse=True)[:n]])


def main():
    conn = sqlite3.connect(config.DB_PATH)
    pd.set_option("display.width", 200)
    for label, external in (("sample graph", False), ("all known edges", True)):
        G = build_graph(conn, include_external=external)
        print(f"== {label}: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
        print(compare_with_networkx(G).to_string(index=False))
        print(ranking_table(G).to_string())
        print()


if __name__ == "__main__":
    main()
