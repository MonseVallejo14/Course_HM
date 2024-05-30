pets = [
    "Murphy",
    "Cleo",
    "Zofy",
    "Mía",
    "Freyja",
    "Tortilla",
    "Wally",
    "Coco"
]

# To insert elements:
pets.insert(3, "Chandler")
pets.append("Nala")  # In the end

# To delete elements:
pets.remove("Coco")  # We write the name
pets.pop(5)  # We writhe the index
del pets[3]  # We write the index
pets.clear()  # Delete all the elements of the list, but not the list
print(pets)
