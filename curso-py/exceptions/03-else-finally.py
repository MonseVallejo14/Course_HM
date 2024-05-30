try:
    n1 = int(input("Enter the first number: "))
except:
    print("An error ocurred :(")
else:
    print("No error ocurred")
finally:
    print("Always runs")
