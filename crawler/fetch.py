"""Polite HTTP fetcher: rate-limited, disk-cached, retrying, robots-aware.

Every page the crawler sees goes through Fetcher.get(), so the politeness
rules from docs/ethics.md are enforced in exactly one place.

Cache layout (<data dir>/cache/):
    <sha1(url)>.body.gz   response bytes, gzip-compressed (HF HTML shrinks ~4x)
    <sha1(url)>.json      {"url", "final_url", "status", "fetched_at"}
The .json is written *after* the body, so a crash mid-write leaves no .json
and the entry counts as missing. That is what makes the crawl safely
resumable.
"""
import gzip
import hashlib
import json
import logging
import os
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser

import requests
import truststore

import config

# Use the OS certificate store; some Windows machines have antivirus/proxy root
# certs that certifi doesn't ship. Certificate verification stays ON.
truststore.inject_into_ssl()

log = logging.getLogger(__name__)

_RATELIMIT_RE = re.compile(r"\br=(\d+);t=(\d+)")


# 429 and 5xx are transient: retry them and never cache them.
# Anything else (200, 400 past-last-page, 401 missing/gated, 404) won't change
# if we ask again, so it's cached like a normal page.
def _is_transient(status):
    return status == 429 or status >= 500


class RobotsDisallowed(Exception):
    """Raised instead of fetching a URL that robots.txt disallows."""


@dataclass
class FetchResult:
    url: str          # what we asked for
    final_url: str    # after redirects (legacy ids like bert-base-uncased redirect)
    status: int       # HTTP status; 0 = network failure after all retries
    body: bytes
    from_cache: bool
    # When the page was really downloaded (UTC ISO-8601). Kept through the cache
    # so `scraped_at` stays honest: download counts are a snapshot of this moment.
    fetched_at: str = ""

    @property
    def ok(self):
        return 200 <= self.status < 300

    @property
    def text(self):
        return self.body.decode("utf-8", errors="replace")


class Fetcher:
    def __init__(
        self,
        cache_dir=config.CACHE_DIR,
        session=None,
        min_interval=config.MIN_REQUEST_INTERVAL,
        max_retries=config.MAX_RETRIES,
        backoff_base=config.BACKOFF_BASE,
        timeout=config.REQUEST_TIMEOUT,
        user_agent=config.USER_AGENT,
        check_robots=True,
        sleep=time.sleep,
        clock=time.monotonic,
    ):
        # sleep/clock are injectable so tests can run instantly with no network.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.session = session or requests.Session()
        self.session.headers["User-Agent"] = user_agent
        self.user_agent = user_agent
        self.min_interval = min_interval
        self.max_retries = max_retries
        self.backoff_base = backoff_base
        self.timeout = timeout
        self.check_robots = check_robots
        self._sleep = sleep
        self._clock = clock
        self._last_request = None
        self._quota_resets_at = None   # set when HF says our rate-limit window is used up
        self._robots = {}  # host -> RobotFileParser, loaded once per run
        self.stats = {"network": 0, "cache_hits": 0, "retries": 0, "quota_pauses": 0}

    # ---- public -----------------------------------------------------------

    def get(self, url):
        """Return the page for `url`, from cache if we've ever fetched it."""
        cached = self._read_cache(url)
        if cached is not None:
            self.stats["cache_hits"] += 1
            return cached

        if self.check_robots and not self._allowed(url):
            raise RobotsDisallowed(url)

        result = self._fetch_with_retries(url)
        if result.status and not _is_transient(result.status):
            self._write_cache(result)
        return result

    # ---- robots.txt ---------------------------------------------------------

    def _allowed(self, url):
        parts = urlsplit(url)
        host = f"{parts.scheme}://{parts.netloc}"
        if host not in self._robots:
            self._robots[host] = self._load_robots(host)
        return self._robots[host].can_fetch(self.user_agent, url)

    def _load_robots(self, host):
        # Re-read live at the start of every run (never from the page cache),
        # so a rule change on HF's side takes effect immediately.
        robots_url = f"{host}/robots.txt"
        result = self._fetch_with_retries(robots_url)
        parser = RobotFileParser(robots_url)
        if result.ok:
            parser.parse(result.text.splitlines())
        elif 400 <= result.status < 500:
            parser.parse([])  # standard convention: no robots.txt = everything allowed
        else:
            # Can't tell what's allowed, so refuse to crawl rather than guess.
            raise RuntimeError(f"could not read {robots_url} (status {result.status})")
        log.info("loaded %s", robots_url)
        return parser

    # ---- network ------------------------------------------------------------

    def _wait_turn(self):
        """Block until at least min_interval has passed since the last request,
        and until the server's rate-limit window has reset if we used it up."""
        if self._quota_resets_at is not None:
            wait = self._quota_resets_at - self._clock()
            if wait > 0:
                self._sleep(wait)
            self._quota_resets_at = None
        if self._last_request is not None:
            wait = self.min_interval - (self._clock() - self._last_request)
            if wait > 0:
                self._sleep(wait)
        self._last_request = self._clock()

    def _note_rate_limit(self, headers):
        """Read HF's `RateLimit: "pages";r=<remaining>;t=<seconds to reset>` header.

        HF's policy (RateLimit-Policy header) is a fixed window of 100 page
        requests per 300 s for anonymous clients. When the remaining quota
        reaches 0, we wait for the reset instead of sending a request we know
        would get a 429.
        """
        m = _RATELIMIT_RE.search(headers.get("RateLimit", ""))
        if m and int(m.group(1)) == 0:
            reset = int(m.group(2)) + 1    # +1 s margin for clock skew
            self._quota_resets_at = self._clock() + reset
            self.stats["quota_pauses"] += 1
            log.info("rate-limit window used up; pausing %d s until it resets", reset)

    def _fetch_with_retries(self, url):
        """GET with exponential backoff on 429 / 5xx / connection errors.

        Waits backoff_base**1, **2, ... seconds between attempts (2, 4, 8, ...),
        or longer if the server sends a Retry-After header.
        """
        status = 0
        for attempt in range(self.max_retries + 1):
            if attempt:
                self.stats["retries"] += 1
            self._wait_turn()
            self.stats["network"] += 1
            retry_after = None
            try:
                resp = self.session.get(url, timeout=self.timeout)
                status = resp.status_code
                self._note_rate_limit(resp.headers)
                if not _is_transient(status):
                    return FetchResult(url, resp.url, status, resp.content,
                                       from_cache=False, fetched_at=_now())
                retry_after = _parse_retry_after(resp.headers.get("Retry-After"))
                log.warning("HTTP %s for %s (attempt %d)", status, url, attempt + 1)
            except requests.RequestException as exc:
                status = 0
                log.warning("network error for %s (attempt %d): %s", url, attempt + 1, exc)

            if attempt < self.max_retries:
                delay = self.backoff_base ** (attempt + 1)
                if retry_after:
                    delay = max(delay, min(retry_after, 300))
                self._sleep(delay)

        log.error("giving up on %s after %d attempts (last status %s)",
                  url, self.max_retries + 1, status)
        return FetchResult(url, url, status, b"", from_cache=False, fetched_at=_now())

    # ---- cache --------------------------------------------------------------

    def _paths(self, url):
        key = hashlib.sha1(url.encode("utf-8")).hexdigest()
        return self.cache_dir / f"{key}.body.gz", self.cache_dir / f"{key}.json"

    def _read_cache(self, url):
        body_path, meta_path = self._paths(url)
        if not meta_path.exists():
            return None
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        return FetchResult(url, meta["final_url"], meta["status"],
                           gzip.decompress(body_path.read_bytes()), from_cache=True,
                           fetched_at=meta["fetched_at"])

    def _write_cache(self, result):
        body_path, meta_path = self._paths(result.url)
        _atomic_write(body_path, gzip.compress(result.body))
        meta = {
            "url": result.url,
            "final_url": result.final_url,
            "status": result.status,
            "fetched_at": result.fetched_at,
        }
        _atomic_write(meta_path, json.dumps(meta).encode("utf-8"))  # last = commit point


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _atomic_write(path, data, attempts=5):
    """Write to a temp file then rename, so a reader never sees a half-written file.

    On Windows, antivirus or the search indexer can hold a just-written file
    open for a moment, and the rename then fails with WinError 32. Retrying
    briefly is the standard workaround.
    """
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    for attempt in range(attempts):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == attempts - 1:
                raise
            time.sleep(0.2 * (attempt + 1))


def _parse_retry_after(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None  # missing, or an HTTP-date we don't bother parsing
