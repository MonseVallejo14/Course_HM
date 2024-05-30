# For x = input("") the value will always be a string

# To make a conversion, we use:
# int() to convert a string in a integer number
# str() to convert any value in a string
# float() to convert any value in a float
# bool() to convert any value in a boolean:
#        Falsy values: Empty string (""), none, 0
#        Truthy values: A string with a space (" "), a string with the value 0 ("0")

print(bool(""))
print(bool(None))
print(bool(0))
print(bool(" "))
print(bool("0"))
