# Problem (P)
# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# - Mental Model:
#  Determine if the number's absolute value is odd, meaning having a remainder after dividing by 2.
# - Input:
#   - a single integer
# - Output:
#   - a Boolean value

# - Explicit Rules:
#   - The functions returns True when the number's absolute value is odd, False otherwise.
# - Implicit Rules:
#   - N/A


# Data Structures
# - Primitive values (int and bool)

# Algorithm
# - Define a fucntion is_odd with a single parameter called integer
#   - Initialize a variable number with the absolute value of integer
#   - Return the boolean value of the expression (if number % 2 != 0), as this will determined if the value of number is odd or not.

# Code

def is_odd(integer):
    number = abs(integer)
    return number % 2 != 0


# Examples/Test Cases (E)
print(is_odd(1))        # => True
print(is_odd(2))        # => False
print(is_odd(0))        # => False (0 is an even number)
print(is_odd(-5))       # => True
print(is_odd(-333))     # => True
