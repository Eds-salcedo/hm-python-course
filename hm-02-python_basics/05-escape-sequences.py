""" 
EXECUTION OF ESCAPE SEQUENCES FOR PROBLEMATIC CHARS
"""

# Some issues could arise when using certain characters or symbols that Python considers as reserved for certain functionalities.
# In the following case, if you you might need to use quotation symbols within your functions values. This will generate a problem.
# course1 = " 'Ultimate' "Python" "

# A possible solution could be using a black-slash:
course2 = "\'Ultimate\' \"Python\""
print(course2)

# file_address = "c:\Users\User\Music\Metallica\UF2.mp3"
# That will return an error, you must then use a double \ to indicate that the following one must be displayed as a char.
file_address = "c:\\Users\\User\\Music\\Metallica\\UF2.mp3"
print(file_address)

# \n is like <br/> in HTML, but it is not visible in Python
course3 = "Ultimate \nPython"
print(course3)
