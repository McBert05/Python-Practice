# for programs that involve complex mathematical operations, we should use the math module
# modules are seperate files with python code
# we import the math module like below
import math 

print(math.ceil(2.2))
# there are three types of numbers in python being integers, floats, and complex numbers
a_integer = 1
a_float = 1.1
a_complex = 1 + 2j

# python includes addition, subtraction, multiplication, division, modulus and exponentiation
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # gives you the whole number of the division only, leaves out remainder
print(10 % 3) # gives you the remainder from divison
print(10 ** 3) # exponent left ^ right (10 ^ 3)

# augmeneted assignment operator
x = 10
# say we wanted to increment 3 times
# we could do this
x = x + 3
# or we use an augmented assignment operator to make it shorter
x += 3
# this can be done with all mathemactical expressionss
x -= 3
x *= 3
x /= 3
x //= 3
x %= 3
x **= 3

# working with numbers
# we can round a number by using the 'round' function 
print(round(2.5))
# we can get the absolute value of a number by using the 'abs' function 
print(abs(-2))

# type conversion
# to get input from the user we can use the input function put a text as a prompt within the parameter for the input
# input always returns a string value so when we try to use it with other numbers we get an error
x = input("x: ")
# y = x + 1

# to avoid this error we can simply use type converters
# we can use these functions for type conversions: 
# 'int': for converting values into an integer
# 'float': for converting values into floating-point
# 'bool': for convertinfg values into boolean
# 'str': for converting values into string
# examples:
# int(x)
# float(x)
# bool(x)
# str(x)

# to view the type of the value you are dealing with you can call the 'type' function
print(type(x))

# lets covert x into an integer and then retry the code
y = int(x) + 1
print(f"x: {x}, y: {y}")

# falsy values in python:
# "" - empty strings
# 0 - number zero
# None - object none