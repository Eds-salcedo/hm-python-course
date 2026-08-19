"""
WE WILL DIVE DEEPER INTO NUMBERS AND ITS APPLICABLE FUNCTIONS
"""
import math
# A basic function applicable to numbers, easy to understand is round():

print(round(1.3))
print(round(1.7))
print(round(1.5))

# You can also extract the absolute mathematical value of a number regardless of its sign
print(abs(-77))
print(abs(55))


# UNFORTUNATELY, PYTHON DOES NOT HAVE TOO MANY NATIVE FUNCTIONS FOR HANDLING NUMBERS
# HOWEVER, IT HAS SUPER POWERFULL TOOLS CALLED "LIBRARIES" AND "MODULES". A MODULE IS A SIMPLE .PY FILE THAT CONTAINS A SET OF DEFINITIONS OF FUNCTIONS, CLASSES AND VARIABLES.
# A LIBRARY IS A PACK OF RELATED MODULES DESTINED TO PERFORM A PARTICULAR KIND OF OPERATIONS.

# The module "MATH" is one of those. You can import the MATH module from the web and use its functions:
print(math.ceil(1.1))
print(math.floor(1.999999))
print(math.isnan(23))

# The following will not work, since the .isnan() function only works with objectypes int or float (numbers), and quoted numbers are considered as strings by Py.
# print(math.isnan("23"))

# Power or "Potencia" in Spanish, only requires a comma as a separator of the elements (base and exponent), instead of " ^ ":
print(math.pow(10, 3))
print(math.sqrt(9))
