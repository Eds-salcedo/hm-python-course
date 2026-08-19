"""
EXERCISE USING STRING METHODS AND OTHER CONTENTS LEARNED SO FAR
"""
# Excercise: Using .replace() for text is easy, but try to do the same only using index positions:
# Try to replace "Memphis the cat" for "Memphys the kitty". Use new variables:

# -----

# Original string
pet = "Memphis the cat"

# Variables for replacement
new_v1 = "y"
new_v2 = "kitty"

# Find positions
index_y = pet.find("i")
print("'i' is at: ", index_y)

index_cat = pet.find("cat")
print("'cat' starts at: ", index_cat)

# Calculate lengths
len_repl = len("cat")
print("the number of characaters to replace is: ", len_repl)

to_replace = index_cat, index_cat + len_repl
print(
    "the limit positions of the indexes to replace are: ",
    to_replace
)

pet_len = len(pet)
print("The complete lenght of the initial string is: ", pet_len)

# Rebuilding the string
new_name = (pet[0:index_y]
            + new_v1
            + pet[(index_y + len(new_v1)): index_cat
                  ]
            + new_v2
            + pet[(index_cat + len(new_v2)):]
            )
print(new_name)
