# The stacks work like LIFO (Last In First Out)

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

last_elem = stack.pop()
print(last_elem)
print(stack)
print(stack[-1])

stack.pop()
stack.pop()
if not stack:
    print("Empty stack")
