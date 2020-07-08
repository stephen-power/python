#!/usr/bin/python
import json
print("start")

# json to python
x = '{"name":"john", "age":30 }'
# parse x
y = json.loads(x)
print(y["age"])

# python to json
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
print(y)

# convert python to json when writing to file
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
