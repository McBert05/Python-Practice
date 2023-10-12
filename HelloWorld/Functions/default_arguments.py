#  if we want to specify a default value within our functuion parameter we can do as so
# def function_name(parameter=default_value)
# default parameters are optional parameters and must come after all required parameters
def increment(number, by=1):
    return number + by


print(increment(2, 1))