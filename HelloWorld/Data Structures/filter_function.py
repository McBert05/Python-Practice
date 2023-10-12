# we use a 'filter' function to specify another list with only certain specifications (aka filtered list)
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# say we were only interested in the products of every item whos prices was greater than or equal to 10
# we could copy the price of each item in each tuple into a new list like so:
filtered = []
for item in items:
    if item[1] >= 10:
        filtered.append(item)

print(filtered)

# although the above method is nice and works, there is a function we use to better implement this
# this is called the 'filter' function


# we can specify lambda in our python method like so
# lambda parameters:expression

# we can use loops to filter or copy a list into another list but we can also use the direct 'filter' function
# the 'filter' function takes two paramters, a function and one or more iterables. 


# the filtered function is iterable so we must cast it into a list function so it can be consrtucted as a list
# function  (lambda function)         iterable (items list)
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# the filter function takes in a boolean condition and returns each tuple from the list that is true according the the boolean expression