numbers = [1, 2, 3]
# if we want to print the individual numbers of a list to the terminal we can use the unpacking operator
# to use the unpacking operator, all we have to do is prefix the the list with an asterisk when we print it
print(*numbers)

# we can create a list like so in which we unpack like so:
values = list(range(5))
print(*values)
# since the range function is an iterable, it can be unpacked and we can do this and we can unpack a list and feed it into a list function
values = [*range(5), *"Hello"]
print(*values)

# we can unpack dictionaries as well but we need to use two asterisks
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}

# if there are multiple values with the same key, the last value will be used
print(combined)
