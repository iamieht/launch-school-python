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


def sum_of_squares(num1, num2):
    def square(num):
        return num * num

    return square(num1) + square(num2)


print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# 4. Write a function called increment_counter that increments a counter variable every time it is called.
counter = 0


def increment_counter():
    global counter
    counter += 1


print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

# 5. There's a bug in this code. Identify the bug, and fix it.


def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101


all_actions()
