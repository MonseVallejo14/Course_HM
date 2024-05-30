class MyError(Exception):
    "This class is to represent my error"

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"{self.message} - code: {self.code}"


def division(n=0):
    if n == 0:
        raise MyError("Can't be divided by zero", 805)
    return 5 / n


try:
    division()
except MyError as e:
    print(e)
