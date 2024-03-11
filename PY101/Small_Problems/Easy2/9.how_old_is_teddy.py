# Problem (P)
# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

# - Input:
#   - Nothing
# - Output:
#   - a random integer between 20 and 100 (inclusive)

# - Explicit Rules:

# - Implicit Rules:

# Examples/Test Cases (E)
# Teddy is 69 years old!

# Data Structures

# Algorithm
# - Declare a function main
# - Initialize a variable years = random.rand(20, 100)
# - Print(f"Teddy is {years} old!")

# Code
import random


# def main():
#     years = random.randint(20, 100)
#     print(f"Teddy is {years} years old!")


# main()

# Further Exploration
def get_name(prompt):
    name = input(prompt)
    return name


def main():
    years = random.randint(20, 100)
    name = get_name("What's your name? ")
    if not name:
        name = "Teddy"
    print(f"{name} is {years} years old!")


main()
