# tuples are read only lists, we can use it contain a sequence of objects but these objects cannot be modified
# when defining tuples we use parentheses instead of square brackets
# we can also exclude the parentheses and python will see this as a tuple
# if we want to define a tuple with only one item we should add a trailing comma to let python know it is a tuple
point = (1, 2)
point = 1, 2
point = 1,

# similar to lists we can also concatenate tuples
point = (1, 2) + (3, 4)
print(point)

# we can also manipulate tuples to have them repeat by muliplying them with a certain number
point = (1, 2) * 3
print(point)

# we can also convert a list to a tuple by calling the 'tuple' function, any iterable such as a string can be passes into the 'tuple' function
point = tuple([1, 2]) * 3
print(point)

# we can obtain tuple elements via indexing like we do with lists
print(point[0:4])

# we can also unpack tuples like so:
x, y, z, *other = point
print(x, y, z)

# similar to lists we can use the 'in' operator to check for the existence of an element
if 10 in point:
    print("exists")


# once again tuples can not be modified
