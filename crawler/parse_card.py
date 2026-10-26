"""Raw model card (README.md) -> metadata dict from its YAML front matter.

URL: https://huggingface.co/<org>/<model>/raw/main/README.md

Not used in the main crawl (config.FETCH_RAW_CARDS = False), because the model
page already embeds the same YAML as `cardData` (verified identical on all
samples). We keep this parser to (a) check that claim on a random sample in
validate/, and (b) parse front matter wherever we do have a raw card.
"""
import logging
import re

import yaml

from crawler.common import as_list

log = logging.getLogger(__name__)

# Front matter = a block between two '---' lines at the top of the file.
_FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(\r?\n|\Z)", re.DOTALL)

LIST_FIELDS = ("base_model", "datasets", "language")
SCALAR_FIELDS = ("license", "license_name", "base_model_relation", "pipeline_tag", "library_name")


def extract_front_matter(text):
    """Return the raw YAML string, or None if the card has no front matter.

    Leading whitespace and a UTF-8 BOM are stripped first: some real cards
    start with a blank line before '---' (samples/card_quantfactory-*.md).
    """
    m = _FRONT_MATTER_RE.match(text.lstrip("﻿ \t\r\n"))
    return m.group(1) if m else None


def parse_card(text):
    """Parse a README. Always returns every key in LIST_FIELDS + SCALAR_FIELDS.

    List fields are always lists (possibly empty); scalars are str or None.
    `has_front_matter` separates "card has no YAML" (common, not an error)
    from "YAML present but broken" (logged in parse_errors).
    """
    result = {name: [] for name in LIST_FIELDS}
    result.update(dict.fromkeys(SCALAR_FIELDS))
    result["has_front_matter"] = False
    result["parse_errors"] = []

    raw = extract_front_matter(text)
    if raw is None:
        return result
    result["has_front_matter"] = True

    try:
        data = yaml.safe_load(raw) or {}
        if not isinstance(data, dict):
            raise ValueError(f"front matter is a {type(data).__name__}, not a mapping")
    except (yaml.YAMLError, ValueError) as exc:
        log.warning("card: unreadable front matter (%s)", exc)
        result["parse_errors"].append("yaml")
        return result

    for name in LIST_FIELDS:
        try:
            result[name] = as_list(data.get(name))
        except ValueError as exc:
            log.warning("card: bad %s (%s)", name, exc)
            result["parse_errors"].append(name)
    for name in SCALAR_FIELDS:
        value = data.get(name)
        if value is None or isinstance(value, str):
            result[name] = value
        else:
            log.warning("card: %s should be a string, got %r", name, value)
            result["parse_errors"].append(name)
    return result
