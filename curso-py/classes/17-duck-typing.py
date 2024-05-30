class User():
    def save(self):
        print("Saving in DB")


class Session():
    def save(self):
        print("Saving to file")


def save(entities):
    for entity in entities:
        entity.save()


user = User()
session = Session()
save([session, user])
