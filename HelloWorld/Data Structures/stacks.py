# stacks resemble a stack of items such as books stacked upon each other in the real world
# the last book placed on top of the stack is the first book you can remove
# this behavior is referred to as Last In First Out (LIFO)
# browsing info is stored in a stack format

# we can use a list object as a stack in python
# we can declare a list to store browsing info and set it to an empty list
browsing_session = []
# we can then call 'append' method when the users navigates to the first website
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

# when the user presses the back button we should remove the last item in the list
# we can do this by calling the 'pop' method which will remove the last item from the stack and return it
last = browsing_session.pop()
print(last)
print(browsing_session)
# we can also do something similar by using the '-1' to get the very last element/website within the list
# we can add a redirect message to this function to make it clear that the user is being redirected to another page
print("redirect", browsing_session[-1])

# we need to first check if the stack is empty before we even enable the back button
# in python 0, "", and [] are also falsy values, 0, an empty string, and an empty list
# if we apply the not operator to an empty string we get the boolean value "True"
# not [] = true
# we can write an 'if' statement like so to check if a list is empty
if not browsing_session:
    print("disable")

