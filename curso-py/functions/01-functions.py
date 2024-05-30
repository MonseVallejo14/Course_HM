# We must first define the functions with "def".
# The function will not be executed until we call it.

# def cat(adjetive):
#     print("Murphy is a cat.")
#     print(f"It's a {adjetive} cat. :)")


# cat("ugly")
# cat("feisty")
# cat("fat")
# cat("lazy")

# When we have two or more arguments, these can be optional, and have a certain value when it isn't provided:


def cat(adj1, adj2="lazy"):
    print("Murphy is a cat.")
    print(f"It's a {adj1} and {adj2} cat. :)")


cat("fat", "ugly")
cat("fat")

# We can name the arguments to define which is which according to the parameters of the function:

cat(adj2="ugly", adj1="feisty")
