# ****************************************************************

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import date
from babel.dates import format_date


# -- Project information -----------------------------------------------------

project = 'remotebox'
author = 'Pablo EA4TX'
email = 'ea4tx@ea4tx.com'

release = '1'
version = '1'


today = date.today()
# compile_date = today.strftime("%B %d, %Y")
compile_date = format_date(today, format='long', locale='es')


rst_epilog  = """
.. |Product| replace:: %s
.. |Author| replace:: %s
.. |Email| replace:: %s
.. |Version| replace:: %s
.. |Date| replace:: %s
""" % (project, author, email, version, compile_date)

# -- General configuration
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
    'collapse_navigation' : False,

}
html_context = {}

html_logo = "images/logo/LOGO_EA4TX.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

def setup(app):
    app.add_css_file('my_theme.css')