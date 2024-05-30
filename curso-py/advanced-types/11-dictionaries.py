# Dictionaries are elements grouped in keys with values: variable = {"key": value, "key2": value2...}

point = {"x": 25, "y": 50}
print(point)

# To acces to a element (value), we need to write the key

print(point["x"])
print(point["y"])

# We can add elements

point["z"] = 45
print(point)

# When the key doesn't exist, it gives us an Keyerror
# The dictionaries have a method called "get"
# This method gives us the answer "none" when a key doesn't exist, and we can give a value to said key

print(point.get("lala", 97))

# To delete a key with his value

# del point["x"]
# del (point["y"])

# print(point)

# To access to all the elements of a dictionary, the keys and them values

for value in point:
    print(value, point[value])

for value in point.items():  # This way gives us tuples
    print(value)

for key, value in point.items():
    print(key, value)

users = [
    {"ID": 1, "Name": "Murphy"},
    {"ID": 2, "Name": "Cleo"},
    {"ID": 3, "Name": "Freyja"},
    {"ID": 4, "Name": "Polar"},
]

# To access only names

for user in users:
    print(user["Name"])
