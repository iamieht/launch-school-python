# Problem (P)
# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

# - Input:
#   - User's name via input()

# - Output:
#   - a String greeting

# - Explicit Rules:
#   - If the user appends a !, the output is printed in uppercase

# - Implicit Rules:

# Examples/Test Cases (E)
# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

# Data Structures
# - String

# Algorithm
# - Declare a function get_input(prompt)
#   - Initialize a variable value = input(input)
#   - Return value
# - Initialize a variable name = get_input("What is your name? ")
# - Check if the last element of value is a !
#   - If so, print(f"HELLO {name}! WHY ARE WE YELLING?"")
#   - else, print(f"Hello {name}"")

# Code
def get_input(prompt):
    value = input(prompt)
    return value


def main():
    name = get_input("What is your name? ")

    if name[-1] == "!":
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}.")


main()
