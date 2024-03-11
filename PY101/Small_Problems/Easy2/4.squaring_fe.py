# Problem (P)
# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

# Further Exploration
# Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?

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
# - Declare a function power_n(num, power)
#   - return multiply(num, num)

# Code
def multiply(num1, num2):
    return num1 * num2


def power_n(num, power):
    result = 1
    for _ in range(1, power + 1):
        result = multiply(result, num)

    return result


print(power_n(5, 2) == 25)   # True
print(power_n(-8, 2) == 64)  # True
print(power_n(2, 8) == 256)  # True
