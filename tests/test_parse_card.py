import pytest

from crawler.parse_card import parse_card
from crawler.parse_model import parse_model_page


def test_base_card_without_parent(load_sample):
    c = parse_card(load_sample("card_qwen2.5-7b.md"))
    assert c["has_front_matter"] and c["parse_errors"] == []
    assert c["base_model"] == []
    assert c["license"] == "apache-2.0"
    assert c["language"] == ["en"]
    assert c["pipeline_tag"] == "text-generation"


def test_front_matter_after_leading_blank_line(load_sample):
    # This real card starts with "\n---"; a naive startswith("---") misses it.
    c = parse_card(load_sample("card_quantfactory-qwen2.5-coder-7b-gguf.md"))
    assert c["base_model"] == ["Qwen/Qwen2.5-7B"]


def test_base_model_as_string_becomes_list(load_sample):
    assert parse_card(load_sample("card_mlx-qwen2.5-7b-instruct-4bit.md"))["base_model"] == ["Qwen/Qwen2.5-7B"]


def test_adapter_relation(load_sample):
    c = parse_card(load_sample("card_adapter-srt-v1.0.md"))
    assert c["base_model_relation"] == "adapter"


def test_merge_card(load_sample):
    c = parse_card(load_sample("card_optitransfer-converge-v2.md"))
    assert len(c["base_model"]) == 14
    assert c["base_model_relation"] == "merge"


@pytest.mark.parametrize("name", [
    "qwen2.5-7b", "qwen2.5-7b-instruct", "mlx-qwen2.5-7b-instruct-4bit",
    "quantfactory-qwen2.5-coder-7b-gguf", "optitransfer-converge-v2", "adapter-srt-v1.0",
])
def test_raw_card_matches_embedded_card_data(load_sample, name):
    # This is the evidence behind FETCH_RAW_CARDS = False: the model page
    # already carries the same front matter, so the README request is redundant.
    card = parse_card(load_sample(f"card_{name}.md"))
    page = parse_model_page(load_sample(f"model_{name}.html"))
    assert card["base_model"] == page["card_base_model"]
    assert card["base_model_relation"] == page["card_base_model_relation"]
    assert card["datasets"] == page["card_datasets"]
    assert card["license"] == page["license"]


# ---- edge cases ------------------------------------------------------------

def test_card_without_front_matter_is_not_an_error():
    c = parse_card("# Just a title\n\nSome text.")
    assert c["has_front_matter"] is False
    assert c["parse_errors"] == []
    assert c["base_model"] == []


def test_bom_and_windows_newlines():
    c = parse_card("﻿---\r\nbase_model: a/b\r\nlicense: mit\r\n---\r\nbody")
    assert c["base_model"] == ["a/b"] and c["license"] == "mit"


def test_broken_yaml_is_logged_not_raised():
    c = parse_card("---\nbase_model: [unclosed\n---\n")
    assert c["has_front_matter"] and c["parse_errors"] == ["yaml"]


def test_front_matter_that_is_not_a_mapping():
    assert parse_card("---\n- a\n- b\n---\n")["parse_errors"] == ["yaml"]


def test_wrong_type_for_one_field():
    c = parse_card("---\nlicense: [mit, apache-2.0]\nbase_model: a/b\n---\n")
    assert c["parse_errors"] == ["license"]
    assert c["base_model"] == ["a/b"]


def test_horizontal_rule_in_body_is_not_front_matter():
    assert parse_card("# Title\n\n---\n\nmore")["has_front_matter"] is False
