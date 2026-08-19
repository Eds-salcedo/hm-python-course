"""
METHODS APPLIED TO STRINGS
"""

# Methods are functions ( f(x) = y ) associated to an specific CLASS or OBJECT

animal = "memphis the cat"
print(animal.upper())

animal2 = "Memphis the cat"
print(animal.lower())

print(animal.capitalize())

# The equivalent of Excel DAX =PROPER() function in Python is ".title()":
print(animal.title())

# The .strip method works in a similar way to the =TRIM() function in Excel DAX:
animal3 = "   Memphis the cat   "
print(animal3)
print(animal3.strip())

# Methods can be used in "chained" way, to obtain the desired result:
print(animal3.capitalize())
print(animal3.strip().capitalize())

# We can also be more specific about .strip, indicating Python whether we only want to eliminate the blank spaces to the left or to the right of the text:
print(animal3.rstrip())
print(animal3.lstrip())

# There is also a way to look for teh exact index position (number) of a specific character inside a string:
print(animal2.find("ca"))
# If the character you are looking for repeats itself several times across the string you are evaluating, you will receive only the first appearance:
print(animal2.find("e"))
# Remember that Python is case-sensitive, so if you try to find those se characters but capitalized or any other character that is not within your variable value, it will show you "-1":
print(animal2.find("CA"))
print(animal2.find("dog"))
# A "-1" result = "I did not find it".

# You can replace any element from your variable value within the print function, to avoid modifying it directly at the source, perhaps for a testing or a temporary need:
print(animal2.replace("cat", "dog"))
# Careful! Always remember: Python is case sensitive and iterable indexes start from 0,1,2...etc. You might think that the program is not working well or that the algorithm is preventing you from modifying parts of the code.
print(animal2.replace("memphis", "tom"))
print(animal2.replace("Memphis", "Tom"))

# The operator "in" inside a print() function also searches a given value within a variable, and returns a booblean ("True" or "False") and it will NOT return any index position.
print("fish" in animal2)
print("fish" not in animal2)
