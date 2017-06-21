#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.githubpages', 'sphinx.ext.intersphinx', 'sphinxcontrib.napoleon']

templates_path = ['templates']
source_suffix = '.rst'

master_doc = 'index'

project = 'ModernGL.ext.obj'
copyright = '2017, Szabolcs Dombi'
author = 'Szabolcs Dombi'

version = '0.1.0'
release = '0.1.0'

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['static']

htmlhelp_basename = 'ModernGL.ext.obj.doc'

latex_elements = {}

latex_documents = [
    (master_doc, 'ModernGL.ext.obj.tex', 'ModernGL.ext.obj Documentation', 'Szabolcs Dombi', 'manual'),
]

man_pages = [
    (master_doc, 'ModernGL.ext.obj', 'ModernGL.ext.obj Documentation', [author], 1)
]

texinfo_documents = [
    (
        master_doc,
        'ModernGL.ext.obj',
        'ModernGL.ext.obj Documentation',
        author,
        'ModernGL.ext.obj',
        'One line description of project.',
        'Miscellaneous'
    ),
]


def setup(app):
    app.add_stylesheet('css/custom.css')


autodoc_member_order = 'bysource'
# autodoc_member_order = 'groupwise'
add_module_names = False
