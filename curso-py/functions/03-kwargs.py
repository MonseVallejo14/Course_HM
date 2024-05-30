# We can encompass multiple parameters in one with the function keyword arguments (activated with double asterisk):
# We need to indicate the name of the parameter before the argument

# def get_product(**data):
#     print(data)


# # get_product(product="Cellphone",
#               brand="iPhone",
#               cost="$1,200")

# We can access certain data from the function if we can't need all the arguments:
# We write the parameters like a strings in the function

def get_product(**data):
    print(data["product"], data["brand"])


get_product(product="Cellphone",
            brand="iPhone",
            cost="$1,200")
