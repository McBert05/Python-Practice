def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        # return statement is purposefully indented to create a bug in the program
        # we use a technique called debugging to find and fix this bug
        # if we place the return statement on this line and press F10 it will take us out of our loop and this means there is a bug
        # return total
    # if we put the return statement here F10 will not automatically force us out of the loop
    return total
        

# (Windows demonstration)
# we can insert a breakpoint by putting the cursor on line 9 and pressing F9
# after doing so we can press F5 to run the application up to this point
# we can execute the program line by line by using the F10
# to jump into the multiply function we press F11
print("Start")
print(multiply(1, 2 ,3))

# note that we could have but the breakpoint in the function to simplify things