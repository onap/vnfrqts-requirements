project = "onap"
release = "master"
version = "master"

#####
# Deprecation of Sphinx context injection at build time
# see https://about.readthedocs.com/blog/2024/07/addons-by-default/
import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
#
#####

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
}

html_last_updated_fmt = "%d-%b-%y %H:%M"


def setup(app):
    app.add_css_file("css/ribbon.css")


needs_extra_options = [
    "target",
    "keyword",
    "introduced",
    "updated",
    "impacts",
    "validation_mode",
]

needs_id_regex = "^[A-Z0-9]+-[A-Z0-9]+"
needs_id_required = True
needs_title_optional = True