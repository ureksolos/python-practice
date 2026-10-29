import json

data = [{"desc": "food", "amount": 12.5}]

# save
with open("data.json", "w") as f:
    json.dump(data, f, indent = 2)

# load
with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print(type(loaded))