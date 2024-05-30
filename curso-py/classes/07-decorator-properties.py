class Dog:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("Going through getter")
        return self.__name

    @name.setter
    def name(self, name):
        print("Going through setter")
        if name.strip():
            self.__name = name


dog = Dog("Choclo")
print(dog.name)
