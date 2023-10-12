# for loops are used to iterate over iterable objects
# while loops are used to repeat something as long as a certain condition is true
# syntax for while loop:
# while condition:
number = 100
while number > 0:
    print(number)
    number //= 2


# another example of a while loop
# command = ""
# while command != "quit":
#     command = input(">")
#     print("ECHO", command)
print()
# in the case where the user does not type in the desired case 
# we can manually correct that and change the users input into lowercase
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# even number exercise
# display even numbers between 1-10
count = 0
for numbers in range(1, 10):
    if numbers % 2 == 0:
        count += 1
        print(numbers)
print(f"We have {count} even numbers")