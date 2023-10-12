list1 = [1, 2, 3]
list2 = [10, 20, 30]

# lets say we want combine these two lists into a single list of tuples like so
# [(1, 10), (2, 20), (3, 30)]
# in this case we can not use a map function or a comprehension functions because they both only work with a single list
# we can use the built in zip function to combine them like in the example above
# the zip function takes in two iterables, and returns a zip object that is also iterable and we can either iterate over it or pass it to the list function
# we can pass in strings into zip functions as well because strings are iterable
# the values we pass into the list will all be accounted for by the taking the most common length of all the iterables passed within the zip function
# the zip function will present the very first elements in each iterable up until the common length is reached
print(list(zip("ABC", list1, list2)))