# For multiple arguments in a function, we need to use aasterisk before the parameter, and "for" to apply the function to all the arguments:
# The asterisk transforms the parameters in iterables

def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


add(5, 3, 7, 4, 2)
add(2, 3)
add(1, 4, 45)
