"""
LET'S LEARN HOW TO MANIPULATE, CHANGE, MODIFY, ETC LISTS IN PYTHON
"""

# Start with an easy example, bys selecting a specific element of a list for printing. try with Pulga:
pets = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(pets[2])   #It's 2 and not 3 because Python always starts with 0 for the first element (0, 1, 2, etc).
# --Pulga

# Now, we can change the values of each element of the list. Tru changing Wolfgag with Bug:
pets[0] = "Bug" 
print(pets)
# --['Bug', 'Pelusa', 'Pulga', 'Copito']

#You can also select a specific range to work with from the list, using ":"
print(pets[0:2])
# --['Bug', 'Pelusa', 'Pulga']

print(pets[1:])   # If you don't specify the final element of the list to operate on, the system will automatically go until the last one.
# --['Pelusa', 'Pulga', 'Copito']

#You can operate with negative arguments to iterate the lists, so you start from the last until the first.
print(pets[-1])
# --Copito

#You can also iterate skipping values
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[0::2])
# --['a', 'c', 'e', 'g']

#Let's try to get the odd numbers:
numbers = list(range(21))
print(numbers[1::2])   #Start with 1 instead of 0, so you start skipping 2 and moving to 3 and so on.
# --[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#Alternate way to do it:
numbers = list(range(1, 21))
print(numbers[0::2]) 
# --[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



