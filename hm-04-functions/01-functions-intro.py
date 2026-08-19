"""
LET'S REWIND WHAT FUNCTIONS DO WE KNOW SO FAR AND LEARN WHAT WE CAN DO
"""

# We've used, for example, PRINT() which will perform a specific action with the value that we enter.
print("Hola Mundo")
print("DONE")

# 1) We can create our own functions with def: def FunctionName(ValueToBeIntroduced): WhatWeWantToDo


def hola():
    print("Hola Mundo!")
    print("Ultimate Python")
    print("Welcome Eduardo")


hola()

# 2) Functions with a parameter:


def hello(name):  # Here we introduced a value within the parentheses.
    print("Hello World!")
    print(f"Welcome {name}")


# Adding that previous value within the parentheses turned the function into an OBLIGATORY-variable function, so the function will always have to be called along with a variable. If not, then the call of the function won't work.
# hello() -- Error

hello("eduardo")
hello("Xyzzz")

# Important: The value that we put within the def value parentheses is called PARAMETER.
# When you call the function and introduce a custom value within a def function parentheses, it becomes an ARGUMENT.

# 3) Several parameters:
# When you create a function, you can configue it so it mandatorily receives a certain number of desired arguments.


def bonjour(nom, age):
    print(f"Ton nom est {nom} et ton âge est {age}")


def Hi(name, last_name, city):
    print(name, last_name, city)

# bonjour("eduardo") -- Error


bonjour("eduardo", 29)

# 4) Optional parameters: In case that there is a parameter that you do not require to be filled mandatorily by all users, you can auto-fill it with a default value in case it remains empty


def olá(nome, edade, cidade="nenhuma"):
    print(f"O seu nome é {nome}, a sua edade é {
          edade} e sua cidade é {cidade}")


# If you add the CIDADE value, the function will take it. Otherwise, instead of generating an error, it will return the default value that you introduced in your function.
olá("Eduardo", 29, "Madrid")
olá("Jose", 30)

# 5) Called arguments: In case that we need to provide certain data required by the code, but we don't know the specific order in how we should enter it, we can enter the data specifying the corresponding name of the field we are providing the data for.
# In this case, if we do it for one, we must do it for all, so we'll have to specify the exact parameter name for which we are introducing the argument.
# Otherwise, if you name just 1 parameter with its corresponding argument, but you leave the other arguments without its structure, Pyhon will consider it as an error.

# Hi(last_name="Salcedo", eduardo) - - Error

Hi(last_name="Salcedo", city="Madrid", name="Eduardo")
