# To make a new class we need to use the word "class"
# To name new classes, we use the convention "Pascal Case" o "Upper Camel Case", to differentiate it from functions

class Dog:
    def talk(self):  # The functions within classes become methods, and the first parameter must always be "self"
        print("Guau!")


my_dog = Dog()
print(type(my_dog))
my_dog.talk()
# This function tell us if the object is a instance of the class
print(isinstance(my_dog, Dog))
