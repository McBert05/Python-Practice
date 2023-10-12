# a lambda function is a one line anonymous functions that we can pass to other functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

#  the code above could be greatly improved using lambda functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# we can omit this function since we are using lambda
# def sort_item(item):
#     return item[1]


# we can specify lambda in our python method like so
# lambda parameters:expression
items.sort(key=lambda item:item[1])
print(items)