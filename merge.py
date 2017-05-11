import os

files = [os.path.join('resmi', 'py2', 'py2-omegat.tmx'),
         os.path.join('resmi', 'py3', 'py3-omegat.tmx'),
         os.path.join('resmi', 'omegat', 'tm', 'auto', 'resmi-omegat.tmx')]
         
os.system('java -jar merge.jar %s' %' '.join(f for f in files))