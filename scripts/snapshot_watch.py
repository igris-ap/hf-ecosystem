"""Publish results from a crawl while it's still running.

    python scripts/snapshot_watch.py --every 1000              # watch, publish, push
    python scripts/snapshot_watch.py --once --no-push          # one snapshot now, local only

Every `--every` scraped models it:
  1. copies the live database to <data dir>/snapshot/hf.db (SQLite's backup
     API gives a consistent copy, and the analysis never locks the crawler's DB),
  2. runs clean -> API spot-check -> report -> charts -> family tree on the copy,
  3. regenerates the README's Results section from the new tables,
  4. commits results/ and README.md, then pushes.

It stops after a final snapshot once the crawl log shows the crawl has ended.
"""
import argparse
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import config  # noqa: E402

LIVE_DB = config.DB_PATH
LIVE_DB_RO = LIVE_DB.as_uri() + "?mode=ro"   # read-only; as_uri() encodes the space in "Aarya p"
SNAP_DIR = config.DATA_DIR / "snapshot"
CRAWL_LOG = config.DATA_DIR / "crawl_full.out"
WATCH_LOG = config.DATA_DIR / "snapshot_watch.log"
PY = sys.executable
CRAWL_ENDED = ("crawl summary:", "Traceback", "interrupted; run the same command")


def log(msg):
    line = f"{datetime.now():%Y-%m-%d %H:%M:%S} {msg}"
    print(line, flush=True)
    with open(WATCH_LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def done_count():
    """Scraped models so far, read from the live DB (retrying if the crawler holds a lock)."""
    for _ in range(10):
        try:
            with sqlite3.connect(LIVE_DB_RO, uri=True, timeout=30) as conn:
                return conn.execute("SELECT COUNT(*) FROM crawl_queue WHERE status = 'done'").fetchone()[0]
        except sqlite3.OperationalError:
            time.sleep(5)
    raise RuntimeError("live database stayed locked")


def crawl_ended():
    try:
        text = CRAWL_LOG.read_text(encoding="utf-8", errors="replace")[-20000:]
    except FileNotFoundError:
        return False
    return any(marker in text for marker in CRAWL_ENDED)


def copy_database():
    SNAP_DIR.mkdir(parents=True, exist_ok=True)
    src = sqlite3.connect(LIVE_DB_RO, uri=True, timeout=60)
    dst = sqlite3.connect(SNAP_DIR / "hf.db")
    src.backup(dst)
    src.close()
    dst.close()


def run(*args, env=None):
    result = subprocess.run([PY, *args], cwd=ROOT, env=env, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed:\n{result.stdout[-2000:]}\n{result.stderr[-3000:]}")
    return result.stdout


def git(*args):
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def snapshot(final=False, push=True):
    done = done_count()
    started = time.monotonic()
    log(f"snapshot at {done:,} models{' (final)' if final else ''}")
    copy_database()
    env = {**os.environ, "HF_ECOSYSTEM_DATA": str(SNAP_DIR), "PYTHONIOENCODING": "utf-8"}
    for step in (["-m", "preprocess.clean"], ["-m", "validate.api_spotcheck"], ["-m", "mining.report"],
                 ["-m", "viz.charts"], ["-m", "viz.family_tree"]):
        t = time.monotonic()
        run(*step, env=env)
        log(f"  {step[-1]:<24} {time.monotonic() - t:6.0f} s")
    readme_args = ["scripts/update_readme_results.py", "--done", str(done), "--target", str(config.MAX_MODELS)]
    run(*readme_args, *(["--final"] if final else []))

    git("add", "results", "README.md")
    if not git("diff", "--cached", "--name-only").strip():
        log("  nothing changed, no commit")
        return done
    label = "Final results" if final else "Results snapshot"
    git("commit", "-q", "-m", f"{label}: {done:,} models")
    if push:
        git("push", "-q")
        log(f"  committed and pushed ({time.monotonic() - started:.0f} s total)")
    else:
        log(f"  committed locally, not pushed ({time.monotonic() - started:.0f} s total)")
    return done


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--every", type=int, default=1000)
    ap.add_argument("--poll", type=int, default=120, help="seconds between progress checks")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--no-push", action="store_true")
    args = ap.parse_args()
    push = not args.no_push

    if args.once:
        snapshot(final=crawl_ended(), push=push)
        return

    next_mark = (done_count() // args.every + 1) * args.every
    log(f"watching: next snapshot at {next_mark:,} models")
    while True:
        if crawl_ended():
            snapshot(final=True, push=push)
            log("crawl ended; watcher done")
            return
        done = done_count()
        if done >= next_mark:
            try:
                snapshot(push=push)
            except Exception as exc:            # keep watching; the next mark tries again
                log(f"  snapshot FAILED: {exc}")
            next_mark = (done_count() // args.every + 1) * args.every
            log(f"next snapshot at {next_mark:,} models")
        time.sleep(args.poll)


if __name__ == "__main__":
    main()
