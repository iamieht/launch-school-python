# Problem (P)
# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5.

# - Input:
#   - Integer
# - Output:
#   - Integer that represents a sum
# - Explicit Rules:
#   - Integers must be divisble by 3 or 5
#   - Integer must be greater than 1
# - Implicit Rules:

# Examples/Test Cases (E)
# These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# Data Structures
# - Integer

# Algorithm
# - Declare a function multisum with a single parameter of type integer
#   - Initialize a variable result with initial value 0
#   - Iterate over the range 1 to integer + 1
#       - If number % 3 == 0 or number % 5 == 0:
#           - result += number
#   - return result

# Code
def multisum(integer):
    result = 0
    for num in range(1, integer + 1):
        if num % 3 == 0 or num % 5 == 0:
            result += num

    return result


print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
