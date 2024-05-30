welcome = "Welcome to the calculator."
instructions = """To exit write \"exit\".
The operations are \"add\", \"subtraction\", \"multiplication\" and \"division\"."""

print(welcome)
print(instructions)

result = ""
while True:
    if not result:
        result = input("Enter a number: ")
        if result.lower() == "exit":
            break
        result = int(result)
    op = input("Enter an operation: ")
    if op.lower() == "exit":
        break
    n2 = input("Enter the next number: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)
    if op.lower() == "add":
        result += n2
    elif op.lower() == "subtraction":
        result -= n2
    elif op.lower() == "multiplication":
        result *= n2
    elif op.lower() == "division":
        result /= n2
    else:
        print("Inavlid operation")

    print(f"The result is {result}")
