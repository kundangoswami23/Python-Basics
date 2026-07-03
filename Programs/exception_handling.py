try:
    a = int(input("Enter Number : "))
    b = int(input("Enter Number : "))

    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Input")
