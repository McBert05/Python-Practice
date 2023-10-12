# sets are collections with no duplicates
# say we have a list with a bunch of duplicates like so
numbers = [1, 2, 2, 3, 1, 3, 4]
# we can call the 'set' function to remove the duplicates like so:
uniques = set(numbers)
print(uniques)
# sets are defined with curly braces liek so:
second = {1, 4}

# we can add new items to a set by using the 'add' method
second.add(5)
print(second)
# we can remove items from the set by using the 'remove' method
second.remove(5)
# we can also use the 'len' function to get the length of the set
print(len(second))

first = {1, 2, 3, 4}
second = {3, 4, 5, 6}

# we can obtain a union of sets by using the vertical bar notation '|'
# union: unique items in both first and second sets
new_set = first | second
print(new_set)

# we can obtain a intersection of sets by using the ampersand notation '&'
# intersection: only items present in both first and second sets
new_set = first & second
print(new_set)

# we can obtain a difference of sets by using the minus/hyphen notation '-'
# difference: items that are only present in one set but not present in the other set
# main set - check set, will return depending on main set
new_set = first - second
print(new_set)

# we can obtain a symmetric difference of sets by using the carot notation '^'
# symmetric difference: items that are present in either set but not both
new_set = first ^ second
print(new_set)

# sets are unordered collections so we can not obtain an item by indexing
# new_set[0] will generate an error

# rather we can use 'if' statements to check if something is present in a set
if 1 in first:
    print("yes")



