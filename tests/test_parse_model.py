from pathlib import Path

import pytest

from config import SAMPLES_DIR
from crawler.parse_model import FIELDS, parents_from_tags, parse_model_page
from tests.conftest import make_page


def test_base_model_fields(load_sample):
    m = parse_model_page(load_sample("model_qwen2.5-7b.html"))
    assert m["parse_errors"] == []
    assert m["id"] == "Qwen/Qwen2.5-7B"
    assert m["author"] == "Qwen"
    assert m["license"] == "apache-2.0"
    assert m["pipeline_tag"] == "text-generation"
    assert m["downloads"] == 437832
    assert m["likes"] == 338
    assert m["created_at"] == "2024-09-15T12:17:40.000Z"
    assert m["gated"] is False
    assert m["parents"] == []
    assert m["card_base_model"] == []
    assert m["children_counts"] == {"adapter": 883, "finetune": 979, "merge": 137, "quantized": 87}


def test_finetune_parent_and_children_not_confused_with_siblings(load_sample):
    # The page also links to the parent's finetune listing ("979"); that's the
    # sibling count and must not be read as this model's children.
    m = parse_model_page(load_sample("model_qwen2.5-7b-instruct.html"))
    assert m["parents"] == [("Qwen/Qwen2.5-7B", "finetune")]
    assert m["card_base_model"] == ["Qwen/Qwen2.5-7B"]
    assert m["children_counts"] == {"adapter": 2838, "finetune": 3220, "merge": 169, "quantized": 442}


@pytest.mark.parametrize("sample, relation", [
    ("model_adapter-srt-v1.0.html", "adapter"),
    ("model_quantfactory-qwen2.5-coder-7b-gguf.html", "quantized"),
    ("model_mlx-qwen2.5-7b-instruct-4bit.html", "finetune"),  # HF's (wrong) label, kept as-is
])
def test_relation_types(load_sample, sample, relation):
    m = parse_model_page(load_sample(sample))
    assert m["parents"] == [("Qwen/Qwen2.5-7B", relation)]


def test_leaf_model_has_no_children(load_sample):
    m = parse_model_page(load_sample("model_quantfactory-qwen2.5-coder-7b-gguf.html"))
    assert m["children_counts"] == {}


def test_merge_with_many_parents(load_sample):
    m = parse_model_page(load_sample("model_optitransfer-converge-v2.html"))
    assert len(m["parents"]) == 14
    assert {rel for _, rel in m["parents"]} == {"merge"}
    assert m["card_base_model_relation"] == "merge"
    # tag-derived edges and the card's declared parents agree
    assert {p for p, _ in m["parents"]} == set(m["card_base_model"])


def test_gated_model_keeps_only_public_fields(load_sample):
    m = parse_model_page(load_sample("model_llama-3.1-8b.html"))
    assert m["parse_errors"] == []
    assert m["gated"] == "manual"
    assert m["license"] == "llama3.1"
    # nothing from the access form (extra_gated_*) leaks into our record
    assert set(m) == set(FIELDS) | {"parse_errors"}
    assert "extra_gated" not in repr(m)


def test_legacy_id_resolves_to_canonical(load_sample):
    m = parse_model_page(load_sample("seeds/bert-base-uncased_legacy.html"))
    assert m["id"] == "google-bert/bert-base-uncased"
    assert m["children_counts"]["finetune"] == 7033
    assert m["created_at"].startswith("2022-03-02")  # HF's createdAt floor, see docs


@pytest.mark.parametrize("path", sorted((SAMPLES_DIR / "seeds").glob("*.html")), ids=lambda p: p.stem)
def test_all_seed_pages_parse_cleanly(path):
    m = parse_model_page(Path(path).read_text(encoding="utf-8"))
    assert m["parse_errors"] == []
    assert m["parents"] == []          # seeds are base models
    assert sum(v or 0 for v in m["children_counts"].values()) > 0


# ---- robustness: bad pages must degrade to None, never raise ----------------

def test_page_without_model_header():
    m = parse_model_page("<html><body>Something changed</body></html>")
    assert m["parse_errors"] == ["ModelHeader"]
    assert all(m[f] is None for f in FIELDS)


def test_broken_json_in_props():
    page = '<div data-target="ModelHeader" data-props="{not json"></div>'
    assert parse_model_page(page)["parse_errors"] == ["ModelHeader"]


def test_one_bad_field_does_not_lose_the_others():
    page = make_page("ModelHeader", {"model": {
        "id": "a/b", "author": "a", "tags": [], "likes": 3,
        "createdAt": "2025-01-01T00:00:00.000Z",
        "downloads": "lots",                         # wrong type
        "cardData": {"base_model": {"oops": 1}},     # wrong type
    }})
    m = parse_model_page(page)
    assert sorted(m["parse_errors"]) == ["card_base_model", "downloads"]
    assert m["downloads"] is None and m["card_base_model"] is None
    assert m["id"] == "a/b" and m["likes"] == 3


def test_list_valued_text_fields_are_flattened():
    # Real case that crashed the crawl: mradermacher/AstroSage-8B-GGUF has `license: [llama3.1]`
    page = make_page("ModelHeader", {"model": {
        "id": "a/b", "author": "a", "tags": [], "downloads": 1, "likes": 0,
        "createdAt": "2025-01-01T00:00:00.000Z",
        "cardData": {"license": ["llama3.1"], "license_name": ["one", "two"],
                     "base_model_relation": {"weird": 1}},
    }})
    m = parse_model_page(page)
    assert m["license"] == "llama3.1"
    assert m["license_name"] == "one, two"
    assert m["card_base_model_relation"] is None
    assert m["parse_errors"] == ["card_base_model_relation"]


def test_missing_optional_fields_are_not_errors():
    page = make_page("ModelHeader", {"model": {
        "id": "a/b", "author": "a", "tags": [], "downloads": 0, "likes": 0,
        "createdAt": "2025-01-01T00:00:00.000Z",
    }})
    m = parse_model_page(page)
    assert m["parse_errors"] == []
    assert m["license"] is None and m["pipeline_tag"] is None
    assert m["card_base_model"] == [] and m["children_counts"] == {}


# ---- parents_from_tags -------------------------------------------------------

def test_plain_base_model_tag_without_relation_is_unknown():
    tags = ["base_model:org/x", "base_model:org/y", "base_model:adapter:org/y", "license:mit"]
    assert parents_from_tags(tags) == [("org/y", "adapter"), ("org/x", "unknown")]


def test_legacy_parent_id_without_org():
    assert parents_from_tags(["base_model:finetune:gpt2"]) == [("gpt2", "finetune")]
