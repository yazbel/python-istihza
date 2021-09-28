import shutil
import os

project_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_root)

build_dir = os.path.join("build", "html")

for i in os.listdir(build_dir):
    path = os.path.join(build_dir, i)

    # delete old documents
    if os.path.exists(i):
        if os.path.isfile(i):
            os.remove(i)
        else:            
            shutil.rmtree(i)
                
    # copy newly build documents
    shutil.move(path, project_root)

