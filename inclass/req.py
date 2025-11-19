import requests

query = "basketball"

c = requests.get("https://api.tvmaze.com/search/shows?q=" + query)

print(c.text)
