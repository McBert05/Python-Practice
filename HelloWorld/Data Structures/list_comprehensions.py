items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = list(map(lambda item: item[1], items))
# in python we have comprehensive expressions 
# the syntax for list comprehension is: 
# [expression for list_iterator in list]
# if we want the price of each item we can write an expression like this:
# for each item in our items list retrieve the item in each tuple at the index of 1
prices = [item[1] for item in items] # this code is the same as the code in line 7 but much simple and cleaner


filtered = list(filter(lambda item: item[1] >= 10, items))
# for each item in our items list retrieve each item (tuple) if its index of 1 is greater than or equal to 10
filtered = [item for item in items if item[1] >= 10]
print(filtered)