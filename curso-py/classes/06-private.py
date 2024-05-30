# When making amethod private we can't acsses it

class Dog:

    def __init__(self, name, age):
        self.__name = name
        self.age = age

# But, if we want to access the private property, we can create a method to do it:
    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name

    def talk(self):
        print(f"{self.__name} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Cleo", 7)


dog1 = Dog.factory()
dog1.talk()
# "__dict__" gives us a dictionary with thw properties asociated to a instance of a class
print(dog1.__dict__)
