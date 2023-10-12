# in the case where we want to create a function with a variable amount of arguments
# we use a special declaration in our arguments
# we use the asterisk and a parameter that is plural to signify that a we will 
# be using several arguments in our function this is known as *args
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# another variation of *args is **args
def save_user(**user):
    # use the bracket notation to get the value of various keys within the dictionary
    print(user["id"])

# with **args we can pass keyword arguments
save_user(id=1, name="John", age=22)
# this will in turn get you a dictionary