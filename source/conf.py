# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.curdir)

import walkup

mc = 'meta_conf.py'

for c, d, f in walkup.walk_up(os.curdir):
    if mc in f:
        sys.path.append(c)

from meta_conf import *

project                 = 'ozgun'
title                   = 'Python'
release                 = '3'
html_title              = u'%s %s için Türkçe Kılavuz' %(title, release)
html_use_modindex       = False
html_use_index          = False

latex_documents         = [('index', '%s%s.tex' %(title.lower(), release),
                            html_title, stdauthor, 'custom')]

epub_title              = html_title
epub_basename           = title.lower() + release

cover                   = '../images/cover/kapak.pdf'
customcls               = '../latex/custom.cls'
latex_additional_files = [cover, customcls]

