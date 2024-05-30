
# A "Set" is a group of elements, we use {} and can be modify

first = {1, 1, 2, 2, 3, 4}
second = [3, 4, 5]
second = set(second)

print(first | second)  # "|" for union
print(first & second)  # "&" for intersection
# "-" for diference, remove the elements of the second set that are in the first
print(first - second)
# "^" for symmetricsl difference, remove the elements of the intersection
print(first ^ second)


# The sets are'n ordered, and we can't access to a element
