import pytest

from preprocess.clean import (infer_aliases, license_category, normalise_license,
                              normalise_model_id, normalise_timestamp, run)
from tests.rawdb import make_db


# ---- pure normalisers ----------------------------------------------------------

@pytest.mark.parametrize("raw, expected", [
    ("Qwen/Qwen2.5-7B", "Qwen/Qwen2.5-7B"),
    ("  Qwen/Qwen2.5-7B \n", "Qwen/Qwen2.5-7B"),
    ("https://huggingface.co/Qwen/Qwen2.5-7B", "Qwen/Qwen2.5-7B"),
    ("huggingface.co/Qwen/Qwen2.5-7B/", "Qwen/Qwen2.5-7B"),
    ("https://hf.co/Qwen/Qwen2.5-7B/tree/main", "Qwen/Qwen2.5-7B"),
    ("https://huggingface.co/a/b/blob/main/model.safetensors", "a/b"),
    ("bert-base-uncased", "bert-base-uncased"),           # legacy id, still valid
    ("./checkpoints/my-model", None),                     # local path
    ("/home/user/models/llama", None),
    ("C:\\models\\x", None),
    ("my fine tuned llama", None),                         # free text
    ("", None),
    ("https://huggingface.co/models/foo", None),
    (None, None),
    (42, None),
])
def test_normalise_model_id(raw, expected):
    assert normalise_model_id(raw) == expected


@pytest.mark.parametrize("raw, expected", [
    ("Apache-2.0 ", "apache-2.0"), ("MIT", "mit"), ("", None), (None, None)])
def test_normalise_license(raw, expected):
    assert normalise_license(raw) == expected


@pytest.mark.parametrize("license_id, category", [
    ("apache-2.0", "permissive"), ("mit", "permissive"), ("bsd-3-clause", "permissive"),
    ("cc-by-4.0", "permissive"),
    ("gpl-3.0", "copyleft"), ("cc-by-sa-4.0", "copyleft"),
    ("cc-by-nc-4.0", "noncommercial"), ("cc-by-nc-sa-4.0", "noncommercial"),
    ("cc-by-nc-nd-4.0", "noncommercial"),
    ("cc-by-nd-4.0", "restricted"),
    ("llama3.1", "restricted"), ("gemma", "restricted"), ("openrail", "restricted"),
    ("creativeml-openrail-m", "restricted"), ("bigscience-openrail-m", "restricted"),
    ("other", "other"), ("cc", "other"), ("something-new", "other"),
    (None, "unknown"),
])
def test_license_category(license_id, category):
    assert license_category(license_id) == category


@pytest.mark.parametrize("raw, expected", [
    ("2024-09-15T12:17:40.000Z", "2024-09-15T12:17:40Z"),
    ("2024-09-15T14:17:40+02:00", "2024-09-15T12:17:40Z"),   # converted to UTC
    ("2024-09-15", "2024-09-15T00:00:00Z"),
    ("not a date", None), (None, None),
])
def test_normalise_timestamp(raw, expected):
    assert normalise_timestamp(raw) == expected


# ---- the whole cleaning run on tiny databases ---------------------------------------

def issues(conn):
    return {(e, i) for e, i, _ in conn.execute("SELECT * FROM quality_issues")}


def test_edges_from_both_sources_are_merged(tmp_path):
    conn = make_db(tmp_path / "db", {"base/m": {}, "kid/a": {}}, [
        ("kid/a", "base/m", "finetune", "tags"),
        ("kid/a", "base/m", "finetune", "listing"),
        ("kid/b", "base/m", "adapter", "listing"),          # child never scraped
    ])
    run(conn)
    rows = {r[:3]: r[3:] for r in conn.execute("SELECT * FROM clean_edges")}
    #                                         in_tags in_listing child_in parent_in anomaly
    assert rows[("kid/a", "base/m", "finetune")] == (1, 1, 1, 1, 0)
    assert rows[("kid/b", "base/m", "adapter")] == (0, 1, 0, 1, 0)


def test_listing_edge_not_confirmed_by_scraped_child_is_flagged(tmp_path):
    conn = make_db(tmp_path / "db", {"base/m": {}, "kid/a": {}},
                   [("kid/a", "base/m", "finetune", "listing")])
    run(conn)
    assert ("kid/a -> base/m", "listing_not_in_child_tags") in issues(conn)


def test_self_loop_is_dropped(tmp_path):
    conn = make_db(tmp_path / "db", {"a/m": {}}, [("a/m", "a/m", "finetune", "tags")])
    run(conn)
    assert conn.execute("SELECT COUNT(*) FROM clean_edges").fetchone()[0] == 0
    assert ("a/m", "self_loop") in issues(conn)


def test_relation_conflict_is_flagged(tmp_path):
    conn = make_db(tmp_path / "db", {"base/m": {}, "kid/a": {}}, [
        ("kid/a", "base/m", "finetune", "tags"), ("kid/a", "base/m", "quantized", "listing")])
    run(conn)
    assert ("kid/a -> base/m", "relation_conflict") in issues(conn)


def test_child_much_older_than_parent_is_flagged_small_gaps_are_not(tmp_path):
    conn = make_db(tmp_path / "db", {
        "base/m": {"created_at": "2025-01-20T00:00:00.000Z"},
        "same/day": {"created_at": "2025-01-19T23:00:00.000Z"},    # uploaded an hour earlier: fine
        "spam/x": {"created_at": "2024-03-01T00:00:00.000Z"},      # ~10 months earlier: suspicious
    }, [("same/day", "base/m", "finetune", "tags"), ("spam/x", "base/m", "finetune", "tags")])
    run(conn)
    flagged = dict(conn.execute("SELECT child_id, temporal_anomaly FROM clean_edges").fetchall())
    assert flagged == {"same/day": 0, "spam/x": 1}


def test_created_at_floor(tmp_path):
    conn = make_db(tmp_path / "db", {
        "old/bert": {"created_at": "2022-03-02T23:29:04.000Z"},
        "kid/a": {"created_at": "2021-01-01T00:00:00.000Z"},       # also a floor-era date
    }, [("kid/a", "old/bert", "finetune", "tags")])
    run(conn)
    floor = dict(conn.execute("SELECT id, created_at_is_floor FROM clean_models").fetchall())
    assert floor == {"old/bert": 1, "kid/a": 1}
    # floor dates are placeholders, so they can't prove a temporal anomaly
    assert conn.execute("SELECT temporal_anomaly FROM clean_edges").fetchone()[0] == 0


def test_declared_bases_renamed_vs_not_linked(tmp_path):
    conn = make_db(tmp_path / "db", {
        "meta-llama/Llama-3.1-8B": {},
        # card uses the old name, HF linked the new one -> evidence of a rename
        "kid/a": {"card_base_model": ["meta-llama/Meta-Llama-3.1-8B"]},
        # a second model with the old name plus a base HF couldn't link
        "kid/b": {"card_base_model": ["meta-llama/Meta-Llama-3.1-8B", "typo/does-not-exist"]},
    }, [("kid/a", "meta-llama/Llama-3.1-8B", "finetune", "tags"),
        ("kid/b", "meta-llama/Llama-3.1-8B", "finetune", "tags")])
    run(conn)
    found = issues(conn)
    assert ("kid/a", "declared_base_renamed") in found
    assert ("kid/b", "declared_base_renamed") in found      # alias learned from kid/a, reused
    assert ("kid/b", "declared_base_not_linked") in found


def test_malformed_declared_base_is_logged_and_dropped(tmp_path):
    conn = make_db(tmp_path / "db", {"kid/a": {"card_base_model": [
        "./outputs/checkpoint-500", "https://huggingface.co/Qwen/Qwen2.5-7B"]}}, [])
    run(conn)
    declared = conn.execute("SELECT declared_bases_json FROM clean_models").fetchone()[0]
    assert declared == '["Qwen/Qwen2.5-7B"]'
    assert {"declared_base_malformed", "declared_base_normalised"} <= {i for _, i in issues(conn)}


def test_alias_inference_needs_unambiguous_evidence():
    models = {"x/1": {"declared_bases": ["old/name"]}, "x/2": {"declared_bases": ["old/name"]}}
    edges = {("x/1", "new/a", "finetune"): {"in_tags": 1}, ("x/2", "new/b", "finetune"): {"in_tags": 1}}
    assert infer_aliases(models, edges) == {}               # old/name -> a or b? conflicting, so none


def test_missing_task_inherited_from_parent_chain(tmp_path):
    conn = make_db(tmp_path / "db", {
        "base/m": {"pipeline_tag": "fill-mask"},
        "kid/a": {"pipeline_tag": None},
        "grandkid/q": {"pipeline_tag": None},
    }, [("kid/a", "base/m", "adapter", "tags"), ("grandkid/q", "kid/a", "quantized", "tags")],
        queue={"base/m": (0, "base/m"), "kid/a": (1, "base/m"), "grandkid/q": (2, "base/m")})
    run(conn)
    rows = {r[0]: r[1:] for r in conn.execute(
        "SELECT id, pipeline_tag, pipeline_tag_source FROM clean_models")}
    assert rows["kid/a"] == ("fill-mask", "inherited")
    assert rows["grandkid/q"] == ("fill-mask", "inherited")
    assert ("kid/a", "missing_pipeline_tag") in issues(conn)   # still counted as missing


def test_no_inheritance_when_parents_disagree(tmp_path):
    conn = make_db(tmp_path / "db", {
        "a/m": {"pipeline_tag": "text-generation"}, "b/m": {"pipeline_tag": "fill-mask"},
        "merge/x": {"pipeline_tag": None},
    }, [("merge/x", "a/m", "merge", "tags"), ("merge/x", "b/m", "merge", "tags")])
    run(conn)
    row = conn.execute("SELECT pipeline_tag, pipeline_tag_source FROM clean_models WHERE id='merge/x'").fetchone()
    assert tuple(row) == (None, "none")


def test_depth_and_root_come_from_the_crawl(tmp_path):
    conn = make_db(tmp_path / "db", {"base/m": {}, "kid/a": {}}, [],
                   queue={"base/m": (0, "base/m"), "kid/a": (1, "base/m")})
    run(conn)
    rows = {r[0]: r[1:] for r in conn.execute("SELECT id, depth, root FROM clean_models")}
    assert rows == {"base/m": (0, "base/m"), "kid/a": (1, "base/m")}


def test_rerunning_is_idempotent(tmp_path):
    conn = make_db(tmp_path / "db", {"base/m": {}, "kid/a": {"license": None}},
                   [("kid/a", "base/m", "finetune", "tags")])
    first = run(conn)
    second = run(conn)
    assert first == second
    assert conn.execute("SELECT COUNT(*) FROM quality_issues").fetchone()[0] == sum(second.values())
