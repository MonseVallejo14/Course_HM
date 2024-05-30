from io import open

# To write in the file
# text = "Hi world!"

# file1 = open("files/hi-world.txt", "w")  # "w" is for "write"
# file1.write(text)
# file1.close()  # DON'T forget to clse the file

# To read the file
# file1 = open("files/hi-world.txt", "r")
# text = file1.read()
# file1.close()
# print(text)

# To read the file like a list
# file1 = open("files/hi-world.txt", "r")
# text = file1.readlines()
# file1.close()
# print(text)

# with and seek
# with open("files/hi-world.txt", "r") as file1:  # "with" is to close teh file automatically
#     print(file1.readlines())
#     file1. seek(0)
#     for line in file1:
#         print(line)

# To add
# file1 = open("files/hi-world.txt", "a+")
# file1.write("Chao world :(")
# file1.close()

# Reading and writing, only replace the characters that you change
with open("files/hi-world.txt", "r+") as file1:
    text = file1.readlines()
    file1.seek(0)
    text[0] = "Happy Murphy"
    file1.writelines(text)
