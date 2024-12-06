import requests
import json

username = "Madhukar525722"
token = YOUR_GITHUB_TOKEN

url = "https://api.github.com/search/issues?q=author:{}+type:pr".format(username)
headers = {
    "Authorization": "token {}".format(token)
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

with open('pr_data.json', 'w') as f:
    json.dump(data, f, indent=4)