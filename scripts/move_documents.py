import os
from os.path import join, dirname, realpath, exists
import shutil
from color import error, success, warning

# TODO: put these in a utils module or something
file = realpath(__file__)
script_dir = dirname(file)
root = dirname(script_dir)
build = join(root, 'build')
target = join(build, 'html')
docs = join(root, 'docs')

def check_dir(d, hint = ""):
	if not os.path.exists(d) or not os.path.isdir(d):
		error(f"ERROR: '{d}' directory is not found. Can't copy files.\n" + hint)
		exit()

check_dir(build, "Hint: Are you sure you built the docs as described in BUILDING.md?")
check_dir(target, "Hint: Are you sure you built the HTML files as described in BUILDING.md?")
check_dir(docs, "Hint: Did you clone the repository succesfully?")

project = 'Yazbel Python Belgeleri'

epub_file = join(build, 'epub', '{}.epub'.format(project))
pdf_file = join(build, 'latex', '{}.pdf'.format(project.replace(' ', '').lower()))
html_file = join(build, 'singlehtml', 'index.html')

output_name = 'YazbelPythonProgramlamaDiliBelgeleri'
for file in [epub_file, pdf_file, html_file]:
	ext = file.rsplit('.', 1)[1]
	target_name = output_name + "." + ext
	file_type = "HTML (single file)" if ext == "html" else ext.upper()
	try:
		shutil.copy2(file, join(target, target_name))
	except FileNotFoundError:
		warning(f"Passing {file_type} file since it is not found in the build directory. Preserving the old {file_type} file instead.")
		# copy the old build so that they don't get deleted
		try:
			shutil.copy2(join(docs, target_name), join(target, target_name))
		except FileNotFoundError:
			error(f"ERROR: Couldn't find the old {file_type} file.\nHint: Did you perhaps delete the files that were in the docs directory?")
			exit()
	else:
		print(f"Copied {file_type} file to the docs directory.")


# fix this, we shouldn't be deleting it altogether
# also we might want to preserve the output files (PDF, EPUB) in a permanent directory in case the script gets killed just after deleting docs
if exists(docs):
	shutil.rmtree(docs)


shutil.copytree(target, docs, copy_function = shutil.copy2)
print("Copied the hosted HTML files to the docs directory.")
success("Successfully copied the required files.")