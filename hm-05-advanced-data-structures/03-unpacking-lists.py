"""
LET'S LEARN HOW TO UNPACK/EXTRACT ELEMENTS FROM LISTS IN PYTHON
"""

# Let's start first by creating a simple list as an example
numbers = [1, 2, 3]

# An improper (and ugly) way to extract a series of values from a list would be creating a variable for each iondexed element:
first = numbers[0]
second = numbers[1]
third = numbers[2]

# A proper way to write an unpacking can be a grouped creation of variables (to be filled) for the list:
first, second, third = numbers
print(first, second, third)
# -- 1 2 3

# Then what's the case if, for example, I needed the first element of this list?
first, = numbers
print(first)
# -- Error

# The proper way would be:
first, *others = numbers
print(first)
# --1
# Keep in mind that this re-organization of the code is grouping all the other values, in order to leave just the first one to be iterated and used.

   # That's because the star is the equivalent to this:
   def n(*numbers):
     n(1, 2, 3)
   # This would create a variable (with a prior star) and then replace it with several iterable values.

# So, going back to the previous example, this is how it'd look if we also print the "others" variable:
first, *others = numbers
print(first, others)
# --1 [2, 3]
# The rest of the list has been left grouped, inside squared brackets and separated by commas.

# Moving on with more complex examples, what would happen if we have a larger list?
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
first, *others, last = numbers
print(first, last, others)
# --1 9 [2, 3, 4, 5, 6, 7, 8]

# If we make it a little larger (the extraction), this is how it'd look like:
numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
first, second *others, penultimate last = numbers
print(second, penultimate, others)
# --2 8 [3, 4, 5, 6, 7]


