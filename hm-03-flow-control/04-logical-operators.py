"""
LOGICAL OPERATORS ARE: "AND", "OR" & "NOT"
"""

# In your case, as an experienced Data Analyst with Excel, you already know how this works
# AND will evaluate whether all entered evaluations are True: 2 > 1 AND 10 < 20 = True
# OR will evaluate whether just one of the entered evaluations is True: (4 > 6) OR (10 > 100) OR (2+1=3) = True
# NOT will evaluate if the result of an evaluation is false (opposite).

# 1) Is my car ready to ride?
gas = True
turned_on = True

if gas and turned_on:
    print("You may move")
else:
    print("You cannot move")

# 2) Another test where its False:
gas = True
turned_on = False

if gas and turned_on:
    print("You may move")
else:
    print("You cannot move")

# 3) Another test, but using OR:
gas = True
turned_on = False

if gas or turned_on:
    print("You may use the car")
else:
    print("You cannot use the car")

# 4) See how NOT changes the boolean value of the variables:
gas = False
turned_on = False

if not gas or turned_on:
    print("You may use the car")
else:
    print("You cannot use the car")

print("Done")

# 5) Lets use multiple variables now, including comparators:
gas = True
turned_on = True
age = 18

if gas and turned_on and age > 17:
    print("You may use the car")

print("Done")
# We had no print, since using AND required that all the variables

# 6) Lets use more combiantions:
gas = False
turned_on = True
age = 18

if not gas and (turned_on or age > 17):
    print("You may use the car")

print("Done")
