# in python there are logical operators to model more complex conditions
# Logical operators:
# and: will pass if both arguments are true (True and True) = True
# or: will pass if at least one argument is true (True or False) = True
# not: will inverse the boolean (not True) = False, (not False) = True
high_income = True
good_credit = True
student = True

# there is no need for you to compare boolean values in if statements like for example:
# if high_income == true
# the statement above is redundant
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")

# you can split conditions into seperate pieces like so 
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# quiz
# what will be printed within these lines of code
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
# c will be printed