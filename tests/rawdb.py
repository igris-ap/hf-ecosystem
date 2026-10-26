"""Build tiny raw crawl databases (same schema as the crawler writes) for
testing preprocessing and graph building without a real crawl."""
import json

from crawler.crawl import connect


def make_db(path, models, edges, queue=None):
    """models: {id: {field: value}}; edges: [(child, parent, relation, source)];
    queue: {id: (depth, root)}, defaulting to depth 0 with each model its own root."""
    conn = connect(path)
    for rank, (mid, fields) in enumerate(models.items()):
        row = {
            "id": mid, "author": mid.split("/")[0], "license": "mit", "license_name": None,
            "pipeline_tag": "text-generation", "library_name": None, "tags_json": "[]",
            "downloads": 0, "downloads_all_time": None, "likes": 0,
            "created_at": "2025-01-01T00:00:00.000Z", "last_modified": None, "gated": "no",
            "card_base_model_json": json.dumps(fields.pop("card_base_model", [])),
            "card_base_model_relation": None, "card_datasets_json": "[]",
            "card_language_json": "[]", "children_counts_json": "{}",
            "parse_errors_json": json.dumps(fields.pop("parse_errors", [])),
            "scraped_at": "2026-10-26T00:00:00+00:00",
        }
        row.update(fields)
        conn.execute(f"INSERT INTO models ({', '.join(row)}) VALUES ({', '.join('?' * len(row))})",
                     list(row.values()))
        depth, root = (queue or {}).get(mid, (0, mid))
        conn.execute("INSERT INTO crawl_queue (id, depth, root, rank, status, model_id) "
                     "VALUES (?, ?, ?, ?, 'done', ?)", (mid, depth, root, rank, mid))
    conn.executemany("INSERT INTO edges VALUES (?, ?, ?, ?)", edges)
    conn.commit()
    return conn
