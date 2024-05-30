# number = 1
# while number < 100:
#     print(number)
#     number *= 2

# cmd = ""

# while cmd.lower() != "salir":
#     cmd = input("$ ")
#     print(cmd)

# Infinite loops can be created, but it is recommended to add an output option:

while True:
    cmd = input("$ ")
    print(cmd)
    if cmd.lower() == "salir":
        break
