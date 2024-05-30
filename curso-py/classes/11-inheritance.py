class Animal:
    def eat(self):
        print("eating")


class Dog(Animal):
    def walk(self):
        print("walking")


class Pig(Dog):
    def program(self):
        print("programing")


pig = Pig()
