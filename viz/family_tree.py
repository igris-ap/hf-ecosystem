"""Interactive family tree (pyvis HTML) for the demo.

    python -m viz.family_tree                         # overview + one page per family
    python -m viz.family_tree --family Llama          # just one family
    python -m viz.family_tree --highlight Qwen,Gemma  # choose the coloured families
    python -m viz.family_tree --top 200               # fewer nodes for slow laptops

Encoding:
  node size   weighted PageRank (area-like: radius grows with sqrt of the score)
  node colour family, for at most 3 highlighted families; the rest are grey.
              More than 3 hues can't all be told apart in a network graph (see
              viz/palette.py), so every family is also identified by its node
              shape, a label on its seed model, and the hover tooltip. The
              per-family pages show each family on its own.
  node shape  family
  edge style  relation: finetune solid, adapter dashed, quantized dotted,
              merge dash-dot. Arrows point child -> parent ("derived from").

Responsive: only the top-N nodes by weighted PageRank are drawn, and the
physics layout is switched off once it settles, so dragging stays smooth.
Output is self-contained (vis.js inlined) so the demo works offline.
"""
import argparse
import math
import re
import sqlite3

from pyvis.network import Network

import config
from mining.graph import build_graph
from mining.ranking import weighted_pagerank
from viz.palette import (FAMILIES, INK, INK_2, MAX_NETWORK_COLOURS, MUTED, NEUTRAL, SEED_FAMILY,
                         SLOTS, SURFACE, short_name)

OUT_DIR = config.RESULTS_DIR / "tree"
SHAPES = dict(zip(FAMILIES, ["dot", "square", "triangle", "diamond", "star", "triangleDown", "hexagon"]))
DASHES = {"finetune": False, "adapter": [6, 4], "quantized": [2, 3], "merge": [10, 3, 2, 3]}
EDGE_COLOUR = "#c3c2b7"
LABEL_TOP = 12          # besides the seeds, label only the 12 highest-ranked models


def family_of(G, node):
    return SEED_FAMILY.get(G.nodes[node].get("root"))


def select_nodes(G, scores, family=None, top=300):
    nodes = [n for n in G if family is None or family_of(G, n) == family]
    return sorted(nodes, key=scores.get, reverse=True)[:top]


def build_page(G, scores, nodes, highlight, title):
    """Return a pyvis Network for the chosen nodes."""
    if len(highlight) > MAX_NETWORK_COLOURS:
        raise ValueError(f"at most {MAX_NETWORK_COLOURS} highlighted families (got {highlight})")
    colour = {fam: SLOTS[i] for i, fam in enumerate(highlight)}
    rank = {n: i for i, n in enumerate(sorted(scores, key=scores.get, reverse=True), start=1)}
    top_score = max(scores[n] for n in nodes)
    label_top = LABEL_TOP if len(nodes) > 150 else LABEL_TOP // 2
    labelled = set(sorted(nodes, key=scores.get, reverse=True)[:label_top])

    net = Network(height="820px", width="100%", directed=True, bgcolor=SURFACE, font_color=INK,
                  cdn_resources="in_line", heading="")
    for n in nodes:
        a = G.nodes[n]
        fam = family_of(G, n)
        is_seed = a.get("depth") == 0
        label = (f"{fam}: {short_name(n)}" if is_seed else short_name(n)) if (is_seed or n in labelled) else ""
        parents = [f"{p} ({d['relation']})" for p, d in G[n].items()]
        net.add_node(
            n, shape=SHAPES.get(fam, "dot"),
            size=8 + 40 * math.sqrt(scores[n] / top_score),     # >= 8 px so every model is visible
            color={"background": colour.get(fam, NEUTRAL), "border": SURFACE,
                   "highlight": {"background": colour.get(fam, NEUTRAL), "border": INK}},
            borderWidth=2,
            title="\n".join([
                n,
                f"family: {fam or 'unknown'}",
                f"derived from: {', '.join(parents) or '(base model)'}",
                f"license: {a.get('license') or 'none'}",
                f"task: {a.get('pipeline_tag') or 'unknown'}",
                f"downloads (30 d): {a.get('downloads') or 0:,}",
                f"children on HF: {a.get('hf_children_total') if a.get('hf_children_total') is not None else 'n/a'}",
                f"created: {a.get('created_month') or 'n/a'}",
                f"weighted PageRank: #{rank[n]}",
            ]),
        )
        # Set these on the stored options directly: pyvis replaces an empty label
        # with the node id (which would label all 300 nodes) and overwrites a
        # per-node font with the network's font colour.
        net.nodes[-1]["label"] = label or " "
        net.nodes[-1]["font"] = {"size": 30 if is_seed else 18, "color": INK if is_seed else INK_2,
                                 "strokeWidth": 6, "strokeColor": SURFACE}
    chosen = set(nodes)
    for child, parent, d in G.edges(data=True):
        if child in chosen and parent in chosen:
            net.add_edge(child, parent, title=d["relation"], dashes=DASHES.get(d["relation"], False),
                         color=EDGE_COLOUR, width=1.2, arrows={"to": {"enabled": True, "scaleFactor": 0.4}})
    # Big pages need short springs or the clusters drift apart and the opening
    # view is mostly empty; small pages need long ones or labels pile up.
    spring = 45 if len(nodes) > 150 else 140
    net.set_options(f"""{{
      "physics": {{"solver": "barnesHut",
                  "barnesHut": {{"gravitationalConstant": -2500, "centralGravity": 0.6,
                                "springLength": {spring}, "springConstant": 0.05, "avoidOverlap": 0.5}},
                  "stabilization": {{"iterations": 500}}}},
      "interaction": {{"hover": true, "tooltipDelay": 120, "navigationButtons": true}},
      "edges": {{"smooth": false}}
    }}""")
    return net, _legend(highlight, colour, title, len(nodes))


def _legend(highlight, colour, title, n_nodes):
    """Small HTML legend: families (colour/shape), relations (edge style)."""
    symbols = {"dot": "●", "square": "■", "triangle": "▲", "diamond": "◆", "star": "★",
               "triangleDown": "▼", "hexagon": "⬢"}
    fams = "".join(
        f'<span style="margin-right:14px;white-space:nowrap">'
        f'<span style="color:{colour.get(f, NEUTRAL)};font-size:15px">{symbols[SHAPES[f]]}</span> {f}</span>'
        for f in FAMILIES)
    rels = "".join(
        f'<span style="margin-right:14px;white-space:nowrap">'
        f'<svg width="34" height="8" style="vertical-align:middle"><line x1="0" y1="4" x2="34" y2="4" '
        f'stroke="{MUTED}" stroke-width="2" stroke-dasharray="{" ".join(map(str, dash)) if dash else "none"}"/></svg> '
        f'{rel}</span>' for rel, dash in DASHES.items())
    note = (f"Coloured: {', '.join(highlight)}. Other families in grey: tell them apart by shape, "
            f"seed label or hover." if len(highlight) > 1 else "")
    return f"""
<div style="font-family:system-ui,'Segoe UI',sans-serif;background:{SURFACE};color:{INK};padding:12px 16px 4px">
  <div style="font-size:18px;font-weight:600">{title}</div>
  <div style="font-size:13px;color:{INK_2};margin:4px 0 8px">{n_nodes} models · node size = weighted PageRank ·
    arrows point from a model to the model it was derived from · hover a node for details, scroll to zoom</div>
  <div style="font-size:13px;color:{INK_2};line-height:1.9">{fams}<br>{rels}</div>
  <div style="font-size:12px;color:{MUTED}">{note}</div>
</div>"""


# Turn physics off once the layout has settled, so dragging and zooming stay smooth.
_FREEZE = """<script>
network.once("stabilizationIterationsDone", function () { network.setOptions({physics: false}); });
</script>"""


def write(net, legend, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    html = net.generate_html()
    # pyvis's template links Bootstrap from a CDN even in "in_line" mode. It only
    # styles a card wrapper, so drop it: the page must work offline.
    html = re.sub(r'<link[^>]+bootstrap[^>]*>\s*', "", html)
    html = re.sub(r'<script[^>]+bootstrap[^>]*>\s*</script>\s*', "", html)
    html = html.replace("<body>", "<body>" + legend, 1).replace("</body>", _FREEZE + "</body>", 1)
    path.write_text(html, encoding="utf-8")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write interactive family-tree HTML pages.")
    parser.add_argument("--family", choices=FAMILIES, help="only this family")
    parser.add_argument("--highlight", help=f"comma-separated families to colour (max {MAX_NETWORK_COLOURS})")
    parser.add_argument("--top", type=int, default=300, help="max nodes per page")
    args = parser.parse_args(argv)

    conn = sqlite3.connect(config.DB_PATH)
    G = build_graph(conn)
    scores, _ = weighted_pagerank(G)

    if args.highlight:
        default_highlight = [f.strip() for f in args.highlight.split(",")]
    else:   # the three families with the most total weighted PageRank
        totals = {f: sum(s for n, s in scores.items() if family_of(G, n) == f) for f in FAMILIES}
        default_highlight = sorted(totals, key=totals.get, reverse=True)[:MAX_NETWORK_COLOURS]

    pages = []
    if args.family is None:
        nodes = select_nodes(G, scores, top=args.top)
        net, legend = build_page(G, scores, nodes, default_highlight, "Hugging Face model lineage: overview")
        pages.append(write(net, legend, OUT_DIR / "family_tree.html"))
    for fam in ([args.family] if args.family else FAMILIES):
        nodes = select_nodes(G, scores, family=fam, top=args.top)
        if nodes:
            net, legend = build_page(G, scores, nodes, [fam], f"{fam} family")
            pages.append(write(net, legend, OUT_DIR / f"family_{fam.lower()}.html"))
    for p in pages:
        print(f"{p}  ({p.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
