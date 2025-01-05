import os
from os.path import join, dirname, realpath, exists
import shutil
from color import error, success, warning

# Utility functions
def check_dir(d, hint=""):
    """Check if directory exists, if not print error and exit."""
    if not os.path.exists(d) or not os.path.isdir(d):
        error(f"ERROR: '{d}' directory is not found. Can't copy files.\n" + hint)
        exit()

def backup_file(file, backup_dir):
    """Backup file before any potentially destructive operation."""
    if not exists(backup_dir):
        os.makedirs(backup_dir)  # Ensure backup directory exists
    backup_path = join(backup_dir, os.path.basename(file))
    try:
        shutil.copy2(file, backup_path)
        print(f"Backup created for {file} at {backup_path}")
    except FileNotFoundError:
        warning(f"Warning: The file {file} to be backed up was not found.")
    except Exception as e:
        warning(f"Warning: Failed to back up {file}. Error: {e}")

# Paths and project setup
file = realpath(__file__)
script_dir = dirname(file)
root = dirname(script_dir)
build = join(root, 'build')
target = join(build, 'html')
docs = join(root, 'docs')

# Check directories
check_dir(build, "Hint: Are you sure you built the docs as described in BUILDING.md?")
check_dir(target, "Hint: Are you sure you built the HTML files as described in BUILDING.md?")
check_dir(docs, "Hint: Did you clone the repository successfully?")

# Project name and output file paths
project = 'Yazbel Python Belgeleri'
epub_file = join(build, 'epub', '{}.epub'.format(project))
pdf_file = join(build, 'latex', '{}.pdf'.format(project.replace(' ', '').lower()))
html_file = join(build, 'singlehtml', 'index.html')

output_name = 'YazbelPythonProgramlamaDiliBelgeleri'

# Process each file
for file in [epub_file, pdf_file, html_file]:
    ext = file.rsplit('.', 1)[1]
    target_name = output_name + "." + ext
    file_type = "HTML (single file)" if ext == "html" else ext.upper()

    try:
        # Copy new file
        shutil.copy2(file, join(target, target_name))
        print(f"Copied {file_type} file to the docs directory.")
    except FileNotFoundError:
        # File missing in the build, try to use the old version from docs
        warning(f"Passing {file_type} file since it is not found in the build directory. Preserving the old {file_type} file instead.")
        try:
            backup_file(join(docs, target_name), join(root, 'backup_files'))  # Backup the old file before copying it
            shutil.copy2(join(docs, target_name), join(target, target_name))
            print(f"Restored {file_type} from docs directory.")
        except FileNotFoundError:
            error(f"ERROR: Couldn't find the old {file_type} file.\nHint: Did you perhaps delete the files that were in the docs directory?")
            exit()
    except Exception as e:
        error(f"ERROR: Failed to copy {file_type} file. Error: {e}")
        exit()

# Handle the removal and copying of directories
if exists(docs):
    try:
        shutil.rmtree(docs)
        print(f"Removed existing docs directory.")
    except Exception as e:
        warning(f"Warning: Failed to remove docs directory. Error: {e}")

# Copy the new HTML files to docs
shutil.copytree(target, docs, copy_function=shutil.copy2)
print("Copied the hosted HTML files to the docs directory.")

# Final success message
success("Successfully copied the required files.")
