# 1. What does the following function do? Be sure to identify the output value.
import math
import math as m
from math import sqrt


def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()


my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))
# Step 1: ['Antonina', 'Chris', 'Clare', 'Karis', 'Karl']
# Step 2: CHRIS

# 2. Write some code to output the square root of 37. Try to write the code in three different ways.
print(math.sqrt(37))
print(sqrt(37))
print(m.sqrt(37))

# 3. Write a nested function in sum_of_squares that will make this code work as shown.


def square(num):
    return num * num


def sum_of_squares(num1, num2):
    return square(num1) + square(num2)


print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)
