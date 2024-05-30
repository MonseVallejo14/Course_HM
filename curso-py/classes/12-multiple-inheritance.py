class Walker:
    def walk(self):
        print("walking")


class Flying:
    def fly(self):
        print("flying")


class Swimmer:
    def swimm(self):
        print("swimming")


class Duck(Walker, Flying, Swimmer):
    def program(self):
        print("programing")


duck = Duck()
