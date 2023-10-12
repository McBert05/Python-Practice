# when dealing with large numbers in python we have a more efficient data type in python called 'arrays'
# arrays take less memory and perform faster than lists, the difference is only recognizable when dealing with a large list of numbers like 10,000+
# for 90% of cases we use lists but with performance problems switch to arrays
# we first import the arrays, we need to import it from the array module, 
from array import array

# now we call the array method and the first parameter it takes is a typecode, a typecode is a string that determines the type of objects in your array
# signed = The term "unsigned" in computer programming indicates a variable that can hold only positive numbers. 
# The term "signed" in computer code indicates that a variable can hold negative and positive values. 
# The property can be applied to most of the numeric data types including int, char, short and long.
# if we are dealing with signed integers we use 'i'
# for the second parameter we pass in a iterable like a list, specifically in this case a list of integers
numbers = array("i", [1, 2, 3])
# we can use methods like 'append' to append a number to the end of a list
numbers.append(4)
# we can use methods like 'insert' to insert a number at a specific index
# insert(index, value)
numbers.insert(3, 5)
# we can use methods like 'pop' and 'remove' exactly like lists
# remove(value)
numbers.remove(4)
numbers.pop()

# we can also acccess items by their index
print(numbers)
# unlike lists the objects in this array are typed
# if we try to put any other kind of object like a floation point number or string we will get an error
# numbers[0] = 1.0, will generate an error

