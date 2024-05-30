from collections import deque

row = deque([1, 2])
# row.append(3)
# row.append(4)
# row.append(5)
print(row)
row.popleft()
row.popleft()
print(row)
if not row:
    print("Empty row")

# The rows work like FIFO (First In First Out)
