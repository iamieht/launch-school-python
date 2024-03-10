# Problem (P)
# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument.

# - Input:
#   - String
# - Output:
#   - Integer
# - Explicit Rules:
#   - The UTF-16 string value is the sum of the UTF-16 values of every character in the string.
# - Implicit Rules:

# Examples/Test Cases (E)

# Data Structures
# - Integer
# - String

# Algorithm
# - Declare a function utf16_value with a single parameter of tyupe string
#   - Initialize a variable string_value = 0
#   - Iterate over each element of the string
#       - invoke the function org passing each character as an argument
#       - Increment string_value with the return value of function ord
#   - return string_value

# Code
def utf16_value(string):
    string_value = 0
    for char in string:
        string_value += ord(char)

    return string_value


# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
