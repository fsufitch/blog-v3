# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "Filip's Blog"

copyright = "2025, Filip Sufitchi"
author = "Filip Sufitchi"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
    "sphinxnotes.strike",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_prompt",
    "sphinxemoji.sphinxemoji",
    "sphinx_gitstamp",
    "sphinx_tags",
    "blogv3.sphinx_extension",
]

templates_path = ["_templates"]
exclude_patterns = []

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# html_theme = "readable"

import sphinx_readable_theme

html_theme = "readable"
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]

html_theme_options = {
    "nosidebar": False,
}

html_title = "Filip Sufitchi's Blog"
html_static_path = ["_static"]
