from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def save(self):
        pass


class User(Model):
    def save(self):
        print("Saving in DB")


class Session(Model):
    def save(self):
        print("Saving to file")


def save(entities):
    for entity in entities:
        entity.save()


user = User()
session = Session()
save([session, user])
