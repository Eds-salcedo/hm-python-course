"""
NOW LET'S PUT INTO PRACTICE WHAT WE'VE LEARNED SO FAR, USING VARIABLES AND CUSTOM DEF FUNCTIONS
"""

# Let's create a function that evaluates whether a word or phrase is a palyndrome.
# A palyndrome refers to a word or phrase than can be written backwards (in a reverse order) and still remain structured in the same way as originally.
# This will show that we know how to create functions and variables to iterate and handle arrays and, in the future, lists.

# Exercise: Create a function that evaluates whether a given string is a palyndrome or not (for example, "Abba").

# 1) Creating a function that eliminates spaces within a string.
def no_space(text):
  new_text = ""
  for x in text:
    if x != " ":
      new_text += x
  return new_text

# 2) Creating a function that iterates any given string and saves every character behind the previously iterated character.
def reverse(text):
  reversed_text = ""
  for y in text:
    reversed_text = y + reversed_text
  return reversed_text

# 3.1) Creating a complied function that includes the previous 2 functions into 1.
def is_palyndrome(text):
  spaceless_text = no_space(text)
  reversed_text = reverse(spaceless_text)
  print(reversed_text)


is_palyndrome("amo la paloma")
is_palyndrome("hello world")
# --amolapaloma
# --dlrowolleh
# It works!

# 3.2) Another way to set your final function, so the system can automatically compare that it can be written both ways correctly (and avoid case-sensitive errors):
def is_palyndrome(text):
  spaceless_text = no_space(text)
  reversed_text = reverse(spaceless_text)
  return text.lower() == reversed_text.lower()


print(is_palyndrome("Amo la paloma"))
print(is_palyndrome("hello World"))
print(is_palyndrome("Somos o no somos"))
# --True
# --False
# --True

# You used the exact equality to compare the initial text and the processed text, both without space characters and both transformed to lower-case texts.
