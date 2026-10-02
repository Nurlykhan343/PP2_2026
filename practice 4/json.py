"""import json

# some JSON:
x =  '{ "name":"Alex","age":25,"city":"London"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


import json

# a Python object (dict):
x = {
  "name": "Alex",
  "age": 25,
  "city": "London"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)"""


import json

print(json.dumps({"name": "Alex", "age": 25}))
print(json.dumps(["orange", "grapes"]))
print(json.dumps(("orange", "grapes")))
print(json.dumps("welcome"))
print(json.dumps(55))
print(json.dumps(28.45))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json

x = {
  "name": "Alex",
  "age": 25,
  "married": False,
  "divorced": False,
  "children": ("Mike", "Sarah"),
  "pets": None,
  "cars": [
    {"model": "Audi A4", "mpg": 30.2},
    {"model": "Toyota Camry", "mpg": 26.8}
  ]
}

print(json.dumps(x))
json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)
