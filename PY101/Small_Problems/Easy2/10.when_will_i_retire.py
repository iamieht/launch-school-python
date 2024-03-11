# Problem (P)
# Build a program that displays when the user will retire and how many years she has to work till retirement.

# - Input:
#   - Age
#   - Retirement Age

# - Output:
#   - Current Year
#   - Retirement Year
#   - Years before retirement

# - Explicit Rules:

# - Implicit Rules:

# Examples/Test Cases (E)
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

# Data Structures

# Algorithm
# - Declare a function get_input(prompt)
#   - Initialize value = input(prompt)
#   - Return value
# - Declare a function years_to_retire(current_age, retirement_age)
#   -
#   - Initialize a variable retirement_year = current.year + retirement_age
#   - Initialize a variable years_to_work = retirement_age - current_age
#   - Return tuple (retirement_year, years_to_work)
# - Declare a main function
#   - current_age = get_input("What is your age? ")
#   - retirement_age = get_input("At what age would you like to retire? ")
#   - Initialize a variable current_year = datetime.now()
#   - retirement_year, years_to_work = years_to_retire(current_age, retirement_age)
#   - print(f"It's {current_year}. You will retire in {retirement_year}.)
#   - print(f"You have only {years_to_work} years of work to go!)

# Code
from datetime import datetime

CURRENT_YEAR = datetime.now().year


def get_age(prompt):
    value = input(prompt)
    return int(value)


def years_to_retire(current_age, retirement_age):
    years_to_work = retirement_age - current_age
    retirement_year = CURRENT_YEAR + years_to_work

    return (retirement_year, years_to_work)


def main():
    current_age = get_age("==> What is your age? ")
    retirement_age = get_age("==> At what age would you like to retire? ")
    retirement_year, years_to_work = years_to_retire(
        current_age, retirement_age)

    print(f"It's {CURRENT_YEAR}. You will retire in {retirement_year}.")
    print(f"You have only {years_to_work} years of work to go!")


main()
