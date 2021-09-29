import shutil
import os

project_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_root)

build_dir = os.path.join("build", "html")

for i in os.listdir(build_dir):
    path = os.path.join(build_dir, i)

    if os.path.isfile(path):
        try:
            # delete the old document
            os.remove(i)
        except FileNotFoundError:
            print(f"INFO: Adding the new file {repr(i)} to the project.")
            pass
        # copy by preserving metadata
        shutil.copy2(path, project_root)
    elif os.path.isdir(path):
        try:
            shutil.rmtree(i)
        except FileNotFoundError:
            print(f"INFO: Adding the new directory {repr(i)} to the project.")
            pass
        shutil.copytree(path, os.path.join(project_root, i), copy_function = shutil.copy2)
    else:
        print(f"WARNING: Passing {path} since it is neither a file nor a directory.")