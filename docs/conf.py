"""Sphinx configuration for vnfrqts/requirements documentation."""

from docutils.parsers.rst import directives

project = "onap"
release = "master"
version = "master"

author = "Open Network Automation Platform"
# yamllint disable-line rule:line-length
copyright = "ONAP. Licensed under Creative Commons Attribution 4.0 International License"

pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "style_nav_header_background": "white",
    "sticky_navigation": "False",
}
html_logo = "_static/logo_onap_2017.png"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_show_sphinx = False

master_doc = "index"

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinxcontrib.needs",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.mermaid",
]

exclude_patterns = [
    ".DS_Store",
    "_build",
    "Thumbs.db",
    ".tox",
]

todo_include_todos = False

linkcheck_ignore = [
    "http://localhost",
]

branch = "latest"

doc_url = "https://docs.onap.org/projects"

intersphinx_mapping = {
    "modeling": (
        "{}/onap-modeling-modelspec/en/latest/".format(doc_url),
        None,
    ),
    "dcae": (
        "{}/onap-dcaegen2/en/latest/".format(doc_url),
        None,
    ),
    "appc": (
        "{}/onap-appc/en/latest/".format(doc_url),
        None,
    ),
    "appc-deployment": (
        "{}/onap-appc-deployment/en/latest/".format(doc_url),
        None,
    ),
}

html_last_updated_fmt = "%d-%b-%y %H:%M"


def setup(app):
    app.add_css_file("css/ribbon.css")


needs_extra_options = {
    "target": directives.unchanged,
    "keyword": directives.unchanged,
    "introduced": directives.unchanged,
    "updated": directives.unchanged,
    "impacts": directives.unchanged,
    "validation_mode": directives.unchanged,
}

needs_id_regex = "^[A-Z0-9]+-[A-Z0-9]+"
needs_id_required = True
needs_title_optional = True