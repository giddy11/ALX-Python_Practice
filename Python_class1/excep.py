try:
    age = int(input("Age: "))
    res = 20 / age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("cannot divide by zero")