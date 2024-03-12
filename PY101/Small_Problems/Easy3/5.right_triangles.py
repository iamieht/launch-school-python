# Problem (P)
# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars.

# - Input:
#   - a positive Integer

# - Output:
#   - a right triangle made of string '*'

# - Explicit Rules:
#   - The hypotenuse of the triangle should have one end at the lower-left of the triangle, and the other end at the upper-right.

# - Implicit Rules:

# Examples/Test Cases (E)
# triangle(5)
#     *
#    **
#   ***
#  ****
# *****
# Data Structures

# Algorithm
# - Declare a function triangle that takes a single argument (integer)
#   - Initialize a variable space = ' '
#   - Initialize a variable stars = 1
#   - Iterate over a range object (integer, 0, -1)
#       - print space times the (iteration number -1) + '*' * stars
#       - Increase stars by 1

# Code
def triangle(integer):
    space = ' '
    number_of_stars = 1
    for count in range(integer, 0, -1):
        print(f"{space * (count - 1)}{'*' * number_of_stars}")
        number_of_stars += 1


triangle(5)
triangle(9)
