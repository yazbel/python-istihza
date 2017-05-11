# -*- coding: utf-8 -*-

'''Common configuration options for all build operations'''

import os, time

master_doc              = 'index'
language                = 'tr'
highlight_language      = 'python3'
stdauthor               = u'Yazan: Fırat Özgül'

base                    = os.path.dirname(__file__)
theme_path              = os.path.join(base, 'theme')
templates_path          = [os.path.join(theme_path, '_templates')]
html_static_path        = [os.path.join(theme_path, '_static')]

repl_file_path          = os.path.join(base, 'replacements.rpl')
repl_file               = open(repl_file_path).readlines()

rst_prolog              = '.. include:: /%s' % repl_file_path

copyright               = u'2007-%s, Fırat Özgül | ' % time.strftime('%Y')

today_fmt               = '%d.%m.%Y'

#html output
html_theme              = 'pyramid'
html_last_updated_fmt   = '%d.%m.%Y'
html_use_smartypants    = True
html_show_sourcelink    = False
html_theme_options      = {'nosidebar': True}

#latex output  
latex_paper_size        = 'a4'
latex_font_size         = '11pt'
latex_elements          = {'inputenc'       : r'\usepackage[utf8]{inputenc}',
                           'fontenc'        : r'\usepackage[T1]{fontenc}',
                           'fontpkg'        : r'\usepackage[defaultsans]{droidsans}',
                           'babel'          : r'\usepackage[english]{babel}',
                           'classoptions'   : ',openany'}
                           
latex_preamble          = u'''
\\usepackage[none]{hyphenat} 
\\usepackage{pdfpages}
\\renewcommand*\\familydefault{\\sfdefault}
\\def\verbatim@font{\\normalfont\\sffamily}
\\definecolor{VerbatimColor}{rgb}{0.9,0.9,0.9}
\\definecolor{VerbatimBorderColor}{rgb}{1,1,1}
\\addto\captionsenglish{\\renewcommand\\chaptername{Bölüm}}
\\addto\captionsenglish{\\renewcommand\\contentsname{İÇİNDEKİLER}}
'''

#epub output
epub_theme              = 'epub'
epub_show_urls          = 'false'
epub_author             = stdauthor
epub_identifier = epub_publisher = 'istihza.com'
