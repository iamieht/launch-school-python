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
