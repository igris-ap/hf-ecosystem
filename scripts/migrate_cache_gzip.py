"""One-off: convert an old uncompressed cache (<key>.body) to the gzip format
(<key>.body.gz) that crawler/fetch.py uses now.

Each entry is compressed, checked by decompressing it again, and only then is
the old file deleted. It's safe to re-run, because finished entries are
skipped.

Usage:  python scripts/migrate_cache_gzip.py [cache_dir]
"""
import gzip
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config  # noqa: E402
from crawler.fetch import _atomic_write  # noqa: E402


def main(cache_dir):
    converted = before = after = 0
    for old in sorted(cache_dir.glob("*.body")):
        new = old.with_suffix(".body.gz")
        data = old.read_bytes()
        packed = gzip.compress(data)
        if gzip.decompress(packed) != data:
            raise RuntimeError(f"round-trip mismatch for {old.name}; stopping")
        _atomic_write(new, packed)
        old.unlink()
        converted += 1
        before += len(data)
        after += len(packed)
    print(f"converted {converted} entries: {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else config.CACHE_DIR)
