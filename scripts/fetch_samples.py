"""Phase-1 helper: download a handful of sample pages for offline inspection.

Why a separate script: the parsers in phase 2 are tested against these saved
files, so we want a reproducible record of exactly which URLs were sampled.
Not part of the crawler; it never re-downloads a file that already exists.

Usage:  python scripts/fetch_samples.py <name>=<url> [<name>=<url> ...]
"""
import sys
import time
from pathlib import Path

import requests
import truststore

# Use the OS certificate store (some Windows machines have AV/proxy roots
# that certifi doesn't know about). Verification stays ON.
truststore.inject_into_ssl()

USER_AGENT = "hf-ecosystem-student-project/0.1 (academic web-mining project; contact: CONTACT_EMAIL_PLACEHOLDER)"
DELAY_SECONDS = 1.5
SAMPLES_DIR = Path(__file__).resolve().parent.parent / "samples"


def main(pairs):
    SAMPLES_DIR.mkdir(exist_ok=True)
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    for pair in pairs:
        name, url = pair.split("=", 1)
        out = SAMPLES_DIR / name
        if out.exists():
            print(f"skip (cached) {name}")
            continue
        resp = session.get(url, timeout=30)
        print(f"{resp.status_code} {len(resp.content):>8} B  {name}  <- {url}")
        if resp.history:  # old un-namespaced ids (e.g. bert-base-uncased) redirect
            print(f"    redirected -> {resp.url}")
        if resp.ok:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(resp.content)
        time.sleep(DELAY_SECONDS)


if __name__ == "__main__":
    main(sys.argv[1:])
