# text is always surrounded by quotes
# this primitive variable type is referred to as string
import string


string_var = "Python Programming"

# if we wanted to specifically format strong a certain way to make it appear a certain way
# we can use triple qoutes as shown below
message = """
Hi John,

This is Bertrand, following Mosh's python course

Blah Blah Blah
"""

# in python, there are functions that exist
# functions are basically reusable pieces of code that carries out a task

# we can use the 'len' fucntion to find the number of characters within a string and print it to the console
# one way to use a fucntion is to call the function by name and use parenthases to place data into the fucntion for it to work with
print(len(string_var))

# if we want to get a specific character from a string we call the name of the string and use square brackets to identify which index of the character we want
print(string_var[0])
# we can also a use a negative index, a negative index of 1 (-1) would return the last character in the string
print(string_var[-1])
# if we want to extract certain values of a string to obtain a substring we can use square brackets and a colon
# the code below extracts the first three characters from our string. The meaning of the syntax is like so: "start index : end index - 1"
# the code below extracts indexes 0-2 (0, 1, 2)
print(string_var[0:3])

# [start index: no specified value] will get you the entire string from that start index
print(string_var[0:])

# [no specified value: end index] will get you the entire string up until the end index -1
print(string_var[0:])


# escape sequences
# backslash '\' in python strings is an escape character
# escape characters are used to escape the character after, allowing it to not interfere with the syntax but appear when printed
string_var = "Double \"Qoutes\""
print(string_var)

# types of escape sequences:
# \" generates: "
# \' generates: '
# \\ generates: \
# \n generates: new line


# formatted strings
first = "Bertrand"
last = "Owusu"
# we can utilize the '+' sign to concatenate or join different strings together
full = first + " " + last
print(full)

# there is a better way of doing the above code using formatted strings
# we can set the variable 'full' to a string prefixed with an 'f' or 'F'
# within the string we can put in as many curly braces for our variables as we need
full = f"{first} {last}"
print(full)

# we could also put a function within this curly brace
full = f"{len(first)} {last}"
print(full)
# expressions can also be put into the culry braces


# string methods
# in python there general purpose functions and specific fucntions
# there are a few functions specific to strings
# you can use the '.' operator to see what fucntions that are specific to the object we are working with
# everything in python is an object and objects have functions called methods we can access using the dot '.' notation


# we can use the 'upper' function that converts the original string into a new string that is all upper case
# this will not effect the original string
print(string_var.upper())
print(string_var)

# we can use the 'lower' function that converts the original string into a new string that is all lower case
print(string_var.lower())

# we can use the 'title' function that converts the original string into a new string that is camel cased
print(string_var.title())

# we can use the 'strip' function that converts the original string into a new string that has the whitespaces trimmed at the beggining and end of a string
string_var = "  fun fun fun   "
print(string_var)

print(string_var.strip())
# there are also two different versions of this function 'lstrip' for left strip, and 'rstrip' right strip

# if we want the index of a character from a string we can use the 'find' function
# the 'find' fucntions takes in parameters, so we can pass in a character or a series of characters that we want to find
# the 'find' function by default is case sensitive so you must type in exactly what you want to find
# the 'find function will return -1 if the string being searched for was not found
print(string_var.find("u"))
print(string_var.find("fun"))

# the 'replace' method allows you to replace certain characters or a sequence of characters within a string
# the syntax for this is string_name.replace("character_sequence_to_replace", "replacement_sequence")
print(string_var.replace("fun", "ohyeahyeah"))
print(string_var)

# if we want to check to see if a certain sequence is within a string, we use the 'in' expression that produces true or false
print("u" in string_var)
# we can apply the same rule to see if a certain sequence is not within our course using the 'not in' expression
print("oh" not in string_var)
