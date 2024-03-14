# Problem (P)
# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

# - Input:
#   - a String
# - Output:
#   - a String
# - Explicit Rules:
#   - All consecutive duplicated characters are collapsed into a single char
# - Implicit Rules:

# Examples/Test Cases (E)
# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# Data Structures

# Algorithm
# - Declare a function crunch that takes a single argument of type string
#   - Initialize a variable result = string[0]
#   - Iterate over original string
#       - if char == string[-1]: continue
#       - else: result.append(char)

# Code
def crunch(string):
    if len(string) > 0:
        result = string[0]
        for char in string:
            if char == result[-1]:
                continue
            else:
                result += char
    else:
        return string

    return result


print(crunch('') == '')
print(crunch('a') == 'a')
print(crunch('abc') == 'abc')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
