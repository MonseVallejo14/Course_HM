class Dog:
    paws = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def talk(cls):  # "cls" is use when we create a method of a class
        print("Guau!")

# We can create a method than create instances of a class, this method are called "Factory Method"
    @classmethod
    def factory(cls):
        return cls("Cleo", 7)


Dog.talk()
dog1 = Dog("Copper", 2)
dog2 = Dog("Morgan", 3)
dog3 = Dog.factory()
print(dog3.age, dog3.name)
