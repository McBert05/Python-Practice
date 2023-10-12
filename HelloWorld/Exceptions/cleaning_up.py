# there are times where we need to work with external resources, like files network connections
# databases and so on, whenever we use these resources after we are done, we need to release them
# for example when we open a file we should always close it after we are done otherwise another process or
# another program may not be able to open that file
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
