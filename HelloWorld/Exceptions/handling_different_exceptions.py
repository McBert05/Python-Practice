# say there is more than one error we need to be ready for in this case there are two
# 1. ValueError
# 2. ZeroDivisionError
# we can simply add another except clause and specify the ZeroDivisionError
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You did not enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")

# if we want a similar message for different errors we can use parenthases to handle multiple errors
# we only have to seperate the different errors by commas
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")
