# Problem (P)
# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.


# - Input:
#   - string1
#   - string2
# - Output:
#   - string
# - Explicit Rules:
#   - resulting string is shorter_str + longer_str + shorter_str
#   - strings are of different lengths
# - Implicit Rules:


# Examples/Test Cases (E)

# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# Data Structures
#   - strings

# Algorithm
# - Declare a function short_long_short with two parameters of type string
#   - Initialize a variable shorter = string2 if len(string1) > len(string2) else string1
#   - Intialize a variable longer = string1 if len(string1) > len(string2) else string2
#   - return shorter + longer + shorteer

# Code
def short_long_short(string1, string2):
    shorter = string2 if len(string1) > len(string2) else string1
    longer = string1 if len(string1) > len(string2) else string2

    return shorter + longer + shorter


print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

# Ternary Operator, Unpacking, f strings
# def short_long_short(str1, str2):
#     short, long = (str1, str2) if len(str1) < len(str2) else (str2, str1)
#     return f"{short}{long}{short}"
