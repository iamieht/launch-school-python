# Problem (P)
# Write a function that takes a non-empty string argument and returns the middle character(s) of the string

# - Input:
#   - String

# - Output:
#   - String

# - Explicit Rules:
#   -If the string has an odd length, you should return exactly one character.
#   -If the string has an even length, you should return exactly two characters.

# - Implicit Rules:


# Examples/Test Cases (E)
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchshool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# Data Structures

# Algorithm
# - Declare a helper function is_odd that takes a single argument of type int
#   - if int % 2 == 0: return False, True otherwise
# - Declare a function center_of that takes a single argument of type string
#   - Initialize a variable middle_idx = len(string) // 2
#   - If is_odd(middle_idx): return string[middle_idx]
#   - else: return string[middle_idx:middle_idx+1]

# Code
def is_odd(integer):
    return True if integer % 2 != 0 else False


def center_of(string):
    middle_idx = len(string) // 2
    if is_odd(len(string)):
        return string[middle_idx]
    else:
        return string[middle_idx - 1: middle_idx + 1]


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
