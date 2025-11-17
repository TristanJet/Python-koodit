import requests
import json

req = requests.get("https://api.chucknorris.io/jokes/random")

if req.status_code != 200:
    print('Request failed')
    exit()

d = json.loads(req.text)
print(d['value'])
