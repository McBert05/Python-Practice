# we use a map function to map or copy a list to another list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# say we were only interested in the price of every item in each tuple from out list above
# we could copy the price of each item in each tuple into a new list like so:
prices = []
for item in items:
    prices.append(item[1])

print(prices)

# although the above method is nice and works, there is a function we use to better implement this
# this is called the 'map' function


# we can specify lambda in our python method like so
# lambda parameters:expression

# we can use loops to map or copy a list into another list but we can also use the direct 'map' function
# the 'map' function takes two paramters, a function and one or more iterables. 


# the map function is iterable so we must cast it into a list function so it can be consrtucted as a list
# function  (lambda function)      iterable (items list)
prices = list(map(lambda item: item[1], items))
print(prices)

# the map function handles values and conditional expressions and gives you that certain value in the form of a list
# example: item[1] would give us 10, 9, and 12