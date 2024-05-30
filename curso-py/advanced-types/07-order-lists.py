numbers = [23, 45, 2, 67, 132, 4, 8]

# numbers.sort()  # Order the numbers from least to greatest
numbers.sort(reverse=True)  # Order the numbers to gratest to lest
# Order the numbers creating a new list
numbers_2 = sorted(numbers, reverse=True)
print(numbers)
print(numbers_2)


users = [
    ["Murphy", 5],
    ["Pulgas", 2],
    ["Cleo", 1],
    ["Freyja", 4],
    ["Polar", 3]
]

# If the ID or number is before the string, there will no problem in sorting.
# But, if the string is before the number, we need a function:


# def order(element):
#     return element[1]


# users.sort(key=order, reverse=True)
# print(users)


# Short way using "lambda"

users.sort(key=lambda element: element[1])
print(users)
