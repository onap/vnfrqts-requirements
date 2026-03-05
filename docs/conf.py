project = "onap"
release = "master"
version = "master"

# Map to 'latest' if this file is used in 'latest' (master) 'doc' branch.
# Change to {releasename} after you have created the new 'doc' branch.
branch = 'latest'

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

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.plantuml',
    'sphinx_needs',
]

master_doc = 'index'

exclude_patterns = [
    '.DS_Store',
    '_build',
    'Thumbs.db',
    '.tox',
]

todo_include_todos = False

intersphinx_mapping = {
    'modeling': ('https://docs.onap.org/projects/onap-modeling-modelspec/en/latest/', None),
    'dcae': ('https://docs.onap.org/projects/onap-dcaegen2/en/latest/', None),
    'appc': ('https://docs.onap.org/projects/onap-appc/en/latest/', None),
    'appc-deployment': ('https://docs.onap.org/projects/onap-appc-deployment/en/latest/', None),
}

linkcheck_ignore = [
    'http://localhost',
]

spelling_word_list_filename = 'spelling_wordlist.txt'
spelling_lang = "en_GB"

html_last_updated_fmt = '%d-%b-%y %H:%M'


def setup(app):
    app.add_css_file("css/ribbon.css")


# -- sphinx-needs configuration ----------------------------------------------

from docutils.parsers.rst import directives

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
