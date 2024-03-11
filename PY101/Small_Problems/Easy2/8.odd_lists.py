# Problem (P)
# Write a function that returns a list that contains every other element of a list that is passed in as an argument.

# Further Exploration
# Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

# - Input:
#   - list of n elements

# - Output:
#   - list of odd elements of original list

# - Explicit Rules:
#   - The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

# - Implicit Rules:
#   - Empty list returns an empty list

# Examples/Test Cases (E)
# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# Data Structures
#   - lists

# Algorithm
# - Declare a function oddities that takes a single argument of type list
#   - Initialize an empty list result
#   - Iterate over the odd elements of the original list
#       - Append the elements to the result list
#   - Return result

# Code
def oddities(lst):
    result = []
    for idx in range(0, len(lst), 2):
        result.append(lst[idx])

    return result


def oddities2(lst):
    return lst[::2]

# Further Exploration


def eventies(lst):
    return lst[1::2]


print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(oddities2([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities2([1, 2, 3, 4]) == [1, 3])        # True
print(oddities2(["abc", "def"]) == ['abc'])     # True
print(oddities2([123]) == [123])                # True
print(oddities2([]) == [])                      # True

print(eventies([2, 3, 4, 5, 6]) == [3, 5])     # True
print(eventies([1, 2, 3, 4]) == [2, 4])        # True
print(eventies(["abc", "def"]) == ['def'])     # True
print(eventies([123]) == [])                   # True
print(eventies([]) == [])                      # True
