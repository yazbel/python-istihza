# Configuration file for the Sphinx documentation builder.
#
# For a full list of options that you can use here see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
from os.path import join
import datetime

_shared = join("..", "shared")

year = datetime.datetime.now().year

# project information
author = 'Fırat Özgül | yazbel.com'
project = 'Yazbel Python Belgeleri'
copyright = '2007-{}, {}'.format(year, 'Fırat Özgül')
basename = project

# project structure
root_doc = 'index'
highlight_language = 'python3'
needs_sphinx = '8.0'

file = os.path.realpath(__file__)
source_dir = os.path.dirname(file)

config_dir = "_configuration"
repl_file_path = join(config_dir, 'replacements.txt')
rst_prolog = '.. include:: {}'.format(repl_file_path)

theme_dir = join(source_dir, "_theme")
templates = join(theme_dir, 'templates')
statics = join(theme_dir, 'static')
templates_path = [templates]
html_static_path = [statics]

logo = join(statics, 'logo.png')

# the full version, including alpha/beta/rc tags
with open(join(_shared, "project_version.txt"), "r") as f:
	_versions = list(map(lambda x: x[:-1] if x.endswith("\n") else x, f))
	_version = _versions[-1]
	release = _version

# general configuration
extensions = ["sphinx.ext.githubpages"]
exclude_patterns = []
language = 'tr'

# this is required for githubpages extension to generate a CNAME file
html_baseurl = 'https://python-istihza.yazbel.com/'

# html
html_title = project
html_theme = 'pyramid'
html_last_updated_fmt = '%d.%m.%Y'
html_show_sourcelink = False
html_theme_options = {'nosidebar': True}
html_favicon = 'favicon.ico'

# epub
suppress_warnings = ["epub.unknown_project_files"] # for suppressing meaningless unknown mimetype warnings
epub_title = project
epub_identifier = epub_publisher = 'yazbel.com'
epub_basename = basename
epub_cover = (logo, '')
epub_theme = 'epub'
epub_show_urls = 'footnote'
version = release

# latex
# also see: https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.latex.LaTeXBuilder
latex_engine = 'pdflatex'
latex_logo = logo
latex_show_urls = 'footnote'
latex_elements = {
	"papersize": "a4paper",
	"pointsize": "11pt",
	"extraclassoptions": "openany",
	"fontpkg": r"\usepackage[defaultsans]{droidsans}",
	"preamble": r"""
\usepackage[none]{hyphenat}
\usepackage{pdfpages}
\renewcommand*\familydefault{\sfdefault}
\def\verbatim@font{\normalfont\sffamily}
\definecolor{VerbatimColor}{rgb}{0.9,0.9,0.9} % kod bloğu arkaplan rengi
\definecolor{VerbatimBorderColor}{rgb}{1,1,1} % kod bloğu çerçeve rengi
\addto\captionsenglish{\renewcommand\chaptername{Bölüm}}
\addto\captionsenglish{\renewcommand\contentsname{İÇİNDEKİLER}}
"""
}

cover = join(config_dir, 'cover', 'kapak.pdf')
customcls = join(config_dir, 'custom.cls')
latex_additional_files = [cover, customcls]

# other
today_fmt = html_last_updated_fmt
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

