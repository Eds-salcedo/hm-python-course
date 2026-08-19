"""
LETS KNOW MORE ABOUT NUMBER FORMATS AND HOW TO WORK WITH THEM
"""

# There are different types of numbers depending on their format:

# Integers (enteros, in Spanish):
number = 2
print(number)
# Float (decimales, in Spanish, and these are separated by dots instead of commas like you would in Spanish):
decimal = 1.2
# Imaginary numbers, for example, "2i" which is:  2i = 2*square root of -1. In Python, it must be written as 2j as it uses "j" instead of "i" for imaginary numbers:
imaginary = 2 + 2j

print(1 + 3)
print(1 - 3)
print(1 * 3)
print(1 / 3)
# Using a single slash "/" will perform the desired division, however, the result will include a float number if that is the case.
# To indicate Python that you need an exact or "integer" number as a result, you will need to use two slashes "//"
print(1 // 3)
# Using the percentage symbol between two numbers will return the remainder
print(1 % 3)
print(2**3)

# Cumulative Assignments:
# In Pyhton, like in general programming, you can define the INITIAL value of a variable (X = 2), 
# and later, you can use that same variable (X) to re-assign a new value for it, still considering the original (X=2  --->  X = X + 1  --->  X = 2 + 1  --->  X = 3).

number = number - 1
number = number + 2
print(number)

# In Python, Cumulative Assignments have an alternative and shorter notation, 
# by putting the desired operation symbol before the equal sign and omitting the re-calling of the variable:

number += 7
number *= 5
number -=10
