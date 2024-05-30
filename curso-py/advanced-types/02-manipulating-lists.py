pets = ["Murphy", "Cleo", "Zofy", "Mía", "Freyja", "Tortilla", "Wally", "Coco"]
print(pets[0])  # We can call only one element of the list
pets[5] = "Polar"  # We can exchange one element for other
print(pets)
# We can call certain list element:
# This is the element from where it starts -> [#:#] <- This is the element from where it ends
# If we don't put any of the numbers, Python fills it with the first or last element
print(pets[2:])
print(pets[:5])
print(pets[-4])

# We can call alternate elements
numbers = list(range(21))
print(numbers)
print(numbers[::2])
print(numbers[1::2])
print(numbers[::3])
