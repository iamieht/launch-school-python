# Problem (P)
# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

# - Input:
#   - number1: positive float
#   - number2: positive float

# - Output:
#   - a floating point per arithmetic operation (+, -m *, /, //, %, **)

# - Explicit Rules:

# - Implicit Rules:

# Examples/Test Cases (E)
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

# Data Structures

# Algorithm
# - Declare a function get_number(prompt)
#   - number = input(prompt)
#   - return float(number)
# - Declare a main function
#   - number1 = get_number("==> Enter the first number: ")
#   - number2 = get_number("==> Enter the second number: ")
#   - print(f"==> {number1} + {number2} = {number1 + number2}")
#   - print(f"==> {number1} - {number2} = {number1 - number2}")
#   - print(f"==> {number1} * {number2} = {number1 * number2}")
#   - print(f"==> {number1} / {number2} = {number1 / number2}")
#   - print(f"==> {number1} // {number2} = {number1 // number2}")
#   - print(f"==> {number1} % {number2} = {number1 % number2}")
#   - print(f"==> {number1} ** {number2} = {number1 ** number2}")

# Code
def get_number(prompt):
    number = input(prompt)
    return float(number)


def main():
    number1 = get_number("==> Enter the first number: ")
    number2 = get_number("==> Enter the second number: ")
    print(f"==> {number1} + {number2} = {number1 + number2}")
    print(f"==> {number1} - {number2} = {number1 - number2}")
    print(f"==> {number1} * {number2} = {number1 * number2}")
    print(f"==> {number1} / {number2} = {number1 / number2}")
    print(f"==> {number1} // {number2} = {number1 // number2}")
    print(f"==> {number1} % {number2} = {number1 % number2}")
    print(f"==> {number1} ** {number2} = {number1 ** number2}")


main()
