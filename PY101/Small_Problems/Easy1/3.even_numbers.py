# Problem (P)

# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# - Input:
#   - Numbers 1 and 99
# - Output:
#   - Even numbers within the range 1 to 99
# - Explicit Rules:
#   - Print only even numbers within the range
# - Implicit Rules:

# Examples/Test Cases (E)
# 2, 4, 6, 8, 10,....

# Data Structures
#   - Only primitive integers

# Algorithm
# - Iterate over the range 1 to 99
#   - Check if each number % 2 == 0
#   - If truthy print number

# Code
for num in range(1, 100):
    if num % 2 == 0:
        print(num)
