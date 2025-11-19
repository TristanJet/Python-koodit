import json

with open("content", "r") as f:
    obj = json.load(f)
    f.close()

for s in obj:
    print(f"{s["show"]["name"]} - {s["show"]["summary"]}\n")
# print(obj[0])
