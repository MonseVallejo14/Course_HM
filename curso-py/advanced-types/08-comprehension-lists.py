users = [
    ["Murphy", 5],
    ["Pulgas", 2],
    ["Cleo", 1],
    ["Freyja", 4],
    ["Polar", 3]
]

# If we need only the names in this list, we can use a "for":

# names = []
# for user in users:
#     names.append(user[0])
#     print(names)

# We are TRANSFORMING the list

# Short way: "variable = [expression for item in items]"

# names = [user[0] for user in users]

# FILTER:

# names = [user for user in users if user[1] > 2]

# FILTER AND TRANSFORM:

# names = [user[0] for user in users if user[1] > 2]

# TRANSFORM using the function "map": "variable = list(map(lambda item: expression, items))"

# names = list(map(lambda user: user[0], users))
# print(names)

# FILTER using the function "filter":

fewer_names = list(filter(lambda user: user[1] > 2, users))
print(fewer_names)
