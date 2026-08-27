"""
NOW WE'LL LEARN ALL THE DIFFERNT DATA STRUCTURES IN PYTHON, SO YOU'LL BE ABLE TO MANAGE REAL-WORLD DATA IN THEIR MOST COMMON FORMS, SUCH AS LISTS, TUPLES, DICTIONARIES, ETC.
"""

# In Python, a list is something similar to what you'd usually do when going to a supermarket; a list of items that you may use as a reference or to be combined for a recipe.
# Lists can be made of numbers (int), texts (str) or even sub-lists.

# The square brackets are used to determine the start and end of a list [...]. Elements can be separated by commas.
# For example: You may start with a similar structure of a variable's creation
numbers = [1, 2, 3]   #You can use integers
letters = ["a", "b", "c"]   #You can use strings
words = ["eduardo", "analyst"]
happywords = ["eduardo", "data", "analysis", "students"]   #You can use any number of elements
booleans = [True, False, True, True]   #You can use boolean values
matrix = [[0, 1], [5, 3]]   #You can also use matrices, which work here as a sort of lists within lists.
zeroes = [0] * 10   #You can also duplicate the values of an initial list
more_zeroes = [0, 1] * 10

print(numbers)
print(words)
print(happywords)
print(booleans)
print(matrix)
print(zeroes)
# --[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(more_zeroes)
# --[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

# You can also merge lists, to create something like a master list
alphanumeric = numbers + letters
print(alphanumeric)
# --[1, 2, 3, 'a', 'b', 'c']

# We can create a list with a rank, with a specific syntax. With no arguments, the list will be empty. The argument must be iterable:
rango = list( range(1, 11) )   #Because Python considers the first iterable as 0.
print(rango)
# --[1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

# We can try to create a list to iterate a string:
chars = list("hello world")
print(chars)
# --['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']




