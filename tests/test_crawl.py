"""Crawler tests against a small fake Hugging Face, served through the real
Fetcher and cache, so resume and no-refetch behaviour are tested for real."""
import pytest

from config import BASE_URL
from crawler.crawl import add_seeds, connect, crawl, round_robin, select_fair
from crawler.fetch import Fetcher
from crawler.parse_listing import listing_url
from tests.conftest import make_page


class FakeHub:
    """A tiny fake site: model pages + paginated listings, built from a lineage dict."""

    def __init__(self):
        self.pages = {}
        self.calls = []
        self.headers = {}
        self.crash_after = None

    def add(self, model_id, parents=(), children=None, url_id=None):
        """children = {relation: [child ids]} (that's what the listings will show)."""
        children = children or {}
        tags = []
        for parent, rel in parents:
            tags += [f"base_model:{parent}", f"base_model:{rel}:{parent}"]
        props = {"model": {"id": model_id, "author": model_id.split("/")[0], "tags": tags,
                           "downloads": 1, "likes": 0, "createdAt": "2025-01-01T00:00:00.000Z",
                           "cardData": {}}}
        tree = "".join(f'<a href="/models?other=base_model:{rel}:{model_id}">{len(ids)} models</a>'
                       for rel, ids in children.items() if ids)
        self.pages[f"{BASE_URL}/{url_id or model_id}"] = make_page("ModelHeader", props).replace(
            "</body>", tree + "</body>")
        for rel, ids in children.items():
            for page in range(0, max(1, -(-len(ids) // 30))):
                self.pages[listing_url(model_id, rel, page)] = make_page("ModelList", {"initialValues": {
                    "activeFilters": {"other": [f"base_model:{rel}:{model_id}"]},
                    "models": [{"id": c} for c in ids[page * 30:(page + 1) * 30]],
                    "numTotalItems": len(ids), "numItemsPerPage": 30, "pageIndex": page}})

    # requests.Session-like interface used by Fetcher
    def get(self, url, timeout):
        if self.crash_after is not None and len(self.calls) >= self.crash_after:
            raise RuntimeError("simulated crash")
        self.calls.append(url)
        body = self.pages.get(url)
        return _Resp(200 if body else 401, (body or "").encode(), url)


class _Resp:
    def __init__(self, status, content, url):
        self.status_code, self.content, self.url, self.headers = status, content, url, {}


def run(tmp_path, hub, seeds, max_models=100, max_depth=3, cap=300):
    conn = connect(tmp_path / "hf.db")
    add_seeds(conn, seeds)
    fetcher = Fetcher(cache_dir=tmp_path / "cache", session=hub, check_robots=False,
                      min_interval=0, sleep=lambda s: None)
    crawl(conn, fetcher, max_models, max_depth, cap)
    return conn


def done(conn):
    return {r["id"]: (r["depth"], r["root"]) for r in
            conn.execute("SELECT id, depth, root FROM crawl_queue WHERE status = 'done'")}


def edges(conn, source):
    return {tuple(r) for r in conn.execute(
        "SELECT child_id, parent_id, relation FROM edges WHERE source = ?", (source,))}


def small_hub():
    hub = FakeHub()
    hub.add("A/base", children={"finetune": ["a/1", "a/2"], "adapter": ["a/3"]})
    hub.add("a/1", parents=[("A/base", "finetune")], children={"quantized": ["a/1-q"]})
    hub.add("a/2", parents=[("A/base", "finetune")])
    hub.add("a/3", parents=[("A/base", "adapter")])
    hub.add("a/1-q", parents=[("a/1", "quantized")])
    hub.add("B/base", children={"merge": ["b/m"]})
    hub.add("b/m", parents=[("B/base", "merge"), ("A/base", "merge")])
    return hub


def test_crawls_whole_small_graph(tmp_path):
    conn = run(tmp_path, small_hub(), ["A/base", "B/base"])
    assert done(conn) == {
        "A/base": (0, "A/base"), "B/base": (0, "B/base"),
        "a/1": (1, "A/base"), "a/2": (1, "A/base"), "a/3": (1, "A/base"), "b/m": (1, "B/base"),
        "a/1-q": (2, "A/base"),
    }
    # the child's own tags know about the second merge parent; B's listing can't
    assert ("b/m", "A/base", "merge") in edges(conn, "tags")
    assert edges(conn, "listing") <= edges(conn, "tags")


def test_depth_limit(tmp_path):
    conn = run(tmp_path, small_hub(), ["A/base"], max_depth=1)
    assert max(depth for depth, _ in done(conn).values()) == 1
    assert "a/1-q" not in done(conn)


def test_budget_is_shared_fairly_between_seeds(tmp_path):
    hub = FakeHub()
    hub.add("A/base", children={"finetune": [f"a/{i}" for i in range(50)]})
    hub.add("B/base", children={"finetune": [f"b/{i}" for i in range(50)]})
    for i in range(50):
        hub.add(f"a/{i}", parents=[("A/base", "finetune")])
        hub.add(f"b/{i}", parents=[("B/base", "finetune")])
    conn = run(tmp_path, hub, ["A/base", "B/base"], max_models=12)
    roots = [root for depth, root in done(conn).values() if depth == 1]
    assert roots.count("A/base") == roots.count("B/base") == 5
    # and within a family it's the top of the (downloads-sorted) listing
    assert {"a/0", "a/1", "a/2", "a/3", "a/4"} <= set(done(conn))


def test_per_relation_cap_limits_listing_pages(tmp_path):
    hub = FakeHub()
    kids = [f"k/{i}" for i in range(95)]          # 4 listing pages
    hub.add("S/base", children={"finetune": kids})
    for k in kids:
        hub.add(k, parents=[("S/base", "finetune")])
    conn = run(tmp_path, hub, ["S/base"], max_models=10, cap=40)
    assert len(edges(conn, "listing")) == 40
    listing_calls = [u for u in hub.calls if "/models?" in u]
    assert len(listing_calls) == 2               # 30 + 30 >= 40, pages 3-4 never requested


def test_leaf_models_cost_no_listing_requests(tmp_path):
    hub = small_hub()
    run(tmp_path, hub, ["A/base", "B/base"])
    listing_calls = [u for u in hub.calls if "/models?" in u]
    # only relations shown in a model's Model tree get a listing request
    assert sorted(listing_calls) == sorted([
        listing_url("A/base", "finetune"), listing_url("A/base", "adapter"),
        listing_url("a/1", "quantized"), listing_url("B/base", "merge")])


def test_missing_child_fails_but_crawl_continues(tmp_path):
    hub = FakeHub()
    hub.add("A/base", children={"finetune": ["gone/model", "a/ok"]})
    hub.add("a/ok", parents=[("A/base", "finetune")])
    conn = run(tmp_path, hub, ["A/base"])
    failed = conn.execute("SELECT id, error FROM crawl_queue WHERE status='failed'").fetchall()
    assert [tuple(r) for r in failed] == [("gone/model", "missing_or_private")]
    assert "a/ok" in done(conn)


def test_legacy_id_is_stored_under_canonical_id(tmp_path):
    hub = FakeHub()
    hub.add("google-bert/bert-base-uncased", url_id="bert-base-uncased")
    conn = run(tmp_path, hub, ["bert-base-uncased"])
    row = conn.execute("SELECT model_id FROM crawl_queue WHERE id='bert-base-uncased'").fetchone()
    assert row["model_id"] == "google-bert/bert-base-uncased"
    assert conn.execute("SELECT id FROM models").fetchone()["id"] == "google-bert/bert-base-uncased"


def test_model_reachable_twice_is_queued_once(tmp_path):
    hub = FakeHub()
    hub.add("A/base", children={"merge": ["m/x"]})
    hub.add("B/base", children={"merge": ["m/x"]})
    hub.add("m/x", parents=[("A/base", "merge"), ("B/base", "merge")])
    conn = run(tmp_path, hub, ["A/base", "B/base"])
    assert conn.execute("SELECT COUNT(*) FROM crawl_queue WHERE id='m/x'").fetchone()[0] == 1
    assert len(edges(conn, "listing")) == 2      # but both parent->child edges are kept


# The small graph takes 11 requests; crash before each one in turn (during
# seed scraping, during listing expansion, and halfway through a level).
@pytest.mark.parametrize("crash_after", range(1, 11))
def test_resume_after_crash_refetches_nothing(tmp_path, crash_after):
    clean = run(tmp_path / "clean", small_hub(), ["A/base", "B/base"])

    hub = small_hub()
    hub.crash_after = crash_after
    with pytest.raises(RuntimeError):
        run(tmp_path / "crashy", hub, ["A/base", "B/base"])
    first_run_calls = list(hub.calls)

    hub.crash_after = None
    resumed = run(tmp_path / "crashy", hub, ["A/base", "B/base"])
    second_run_calls = hub.calls[len(first_run_calls):]
    assert not set(first_run_calls) & set(second_run_calls)   # nothing downloaded twice
    assert done(resumed) == done(clean)
    assert edges(resumed, "tags") == edges(clean, "tags")
    assert edges(resumed, "listing") == edges(clean, "listing")


def test_raising_the_budget_later_tops_up_the_same_level_first(tmp_path):
    hub = FakeHub()
    hub.add("A/base", children={"finetune": ["a/1", "a/2", "a/3"]})
    hub.add("a/1", parents=[("A/base", "finetune")], children={"finetune": ["a/1/x"]})
    hub.add("a/2", parents=[("A/base", "finetune")])
    hub.add("a/3", parents=[("A/base", "finetune")])
    hub.add("a/1/x", parents=[("a/1", "finetune")])
    run(tmp_path, hub, ["A/base"], max_models=2)
    conn = run(tmp_path, hub, ["A/base"], max_models=4)
    # BFS order holds across runs: all of level 1 before anything at level 2
    assert set(done(conn)) == {"A/base", "a/1", "a/2", "a/3"}


# ---- the selection helpers on their own ------------------------------------------

def test_round_robin():
    assert round_robin([[1, 2, 3], ["a"], [10, 20]]) == [1, "a", 10, 2, 20, 3]
    assert round_robin([]) == []


def test_select_fair_alternates_families_and_relations():
    streams = {"A": [["a-ft1", "a-ft2", "a-ft3"], ["a-ad1"]], "B": [["b-ft1", "b-ft2"]]}
    chosen = select_fair(streams, budget=5, already_queued={"b-ft1"})
    assert chosen == [("a-ft1", "A"), ("a-ad1", "A"), ("b-ft2", "B"), ("a-ft2", "A"), ("a-ft3", "A")]
