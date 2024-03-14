# Problem (P)
# Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

# - Input:
#   - a String with non-alphabetic chars

# - Output:
#   - a String with non-alphabetic chars replaced by space

# - Explicit Rules:
# -  If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

# - Implicit Rules:

# Examples/Test Cases (E)
# print(clean_up("---what's my +*& line?") == " what s my line ")
# True

# Data Structures

# Algorithm
# - Declare a function clean_up that takes a single argument of type string
#   - Initialize a variable cleaned_up_str = ''
#   - Iterate over the string:
#       - check if char.isalpha() or char.isspace():
#           - append it to cleaned_up_str
#       - else:
#           - if cleaned_up_str.endswith(' '): continue
#           - else: cleaned_up_str += ' '
#   - return cleaned_up_str

# Code
def clean_up(str):
    cleaned_up_str = ''
    for char in str:
        if char.isalpha():
            cleaned_up_str += char
        else:
            if not cleaned_up_str.endswith(' '):
                cleaned_up_str += ' '

    return cleaned_up_str


print(clean_up("---what's my +*& line?") == " what s my line ")  # True
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # True
