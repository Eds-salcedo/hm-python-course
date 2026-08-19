"""
LETS START CONDITIONALS WITH 'IF', 'ELIF' AND 'ELSE'
"""

# Conditionals are used to indicate your code what criteria it must meet in order to proceed with a certain functionality or branch of your code.
# Lets learn this with a practical exercise! Imagine that we need to create an automated script for a cinema that validates all customer ages so they are allowed 
# to enter +18 movie projections or not and also validates if a discount applies to +55 year-old customers.

# 1) Simple flow in a Truthy scenario:
age = 22
if age > 17:
    print("Allowed to enter")

print("Done")

# 2) Simple flow if/else in a Falsy scenario:
age = 15
if age > 17:
    print("Allowed to enter")
else:
    print("NOT allowed to enter")
print("Done")

# 3) Multiple conditions:
age = 60
if age > 54:
    print("You may enter with a Discount!")
elif age > 17:
    print("You are allowed")
else:
    print("You are NOT allowed")

print("Done")
# You have to be aware of the execution order. First, Python will execute whats above and, in case it is not TRUE, it will keep executing the following instructions.
# If we had written the +17 condition first and the instructed age (60) thus had evaluated as True, the code would have stopped right there, at the beginning.
# Considering that, by logic, the +17 requirement is obviously met when a customer is +54 y.o., so the most important part turns into the +54 discount and that is 
#the execution order that we should type, to avoid skipping the discount when all the +54 evaluate as True for the +17 condition.
# All +54yo are +17; but NOT all +17 are +54.

# 4) Logic order for if/elif/else. Wrong priority order, wrong result:
age = 60
if age > 17:
    print("You may enter")
elif age > 54:
    print("You may enter with a Discount!")
else:
    print("You are NOT allowed")

print("Done")

# 5) You can get rid of the final "else" and just leave the "elif". In the following case, the entered data that does not match the conditions will not have a 
#    negative anwser, but rather just a final answer closing the code ("Done").
age = 15
if age > 17:
    print("You may enter")
elif age > 54:
    print("You may enter with a Discount!")

print("Done")

# 6) Multiple conditions with multiple "elif". Remember the evaluation priority order
ages = [70, 55, 18, 16]

for age in ages:
    if age > 65:
        print(f"With {age}, you may enter with a Super Discount!!")
    elif age > 54:
        print(f"With {age}, you may enter with a Discount!")
    elif age > 17:
        print(f"With {age}, you are allowed to enter")
    else:
        print(f"Sorry, with {age} you are NOT allowed")
print("Done")
# In this exercise I used the conditionals with their priority order, and also a little help from a list to show automatically several cases of the conditionals. 
#To operate with lists like this, it was necessary to unpack it with a FOR IN interation through each element of the list.
