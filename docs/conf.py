# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "jungle-scout"
copyright = "2024, Jungle Scout <support@junglescout.com>"  # noqa: A001
author = "Jungle Scout <support@junglescout.com>"
release = "0.2.2"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx.ext.extlinks",
    "sphinxcontrib.autodoc_pydantic",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extlinks = {
    "js_api_docs": ("https://developer.junglescout.com/%s", "[API Docs; page %s]"),
    "js_postman": ("https://postman.junglescout.com/%s", "[Postman Collection; page %s]"),
    "pydantic": ("https://docs.pydantic.dev/latest/%s", "[Pydantic; page %s]"),
    "httpx": ("https://www.python-httpx.org/%s", "[httpx; page %s]"),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "style_external_links": False,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}
html_static_path = ["_static"]
