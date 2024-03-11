# Problem (P)
# Write a function that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the argument is a negative number, return it as-is.

# - Input:
#   - integer
# - Output:
#   - negative integer

# - Explicit Rules:
#   - If the argument is a positive number, return the negative of that number.
#   - If the argument is a negative number, return it as-is.

# - Implicit Rules:

# Examples/Test Cases (E)
# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True
# Data Structures

# Algorithm
# - Declare a function negative that takes a single argument of type integer
#   - check if number is negative return thenumber
#   - else return the number * -1

# Code
def negative(integer):
    if integer < 0:
        return integer
    else:
        return integer * -1


def negative2(number):
    return -abs(number)


print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
