# to write code based on a certain condition we can use if statements
temp = 35
# when using an if statement terminate your if statement condition with a colon
if temp > 30:
    # indented code belongs to the if statement
    print("It's warm")
    print("Drink water")
# if we want multiple considitons we can use the elif statement which stands for else if
elif temp > 20:
    print("It's nice")
# if none of the previous conditions happens to be true, the else block will execute
else:
    print("It's cold")

print("done")

# ternary operator
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# we can re-write the code above to test not eligible
# this is called a ternary operator
message = "Eligible" if age <= 18 else "Not eligible"
print(message)