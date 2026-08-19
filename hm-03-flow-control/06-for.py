"""
LETS DIVE DEEPER INTO "FOR"-"IN" LOOPS. YOU WILL USE IT A LOT, ESPECIALLY IN DATA ANALYSIS & DATA SCIENCE
"""

# A typical use of the FOR loop is to search elements, perform mathematical operations and much more.

# 1) Example: Lets create a sequence of five numbers with "range (5)" and lets evaluate each of those numbers adding "for".
for number in range(5):
    print(number)
# Remember that, by default, list and range positions in Pyhton start with 0, so: range = 0, 1, 2, 3, 4; Thats a sequence 5 numbers but starting with number zero.
# The variable of "number", by command of the "for" instruction, will temporarily take each value of the sequence of numbers created by "range". This is super useful when you try to search a specific value or to evaluate if a certain condition/result is met throughout a list.
# For now, we will just iterate through every value of the range and just print them. In the future, we will try to apply certain evaluations.

# 2) Example: You can try to start applying virtual modifications to the initial sequence of values or lists.
for number in range(5):
    print(number, (number * 'hola mundo, '))
    print("Done")
# Here you printed each number of the list automatically with the "for" loop + (took each corresponding number as a factor to multiply the phrase 'hola mundo' so it repeats the number of times corresponding to the list numeric value).


# FOR + ELSE


# 3) Example: Lets try to create a simple search code using FOR.
search = 3

for number in range(50):
    print(number)  # Print every iteration
    if number == search:
        print("found:", search)
        break

# REMEMBER TO USE "==", AS "=" IS ONLY USED TO ASSIGN A VALUE TO A VARIABLE AND THE "==" IS USED TO INDICATE EQUALITY.
# Also, remember that in programming efficiency is very important; that is why a "break" command will stop the program from keeping its execution until the last list value, stopping when the desired value is found.

# 4) Now, taking that same example, we can delete the "BREAK" command and let the code to execute the entire iteration and give us a notification in case that the desired evaluation is not met throughout the whole list iteration.
search = 85

for number in range(50):
    print(number)
    if number == search:
        print("found:", search)
        break  # If you dont add a break here, the "ELSE" evaluation will keep being executed IN PARALELL along with every single loop of the original instruction and not at the end as a final command in case last resort.
else:
    print(f"Value {search} not found!")


# THERE ARE SEVERAL ITERABLE ITEMS ON PYTHON (LISTS, TUPLES, DICTIONARIES, ETC)
# AMONG THOSE, WE CAN INCLUDE STRINGS (TEXT CHAINS)

# Example #1:
for char in "Ultimate python":
    print(char)
print("DONE")

# Example #2:
security_code = "AzDxYssMLOPSrrjkgls"

revision_A = "ÑÑÑ"
revision_O = "000"

new_code = security_code
for letter in security_code:
    if letter == "A":
        new_code = new_code.replace("A", revision_A)
    if letter == "O":
        new_code = new_code.replace("O", revision_O)

print(new_code)
