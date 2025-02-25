""" Here we will learn about the json module """
from xml.etree.ElementTree import indent

"""
Json : Json is an JavaScript ObjectNotation it light weight data format.
"""
import json
data = {
    "name" : "Jon",
    "age" : 27,
    "tools" : ["Automation Testing", "Performance Testing"],
    "student" : False
}
print(json.dumps(data, indent= 4))

with open('sample.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('sample.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)


