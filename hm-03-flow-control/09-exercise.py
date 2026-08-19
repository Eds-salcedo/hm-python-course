"""
LET'S SOLVE AN EXERCISE WITH THE CONTENT LEARNED ON THIS BLOCK
"""

# We need to create an interactive application that verifies whether we have previously entered a number.
# In case the user had not entered a number, ask them to enter one, then to enter an operation, then a second number and then show them the result.
# Then, we have to save that result as an initial number and repete the scheme to ask for an operation and then a second number.
# To exit, aske them to type "exit"
# The operations must be the basic math operations.

print("CALCULATOR")
print("For exitting the app type 'exit'")
print("Allowed operations are: sum, sub, mul and div")


# First, we have to initiate with an empty variable in order to fill it with an input value from the customer afterwards.
result = ""

# Now we have to establish an infite WHILE loop, as the calculator should remain executed indefitely until the customer types "exit".
while True:

    # Aferward, we havve to open a first IF conditional to indicate that, if the RESULT variable is a Falsey value (Falseys: empty list [] or string "", etc , 0, False & None).
    if not result:
        # That will be useful to pick an initially empty RESULT variable (empty string) and re-assign a customized INPUT value assigned by the user.
        result = input("Enter the first number: ")

        if result.lower() == "exit":  # Inside the indentation of that input, we have to open another conditional so the program is always ready to EXIT if the user types so at any input.
            break
        else:  # In case that the user's input is not "exit", then we have to convert that input into an integer.
            result = int(result)
    # At this point, the original WHILE loop keeps being open, we already filled the RESULT variable that was originally empty thanks to our conditional IF NOT and we either exited according to the user or we just saved the new variable's value through the users INPUT to be used afterward.

    # Now, we have to open a sub-loop to define the OP (operations) variable, which will be filled with an imput value specified by the customer and alwways ready to exit, primarily.
    while True:
        op = input("Enter operation: ")
        if op.lower() == "exit":
            break
        # Afterward, we have to evaluate whether the customer's input is any of the 4 valid operations (this could be also done with a list to avoid redundancy)
        elif op == "sum" or op == "sub" or op == "mul" or op == "div":
            break
        # Otherwise, if the introduced vale is not EXIt or any of the valid operations (else), then we have to print an error so this sub-loop of OPERATION starts again.
        else:
            print("Error: Invalid operation. Allowed operations are: sum, sub, mul, div.")
    # Here we indicate a closing condition fo the WHILE loop, which the customer's EXIT command.
    if op == "exit":
        break

    # Now we define the n2 variable
    n2 = input("Enter the next number: ")
    if n2.lower() == "exit":
        break
    n2 = int(n2)

    # Here, having the 2 values and the correct operation, we have to list what to do with any of the valid operations considered, a possible error message and the regular printing of an eventual result.
    if op.lower() == "sum":
        result = result + n2  # Or result += n2
    elif op.lower() == "sub":
        result = result - n2  # Or result -= n2
    elif op == "mul":
        result = result * n2  # Or result *= n2
    elif op == "div":
        if n2 == 0:
            print("Division by 0 is not allowed.")
            continue
        result = result / n2  # Or result /= n2
    else:
        print("Error: Invalid type of operation")
        break
    print(f"The result is: {result}")
