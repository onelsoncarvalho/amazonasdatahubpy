# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import re
from pathlib import Path
from sphinx.util import logging

# -- Project information -----------------------------------------------------

project = u"amazonasdatahub"
copyright = u"2026, Nelson Geraldo Aquino de Carvalho"
author = u"Nelson Geraldo Aquino de Carvalho"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autoapi_dirs = ["../src"]

# MyST-NB option to execute code
nb_execution_mode = "auto"
nb_execution_timeout = 60
nb_mime_priority_excludes = ["application/vnd.jupyter.widget-view+json"]
nb_render_markdown_format = "myst"

# Custom block code colors
# Syntax highlighting
def copy_theme_assets(app):
    import shutil

    src_js = CONF_DIR.parent / "scripts" / "mystnb-theme.js"
    dest_js = CONF_DIR / "_static" / "mystnb-theme.js"
    dest_js.parent.mkdir(parents=True, exist_ok=True)
    if src_js.exists():
        shutil.copy2(src_js, dest_js)

    src_css = CONF_DIR.parent / "scripts" / "custom.css"
    dest_css = CONF_DIR / "_static" / "custom.css"
    if src_css.exists():
        shutil.copy2(src_css, dest_css)

REPO_URL = "https://onelsoncarvalho.github.io/amazonasdatahubpy"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_static_path = ['_static', '../assets']

html_js_files = [
    "mystnb-theme.js",
]

html_css_files = [
    "custom.css",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "shibuya"
html_logo = "../assets/figures/logo_amazonasdatahub.png"
html_context = {
    "languages": [
        ("🇺🇸 English", f"{REPO_URL}/en/"),
        ("🇧🇷 Português (BR)", f"{REPO_URL}/br/")
    ]
}
html_theme_options = {
    "accent_color": "jade",
    "color_mode": "dark",
    "dark_code": False,
        "nav_socials": [
        {
            "name": "GitHub",
            "url": "https://github.com/onelsoncarvalho/amazonasdatahubpy",
            "icon": "simple-icons:github"
        }
    ],
    "hide_breadcrumbs": True,
    "navigation_with_keys": True,
}



# Custom build
logger = logging.getLogger(__name__)

CONF_DIR = Path(__file__).parent.resolve()
SRC_DOCS_DIR = (CONF_DIR / ".." / "src" / "amazonasdatahub" / "documentations").resolve()
STUBS_DIR = CONF_DIR / "datasets"

EXAMPLE_RE = re.compile(r"^### Example\s*$")
PY_FENCE_RE = re.compile(r"^```python\s*$")

STUB_HEADER = """\
---
file_format: mystnb
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

% ARQUIVO GERADO por docs/conf.py. Não edite aqui: edite {origem}
"""


def _build_stub(source: Path, stub_path: Path) -> str:
    lines = source.read_text(encoding="utf-8").splitlines()
    # Skip yaml from original file (if has yaml)
    start = 0
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                start = i + 1
                break

    example_idx = next((i for i, l in enumerate(lines) if EXAMPLE_RE.match(l)), None)

    rel = Path(os.path.relpath(source, stub_path.parent)).as_posix()
    include = [f"```{{include}} {rel}", ":relative-images:", f":start-line: {start}"]
    if example_idx is not None:
        include.append(f":end-line: {example_idx}")  # exclusivo: para antes do Example
    include.append("```")

    parts = [STUB_HEADER.format(origem=rel), "\n".join(include)]

    if example_idx is not None:
        example = [
            "```{code-cell} python" if PY_FENCE_RE.match(l) else l
            for l in lines[example_idx:]
        ]
        parts.append("\n".join(example))

    return "\n\n".join(parts) + "\n"


def generate_dataset_stubs(app):
    STUBS_DIR.mkdir(exist_ok=True)
    for source in sorted(SRC_DOCS_DIR.glob("*.md")):
        stub_path = STUBS_DIR / source.name
        content = _build_stub(source, stub_path)
        
        if stub_path.exists() and stub_path.read_text(encoding="utf-8") == content:
            continue
        stub_path.write_text(content, encoding="utf-8")
        logger.info(f"stub gerado: {stub_path.name}")


def setup(app):
    app.connect("builder-inited", generate_dataset_stubs)
    app.connect("builder-inited", copy_theme_assets)
