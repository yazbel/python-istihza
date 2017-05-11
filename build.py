import os
import sys
import shutil
import subprocess
import glob

projects = [sys.argv[1]]

basedir = os.path.abspath(os.path.dirname(__file__))

cmds = {"build"   : "sphinx-build -b {} {} {}", #builds html or tex files
        "win_pdf" : "texify --clean --pdf --tex-option=-synctex=1", #compiles pdf on Windows
        "glin_pdf" : "make all-pdf", #compiles pdf on GNU/Linux
       } 
            
def make_output(output):
    '''
    Generates html, latex or epub depending on the value of output.
    output is one of 'html', 'latex' or 'epub'.
    '''
    for project in projects:
        source = os.path.join(project, "sphinx_source") 
        target = os.path.join(project, "build", output)
        subprocess.call(cmds["build"].format(output, source, target).split())

def make_pdf():
    '''Generates a pdf file from tex files. Note that this function does not 
    create any tex files. ``make_output('latex')`` does that. So before
    running this function, we must make sure that tex files exist.
    '''
    for project in projects:
        try:
            os.chdir(os.path.join(project, "build", "latex"))
            if os.name == "nt":
                subprocess.call(cmds["win_pdf"].split() + glob.glob("*.tex"))
            else:
                subprocess.call(cmds["glin_pdf"].split() + glob.glob("*.tex"))
        except OSError: #ignore missing build directory
            pass
        
        #all the way back to the starting dir
        os.chdir(os.path.join(basedir))
       
def production():
    '''Creates html and pdf all at once.'''
    
    make_output('html')
    make_output('latex') #first create tex...
    make_pdf()  #...and then pdf...
    make_output('epub') #create epub
    
def move():
    '''Moves compiled files to their respective locations'''
    for project in projects:
        htmldir = os.path.join(project, "build", "html")
        pdfdir = os.path.join(project, "build", "latex")
        epubdir = os.path.join(project, "build", "epub")
        
        wwwbelgeler = "/var/www/html/belgeler/{}".format(project)
        wwwindir = "/var/www/html/indir/belgeler/{}".format(project)
        
        shutil.rmtree(wwwbelgeler)
        shutil.rmtree(wwwindir)
        
        pdf = glob.glob(os.path.join(pdfdir, '*.pdf'))[0]
        epub = glob.glob(os.path.join(epubdir, '*.epub'))[0]

        if not os.path.exists(wwwbelgeler):
            os.makedirs(wwwbelgeler)
            
        for f in os.listdir(htmldir):
            shutil.move(os.path.join(htmldir, f), wwwbelgeler)
            
        if not os.path.exists(wwwindir):
            os.makedirs(wwwindir)
        
        shutil.move(pdf, wwwindir)
        shutil.move(epub, wwwindir)
                    
def delete():
    '''Deletes all files in build directory'''
    for project in projects:
        target = os.path.join(project, "build")
        if os.path.exists(target):
            shutil.rmtree(target)
        else:
            pass

arg = sys.argv[2]

if arg in ('html', 'latex', 'epub'):
    make_output(arg)
    
else:
    if arg == 'delete':
        delete()
        
    elif arg == 'htmlpdf':
        make_output('html')
        make_output('latex')
        make_pdf()
        
    elif arg == 'pdf':
        make_output('latex')
        make_pdf()
        
    elif arg == 'production':
        production()
        
    elif arg == 'move':
        move()
        


        
