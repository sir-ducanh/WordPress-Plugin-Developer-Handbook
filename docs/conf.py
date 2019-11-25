# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'sphinx_tabs.tabs',
    'sphinx-prompt',
    'recommonmark',
    'sphinx_search.extension',
    'sphinx_rtd_theme',
    'sphinxcontrib.inlinesyntaxhighlight'
]
# use language set by highlight directive if no language is set by role
inline_highlight_respect_highlight = False

# use language set by highlight directive if no role is set
inline_highlight_literals = False

templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'WordPress-Plugin-Developer-Handbook'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
htmlhelp_basename = 'wordpress-plugin-developer-handbook'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False
latex_documents = [
  ('index', 'wordpress-plugin-developer-handbook.tex', u'WordPress-Plugin-Developer-Handbook Documentation',
   u'', 'manual'),
]

# -- Options for sphinx-intl example

locale_dirs = ['locale/']   # po files will be created in this directory
gettext_compact = False     # optional: avoid file concatenation in sub directories.
