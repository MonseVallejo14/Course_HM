class Model():
    table = False

    def __init__(self):
        if not self.table:
            print("Eror, you have to define a table")

    def save(self):
        print(f"Saving {self.table} in DB")

    @classmethod
    def search_by_ID(self, _ID):
        print(f"Searching by ID {_ID} in the table {self.table}")


class User(Model):
    table = "User"


user = User()
user.save()
User.search_by_ID(23)
