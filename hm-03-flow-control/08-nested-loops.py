"""
LET'S LEARN HOW NESTED LOOPS WORK
WE'LL SEE THE TYPICAL BOOTCAMP EXAMPLE
"""

# It's basically inserting a for-in loop within another such loop

# Exercise #1 - Here we'll iterate the 3 values contained in this range of values, which are: 0, 1 and 2.
for j in range(3):
    # Here we'll iterate the 2 values contained in this created range (the second range), which are: 0 and 1.
    for k in range(2):
        print(f"{j}, {k}")
# When executing this nested iteration, the result will reflect that the iteration of the first value contained in the first iterable (range(3)) will be processed along with the first of the second iterable.
# After that, Python will execute the same first value of the first iterable but NOW along the SECOND value of the second iterable.
# In conclusion, Python will keep processing the same first element of the first iterable until it finished iterating the last value of the last iterable. Then it will start iterating the second value of the first iterable along with all thw other iterables.

print("DONE")

# Exercise #2:
for j in ["a", "b", "c"]:  # Outter loop
    for k in ["1", "2", "3"]:  # Inner loop
        print(f"{j}, {k}")
        print(f"{k}, {j}")
# Regardless of the order that you indicate to print the veriables, the execution logic will prevail.
