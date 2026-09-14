# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_static_path = ['_static', '../assets']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "shibuya"
html_logo = "../assets/figures/logo_amazonasdatahub.png"
html_theme_options = {
    "accent_color": "jade",
    "nav_socials": [
        {
            "name": "GitHub",
            "url": "https://github.com/onelsoncarvalho/amazonasdatahubpy",
            "icon": "simple-icons:github"
        }
    ],
    "hide_breadcrumbs": True
}
