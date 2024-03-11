# Problem (P)
# write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

# - Input:
#   - 2 arguments of any type

# - Output:
#   - Boolean: True if exactly one of its arguments is truthy, False otherwise.

# - Explicit Rules:
# -
# - Implicit Rules:

# Examples/Test Cases (E)
# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# Data Structures

# Algorithm
# - Declare a function xor that takes two arguments of any type
#   - return bool(arg1 or arg2)

# Code
def xor(arg1, arg2):
    if arg1 and arg2:
        return False
    else:
        return bool(arg1 or arg2)


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
