# Problem (P)
# Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

# - Input:
#   - 3 positive integers

# - Output:
#   - a string char representing a grade

# - Explicit Rules:
# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# - Implicit Rules:
#  - There is no need to check for negative values or values greater than 100.

# Examples/Test Cases (E)
# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# Data Structures

# Algorithm
# - Declare a function get_grade that takes 3 arguments, each a positive integer
#   - Compute the average of the 3 arguments: (arg1 + arg2 + arg3) // 3 (implement a helper function)
#   - Use the match/case statement to determine the grade based onm the average calculated in the previous step
#

# Code
def avg(num1, num2, num3):
    return (num1 + num2 + num3) // 3


def get_grade(num1, num2, num3):
    average = avg(num1, num2, num3)

    match average:
        case average if average < 60:
            return 'F'
        case average if average < 70:
            return 'D'
        case average if average < 80:
            return 'C'
        case average if average < 90:
            return 'B'
        case average if average <= 100:
            return 'A'


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
