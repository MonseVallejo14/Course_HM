class Bird:  # <- Parent class
    def fly(self):
        print("Fly bird")


class Duck(Bird):  # <- Subclass
    def fly(self):
        super().fly()  # This word shows us all the methods of the parent class
        print("Fly duck")


Duck = Duck()
Duck.fly()
