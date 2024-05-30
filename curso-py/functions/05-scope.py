# The value of a variable defined within a function, can only be called within said function:
# It doesn't matter if are more than one variable with the same name as long as they are in different functions.

greeting = "Global hello"


def greet_world():
    greeting = "Hello world"
    print(greeting)


def greet_cat():
    greeting = "Hello Murphy"
    print(greeting)


print(greeting)
greet_cat()
greet_world()

# The variables outside of a context are called "global variables", and isn't recommend to use it because they can be exchanged unintentionally and interfere with the code.
