# when writing programs our programs may encounter an error and terminate
# some things that can cause errors are:
# programming mistakes
# bad data we get from users
# resources not being avaliable
# it is important to control what can happen in situations when an error arises in our program so our program does not terminate
numbers = [1, 2]
# above we have defined a list with only two items
# when we try to access a third item that does not exist we will get an error, specifically an exception


# another example of an error is an input error, say we ask for the users age, if the user enters a non numeric value our program crashes
age = int(input("Age: "))
