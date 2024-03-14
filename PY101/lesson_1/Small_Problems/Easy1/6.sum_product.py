# Problem (P)

# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# - Input:
#   - Integer greater than 0
#   - 's' to compute sum or 'p' to compute product
# - Output:
#   - The sum or product of the integers from 1 to integer provided
# - Explicit Rules:
#   - Integer must be greater than zero
# - Implicit Rules:
#   - If 0 return 0

# Examples/Test Cases (E)
# print(sum_integers(5))  # => 15
# print(product_integers(6))  # => 720

# Data Structures
# - Integers

# Algorithm
# - Declare a function get_input(prompt)
#   - Initialize a variable value = input(prompt)
#   - Return value
# - Declare a function sum_integers(integer)
#   - Initialize a variable result = 0
#   - iterate over a range(1, integer + 1)
#       - sum each number and add to result
#       - return result
# - Declare a function product_integers(integer)
#   - Initialize a variable result = 1
#   - iterate over a range(1, integer + 1)
#       - multiply each number and add to result
#       - return result
# - Declare a function main()
#   - Initialize variable integer = get_input("Please enter an integer greater than 0:")
#   - Initialize a variable compute = get_input("Enter "s" to compute the sum, or "p" to compute the product.")
#   - if compute == "s": sum_integers(integer) print(f""The sum of the integers between 1 and {integer} is {result}")
#   - if compute == "p": product_integers(integer) print(f"The product of the integers between 1 and {integer} is {result}")

# Code


def get_input(prompt):
    value = input(prompt)
    return value


def sum_integers(integer):
    result = 0
    for num in range(1, integer + 1):
        result += num

    return result


def product_integers(integer):
    result = 1
    for num in range(1, integer + 1):
        result *= num

    return result


def main():
    integer = int(get_input("Please enter an integer greater than 0: "))
    compute = get_input(
        'Enter "s" to compute the sum, or "p" to compute the product. ')

    if compute == "s":
        result = sum_integers(integer)
        print(f"The sum of the integers between 1 and {integer} is {result}.")
    elif compute == "p":
        result = product_integers(integer)
        print(
            f"The product of the integers between 1 and {integer} is {result}.")
    else:
        print("Invalid Input")


main()
