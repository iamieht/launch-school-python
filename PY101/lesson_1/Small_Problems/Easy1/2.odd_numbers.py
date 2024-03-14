# Problem (P)

# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# - Mental Model:
# - Input:
#   - Integer number from 1 to 99
# - Output:
#   - Odd integer numbers within the range 1 to 99

# - Explicit Rules:
#   - Only odd numbers must be printed
#   - Each number must be printed in a separate line
# - Implicit Rules:
#   - Function takes a single parameter of type integer, in this case 99.
#   - Zero is not included.

# Data Structures
#   - Primitive integer

# Algorithm
# - Define a function odd_numbers with a single parameter integer
#   - Iterate from number 1 until the integer provided (inclusive)
#   - Define a function is_odd that takes a single integer
#       - return if the number is odd (number % 2 == 1)
#   - With each iteration check if the number is odd by invoking the is_odd function
#   - If the number is odd print it

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# Algorithm
# - Define a function odd_numbers_bonus with a single parameter integer
#   - Iterate from number 1 until the integer provided (inclusive) by using a step of 2, so the iteration only happens over the odd numbers
#   - print the numbers

# Further Exploration
# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

# Algorithm
# - Define a function odd_numbers_fe with two parameters (start, stop) of type integer
#   - Iterate from start until the stop (inclusive).
#   - Define a function is_odd that takes a single integer
#       - return if the number is odd (number % 2 == 1)
#   - With each iteration check if the number is odd by invoking the is_odd function
#   - If the number is odd print it

# Code
def odd_numbers(integer):
    for num in range(1, integer + 1):
        if is_odd(num):
            print(num)


def is_odd(integer):
    number = abs(integer)
    return number % 2 == 1


def odd_numbers_bonus(integer):
    for num in range(1, 100, 2):
        print(num)


def odd_numbers_fe(start, stop):
    for num in range(start, stop + 1):
        if is_odd(num):
            print(num)


# Examples/Test Cases (E)
# => 1, 3, 5, 7, 9.....99 (each number printed in its own line)
print("---- odd numbers -------")
odd_numbers(99)
print("---- odd numbers bonus --------")
odd_numbers_bonus(99)
print("---- odd numbers further exploration --------")
odd_numbers_fe(-20, 20)
