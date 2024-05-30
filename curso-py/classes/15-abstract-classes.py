from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self):
        if not self.table:
            print("Eror, you have to define a table")

    @property
    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @classmethod
    def search_by_ID(self, _ID):
        print(f"Searching by ID {_ID} in the table {self.table}")


class User(Model):
    table = "User"

    def save(self):
        print("Saving user")


user = User()
user.save()
user.search_by_ID(23)
