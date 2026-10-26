"""Export the lineage data for the Model Lineage Explorer (site/).

    python -m viz.site_data          # writes site/data.js

The page is static, so everything it needs ships as one script that sets
`window.LINEAGE`. Arrays instead of objects keep it small (field order is in
`fields`). Models we only saw in a listing (not scraped) are included by id,
so chains and children can name them, but they have no metadata.
"""
import json
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone

import config
from mining.graph import break_cycles, build_graph, find_cycle_groups
from mining.ranking import weighted_pagerank
from viz.palette import SEED_FAMILY

OUT = config.ROOT / "site" / "data.js"
RELATIONS = list(config.RELATIONS) + ["unknown"]
MODEL_FIELDS = ["license", "license_category", "task", "task_source", "downloads", "likes",
                "created_month", "gated", "seed", "hf_children_total", "hf_children", "depth",
                "created_at_is_floor"]
# Quality issues the page explains (per model); edge-level ones travel as edge flags.
ISSUES = ("declared_base_not_linked", "declared_base_renamed", "parse_error")


def export(conn):
    G = build_graph(conn, include_external=True)
    if find_cycle_groups(G):
        break_cycles(G)
    scores, _ = weighted_pagerank(G)

    ids = sorted(G, key=lambda n: -scores[n])          # index 0 = most influential
    index = {n: i for i, n in enumerate(ids)}
    seeds = list(SEED_FAMILY)

    models = []
    for n in ids:
        a = G.nodes[n]
        if not a.get("in_sample"):
            models.append(None)
            continue
        kids = a.get("hf_children") or {}
        models.append([
            a.get("license"), a.get("license_category"), a.get("pipeline_tag"),
            {"own": "o", "inherited": "i"}.get(a.get("pipeline_tag_source"), "n"),
            a.get("downloads"), a.get("likes"), a.get("created_month"), a.get("gated"),
            seeds.index(a["root"]) if a.get("root") in seeds else None,
            a.get("hf_children_total"), [kids.get(r) or 0 for r in config.RELATIONS],
            a.get("depth"), a.get("created_at_is_floor"),
        ])

    edges = []
    for child, parent, d in G.edges(data=True):
        flags = (1 if d.get("temporal_anomaly") else 0) | (2 if d.get("in_tags") else 0) \
            | (4 if d.get("in_listing") else 0)
        edges += [index[child], index[parent], RELATIONS.index(d["relation"]), flags]

    conn.row_factory = None          # build_graph switched it to sqlite3.Row
    issues = defaultdict(list)
    for entity, issue, detail in conn.execute(
            f"SELECT entity_id, issue, detail FROM quality_issues WHERE issue IN ({','.join('?' * len(ISSUES))})",
            ISSUES):
        if entity in index:
            issues[index[entity]].append([issue, detail])

    scraped = sum(1 for m in models if m)
    return {
        "meta": {
            "generated": datetime.now(timezone.utc).isoformat(timespec="minutes"),
            "scraped": scraped, "known": len(ids), "edges": len(edges) // 4,
            "scraped_dates": list(conn.execute("SELECT MIN(scraped_at), MAX(scraped_at) FROM clean_models").fetchone()),
            "seeds": seeds, "families": [SEED_FAMILY[s] for s in seeds],
            "relations": RELATIONS, "fields": MODEL_FIELDS,
        },
        "ids": ids,
        "pr": [float(f"{scores[n]:.4g}") for n in ids],
        "m": models,
        "e": edges,
        "q": issues,
    }


def main():
    conn = sqlite3.connect(config.DB_PATH)
    data = export(conn)
    OUT.parent.mkdir(exist_ok=True)
    payload = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    OUT.write_text(f"window.LINEAGE={payload};\n", encoding="utf-8")
    print(f"{OUT}  ({OUT.stat().st_size / 1e6:.1f} MB, {data['meta']['scraped']:,} scraped, "
          f"{data['meta']['known']:,} known models, {data['meta']['edges']:,} edges)")


if __name__ == "__main__":
    main()
