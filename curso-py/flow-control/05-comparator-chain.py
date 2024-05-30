age = input("How old are you?")

age = int(age)

# Large way:
# if age >= 15 and age <= 65:
#     print("You can use the pool.")
# else:
#     print("You can't use the pool.")

# Short way:
if 15 <= age <= 65:
    print("You can use the pool.")
else:
    print("You can't use the pool.")
