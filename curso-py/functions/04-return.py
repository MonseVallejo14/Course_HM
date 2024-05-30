# We can assing the product or result of the content or the instructions of a function to a variable with the word "return":

def add(a, b):
    result = a + b
    return result


c = add(2, 3)   # The varible "c" will have the resulting value of the function
d = add(c, 8)

print(d)
