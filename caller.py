from dotenv import load_dotenv
import os
import requests
import json
load_dotenv(".env")
groups = {
    
    "22A":os.environ.get("SD22_A"),
    "22B":os.environ.get("SD22_A"),
    "23":os.environ.get("SD23"),
}
url = "https://git.nexed.com/api/v4/"
api_key = str(os.environ.get("API_KEY"))
urlstring = f"{url}groups/{groups['22A']}/subgroups?private_token={api_key}&per_page=100"
print(urlstring)

membersSD22A= requests.get(urlstring)

with open("members.json", "w") as file:
    file.write(json.dumps(membersSD22A.json()))
