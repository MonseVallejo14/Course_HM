# Ugly way:
# numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# print(first, second, third)

# Nice way:
# numbers = [1, 2, 3]
# first, second, third = numbers
# print(first, second, third)

large_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *others, last = large_num
print(first, last, others)
