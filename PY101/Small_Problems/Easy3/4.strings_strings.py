# Problem (P)
# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

# - Input:
#   - a single integer

# - Output:
#   - a string of 1's and 0's with the length == integer

# - Explicit Rules:
#   - Always start with 1
#   - Always a positive integer

# - Implicit Rules:

# Examples/Test Cases (E)
# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# Data Structures

# Algorithm
# - Declare a function stringy that takes a single argument of type integer
#   - Initialize a variable result = ''
#   - Iterate over a range object (integer)
#       - check if result endswith(0) if so append a 1
#       - else, append a 0
#   - return result

# Code
def stringy(integer):
    result = ''
    for _ in range(integer):
        result += '1' if result.endswith('0') or result == '' else '0'

    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
