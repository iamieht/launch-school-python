# Problem (P)
# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

# - Input:
#   - a String
#   - a positive integer
# - Output:
#   - a String repeated as many times as the integer indicates
# - Explicit Rules:
#   - a positive integer
# - Implicit Rules:

# Examples/Test Cases (E)
# repeat('Hello', 3)
# Data Structures

# Algorithm
# - Declare a function repeat that takes two arguments, a String and an integer
#   - return string times integer

# Code
def repeat(string, integer):
    for _ in range(integer):
        print(string)


repeat('Hello', 3)
