"""
LET'S LEARN HOW TO ORGANIZE AND RE-ORGANIZE LISTS
"""

# Let's create an initial example list.
numbers = [2, 4, 1, 45, 75, 22]

numbers.sort()
print(numbers)
# -- [1, 2, 4, 22, 45, 75]

# If you want to order the list in a descendent (reverse) sequence
numbers.sort(reverse=True)
# -- [75, 45, 22, 4, 2, 1]

# In case that you want to create a NEW list (not to affect the original one), you can use the following function and create an ordered copy.
numbers_2 = sorted(numbers)
print(numbers)
print(numbers_2)
# -- [2, 4, 1, 45, 75, 22]
# -- [1, 2, 4, 22, 45, 75]

# You can also use the "reverse" keyword with sorted()
numbers_3 = sorted(numbers, reverse=True)

# Now we can try to order a more complex list. For example the following list that contains sub-lists, with ID and name.
users = [
  [4, "Chanchito"], 
  [1, "Felipe"], 
  [5, "Pulga"]
]
users.sort()
print(users)
# -- [1, "Felipe"], [4, "Chanchito"], [5, "Pulga"]
# The method ordered the elements of the list by its index

# What happens if we create the sublists with: names, IDs
users_2 = [
  ["Chanchito", 4], 
  ["Felipe", 1], 
  ["Pulga", 5]
]
print(users_2)
# --   ["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]
# Here you can see that the elements of the list weren't ordered this time, because the method only works when the FIRST ELEMENT of the lists are orderable.

# However, there is a way to specify how the ordering must work, creating a customized function
def ordering(element):
  return element[1]
# Here we created a custom def function that takes a given variable and returns its second element (0, 1, etc..), as we already know that we're working with a sublist from which we need its second element.

# We can then insert this function that will return the specified element, but first indicating the name of the parameter (key=...)
users_2.sort(key=ordering)
print(users_2)
# -- [["Felipe", 1], ["Chanchito", 4], ["Pulga", 5]]

# Also, if we want to order our list in a descending/reverse way, we can also use the "reverse" keyword.
users_2.sort(key=ordering, reverse=True)

