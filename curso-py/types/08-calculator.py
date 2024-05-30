import math

n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))

add = n1 + n2
subt = n1 - n2
div = n1 / n2
multi = n1 * n2
power = pow(n1, n2)

mensaje = f"""
For the numbers {n1} y {n2},
the result of the sum is {add},
the result of the subtraction is {subt},
the result of the division is {div},
the result of the multiplication is {multi},
and the result of {n1} to the power to {n2} is {power}.
"""

print(mensaje)
