list_1 = [1, 2, 3, 4]
tuple = (1, 2, 3, 4)
# print(1, 2, 3, 4)
# print(*list)
# print(*tuple)

list_2 = [5, 6]
mix = ["Murphy", *list_1, *list_2]
print(mix)

coor_1 = {"x": 19}
coor_2 = {"y": 15}
point = {**coor_1, **coor_2, "z": 32}
print(point)
