# and, or, not

# We use "and" when we need that 2 or more conditions to be true to validate a process. For example:
print("Please, answer the questions with \"Yes\", \"No\", and numbers in your age:")

gas = input("Does your car have gasoline?")
gas = True if gas == "Yes" else False

on = input("Your car is on?")
on = True if on == "Yes" else False

age = input("How old are you?")
age = int(age)

if gas and on and age >= 18:
    print("You can drive.")
else:
    print("You can't drive.")

# We use "or" when only need that one of 2 or more conditions to be true to validate a process. For example:
print("Please, answer the questions with \"Yes\" or \"No\":")

exp = input("Do you have experience?")
exp = True if exp == "Yes" else False

cont = input("Do you have contacts?")
cont = True if cont == "Yes" else False

if exp or cont:
    print("You're hired.")
else:
    print("We'll call you.")

# We use "not" when we need to negate the result of a condition. For example:
print("Please, answer the questions with \"Yes\", \"No\", and numbers in your age:")

gas = input("Doesn't your car have gasoline?")
gas = True if gas == "No" else False

on = input("Your car is on?")
on = True if on == "Yes" else False

age = input("How old are you?")
age = int(age)

if not gas and on and age >= 18:
    print("You can drive.")
else:
    print("You can't drive.")

# This logical operators are ejecuted from left to right:
# When we use "and" or "or", the first value that is evaluaed as "True" stop the evaluation of the others values.
