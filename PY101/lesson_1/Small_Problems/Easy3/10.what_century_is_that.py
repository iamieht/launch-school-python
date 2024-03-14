# Problem (P)
# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# - Input:
#   - a positive integer

# - Output:
#   - a string that represents the century

# - Explicit Rules:
#   - New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.
#   - The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

# - Implicit Rules:

# Examples/Test Cases (E)
# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True

# Data Structures

# Algorithm
# - Declare a helper function get_century with a single parameter year
#   - return year % 100
# - Declare a century function with a single parameter year
#   - Initialize a variable century = get_century(year)
#   - if century <


# Code
def get_century(year):
    if year <= 100:
        return 1
    elif year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1


def century_suffix(century):
    last_two = century % 100
    last_digit = century % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'

    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'


def century(year):
    century = get_century(year)
    suffix = century_suffix(century)
    return f"{century}{suffix}"


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
