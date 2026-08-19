"""
LETS SEE THE MOST COMMON TOOLS TO CONVERT THE TYPES OF DATA VALUES
"""

# int()  ---> converts to integer (numbers)
# str()  ---> converts to string (text or numbers stored as text)
# float()---> converts to float
# bool() ---> converts to boolean

# In the case of Boolean types, you have to keep in mind that this type conversion will evaluate the initial data and turn it into True or False.
# In those cases, boolans consider "Falsy" and "Truthy" values
Falsy = "", 0, None

print(bool(""))
print(bool(None))
print(bool(0))

# This zero has quotation marks, so it is considered as a string and not a number.
print(bool("0"))
# This one is not an empty string but single space character inside a string.
print(bool(" "))
