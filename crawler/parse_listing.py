"""Children listing page -> child ids + pagination.

URL: https://huggingface.co/models?other=base_model:<relation>:<parent>&sort=downloads&p=<n>
Data source: the `ModelList` component's embedded JSON. See
docs/page_structure.md, section 2.

Listings are the crawl frontier: they tell us which models to visit next.
They list *direct* children only (verified on samples).
"""
import logging
import math
from urllib.parse import quote

from bs4 import BeautifulSoup

from config import BASE_URL, RELATIONS
from crawler.common import find_props

log = logging.getLogger(__name__)


def listing_url(parent_id, relation, page=0):
    """Build the listing URL, most-downloaded children first.

    Sorting by downloads means the per-parent cap keeps the most-used children
    instead of whatever happens to be "trending" today.
    """
    if relation not in RELATIONS:
        raise ValueError(f"unknown relation {relation!r}")
    url = f"{BASE_URL}/models?other=base_model:{relation}:{quote(parent_id, safe='/')}&sort=downloads"
    return url + (f"&p={page}" if page else "")


def parse_listing(html):
    """Parse one listing page.

    Returns:
        parent_id, relation: which filter this page shows (read from the page itself)
        children:   [(child_id, relation), ...] in page order
        total:      number of children HF reports for this parent+relation
        page_index: 0-based page number
        next_page:  page number to fetch next, or None if this was the last page
        parse_errors: names of anything that failed
    Per-model `authorData` (avatars, follower counts) is deliberately ignored:
    it's user-profile data and out of scope (docs/ethics.md).
    """
    result = {"parent_id": None, "relation": None, "children": [], "total": None,
              "page_index": None, "next_page": None, "parse_errors": []}
    soup = BeautifulSoup(html, "html.parser")

    try:
        values = find_props(soup, "ModelList")["initialValues"]
    except (LookupError, ValueError, TypeError, KeyError) as exc:
        log.error("listing: ModelList missing or unreadable (%s)", exc)
        result["parse_errors"].append("ModelList")
        return result

    try:
        result["parent_id"], result["relation"] = _active_filter(values)
    except (KeyError, ValueError) as exc:
        log.warning("listing: could not read active base_model filter (%s)", exc)
        result["parse_errors"].append("filter")

    for item in values.get("models", []):
        child_id = item.get("id") if isinstance(item, dict) else None
        if not child_id:
            log.warning("listing: model entry without id skipped")
            result["parse_errors"].append("model_id")
            continue
        result["children"].append((child_id, result["relation"]))

    try:
        total = int(values["numTotalItems"])
        per_page = int(values["numItemsPerPage"])
        page = int(values["pageIndex"])
        result["total"], result["page_index"] = total, page
        last_page = math.ceil(total / per_page) - 1
        result["next_page"] = page + 1 if page < last_page else None
    except (KeyError, ValueError, TypeError, ZeroDivisionError) as exc:
        log.warning("listing: pagination fields unreadable (%s)", exc)
        result["parse_errors"].append("pagination")

    return result


def _active_filter(values):
    """Return (parent_id, relation) from the filter HF says it applied.

    We read it back from the page instead of trusting the URL we requested:
    if HF ever ignored or rewrote the filter, we'd notice rather than
    record wrong edges.
    """
    filters = [f for f in values["activeFilters"]["other"] if f.startswith("base_model:")]
    if len(filters) != 1:
        raise ValueError(f"expected one base_model filter, got {filters}")
    relation, _, parent = filters[0][len("base_model:"):].partition(":")
    if relation not in RELATIONS or not parent:
        raise ValueError(f"unrecognised filter {filters[0]!r}")
    return parent, relation
