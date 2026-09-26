"""
1) LET'S LEARN HOW TO ADD ELEMENTS INTO LISTS!
"""

# Let't use an example list again
pets = [
  "Wolfgang", 
  "Pelusa", 
  "Pulga", 
  "Felipe", 
  "Pulga", 
  "Chanchito feliz"]

# In general, if we want to add an element in the middle of the list, we have to type the folling code, specifying the index number where we want to add it and then the value itself.
# Let's suppose that you want to add the pet name Melvin at the 2nd position of your list:
pets.insert(1, "Melvin")
print(pets)
# -- ['Wolfgang', 'Melvin', 'Pelusa', 'Pulga', 'Felipe', 'Pulga', 'Chanchito feliz']

# If you want to add the element at the end of your list, you could use a "-1" as index number, but there's another way to do it.
pets.append("Chanchito triste")
print(pets)
# -- ['Wolfgang', 'Melvin', 'Pelusa', 'Pulga', 'Felipe', 'Pulga', 'Chanchito feliz', 'Chanchito triste']

"""
2) LET'S LEARN HOW TO REMOVE ELEMENTS FROM LISTS!
"""

# Here you don't type the index but the actual VALUE:
pets.remove("Pulga")
print(pets)
# -- ['Wolfgang', 'Melvin', 'Pelusa', 'Felipe', 'Pulga', 'Chanchito feliz', 'Chanchito triste']
# As you can see, only the first appearance was removed, not all the other repeated occurrence of the introduced value.

# In case you want to remove the last repeated value of your introduced text, you can use .pop .
pets.pop("Pulga")
print(pets)
# -- ['Wolfgang', 'Melvin', 'Pelusa', 'Pulga', 'Felipe', 'Chanchito feliz', 'Chanchito triste']

# If you want to remove a specific element, you can use .pop and the exact index number of the element you mean to¡.
pets.pop(1)
print(pets)
# -- ['Wolfgang', 'Pelusa', 'Pulga', 'Felipe', 'Pulga', 'Chanchito feliz', 'Chanchito triste']

# There's another method to remove elements from a list. You can use the "del" command and then specify within brackets what's the index number that you want to delete.
del pets[0]

# Fianlly, if you want to remove all the elements from a list, you can use the following method.
pets.clear()
