# Problem (P)
# Write a function that takes a short line of text and prints it within a box.

# - Input:
#   - a String
# - Output:
#   - a String
# - Explicit Rules:
# - Implicit Rules:
#   - Length of the box is len of string + 1 space at each side
#   - Width of the box is 5 chars

# Examples/Test Cases (E)
# print_in_box('To boldly go where no one has gone before.')
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Data Structures

# Algorithm
# - Declare a function print_in_box that takes a single string as argument
#   - Initialize a variable length = len(string)
#   - Initialize a variable top_bottom_box = f"+{length * -}+"
#   - print(top_bottom_box)
#   - print("|"{length * ''}|)
#   - print(f"| {string}. |")
#   - print("|"{length * ''}|)
#   - print(top_bottom_box)

# Code
def print_in_box(string):
    length = len(string)
    top_bottom_box = f"+-{length * "-"}-+"
    top_bottom_space = f"| {length * ' '} |"
    print(top_bottom_box)
    print(top_bottom_space)
    print(f"| {string} |")
    print(top_bottom_space)
    print(top_bottom_box)


print_in_box('')
print_in_box('To boldly go where no one has gone before.')

