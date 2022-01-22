import os
from os.path import join, dirname, realpath, exists
import shutil

file = realpath(__file__)
script_dir = dirname(file)
root = dirname(script_dir)
build = join(root, 'build')
target = join(build, 'html')
docs = join(root, 'docs')

project = 'Yazbel Python Belgeleri'

epub_file = join(build, 'epub', '{}.epub'.format(project))
pdf_file = join(build, 'latex', '{}.pdf'.format(project.replace(' ', '').lower()))
html_file = join(build, 'singlehtml', 'index.html')

output_name = 'YazbelPythonProgramlamaDiliBelgeleri'
for file in [epub_file, pdf_file, html_file]:
	ext = file.rsplit('.', 1)[1]
	target_name = output_name + "." + ext
	try:
		shutil.copy2(file, join(target, target_name))
	except FileNotFoundError:
		print(f"Passing {ext.upper()} file since it is not found in build directory.")
		# copy the old build so that they don't get deleted
		shutil.copy2(join(docs, target_name), join(target, target_name))


# fix this, we shouldn't be deleting it altogether
if exists(docs):
	shutil.rmtree(docs)


shutil.copytree(target, docs, copy_function = shutil.copy2)