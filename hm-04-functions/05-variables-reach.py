"""
LET'S LEARN HOW VARIABLES DEFINITION WORKS AND ITS REACH WITHIN A WHOLE CODE
"""

# To understand this, let's create two different functions containing internal variables that are named identically in each one:

def salute():
  salutation = "Hello world"

def saluteEduardo():
  salutation = "Hello Eduardo"

# Now let's try printing that "salutation" variable to see wich value does the system picks
print(salutation)
# NameError: name 'salutation' is not defined. Did you mean: 'salutation'?

# As you can see, the system is not picking any of the variables that you created within each function due to the variables reach depending on their place of creation.
# This place/space of creation, in Python, is defined by the INDENTATION. Thus, the print() function is within a Global Context, so it doesn't match the salutations.

# Example with global variables - Let's see how they work, but it's not a good practice for variables intended to be modified afterwards.

salutation = "Hello global"

def salute():
  salutation = "Hello world"

def saluteEduardo():
  salutation = "Hello Eduardo"

print(salutation)
# --Hello global

# As you can see, the print() function was indented in a global position, and that variable wasn't modified because dispite having multiple identical variables in the code,
# the other salutation variables are defined located within the functions. Those are not callig the global variable, those are creating new variables regardless of the name.

# The correct use for global variables are for addresses or tags, fixed, that we won't modify in the rest of the code.
salutation = "Hello global"

def salute():
  global salutation
  salutation = "Hello world"

print(salutation)
salute()
print(salutation)
# --Hello global
# --Hello world

- - - - 
# Example with operation
salutation = 25

def salute():
  global salutation
  saluation = "Hello world"

result1 = salutation + 3
print(result1)

salute()

result2 = salutation + 3
print(result2)
# --Error salutation + 3 --Can only concatenate str (not "int") to str
# The reason for it is that, despite having your first line defining your global variable as an int on line 51, you used that global variable to change it inside a function
# That salute function on line 53 to 55 changed the global variable for internal purposes and changed its value from 25 to "Hello world", int to str, permanently.





