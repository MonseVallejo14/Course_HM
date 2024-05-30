# We can iterate elements of a list with "for", and we get a list of tuples:
pets = ["Murphy", "Cleo", "Zofy", "Mía", "Freyja", "Tortilla", "Wally", "Coco"]

for pet in enumerate(pets):
    print(pet)

# Tuples are like list, we can access a one of the elements:

for index, pet in enumerate(pets):
    # print(pet[0])  # For numbers
    # print(pet[1])  # For names
    print(index, pet)  # For names with their number
