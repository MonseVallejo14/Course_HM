# The magic methods are executed even when we don't call them
# Magic method: "__method__"
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Bye dog :( {self.name}")

    def __str__(self):
        return f"Class Dog: {self.name}"

    def talk(self):
        print(f"{self.name} dice: Guau!")


dog = Dog("Cleo", 7)
del dog
