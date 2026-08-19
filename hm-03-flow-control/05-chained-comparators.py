"""
LETS SEE HOW WE CAN CHAIN THE COMPARATORS THAT WE HAVE ALREADY LEARNED HOW TO USE
"""

# Excercise: We need to implement an automated systems that evaluates the customers age and forbids children younger than 15 years old and older than 65 years old from entering our swimming pool

# 1.1) Initially, lets try the classic structure:
age = 25

if age >= 15 and age <= 65:
    print("You may enter")
else:
    print("You cannot pass")

# 1.2) Now, lets try the shortened and more efficient method:
age = 14

if 15 <= age <= 65:
    print("You may enter")
else:
    print("You caanot pass")
