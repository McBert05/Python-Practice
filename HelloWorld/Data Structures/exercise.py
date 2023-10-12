from pprint import pprint
# find the most repeated character within a text
sentence = "This is a common interview question"
# first we need to know how many times each character is repeated
# a dictionary is best for storing information like this
char_frequency = {}
# we need to get each character and update its frequency in the dictionary
# for every character in the sentence
for char in sentence:
    # if that character is already within then the char_frequency dictionary increment it by 1
    if char in char_frequency:
        char_frequency[char] += 1
    # if the character is not already in the char_frequency dictionary set the key and intialize its value to 1
    else:
        char_frequency[char] = 1

# the format of this dictionary will look very hard to read so we can use the pretty print module to help us with this
# when we import the file we use the 'pprint' method instead of the default print statement
pprint(char_frequency, width=1)

# we can use the sorted mthod to sort the dictionary
# we would have to use the 'items' method returns all the key value pais in the form of tuples
# since this 'sorted' function does not know how to solve tuples
# so to fix tis we can pass a second argument, key and set it to a lambda (an annonymous function) and this function takes a key value pair and returns a value
# after that we can reverse the sorting by passing a keyword argument 'reverse' and setting it to true
# then we can store this sorted list into a new list
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
# the first item in this list would be the solution to our problem
print(char_frequency_sorted[0])
