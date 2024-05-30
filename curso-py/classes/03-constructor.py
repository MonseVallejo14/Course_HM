# The constructor is a funtion that alwals be ejecuted when we create a new instance of the class

class Dog:
    # "self" is a reserved word use in all the classes, to reference all the instances of the class
    def __init__(self, name, age):
        self.name = name  # By adding a dot to "self" we create a property, that is, a variable associated with an instance of a class
        self.age = age

    def talk(self):
        print(f"{self.name} dice: Guau!")


my_dog = Dog("Cooper", 2)
my_dog.talk()
