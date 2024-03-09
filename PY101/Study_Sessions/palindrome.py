# Problem (P)
# Write a palindrome function with two integer numbers as parameters ("num" and "s") and outputs a list that contain an "s" number of elements, all palindromes, higher than the first number  "num". No single digit numbers can be palindromes

# - Input:
#   - Integer num
#   - Integer s
# - Output:
#   - a list that contain an "s" number of elements, all palindromes, higher than the first number  "num".

# - Explicit Rules:
#   - No single digit numbers can be palindromes
# - Implicit Rules:
#   - List elements order is ascending

# Examples/Test Cases (E)

# Data Structures
# - list

# Algorithm
# - Declare a function palindromes with two parameters (num, s)
# - Initialize a result list with empty elements
# - If s is 0 return an empty list
# - If num < 10, replace num with 10
# - Declare a helper function is palindrome with a single parameter of type string
#   - if string == "".join(list(string).reverse()) return True, False otherwise
# - Iterate while result < s
#   - if is_palindrome(str(num)):
#       - result.append(num)
#   - else: num + 1
# - return result

# Code
def is_palindrome(string):
    return string == "".join(list(reversed(list(string))))


def palindromes(num, s):
    result = []
    if s == 0:
        return result

    if num < 10:
        num = 10

    while len(result) < s:
        if is_palindrome(str(num)):
            result.append(num)

        num += 1

    return result


# #Examples/Test Cases
print(palindromes(6, 4))  # => [11, 22,33,44]
print(palindromes(0, 4))  # => [11, 22,33,44]
print(palindromes(20, 0))  # => []
print(palindromes(75, 1))  # => [77]
print(palindromes(100, 2))  # => [101, 111 ]

# print(is_palindrome(str(100)))
