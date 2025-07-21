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
]

templates_path = ["_templates"]
exclude_patterns = []

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Some popular Sphinx HTML themes you can use:
html_theme = "haiku"
html_theme_options = {
    "nosidebar": True,
}

html_title = "Filip Sufitchi's Blog"
html_static_path = ["_static"]
