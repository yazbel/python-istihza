import shutil
import os

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

builds = os.path.join("build", "html")

for i in os.listdir(builds):
    full_path = os.path.join(builds, i)

    if os.path.exists(i):
        if os.path.isfile(i):
            os.remove(i)
        else: # klasör ise
            if i.startswith("_"): # _static klasörü
                for file in os.listdir(i):
                    dir_in_builds = os.path.join(builds, i)
                    if file not in os.listdir(dir_in_builds):
                        shutil.move(os.path.join(i, file), dir_in_builds)
            
            shutil.rmtree(i)
                

    shutil.move(full_path, current_path)


shutil.rmtree("build")
