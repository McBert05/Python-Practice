# python has built in functions such as print() and round()

# sometimes fucntions are use to break down code into smaller chunks
# the syntax for functions are as follows:
# def name_of_function():
def greet():
    print("Hi there") 
    print("Welcome aboard")
greet()


# if we want to pass inputs into our function, we use parameters
# to add parameters when defining a function in between our parenthases we list our parameters
# the syntax for functions with parameters are as follows:
# def name_of_function(parameters):
def greet_(first_name, last_name):
    print(f"Hi {first_name} {last_name}") 
    print("Welcome aboard")
# when calling a function that has parameters values/arguments must be supplied to those parameters
greet_("Bertrand", "Owusu")
greet_("John", "Smith")
# note that parameters are the input you define for you function and a argument is the actual value for a given parameter

# there are two types of functions in programming
# 1. functions that perform a task
# 2. functions that calculate and return a value
# the print function and greet function are fucntions that perform a task, they print something on th terminal
# the round function is an example of a function that calculates and returns a value

# this is how you would go about creating a function that returns something
# we used the keyword argument "return" can be used to return something
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Bertrand Owusu")
print(message)

# all functions return "None" by default unless you specifically return a value
print(greet())