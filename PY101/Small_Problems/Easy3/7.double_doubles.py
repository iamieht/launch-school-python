# Problem (P)
# Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.

# - Input:
#   - a positive integer

# - Output:
#   - a positive integer

# - Explicit Rules:
#   - A double number is an even-length number whose left-side digits are exactly the same as its right-side digits.
#   - If the argument is a double number, return the double number as-is.
#   - If not, then multiply the number by 2

# - Implicit Rules:

# Examples/Test Cases (E)
# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# Data Structures

# Algorithm
# - Declare a helper function is_double that takes a single argument (a positive integer)
#   - Initialize a variable str_number = str(integer)
#   - check if the lenght of str_number is even, if so:
#       - split the str_number in half and compare both halves, if they are the same return True, else False
#   - If is odd: return False
# - Declare a function twice that takes a single argument (a positive integer)
#   - if is_double(integer): return integer
#   - else: return integer * 2

# Code
def is_double(number):
    str_number = str(number)
    middle = len(str_number) // 2
    left = str_number[:middle]
    right = str_number[middle:]

    return left == right
    # if len(str_number) % 2 == 0:
    #     middle_idx = len(str_number) // 2
    #     if str_number[:middle_idx] == str_number[middle_idx:]:
    #         return True

    # return False


def twice(number):
    return number if is_double(number) else number * 2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
