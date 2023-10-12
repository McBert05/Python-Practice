# this function is supposed to take an input do something depending on the kind of input it is
# if the input is divisible by 3, it will return the string fizz
def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Fizz"
    elif (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    return input


print(fizz_buzz(7))