"""
LET'S LEARN HOW TO USE THE "RETURN" INSTRUCTION
"""

# We've used, for example, PRINT() to show us back the results after any specific operation or general command to handle data.
# With the "return" instruction, we'll be able to obtain and re-use a specific result or general output for a future additional operation.

# For example: A regular function definition to obtain the result of a mathematical operation would be this:
def sum (a, b):
  result = a+b
  print(result)

sum (3, 2)
# 5

# However, what if we want to carry out that summation function and re-use that result into another function? Then we must:
def sum (a, b):
  result = a+b
  return result
# Nothing in the terminal.

# If we want to see a visual result of this, then we'd simply need to create a new variable to use print() on:
c = sum (3, 2)
d = sum (c, 7)
print(d)
#12
# The sequence is just carrying out the first sum function (3+2 = 5), that result "return" will internally be re-used for a new sum function (5+7) and finally be printed.
