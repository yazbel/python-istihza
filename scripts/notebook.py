# pip install sphinx-markdown-builder
# pip install notedown

# build markdown first with: make markdown
# then run this script

import os
from os.path import join, dirname, realpath, exists, relpath
import shutil

file = realpath(__file__)
script_dir = dirname(file)
root = dirname(script_dir)
build = join(root, 'build')
markdown = join(build, 'markdown')
notebook = join(build, 'notebook')

if not exists(markdown):
	raise Exception("Error: Run 'make markdown' first.")

if exists(notebook):
	shutil.rmtree(notebook)
	os.mkdir(notebook)

for path, dirs, files,  in os.walk(markdown):
	path = relpath(path, markdown)
	for d in dirs:
		os.mkdir(join(notebook, path, d))
	for file in files:
		name, ext = file.rsplit(".", 1)
		if ext == "md":
			d = os.system('''notedown "{}" > "{}"'''.format(join(markdown, path, file), join(notebook, path, name + ".ipynb")))
			if d != 0: # exit on error
				exit()
			print("Done:", join(path, file))
