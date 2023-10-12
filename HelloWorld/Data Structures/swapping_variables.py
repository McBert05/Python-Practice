from re import X


x = 10
y = 11
# to swap two variables we need a third variable
# z is set to x as a placeholder for the swapping
z = x
# since x is already stored in z we can change its value to y first before we adjust the value of y
x = y
# now that we have store y into x, we can now change the value of y to z which holds the previous value of x before it was swapped to y
y = z

print(x, y)

# in python we can use one line of code to swap like so:
x, y = y, x # here we are basically unpacking a tuple
# the syntax above is as so:
# x, y = (y, x)
