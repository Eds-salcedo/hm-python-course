"""
LET'S LEARN HOW TO ITERATE THE ELEMENTS FROM LISTS TO SEARCH AND FIND A REFERENCE VALUE
"""

# Let't take again our previous list
pets = ["Tobby", "Teddy", "Bella", "Memphis the cat"]

# As a first example, we can search the index number of an element inside a list (as long as the element exists)
pets.index("Teddy")
print(pets.index("Teddy"))
# -- 1

# What happens if we search for a value that doesn't exist in our list? In other programming languages we would get a "-1" result, as inexistent.
print(pets.index("Wolfgang"))
# -- ValueError: 'Wolfgang' is not in list

# An important function is the couinting of repeated elements inside a list:
pets_2 = ["Tobby", "Teddy", "Bella", "Teddy", "Memphis the cat"]
  print(pets.index("Teddy"))
# --1
# The result would be the index number of your value's first appearance. Thus:
print(pets.count("Teddy")
# -- 2

# If you just want to know whether a value exists in a list, you can also use an interation with a new variable and Python will automatically come back with a boolean (TRUE / FALSE)
result = "Bella" in pets_2

print(result)
# -- TRUE
