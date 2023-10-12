# to handle an exception we can use the 'try' clause for the code we want to try
# and an 'except' clause following the code we want to try to handle the kind of exception that may occur
# try:
#     code_to_test
# except error_type:
#     error_handler_message

# there is also an optional 'else' clause to handle the case where no exptions were thrown in the try block
# try:
#     code_to_test
# except error_type:
#     error_handler_message
# else:
#     successful_handler_message


try:
    age = int(input("Age: "))
except ValueError:
    print("You did not enter a valid age.")

# if the program runs fine the except portion of the code will be ignored
# if an exception occurs the program will display the error message and the program will carry onward without terminating

# we can optionally define a variable that will include the details about the error message
# try:
#     code_to_test
# except error_type as error_details:
#     error_handler_message

try:
    age = int(input("Age: "))
except ValueError as error_details:
    print("You did not enter a valid age.")
    print(error_details)
    print(type(error_details))
