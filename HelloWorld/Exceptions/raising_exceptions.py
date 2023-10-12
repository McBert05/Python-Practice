# in python we can raise or throw exceptions in our own code

def calculate_xfactor(age):
    # here the parameter age cannot be zero since it is being used as a divisor
    # so first we can check with an 'if' statement
    # and then we use the 'raise' statement and then specify the type of our exception
    # we can see built in exceptions in python by looking for python3 built in exceptions
    # once we specify the kind of error we can call it like a method and use parenthases
    # within the parenthases we can specify our message
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


# when we run the method like so we will infact encounter a termination of our program due the the error
# but our message from our 'raise' statement will be output to the console
# calculate_xfactor(-1)


# to fix this issue we can surround oour code with a 'try' block and 'except' a 'ValueError' as a variable
# this variable will hold the message we specified in the 'raise' statement
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


# this is not an advisable way of handling exceptions because raising exceptions is costly
