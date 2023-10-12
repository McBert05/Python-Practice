# in python we can raise or throw exceptions in our own code
# when writing your own function prefer not to raise exceptions because they come with a cost
# from the 'timeit' module we will import a function called 'timeit'
from timeit import timeit

# imagine we want to calculate the execution time of this piece of code we define a variable and set it to a string
# this string should contain our python code

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    # instead of printing the error message let's pass the statement so it is not repeated several times when using the time it function
    # print(error)
    pass

"""
# after our code we call the 'timeit' method
# as the first argument we pass our python code
# the for are second argument we will use a keyword argument to represent the number of times we want to execute this piece of code
# this will return the execution time of how long it takes to execute the code the specified number of times
# we can simply print this to the console
print("first code=", timeit(code1, number=10000))

# lets try the same approach but instead of raising an exception lets try returning 'None'
# with this new implementation we dont need a try block or except we just check if the fucntion returns none and pass
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("second code=", timeit(code2, number=10000))
