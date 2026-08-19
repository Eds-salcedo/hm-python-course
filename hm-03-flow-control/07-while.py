"""
LETS HOW TO USE THE 'WHILE' LOOP
"""

# Primarily, the WHILE iterator is intended to be used when iterating a length-undetermined or infinite set of values
# Its main difference with the FOR loop is that FOR should be used when the programmer knows that the set of values (like a list) is finite
# And WHILE loop should contain a specific loop-breaking condition to avoid any potential infinite loops that would consume all our PCs memory and undetermined amount of time.

# 1) Exercise 1:
number = 1

while number < 100:  # This will iterate the NUMBER variable until it is 99. 'Is it true? No? Then iterate and iterate again until the condition is met'.
    # Here we print the current value of NUMBER in every iteration to see how it was modified.
    print(number)
    # Here we indicate that the NUMBER variable will be modified over and over in an incremental way, multiplying itself by 2 with every iteration.
    number *= 2

print("DONE")

# 2) Exercise 2:

command = ""  # We start with and empty variable
# Here we evaluate if the command is NOT equal to one of those specified texts
while command.strip().lower() != "exit":
    # Then we indicate to open an input option for the use to introduce a value to the code, which will change the value of the COMMAND variable and will be evaluated in a new loop
    command = input("$")
print(command)  # Here we indicate that, if in any loop the variable COMMAND is different from "exit" or "salir", the value will be printed. If it is equal to one of those, the introduced COMMAND value will no longer be printed

# 3) Exercise 3: Always remember that a WHILE infinite loop might generate problems consuming too much memory from your PC, causing your Operative System to terminate the WHILE operation of you text editor.
# This is why you should always add an exit condition when using WHILE loops

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
print("YOU'RE OUT")
# The BREAK condition shoul be ideally used as an ending to a conditional. This will stop the loop in general
