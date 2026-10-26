import pytest

from crawler.parse_listing import listing_url, parse_listing
from tests.conftest import make_page


def test_first_page(load_sample):
    r = parse_listing(load_sample("listing_qwen2.5-7b_finetune_p0.html"))
    assert r["parse_errors"] == []
    assert r["parent_id"] == "Qwen/Qwen2.5-7B"
    assert r["relation"] == "finetune"
    assert len(r["children"]) == 30
    assert r["children"][0] == ("Qwen/Qwen2.5-7B-Instruct", "finetune")
    assert r["total"] == 980
    assert (r["page_index"], r["next_page"]) == (0, 1)


def test_second_page(load_sample):
    r = parse_listing(load_sample("listing_qwen2.5-7b_finetune_sortdl_p1.html"))
    assert (r["page_index"], r["next_page"]) == (1, 2)


@pytest.mark.parametrize("relation, total", [("adapter", 883), ("merge", 137), ("quantized", 87)])
def test_relation_read_from_page(load_sample, relation, total):
    r = parse_listing(load_sample(f"listing_qwen2.5-7b_{relation}_p0.html"))
    assert r["relation"] == relation
    assert r["total"] == total
    assert all(rel == relation for _, rel in r["children"])


def test_author_profile_data_is_dropped(load_sample):
    # The page embeds avatars and follower counts for every model; we keep none of it.
    r = parse_listing(load_sample("listing_qwen2.5-7b_merge_p0.html"))
    assert "avatar" not in repr(r) and "follower" not in repr(r)


def _page(total, page_index, n_models=0, other=("base_model:finetune:org/base",)):
    return make_page("ModelList", {"initialValues": {
        "activeFilters": {"other": list(other)},
        "models": [{"id": f"u/m{i}"} for i in range(n_models)],
        "numTotalItems": total, "numItemsPerPage": 30, "pageIndex": page_index,
    }})


@pytest.mark.parametrize("total, page, expected_next", [
    (137, 3, 4),      # 137 items = pages 0..4
    (137, 4, None),   # last page
    (30, 0, None),    # exactly one full page
    (31, 0, 1),
    (0, 0, None),     # no children at all
])
def test_next_page_arithmetic(total, page, expected_next):
    assert parse_listing(_page(total, page))["next_page"] == expected_next


def test_unexpected_filter_is_flagged_not_trusted():
    r = parse_listing(_page(10, 0, n_models=2, other=["license:mit"]))
    assert "filter" in r["parse_errors"]
    assert r["parent_id"] is None


def test_model_entry_without_id_is_skipped():
    page = make_page("ModelList", {"initialValues": {
        "activeFilters": {"other": ["base_model:adapter:org/base"]},
        "models": [{"id": "u/ok"}, {"downloads": 5}],
        "numTotalItems": 2, "numItemsPerPage": 30, "pageIndex": 0,
    }})
    r = parse_listing(page)
    assert r["children"] == [("u/ok", "adapter")]
    assert r["parse_errors"] == ["model_id"]


def test_page_without_model_list():
    assert parse_listing("<html></html>")["parse_errors"] == ["ModelList"]


def test_listing_url():
    assert listing_url("Qwen/Qwen2.5-7B", "finetune") == (
        "https://huggingface.co/models?other=base_model:finetune:Qwen/Qwen2.5-7B&sort=downloads")
    assert listing_url("Qwen/Qwen2.5-7B", "merge", page=2).endswith("&sort=downloads&p=2")
    with pytest.raises(ValueError):
        listing_url("a/b", "distilled")
