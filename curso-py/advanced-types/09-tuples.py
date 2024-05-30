# A "tuple", is a list that can't be modified, we use "()"

numbers = (1, 2, 3) + (4, 5, 6)

# We can transform a list in a tuple:
point = tuple([1, 2])
print(point)

# We can acces to a elements of a tuple

fewer_numbers = numbers[:2]
print(fewer_numbers)

first, second, *others = numbers
print(first, second, others)

for n in numbers:
    print(n)

# If we need to modify a tuple, we need to create a list:

numbers_list = list(numbers)
numbers_list[0] = "Murphy"
print(numbers_list)
