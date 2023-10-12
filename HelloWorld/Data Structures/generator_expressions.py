from sys import getsizeof
# generator objects are iterable just like lists, and each generation they spit out a new value
# for instances in which we have a large data set or an infinite stream of data we use generators
# to implement a generator object we can use the list comprehension in the form of a tuple with parentheses
values = (x * 2 for x in range(100000))
# when we print the values tuple it will show up as a generator object
print(values)

# what it is interesting about generator objects is their size
# to see the size of an object we can import the 'getsizeof' function from the 'sys' module
print("gen", getsizeof(values))

# we can change values into a list to see the memory size difference
values = [x * 2 for x in range(100000)]
print("list", getsizeof(values))

# because the generator function does not store all the items in memory, we wont be able to get the total number of items we are working with
# so functions like 'len' will not work on generator objects