from docs_conf.conf import *

branch = 'latest'
master_doc = 'index'
version = 'guilin'

linkcheck_ignore = [
    'http://localhost',
]

intersphinx_mapping.update({
    'modeling': ('https://docs.onap.org/projects/onap-modeling-modelspec/en/latest/', None)
})

html_last_updated_fmt = '%d-%b-%y %H:%M'

def setup(app):
    app.add_stylesheet("css/ribbon.css")


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
