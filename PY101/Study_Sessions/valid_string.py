# Problem (P)
# Given a string s containing only '(', ')', '{', '}', '[' and ']', determine whether the string is valid.

# - Input:
#   - String of '(', ')', '{', '}', '[' and ']'
# - Output:
#   - Boolean: True if string is valid, False otherwise
# - Explicit Rules:
#   - opening brackets must be closed by the same type
#   - opening brackets must be closed in the proper order
#   - every closing bracket must have a corresponding opening bracket of the same type
# - Implicit Rules:

# Examples/Test Cases (E)
# is_valid("{}")             -> True
# is_valid("[]{}()")         -> True
# is_valid("[)")             -> False
# is_valid("{{{}}})(")       -> False
# is_valid(")(")             -> False
# is_valid("[{]}[]{{}}")     -> True

# Data Structures
#   - Dictionary: open/close pairs
#   - List

# Algorithm
# - Declare a function is_valid with a single parameter of type string
#   - Initialize a dictionary open_close with: {'(':')', '{':'}', '[':']'}
#   - Initialize am empty list stack
#   - loop over the string:
#       - if char in key of open_close dictionary -> append to the list
#       - else: if last element of the list is a value of a key in open_close, remove element from the list
#       - else return false

# Code
def is_valid(string):
    open_close = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in string:
        if char in open_close:
            stack.append(char)
        else:
            if stack == []:
                return False

            if char == open_close.get(stack[-1]):
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(is_valid("{}"))             # -> True
print(is_valid("[]{}()"))         # -> True
print(is_valid("[)"))             # -> False
print(is_valid("{{{}}})("))       # -> False
print(is_valid(")("))             # -> False
print(is_valid("[{]}[]{{}}"))     # -> False
