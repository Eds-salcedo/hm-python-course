"""
LETS CREATE A BASIC CALCULATOR TO PRACTICE THE LEARNED CONTENTS
"""

# Lets remind how input and concatenation work:
n1 = input("Ingrese primer número: ")
n2 = input("Ingrese segundo número: ")

print(n1, n2)
print(n1 + n2)
# We can see that the commas separate the variables at the moment of printing.
# When printing, using a "+" with strings will only concatenate them (put a text next to the other).

# For a summation within the printing function, you will need to indicate the conversion of data type first, which in this case was intially a string among quotation marks " " that you used to introduce a text.

n1 = int(n1)
n2 = int(n2)

print(n1 + n2)


# KEEPING IN MIND THOSE BASIC RULES OF PYTHON, LETS PROCEED


number1 = input("Introduce the first number: ")
number2 = input("Introduce the second number: ")

number1 = int(number1)
number2 = int(number2)

add = number1 + number2
subs = number1 - number2
multi = number1 * number2
div = number1 / number2

message = f""" For numbers {number1} and {number2},
the result of the addition is {add}.
the result of the substraction is {subs}.
the result of the multiplication is {multi}.
the result of the division is {div}.
"""

print(message)
