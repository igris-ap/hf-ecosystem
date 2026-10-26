"""Model page (https://huggingface.co/<org>/<model>) -> metadata dict.

Data source: the `ModelHeader` component's embedded JSON, plus the
"Model tree" links for child counts. See docs/page_structure.md, section 1.

Failure policy: one bad field must never crash the crawl. Each field is
parsed on its own; if one fails, it's logged, set to None, and its name is
added to `parse_errors`. That list feeds the data-quality report.
"""
import logging
import re

from bs4 import BeautifulSoup

from config import RELATIONS
from crawler.common import as_list, find_props

log = logging.getLogger(__name__)

FIELDS = (
    "id", "author", "license", "license_name", "pipeline_tag", "library_name",
    "tags", "downloads", "downloads_all_time", "likes", "created_at",
    "last_modified", "gated", "card_base_model", "card_base_model_relation",
    "card_datasets", "card_language", "parents", "children_counts",
)

_COUNT_RE = re.compile(r"([\d,]+)\s+models?\b")


def parse_model_page(html):
    """Parse a model page. Always returns a dict with every key in FIELDS."""
    result = dict.fromkeys(FIELDS)
    result["parse_errors"] = []
    soup = BeautifulSoup(html, "html.parser")

    try:
        model = find_props(soup, "ModelHeader")["model"]
    except (LookupError, ValueError, TypeError) as exc:
        # Without ModelHeader there's nothing to parse; HF probably changed the page.
        log.error("model page: ModelHeader missing or unreadable (%s)", exc)
        result["parse_errors"].append("ModelHeader")
        return result

    card = model.get("cardData") or {}

    def field(name, extract):
        try:
            result[name] = extract()
        except Exception as exc:  # noqa: BLE001  (deliberate: log + null, keep crawling)
            log.warning("model page %s: could not parse %s (%s: %s)",
                        model.get("id"), name, type(exc).__name__, exc)
            result["parse_errors"].append(name)

    # Required: every model page we've seen has these, so a miss is a real error.
    field("id", lambda: _str(model["id"]))
    field("author", lambda: _str(model["author"]))
    field("tags", lambda: [str(t) for t in model["tags"]])
    field("downloads", lambda: int(model["downloads"]))
    field("likes", lambda: int(model["likes"]))
    field("created_at", lambda: _str(model["createdAt"]))

    # Optional: legitimately absent on many community repos -> None, no error.
    field("license", lambda: card.get("license") or _license_from_tags(model.get("tags", [])))
    field("license_name", lambda: card.get("license_name"))
    field("pipeline_tag", lambda: model.get("pipeline_tag"))
    field("library_name", lambda: model.get("library_name"))
    field("downloads_all_time", lambda: _int_or_none(model.get("downloadsAllTime")))
    field("last_modified", lambda: model.get("lastModified"))
    field("gated", lambda: model.get("gated", False))   # False, "auto" or "manual"
    field("card_base_model", lambda: as_list(card.get("base_model")))
    field("card_base_model_relation", lambda: card.get("base_model_relation"))
    field("card_datasets", lambda: as_list(card.get("datasets")))
    field("card_language", lambda: as_list(card.get("language")))

    # Lineage
    field("parents", lambda: parents_from_tags(model["tags"]))
    if result["id"]:
        field("children_counts", lambda: children_counts(soup, result["id"]))

    return result


def parents_from_tags(tags):
    """Extract (parent_id, relation) pairs from HF's computed tags.

    HF adds two tags per declared parent:
        base_model:<parent>               plain "has parent"
        base_model:<relation>:<parent>    with relation in RELATIONS
    Model ids can't contain ':', so splitting on the first ':' is safe.
    A parent seen only in the plain form gets relation 'unknown'.
    """
    with_relation = []
    plain = []
    for tag in tags:
        if not tag.startswith("base_model:"):
            continue
        rest = tag[len("base_model:"):]
        relation, sep, parent = rest.partition(":")
        if sep and relation in RELATIONS:
            with_relation.append((parent, relation))
        else:
            plain.append(rest)

    known = {parent for parent, _ in with_relation}
    unknown = [(p, "unknown") for p in plain if p not in known]
    return _dedupe(with_relation + unknown)


def children_counts(soup, model_id):
    """Read {relation: n_children} from the Model tree box.

    Only links that end in *this* model's id count. A child page also links to
    its parent's listing (the sibling count), and counting that would be wrong.
    A link with no number ("Browse Quantizations") maps to None, meaning
    "has children, count unknown", so the crawler fetches the listing to find out.
    A relation with no link at all has 0 children and is simply absent.
    """
    pattern = re.compile(
        r"^/models\?other=base_model:(" + "|".join(RELATIONS) + r"):" + re.escape(model_id) + r"$"
    )
    counts = {}
    for a in soup.find_all("a", href=pattern):
        relation = pattern.match(a["href"]).group(1)
        m = _COUNT_RE.search(a.get_text(" ", strip=True))
        if m:
            counts[relation] = int(m.group(1).replace(",", ""))
        else:
            counts.setdefault(relation, None)
    return counts


def _license_from_tags(tags):
    for tag in tags:
        if tag.startswith("license:"):
            return tag[len("license:"):]
    return None


def _str(value):
    if not isinstance(value, str) or not value:
        raise ValueError(f"expected non-empty string, got {value!r}")
    return value


def _int_or_none(value):
    return None if value is None else int(value)


def _dedupe(pairs):
    """Drop repeats but keep the original order."""
    seen = set()
    unique = []
    for pair in pairs:
        if pair not in seen:
            seen.add(pair)
            unique.append(pair)
    return unique
