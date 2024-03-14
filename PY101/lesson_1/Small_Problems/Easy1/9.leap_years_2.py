# Problem (P)
# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.


# - Input:
#   - integer greater than zero that represents a year
# - Output:
#   - True if year is leap / False otherwise
# - Explicit Rules:
#   - If the year is less than 1752 a leap year is divisible by 4
#   - If the year is divisible by 400, it is a leap year.
#   - If the year is divisible by 100 but not by 400, it is not a leap year.
#   - If the year is divisible by 4 but not by 100, it is a leap year.
#   - All other years are not leap years.
# - Implicit Rules:

# Examples/Test Cases (E)
# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Data Structures
# - Integer / Booleans

# Algorithm
#  - Declare a function is_leap_year with a single parameter year
#       - if the year is divisible by 400 return True
#       - elif year is divisible by 100 and not divisible by 400 return False
#       - elif year i divisble by 4 and not divisible by 100 return True
#       - else return False

# Code
def is_leap_year(year):
    if year <= 0:
        return "Year must be greater than zero"

    if year < 1752:
        return year % 4 == 0

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)
