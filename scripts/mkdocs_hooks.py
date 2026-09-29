"""MkDocs hooks: the site menu comes from the content, and links stay inside the site."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from atlas import site
from atlas.content import load


def on_config(config):
    config["nav"] = site.nav(load(ROOT / "src" / "content"))
    return config


def on_page_markdown(markdown, page, config, files):
    return site.rewrite_links(site.nest_lists(markdown), page.file.src_uri)
