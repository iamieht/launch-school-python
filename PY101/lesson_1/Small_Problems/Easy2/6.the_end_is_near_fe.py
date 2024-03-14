# Problem (P)

# Write a function that returns the middle word of a phrase or sentence. It should handle all of the edge cases you thought of.

# - Input:
#   - a String
# - Output:
#   - a String that represents the next to last word in the original string

# - Explicit Rules:
# - Words are any sequence of non-blank characters.

# - Implicit Rules:
#  - You may assume that the input string will always contain at least two words.

# Examples/Test Cases (E)
# These examples should print True
# print(middle_word("last word") == "word")
# print(middle_word("Launch School is great!") == "is")
# print(middle_word("") == "")
# print(middle_word("LS") == "LS")
# print(middle_word(""Python Track is very weird!"") == "is")

# Data Structures
# - a list

# Algorithm
# - Declare a function middle_word that takes a single argument (string)
#   - Guard clause: if string.isempty() or len(string) == 1: return string
#   - Initialize a string_lst = string.split(" ")
#   - middle_idx = Determine the length of the list and divide by 2
#   - Return string_lst[middle_idx]

# Code
def middle_word(string):
    if len(string) < 2:
        return string

    string_lst = string.split(" ")
    middle_idx = len(string_lst) // 2
    return string_lst[middle_idx]


print(middle_word("last word") == "word")
print(middle_word("Launch School is great!") == "is")
print(middle_word("") == "")
print(middle_word("LS") == "LS")
print(middle_word("Python Track is very weird!") == "is")
