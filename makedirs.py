import json
import os

parent = "Students"
def makedirs(file):
    group_objects = json.load(file)
    print(group_objects)
    for name in group_objects:

        try:
            os.mkdir(os.getcwd()+f"/{parent}/{name}")
            print(f"created folder {name}")
        except FileExistsError:
            print(f"found folder {name}")
        for member in group_objects[name]:
            try: 
                os.mkdir(os.getcwd()+f"/{parent}/{name}/{member}")
                print(f"created folder {member}")
            except FileExistsError:
                print("found student {member}")
