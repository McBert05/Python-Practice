# dictionaries are a collection of key value pairs
# it is similar to a phone book where you have a persons name mapped to their contact details
# name would be the key, and contact info would be the value

# immutable types are often used as keys
point = {"x": 1, "y": 2}
# we also have the 'dict' function in which we can use to redefine dictionaries
# whenever we pass in arguments to our dict function we pass them in as keyword arguments
point = dict(x=1, y=2)
# now that we have a dictionary we can get the value associated with the key using an index
# here our index would be simply the name of the key rather than a position
print(point["x"])
# we can assign a key a new value like so:
point["x"] = 10
# we can add a new key and value like so:
point["z"] = 20
# we can check for the existence of a key like so:
if "a" in point:
    print(point["a"])

# or we can use the get method like so:
# the get method will return "None", but we can specify what it returns by the putting a value as the second parameter
print(point.get("a", 0))
# to delete an item we use the 'del' statement
del point["x"]
print(point)

# we can loop over dictionaries like so:
for key in point:
    print(key, point[key])

# we can also do this to loop over dictionaries by using the items method
# this will give us a tuple in which we can unpack within the for loop
for key, value in point.items():
    print(key, value)


# dictionary comprehensions


values = []
for x in range(5):
    values.append(x * 2)


# when ever we want to map or copy something into a list we use list comprehensions, this is much simpler than the code above
# the code below has the same functionality as the for loop above
values = [x * 2 for x in range(5)]

# we also have dictionary comprehension in which we use curly braces instead of square brackets, this code here would generate a set, because there is no key value pairs
values = {x * 2 for x in range(5)}
# to specify key value pairs in the comprehension we can use the colon (since it is a dictionary {}) in our expression part of our dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)
