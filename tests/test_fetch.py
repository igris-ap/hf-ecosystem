"""Fetcher tests with a fake HTTP session and a fake clock: no network, no
real sleeping, but the same code paths the crawler uses."""
import pytest
import requests

from crawler.fetch import Fetcher, RobotsDisallowed

URL = "https://huggingface.co/org/model"


class FakeResponse:
    def __init__(self, status, body=b"", url=None, headers=None):
        self.status_code = status
        self.content = body
        self.url = url
        self.headers = headers or {}


class FakeSession:
    """Returns queued responses per URL; an Exception in the queue is raised."""
    def __init__(self, responses):
        self.queues = {url: list(items) for url, items in responses.items()}
        self.calls = []
        self.headers = {}

    def get(self, url, timeout):
        self.calls.append(url)
        item = self.queues[url].pop(0)
        if isinstance(item, Exception):
            raise item
        item.url = item.url or url
        return item


class FakeClock:
    def __init__(self):
        self.t = 1000.0
        self.sleeps = []

    def now(self):
        return self.t

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.t += seconds


def make_fetcher(tmp_path, responses, check_robots=False, **kw):
    clock = FakeClock()
    session = FakeSession(responses)
    f = Fetcher(cache_dir=tmp_path, session=session, check_robots=check_robots,
                sleep=clock.sleep, clock=clock.now, **kw)
    return f, session, clock


def test_sets_user_agent(tmp_path):
    f, session, _ = make_fetcher(tmp_path, {}, user_agent="test-agent/1.0")
    assert session.headers["User-Agent"] == "test-agent/1.0"


def test_success_is_cached_and_never_refetched(tmp_path):
    f, session, _ = make_fetcher(tmp_path, {URL: [FakeResponse(200, b"<html>hi</html>")]})
    first = f.get(URL)
    second = f.get(URL)
    assert first.ok and not first.from_cache
    assert second.from_cache and second.text == "<html>hi</html>"
    assert second.fetched_at == first.fetched_at
    assert session.calls == [URL]


def test_cache_is_stored_compressed(tmp_path):
    page = b"<html>" + b"model card " * 1000 + b"</html>"
    f, _, _ = make_fetcher(tmp_path, {URL: [FakeResponse(200, page)]})
    f.get(URL)
    body_path, _ = f._paths(URL)
    assert body_path.name.endswith(".body.gz")
    assert body_path.stat().st_size < len(page) / 10
    assert f.get(URL).body == page


def test_atomic_write_retries_when_file_is_briefly_locked(tmp_path, monkeypatch):
    import os
    from crawler import fetch
    real_replace, calls = os.replace, []

    def flaky_replace(src, dst):      # first attempt fails like WinError 32
        calls.append(dst)
        if len(calls) == 1:
            raise PermissionError("in use by another process")
        real_replace(src, dst)

    monkeypatch.setattr(fetch.os, "replace", flaky_replace)
    monkeypatch.setattr(fetch.time, "sleep", lambda s: None)
    fetch._atomic_write(tmp_path / "x.body.gz", b"data")
    assert (tmp_path / "x.body.gz").read_bytes() == b"data"
    assert len(calls) == 2


def test_cache_survives_restart(tmp_path):
    # Resumability: a brand-new Fetcher on the same cache dir doesn't re-download.
    f1, _, _ = make_fetcher(tmp_path, {URL: [FakeResponse(200, b"page")]})
    f1.get(URL)
    f2, session2, _ = make_fetcher(tmp_path, {URL: []})
    assert f2.get(URL).body == b"page"
    assert session2.calls == []


def test_half_written_entry_counts_as_missing(tmp_path):
    f, session, _ = make_fetcher(tmp_path, {URL: [FakeResponse(200, b"new")]})
    body_path, _ = f._paths(URL)
    body_path.write_bytes(b"partial")    # crash after body, before .json
    assert f.get(URL).body == b"new"
    assert session.calls == [URL]


def test_redirect_final_url_is_kept(tmp_path):
    canonical = "https://huggingface.co/google-bert/bert-base-uncased"
    legacy = "https://huggingface.co/bert-base-uncased"
    f, _, _ = make_fetcher(tmp_path, {legacy: [FakeResponse(200, b"x", url=canonical)]})
    assert f.get(legacy).final_url == canonical
    assert f.get(legacy).final_url == canonical   # also from cache


@pytest.mark.parametrize("status", [400, 401, 404])
def test_terminal_errors_are_not_retried_and_are_cached(tmp_path, status):
    f, session, clock = make_fetcher(tmp_path, {URL: [FakeResponse(status)]})
    assert f.get(URL).status == status
    assert f.get(URL).from_cache
    assert session.calls == [URL]
    assert clock.sleeps == []


def test_429_backs_off_then_succeeds(tmp_path):
    f, session, clock = make_fetcher(
        tmp_path, {URL: [FakeResponse(429), FakeResponse(503), FakeResponse(200, b"ok")]},
        min_interval=0)
    r = f.get(URL)
    assert r.status == 200
    assert clock.sleeps == [2.0, 4.0]        # exponential: 2^1, 2^2
    assert f.stats["retries"] == 2


def test_retry_after_header_is_respected(tmp_path):
    f, _, clock = make_fetcher(
        tmp_path, {URL: [FakeResponse(429, headers={"Retry-After": "30"}), FakeResponse(200)]},
        min_interval=0)
    f.get(URL)
    assert clock.sleeps == [30.0]


def test_connection_error_is_retried(tmp_path):
    f, _, _ = make_fetcher(
        tmp_path, {URL: [requests.ConnectionError("reset"), FakeResponse(200, b"ok")]})
    assert f.get(URL).body == b"ok"


def test_gives_up_after_max_retries_and_does_not_cache(tmp_path):
    f, session, clock = make_fetcher(
        tmp_path, {URL: [FakeResponse(503)] * 3 + [FakeResponse(200, b"later")]},
        max_retries=2, min_interval=0)
    r = f.get(URL)
    assert r.status == 503 and not r.ok
    assert len(session.calls) == 3
    assert clock.sleeps == [2.0, 4.0]
    # not cached, so a later run (e.g. after resume) tries again
    assert f.get(URL).body == b"later"


def test_rate_limit_between_requests(tmp_path):
    a, b = URL + "/a", URL + "/b"
    f, _, clock = make_fetcher(tmp_path, {a: [FakeResponse(200)], b: [FakeResponse(200)]},
                               min_interval=1.0)
    f.get(a)
    f.get(b)
    assert clock.sleeps == [1.0]


def test_pauses_when_rate_limit_window_is_used_up(tmp_path):
    a, b, c = URL + "/a", URL + "/b", URL + "/c"
    f, _, clock = make_fetcher(tmp_path, {
        a: [FakeResponse(200, headers={"RateLimit": '"pages";r=5;t=200'})],
        b: [FakeResponse(200, headers={"RateLimit": '"pages";r=0;t=120'})],
        c: [FakeResponse(200)],
    }, min_interval=0)
    f.get(a)
    f.get(b)
    assert clock.sleeps == []          # quota left after a: no pause
    f.get(c)
    assert clock.sleeps == [121.0]     # waited for the window to reset (+1 s margin), no 429
    assert f.stats["quota_pauses"] == 1


def test_cache_hits_are_not_rate_limited(tmp_path):
    f, _, clock = make_fetcher(tmp_path, {URL: [FakeResponse(200)]}, min_interval=1.0)
    f.get(URL)
    for _ in range(5):
        f.get(URL)
    assert clock.sleeps == []


# ---- robots.txt --------------------------------------------------------------

ROBOTS = "https://huggingface.co/robots.txt"


def test_robots_disallow_is_enforced(tmp_path):
    robots = FakeResponse(200, b"User-agent: *\nDisallow: /private/\n")
    f, session, _ = make_fetcher(tmp_path, {ROBOTS: [robots], URL: [FakeResponse(200)]},
                                 check_robots=True)
    with pytest.raises(RobotsDisallowed):
        f.get("https://huggingface.co/private/secret")
    assert f.get(URL).ok
    assert session.calls == [ROBOTS, URL]     # robots.txt read once, disallowed URL never requested


def test_real_hf_robots_allows_our_urls(tmp_path, load_sample):
    robots = FakeResponse(200, load_sample("robots.txt").encode())
    listing = "https://huggingface.co/models?other=base_model:finetune:a/b&sort=downloads"
    f, _, _ = make_fetcher(tmp_path, {ROBOTS: [robots], URL: [FakeResponse(200)],
                                      listing: [FakeResponse(200)]}, check_robots=True)
    assert f.get(URL).ok and f.get(listing).ok


def test_missing_robots_means_allowed(tmp_path):
    f, _, _ = make_fetcher(tmp_path, {ROBOTS: [FakeResponse(404)], URL: [FakeResponse(200)]},
                           check_robots=True)
    assert f.get(URL).ok


def test_unreadable_robots_stops_the_crawl(tmp_path):
    f, _, _ = make_fetcher(tmp_path, {ROBOTS: [FakeResponse(503)] * 2}, check_robots=True,
                           max_retries=1)
    with pytest.raises(RuntimeError):
        f.get(URL)
