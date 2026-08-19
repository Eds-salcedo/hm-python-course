"""
PYTHON FUNDAMENTALS
"""

# Triple quotation:

# 1) Example of a regular variable
course_name = "Ultimate Python"

# 2) Example of a DocString:
course_description = """
Ultimate Python, this course contains all the
necessary tools to find a job as a Python data analyst
"""
# The DocStrings, applied the triple quotes, have a relevant functionality of documenting classes or modules like describing how a new customized function works, and also of showing multi-line long strings.
print(course_name, course_description)


# Exploring more about strings:

# Strings in python are iterable elements, where each of its characters has a unique and ascending index number according to its position from left to right, and which you can loop through.

# This will print the result of the LEN function, which counts the lenght or the number of characters of the string you assigned to your variable:
print(len(course_name))

# This will print the first index position of the selected string (iterable), which in Python start at 0, 1, 2 ... In this case it is "U".
print(course_name[0])

# How to cut or trim the string, which in this case is the name of the course and contians 2 words? Using a method called "Slicing", which allows you to limit the index postions of the string to be printed:
print(course_name[0:8])

# Start at the letter P of Python (the 9th index) and go until an undetermined index position at which the string ends: Leave the last desired index empty so the function will keep working until the last char.
print(course_name[9:])

# Testing the opposite situation:
print(course_name[:8])

# As expected, if you leave both indexes empty the result will reflect the default performance of the function, having no limits:
print(course_name[:])

# Last lesson: You can add a third argument to that method, which is called "Step" and that will help you to iterate the printing function of the characters every X index positions that you indicate with a number:
# Print from the first character until the 9th (position nº10), iterating every 2 numbers or "even" positions. Then do the same every 3 numbers but for all the string chars:
print(course_name[0:10:2])

cnl = len(course_name)
print(course_name[0:cnl:3])
# Note: It will INCLUDE the 3rd position, it will overlook the ones in the middle.
