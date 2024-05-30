age = input("How old are you?")

age = int(age)

if age >= 50:
    print("You can watch the movie with a discout.")
elif age >= 18:
    print("You can watch the movie.")
else:
    print("You can't watch the movie.")
    print("You should watch a kids movie haha.")
