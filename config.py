"""Central settings for the crawl. Everything tunable lives here so the
crawler code never hard-codes a number we might want to change for a run."""
import os
from pathlib import Path

# --- Seeds -----------------------------------------------------------------
# Major base models, one or two per family. Every id was verified by scraping
# its model page on 2026-10-26 (see docs/page_structure.md, "Seed counts").
SEEDS = [
    "meta-llama/Llama-3.1-8B",
    "meta-llama/Llama-3.2-1B",
    "mistralai/Mistral-7B-v0.1",
    "Qwen/Qwen2.5-7B",
    "Qwen/Qwen3-8B-Base",
    "google/gemma-2-9b",
    "google/gemma-3-4b-pt",
    "microsoft/phi-2",
    "deepseek-ai/DeepSeek-R1",
    "google-bert/bert-base-uncased",
]

# --- Crawl limits ----------------------------------------------------------
MAX_DEPTH = 3              # seeds are depth 0
MAX_MODELS = 500           # global cap; 500 for testing, 20_000 for the full run
# Without a per-parent cap, bert-base-uncased alone (7k fine-tunes) would eat a
# third of the full budget. We take the most-downloaded children first.
MAX_CHILDREN_PER_RELATION = 300
RELATIONS = ("finetune", "adapter", "quantized", "merge")

# The raw README is never fetched by the crawler: it duplicates
# ModelHeader.cardData exactly (verified on samples), so skipping it halves the
# request count. crawler/parse_card.py is used by validate/ to re-check that.

# --- Politeness ------------------------------------------------------------
BASE_URL = "https://huggingface.co"
USER_AGENT = (
    "hf-ecosystem-student-project/0.1 "
    "(academic web-mining project; contact: CONTACT_EMAIL_PLACEHOLDER)"
)
# HF advertises `RateLimit-Policy: "fixed window";"pages";q=100;w=300`, i.e. 100
# page requests per 5 minutes for anonymous clients. 300 s / 100 = 3 s per request
# keeps us under it (stricter than the brief's ~1 req/s ceiling). The fetcher also
# reads the live `RateLimit` header and pauses if the window is used up anyway.
MIN_REQUEST_INTERVAL = 3.0
MAX_RETRIES = 5              # for 429 / 5xx / connection errors
BACKOFF_BASE = 2.0           # wait 2, 4, 8, 16, 32 s between retries
REQUEST_TIMEOUT = 30

# --- Paths -----------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
# Crawl data lives OUTSIDE the repo: the full crawl's cache is gigabytes, and the
# repo sits in a cloud-synced folder (OneDrive). Override per machine with the
# HF_ECOSYSTEM_DATA environment variable; a relative path is taken from the repo
# root, so HF_ECOSYSTEM_DATA=sample_data uses the bundled 500-model sample.
SAMPLE_DATA_DIR = ROOT / "sample_data"
DATA_DIR = Path(os.environ.get("HF_ECOSYSTEM_DATA", Path.home() / "hf-ecosystem-data"))
if not DATA_DIR.is_absolute():
    DATA_DIR = ROOT / DATA_DIR
CACHE_DIR = DATA_DIR / "cache"
DB_PATH = DATA_DIR / "hf.db"
LOG_PATH = DATA_DIR / "crawl.log"
SAMPLES_DIR = ROOT / "samples"
RESULTS_DIR = ROOT / "results"   # small derived tables, committed (see mining/report.py)
