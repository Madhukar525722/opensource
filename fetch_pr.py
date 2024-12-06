import requests
import json

username = "Madhukar525722"
token = "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"

url = "https://api.github.com/search/issues?q=author:{}+type:pr".format(username)
headers = {
    "Authorization": "token {}".format(token)
}

response = requests.get(url, headers=headers, verify=False)
data = response.json()

with open('pr_data.json', 'w') as f:
    json.dump(data, f, indent=4)