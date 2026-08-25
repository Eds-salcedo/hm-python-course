"""
NOW LET'S LEARN HOW TO DEBUG VARIABLE
"""

# Let's try an example. A default function called len() already exists in Python, but let's see a very similar example to easily understand how this works. 
# First, let's create the function, inserting an iteration (for) that sums +1 to itself with every round. 
def length(text):
  result = 0
  for character in text:
    result += 1
    return result

# Let's insert a generic "Hello world" argument into the recently created lenght() function and let's save it all inside a variable
l = length("Hello world")
print(l)
# --1
# There it is, the console is returning 1 instead of the full count of the string's characters. Now we can use a simple debugging.

"""
The debugging on VScode can be implemented by clicking on the "play and insect (bug)" button in left bar and then on "launch .json file" option.
Then, in the subsequent option, we'll click on the "python file" option, then we'll see a new folder ".vscode" and a new file "launch.json" in the folders section (left).
You can use Breakpoints by clicking on the left of any code line (thin blank space) to add a red dot that will make the debugging to stop in that line.
If you click on "play", you'll be able to see a dropdown menu that includes Variables > Locals > 1) Special Variables. 2) Function variables
""""

# Now, using the debugger, we can see that the execution of the variable l is equal to 1.
# Using the functionalities of "Step in" and "Step over" on a function you'll be able to execute the funtion line by line to find the error.
# Proceeding as mentioned, we see that the iterator FOR returns the letter H (correctly, from "Hello world"), but after that, the debugger exits before the whole iteration.
# We can imply that the iteration stopped when counting the first letter (1) as the return keyword was indented right after result+=1 and not aligned to the for iterator.

