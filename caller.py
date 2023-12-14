from dotenv import load_dotenv
import os
import requests
import json
load_dotenv(".env")
group_names = {
    
    "22A":os.environ.get("SD22_A"),
    "22B":os.environ.get("SD22_A"),
    "23":os.environ.get("SD23"),
}
cwd = os.getcwd()
url = "https://git.nexed.com/api/v4/"
api_key = str(os.environ.get("API_KEY"))
group_objects={}
for group in group_names:
    print(group)
    urlstring = f"{url}groups/{group_names[f'{group}']}/subgroups?private_token={api_key}&per_page=65"

    
    
    members =requests.get(urlstring)
    
    member_objects =[] 
    for member in members.json():
       member_objects.append(member["name"])
       """
        group_id = member["id"]
        repos_url =f"{url}groups/{group_id}/projects?private_token={api_key}&per_page=65"

        projects = requests.get(repos_url)
        member_objects.append(projects.json())
"""
    group_objects.update({f"{group}":member_objects})
with open("members.json", "w") as file:
    file.write(json.dumps(group_objects))
print(group_objects["22A"][0])


