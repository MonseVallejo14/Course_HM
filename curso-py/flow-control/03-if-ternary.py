### Other ways to do the last lesson: ###

age = input("How old are you?")

age = int(age)

## First way: ##

# if age >= 18:
#     message = "You're an adult."
# else:
#     message = "You're a child."

## Second way (short way): ##

message = "You're an adult." if age >= 18 else "You're a child."

print(message)
