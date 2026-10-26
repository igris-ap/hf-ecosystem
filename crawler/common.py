"""Small helpers shared by the parsers."""
import json


def find_props(soup, target):
    """Return the JSON props of the Svelte component called `target`.

    HF server-renders each interactive component as
        <div class="SVELTE_HYDRATER" data-target="ModelHeader" data-props="{...json...}">
    so the page's data is already structured JSON. This is more robust than
    scraping visible text, which changes whenever HF restyles the page.
    Raises LookupError if the component isn't on the page.
    """
    el = soup.find(attrs={"data-target": target, "data-props": True})
    if el is None:
        raise LookupError(f"no {target} component on page")
    return json.loads(el["data-props"])


def as_list(value):
    """Normalise a card field that may be absent, a string, or a list.

    `base_model`, `datasets` and `language` all appear in both forms in real
    cards, e.g. `base_model: Qwen/Qwen2.5-7B` vs `base_model: [a/b, c/d]`.
    """
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, list):
        return [str(v) for v in value if v is not None and str(v).strip()]
    raise ValueError(f"expected str or list, got {type(value).__name__}")
