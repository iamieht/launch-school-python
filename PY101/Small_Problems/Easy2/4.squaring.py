# Problem (P)
# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

# - Input:
# - A number: float or int

# - Output:
#   - The number squared

# - Explicit Rules:
#   - multiply function must be used

# - Implicit Rules:

# Examples/Test Cases (E)
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Data Structures

# Algorithm
# - Declare a function square(num)
#   - return multiply(num, num)

# Code
def multiply(num1, num2):
    return num1 * num2


def square(num):
    return multiply(num, num)


print(square(5) == 25)   # True
print(square(-8) == 64)  # True
