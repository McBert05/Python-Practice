# loops are used to create repetition
# syntax for for loops:
# for number in iterable:
# number is the controlled variable, this is a variable of type integer
# range is a built in function to specify how long the loop should run
for number in range(3):
    print("Attempt:", number + 1, (number + 1) * ".")


# we can further specify our range to have it start and end in a specfic range
# the range argument below will generate a loop that runs 1-(4-1) or 1-3
for number in range(1, 4):
    print("Attempt:", number, number  * ".")

  
# for else 
# the "else" statement in for else statements will only be executed if the loops runs without an early termination
successful = False
for number in range(3):
    print("Attempt:")
    if successful:
        print("Successful")
        break # break statements are used to jump out of loops
else:
    print("Attempted 3 times and failed")


# nested loops
# outer loop is set to run and inner loops terminates before outer loop finishes
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")