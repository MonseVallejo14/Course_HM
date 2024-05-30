def division(n=0):
    if n == 0:
        raise ZeroDivisionError(f"Can't be divided by zero, {n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)
