class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - Price:{self.price}"


class Category:
    products = []

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add(self, product):
        self.products.append(product)

    def prin(self):
        for product in self.products:
            print(product)


kayak = Product("Kayak", 1000)
bicicle = Product("Bicicle", 750)
surfboard = Product("Surfboard", 800)
sports = Category("Sports", [kayak, bicicle])
sports.add(surfboard)
sports.prin()
