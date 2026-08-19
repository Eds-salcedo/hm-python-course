"""
YOU CAN USE SPECIFIC SYMBOL CHARACTERS TO REQUEST YOUR PC 
TO COMPARE NUMBERS AND TAKE AN AUTOMATIC DECISION BASED ON IT
"""

# Logical comparators are symbols that can be used within expressions and mathematical operations to compare values, these will evaluate the result of the specified comparison and return a boolean value (True or False)
print(2 > 3)  # False
print(2 < 3)  # True

# Logical comparators can be combined with the equality symbol (=) so it forms a new whole comparator which is inclusive, unlike the regular comparators that are not.
print(2 >= 3)  # False
print(2 <= 3)  # True

# IMPORTANT: You might have noticed that, on programming, we use the equality symbol to assign a value for a variable, for example: X = 5
# In case that you need to indicate that a value or a variable MUST be exactly equal to another specified number, you have to the the double equality:
print(2 == 2)
print(2 == 3)
# Not equal: !=
print(2 != 4)

# CAREFUL: An equality comparison might have an apparent wrong answer, but remember that comparing a NUMBER against a STRING containing the same number will wvaluate as FALSE,
# because regardless of the apparent number, a NUMBER (integer) and a STRING are different datatypes and will alaways evaluate as FALSE.
print(2 == "2")
print(2 != "2")
print(2 != 2)
