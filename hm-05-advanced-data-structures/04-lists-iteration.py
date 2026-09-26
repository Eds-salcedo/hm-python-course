"""
LET'S LEARN HOW TO ITERATE LISTS!
"""

# Let's create a list as an example. Remember that also strings are iterables, as well as the results from the function "range". Iterations are carried out with "for".
pets = ["Tobby", "Teddy", "Bella", "Memphis the cat"]

for pet in pets:
  print(pet)
# -- Tobby
# -- Teddy
# -- Bella
# -- Memphis the cat

# What if we wanted to know the index number of any value from the list? That's not possible to obtain directly, but there's an intermediate function for it.
for pet in enumerate(pets):
  print(pet)
# -- (0, 'Tobby')
# -- (1, 'Teddy')
# -- (2, 'Bella')
# -- (3, 'Memphis the cat')

# This result retrieves a grouped type of data that includes the index number and its corresponding value (arrays with pet names). This data is called TUPLE.
# Tuples are a fixed-size (2 elements in this case) and ordered collection of elements that contain multiple data types.

# An important thing tu know is that when you use the function ENUMERATE, you'll retrieve your initial list with the whole number of values linked/grouped to their index number.
# Thus, you can iterate the each tuple (index + value) from your list, as well as iterate each type of element from the tuples. You can extract the index only or the names only.
for pet in enumerate(pets):
  print(pet[0])
# -- 0
# -- 1
# -- 2
# -- 3

# Here we selected the first element of the tuples (in python every collection starts with 0)

for pet in enumerate(pets):
  print(pet[1])
# -- Tobby
# -- Teddy
# -- Bella
# -- Memphis the cat

# Now, we can use the tools we learned recently regarding the lists unpacking. We can create variables to pre-define the names of each element from a tuple for a future use that more direct.

for index, pet_name in enumerate(pets):
  print(index, pet_name)
# -- 0 Tobby
# -- 1 Teddy
# -- 2 Bella
# -- 3 Memphis the cat



