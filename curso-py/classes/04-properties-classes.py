# We can create a propierty for a class

class Dog:
    paws = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"{self.name} dice: Guau!")


Dog.paws = 3
my_dog = Dog("Cooper", 2)
my_dog.paws = 5
my_dog2 = Dog("Morgan", 3)
print(Dog.paws)
print(my_dog.paws)
print(my_dog2.paws)
