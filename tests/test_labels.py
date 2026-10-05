"""Both languages carry the same keys, so neither can quietly lose a string.

Nothing else catches this. A key added to `en` but not `ru` raises `KeyError` only on the
page that happens to use it, and a key left behind in `ru` alone is never noticed at all.
"""

import pytest

from atlas.charts import LABELS as FIGURE_LABELS
from atlas.pdf import BOOK
from atlas.render import LABELS as PAGE_LABELS

DICTIONARIES = {
    "render.LABELS": PAGE_LABELS,
    "pdf.BOOK": BOOK,
    "charts.LABELS": FIGURE_LABELS,
}


@pytest.mark.parametrize("name", sorted(DICTIONARIES))
def test_english_and_russian_hold_the_same_keys(name):
    english, russian = DICTIONARIES[name]["en"], DICTIONARIES[name]["ru"]
    assert sorted(english) == sorted(russian), (
        f"{name}: only in en {sorted(set(english) - set(russian))}; "
        f"only in ru {sorted(set(russian) - set(english))}"
    )


@pytest.mark.parametrize("name", sorted(DICTIONARIES))
def test_a_nested_mapping_holds_the_same_keys_in_both_languages(name):
    english, russian = DICTIONARIES[name]["en"], DICTIONARIES[name]["ru"]
    for key, value in english.items():
        if isinstance(value, dict):
            assert sorted(value) == sorted(russian[key]), f"{name}[{key!r}]"


@pytest.mark.parametrize("name", sorted(DICTIONARIES))
def test_a_list_of_items_has_the_same_length_in_both_languages(name):
    """A list is rendered by position, so differing lengths drop or duplicate an item."""
    english, russian = DICTIONARIES[name]["en"], DICTIONARIES[name]["ru"]
    for key, value in english.items():
        if isinstance(value, list | tuple):
            assert len(value) == len(russian[key]), f"{name}[{key!r}]"


@pytest.mark.parametrize("name", sorted(DICTIONARIES))
def test_a_format_string_names_the_same_placeholders_in_both_languages(name):
    """A placeholder present in one language only raises KeyError or prints a brace."""
    import string

    def fields(text: str) -> set[str]:
        return {f for _, f, _, _ in string.Formatter().parse(text) if f}

    english, russian = DICTIONARIES[name]["en"], DICTIONARIES[name]["ru"]
    for key, value in english.items():
        if isinstance(value, str):
            assert fields(value) == fields(russian[key]), f"{name}[{key!r}]"
