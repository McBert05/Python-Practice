# we use square brackets to define a list or a sequence of objects
letters = ["a", "b", "c", "d"]
# we can also have a list that contains lists, this is called a matrix
matrix = [[0, 1], [2, 3]]

# if we want to have a list that has repeated values like this: [0, 0, 0, 0, 0]
# typing it out would be redundant, we can rather do like so:
zeros =  [0] * 5

# we can also concatenate lists by using the '+' operator
combined = zeros + letters
print(combined)

# say you wanted a list that went up to a certain number (1-20)
# as long as we put in an iterable object within the list function, like the range and string object
# you can specify it like so
numbers = list(range(1, 21))
print(numbers)

# we can also do something similar with strings
chars = list("Hello World")
print(chars)

# we can print the length of a list using the len function
print(len(chars))




# accessing items from lists

# we can use square brackets along with a specified index to access a list item
print(letters[0])
# if we repeat this notation but use a negative number, this will return the first item from the end of the list
print(letters[-1])
# we can also modify items in the list by specifying the index and assigning it a value
letters[0] = "A"
print(letters)

# we can use two indexes to slice a string or generate a substring
# the code below will return a new list with the first three items (0, 1, 2). Up to 3 but excluding 3 this will not affect the original list
print(letters[0:3])
# if we dont include a starting index python will automatically start from index of 0
print(letters[:3])
# same thing applies if we dont specify a end index, python will go up until the end of the string
print(letters[0:])
# we can also pass a step, which will return every second or every third element in a list
print(letters[::2])
# to get a better idea of how this works lets create a new list and use the step method
demo_list = list(range(20))
print(demo_list)
print(demo_list[::2])
# if we were to do the same with a negatative number the same results would apply but in negative order
print(demo_list[::-2])



# unpacking lists

first = numbers[0]
second = numbers[1]
third = numbers[2]
# the code above is valid but there is a cleaner way to achieve the above code with list unpacking
first, second, third, *other = numbers
# the code above has the same functionality as:
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# when unpacking the number of variables to the left side of the assignment operator
# should be the same as the number of items present in the list, if not the an error will generated
# we can avoid this error by packing the remaining values in a seperate list like so:
first, second, *other = numbers 
# this will generate the first and second items from the list and store the remaining list items in another list called other
print(first)
print(other)

# if we want only the first and the last item in the list we can unpack like so:
first, *other, last = numbers
print(first, last)




# looping through lists

letters = ["a", "b", "c"]
# to loop through a simple list we can do as so:
for letter in letters:
    print(letter)


# if we want the index of each item as well we can use the built in enumerate function
# in each iteration we will be given a tuple of two items (index, item)
# we can use square bracket to access the first item in this tuple
for letter in enumerate(letters):
    print(letter[0], letter[1])


# the above code could be cleaned up and made nicer using list/tuple unpacking
# we can unpack the tuple within the declaration of our for loop
# since we know each tuple holds two values we can simply call the for loop like so:
for index, letter in enumerate(letters):
    print(index, letter)


# adding/removing items from a list

# to add an element to the end of a list we use the 'append' method
# we can use the dot notation to access individual functions/methods of objects in python
letters.append("d")
print(letters)

# if we want to add an item at a specific position we use the insert method
letters.insert(0, "-")
print(letters)

# to remove items from the end of a list we use the 'pop' method
letters.pop()
print(letters)

# with the pop index we can remove an item at a given index just by specifying it like so:
letters.pop(0)
print(letters)

# in certain cases we want to remove an object but we dont know its index, in that case we use the remove method
# the remove method will only remove the first instance of the object in the list
letters.remove("b")
print(letters)

letters = ["a", "b", "c", "d", "e", "f"]
# we can also use the 'del' statement to remove an item from the list by its index like so
del letters[0]
print(letters)
# we can also delete a range of numbers using the same statement
del letters[0:3]
print(letters)

# if we want to remove everything from a list we use the 'clear' method
letters.clear()
print(letters)


# finding object within a list

letters = ["a", "b", "c", "d", "e", "f"]
# we can find the index of an item in a list byu using the 'index' method
# if the item is not present within the list then you will recieve a value error
# to bypass this we can use a 'if' statement in conjunction with the 'in' operator like so:
if "p" in letters:
    print(letters.index("p"))


# we also have the count method which allows us to count the occurences of a given item in a list
print(letters.count("d"))


# sorting lists
numbers = [3, 51, 2, 8, 6]
# in python we can use the 'sort' method to sort values in a list
# we also have keyword arguments we can use in the sort function to change the sort order
# here we use the reverse keyword and this can be set to true to sort the numbers in descending order
numbers.sort(reverse=True)
print(numbers)

# we can also use a similar method called "sorted" which takes in an iterable argument such as a list and returns a sorted version
# this method will not modify the original list as will the 'sort' method
# we can also apply the keyword argument to this method like below
print(sorted(numbers, reverse=True))

# if we are dealing with a list of complex objects
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# if we try to call the sort method on this kind of list that includes tuples, python will not understand how to sort the list
# we can define our own function/method and pass in a paremeter to recieve our list and since it has tuples within
# we can specify which index of each tuple we need (0, 1,...n) by calling parameter[1]
def sort_item(item):
    return item[1]


# we can call the sort method on this function and then pass in the method we made 'sort_item"' inside the sort method
# (note we are not calling the method but rather just refering to its name, python will get the values from the item list and pass it to the 'sort_item' method for us)
# the sort method takes no positional arguments but only key arguments so we need to specify that the sort_item method is a key argument
items.sort(key=sort_item)
print(items)

