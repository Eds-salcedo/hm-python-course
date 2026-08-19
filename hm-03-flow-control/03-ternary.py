"""
THE TERNARY OPERATOR USES THE CONDITIONALS "IF/ELSE" BUT WITH A DIFFERENT STRUCTURE, MORE REDUCED, IN A SINGLE LINE.
"""

# The traditional structure for conditionals is the following:
age = 15

if age > 17:
    print("Ok")
else:
    print("No")

print("END")

# The key for understanding the Ternary Operator is to know that instead of calling a certain function for each scenario of every conditional, you can assign a value in each case to a single central variable:
# Lets create the new variable called 'notification' to assign a different value for each conditional scenatio and the print it. Python will automatically print the corresponding value according to the enetered conditions.
age = 15

if age > 17:
    notification = "Is overage"
else:
    notification = "Is underage"

print(notification)

print("END")
# TERNARY:
# Now, understanding that we can create a multi-use variable for each conditional scenario, lets see the Ternary Operator structure:
age = 15

notification = "Is overage" if age > 17 else "Is underage"
print(notification)

print("END")

#STRUCTURE: (X_variable) IF (conditional_evaluation) ELSE (Y_variable)
