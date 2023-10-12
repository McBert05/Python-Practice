try:
    # let us try an open a file, so we call the open function, which returns a file object
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # once we have finished opening our file, we can call the close method to close the file
    # the problem with this code is that if either line 8 or line 9 throws an exception the
    # program will not execute/reach the line of code that closes that file
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")
finally:
    # instead we can use a finally clause that will execute regardless if or not an exception is thrown in the program
    file.close()

# we can use a 'with' statement to do something similar to the finally clause but the with statement only works in certain situations
# whenever we open a file using the with statement, python will automatically call file.close() whether we have a 'finally' clause or not
# the with statement is used to automatically release external resources
try:
    # so we call the open function, which returns a file object
    # we will attach a 'with' statement to this line, and we get access to the return value of the open function by using the 'as' statement
    # we terminate the line of code with a colon in which we can work with the file object such as read annd write to it
    # with open(file_name) as file_object_name:
    # if we want to work with multiple external resource the syntax would be as so:
    # with open(file_name) as file_object_name, open(file_name) as another_file_object_name:
    with open("app.py") as file:
        print("File opened.")
        # the file object has the methods that begin with two underscores, these methods are enter and exit
        # when an object has these two methods we say that object supports "content management protocol"
        # python will automatically call the exit method that is attached to the file object so it can be used in conjuction with the with statment
        # this is the reason why we dont need a finally clause when we are working with  objects that support "content management protocol"
        file.__enter__
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did not enter a valid age.")
finally:
    # instead we can use a finally clause that will execute regardless if or not an exception is thrown in the program
    file.close()
