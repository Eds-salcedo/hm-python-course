"""
INTRODUCTION TO PYTHON
"""
# What are variables:
course_name = 'Ultimate Python'
# Variables are simple elements that serve as 'shortcut names' or containers for a value, which can either be a direct value or the result of a numeric operation.
# In the IT field, when you introduce a value or operation into a variable, this element is stored in the RAM memory ready to be called, copied or even modified in the future.

# Printing variables:
print(course_name)
# When you ask Python to PRINT your variable, you must introduce the variable's name inside the parentheses, so PRINT calls the value inside the variable and shows it.

# Restrictions:
1 = 5
3computers = 10-7
# As you were able to notice, you cannot start the name of a variable with a number or name it with a single number. However, it can contain a number after an alphabetic character.

# Python is case sensitive:
nombre = "Ultimate Python"
nOmbre = "Curso de Javascript"
NoMbRe = "Código de HTML"
nombre1 = "Primer Py"
coursename = "First CSS"

print(nombre, nOmbre, NoMbRe, nombre1, course_name, coursename)
# As you could see, some programming languages might not be case-sensitive, but Python is. Be careful when naming or calling your varibales, using functions, etc.

# Operating with variables:
alumnos = 200
egresados = 150
reprobados = alumnos - egresados
# As you already might have guessed, you can make algebraic operations with these.
# This means that you can do mathematic operations such as summation, rest, multiplication, etc. by calling the name of the variables and the system will perform the mathematic calculation of the values.
# You can create new variables on top of the previous variables you are operating with, to avoid redundancy using them as 'shortcuts'.

# Booleans:
Published_edition = True
Published_edition = TRUE #This won't work
Published_edition = true #This won't work either.
# The True-False boolean values in Python must be carefully typed with a first capitalized letter and the rest in lower-cased letters.
