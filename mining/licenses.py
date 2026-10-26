"""License drift: does a derivative keep its parent's license?

    python -m mining.licenses

For every lineage edge where we know both licenses, compare child and parent.
License categories (from preprocess.clean) are ordered by how much they
restrict what you may do with a derivative:

    permissive (0) < copyleft (1) < restricted (2) < noncommercial (3)

    copyleft      derivatives must keep the same terms (share-alike)
    restricted    model-specific licenses with use rules (Llama, Gemma, OpenRAIL)
    noncommercial no commercial use at all

A child whose category is *lower* than its parent's claims fewer restrictions
than it inherited, e.g. a Llama fine-tune published as Apache-2.0. Most such
licenses don't allow that, so we flag it as a **likely conflict**. It's a flag,
not a legal judgement: the parent's license text decides, and some parents
(e.g. a dual-licensed one) may genuinely permit it.

'other' (custom license text) and 'unknown' (no license) can't be ordered, so
edges involving them are counted separately, not as conflicts.
"""
import sqlite3

import pandas as pd

import config
from mining.graph import build_graph

LEVEL = {"permissive": 0, "copyleft": 1, "restricted": 2, "noncommercial": 3}


def classify(child_license, child_cat, parent_license, parent_cat):
    if parent_cat == "unknown":
        return "parent_unknown"
    if child_cat == "unknown":
        return "child_unknown"            # derivative published with no license at all
    if child_license == parent_license:
        return "same"
    if child_cat in LEVEL and parent_cat in LEVEL:
        if LEVEL[child_cat] < LEVEL[parent_cat]:
            return "loosened"             # likely conflict
        if LEVEL[child_cat] > LEVEL[parent_cat]:
            return "tightened"            # allowed for permissive parents; worth noting
        return "changed_same_category"    # e.g. llama3 -> llama3.1, apache-2.0 -> mit
    return "changed_custom"               # 'other' on one side: can't be ordered


def edge_table(G):
    """One row per child -> parent edge where both models were scraped."""
    rows = []
    for child, parent, d in G.edges(data=True):
        c, p = G.nodes[child], G.nodes[parent]
        if not (c.get("in_sample") and p.get("in_sample")):
            continue
        rows.append({
            "child": child, "parent": parent, "relation": d["relation"],
            "family": c.get("root"),
            "child_license": c.get("license"), "parent_license": p.get("license"),
            "child_category": c.get("license_category"), "parent_category": p.get("license_category"),
            "outcome": classify(c.get("license"), c.get("license_category"),
                                p.get("license"), p.get("license_category")),
        })
    return pd.DataFrame(rows, columns=["child", "parent", "relation", "family", "child_license",
                                       "parent_license", "child_category", "parent_category", "outcome"])


def transition_matrix(edges):
    """Rows: parent's license category; columns: child's. Counts of edges."""
    return pd.crosstab(edges["parent_category"], edges["child_category"])


def by_group(edges, column):
    """Outcome counts per family (or per relation), plus drift and conflict rates."""
    table = pd.crosstab(edges[column], edges["outcome"])
    known = table.drop(columns=[c for c in ("parent_unknown", "child_unknown") if c in table], errors="ignore")
    table["edges"] = table.sum(axis=1)
    table["drift_rate"] = 1 - table.get("same", 0) / known.sum(axis=1).where(known.sum(axis=1) > 0)
    table["conflict_rate"] = table.get("loosened", 0) / known.sum(axis=1).where(known.sum(axis=1) > 0)
    return table.reset_index()


def conflicts(edges):
    return edges[edges["outcome"] == "loosened"].sort_values(["family", "child"]).reset_index(drop=True)


def main():
    conn = sqlite3.connect(config.DB_PATH)
    pd.set_option("display.width", 220)
    edges = edge_table(build_graph(conn))
    print(edges["outcome"].value_counts().to_string())
    print(transition_matrix(edges).to_string())
    print(by_group(edges, "family").to_string(index=False))
    print(by_group(edges, "relation").to_string(index=False))
    print(conflicts(edges)[["child", "parent", "relation", "child_license", "parent_license"]].to_string(index=False))


if __name__ == "__main__":
    main()
