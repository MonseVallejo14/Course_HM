# "range(#)" indicates the number of elements of a list -1

search = input("What user are you looking for?")
search = int(search)

for number in range(7):
    print(number)
    if number == search:
        print("User found.", search)
        break
else:
    print("User not found. :(")

# The strings are iterable to:
# "char" is for character

for char in "Ultimate python":
    print(char)
