import random
import string

list = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(list)
print(
    random.random(),
    random.randint(1, 10),
    list,
    random.choice(list2),
    random.choices(list2, k=3),
    random.choices("abcushgdfiughfg", k=3)
)

chars = string.ascii_letters
digits = string.digits
selection = random.choices(chars + digits, k=16)
password = "".join(selection)
print(password)
