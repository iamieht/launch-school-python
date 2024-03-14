# Problem (P)

# Write a function that returns the next to last word in the string argument.

# - Input:
#   - a String
# - Output:
#   - a String that represents the next to last word in the original string

# - Explicit Rules:
# - Words are any sequence of non-blank characters.

# - Implicit Rules:
#  - You may assume that the input string will always contain at least two words.

# Examples/Test Cases (E)
# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Data Structures
# - a list

# Algorithm
# - Declare a function penultimate that takes a single argument (string)
#   - Initialize a string_lst = string.split(" ")
#   - Return string_lst[-2]

# Code
def penultimate(string):
    string_lst = string.split(" ")
    return string_lst[-2]


print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
