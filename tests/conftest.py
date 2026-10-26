"""Shared test helpers. Tests never touch the network: parsers read saved
pages from samples/, and the fetcher gets a fake session and a fake clock."""
import html
import json

import pytest

from config import SAMPLES_DIR


@pytest.fixture
def load_sample():
    def load(name):
        return (SAMPLES_DIR / name).read_text(encoding="utf-8")
    return load


def make_page(target, props):
    """A minimal HF-style page with one hydrated component, for edge cases
    that the real samples don't cover (missing fields, wrong types...)."""
    escaped = html.escape(json.dumps(props), quote=True)
    return (f'<html><body><div class="SVELTE_HYDRATER" data-target="{target}" '
            f'data-props="{escaped}"></div></body></html>')
