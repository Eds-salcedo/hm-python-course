"""
LET'S LEARN HOW XARGS OR *ARGS WORK
"""

# Xargs are used in case that you want to enter an undetermined number of arguments into a DEF function


def suma(a, b, c):
    print(a + b + c)


suma(2, 5, 3)

# In this case, the quantity of arguments that we are entering match the same quantity of pre-defined parameters
# that we specified this def function should have.

# So, in case we try to enter a different number of arguments, we will receive an error notification:

# suma(3, 8)
# suma(9, 2, 5, 10)

# Fortunately, in Python we have an instruction intended for us to indicate to our DEF functions to consider all the arguments that we may introduce in the future aynyways, regardless of the pre-defined number of parameters:
# The variable (with any customized name) should contain a previous asterix "*", right at the beginning it.


def sumas(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


sumas(3, 7, 10)
sumas(3, 5)
sumas(32, 45, 78, 99, 101)

# Also, keep in mind that Xargs are used for opening the doors into  DEF function to multiple (intially undetermined) number of arguments that do not have a previously defined name, so you will have to enter the whole data structure, whether it is just a simple number or if it's a dictionary, tuple, list, etc.
# In this context, we have to understand that utilizing the Xargs will turn our DEF functions parameters into iterable elements.
