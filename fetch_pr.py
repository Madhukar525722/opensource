import requests

username = "Madhukar525722"
token = "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"

url = f"https://api.github.com/search/issues?q=author:{username}+type:pr"
headers = {
    "Authorization": f"token {token}"
}

response = requests.get(url, headers=headers)
data = response.json()

with open('pr_data.json', 'w') as f:
    json.dump(data, f, indent=4)