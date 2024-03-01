# Problem
"""
# Write a function to find the longest common prefix string amongst a list of strings.
# If there is no common prefix, return an empty string.
"""
# Algorithm
"""
- Define a function lcp with a list of strings as single parameter
- Sort the list
- Determine the number of elements in the list
- Initialize a variable longest_common_prefix with an empty string
- loop over the elements of the list
- compare each character of each element:
    - if they are equal, assign it to the variable longest_common_prefix
    - else: break and return longest_common_prefix
"""

# Examples
"""
Example 1:
s = ["flower","flow","flight"]         ->  "fl"
Example 2:
["bob","charles","sally"]          ->   ""

["flower","flow","flight"]
["flow", "flight", "flower"]
3 elements
longest_common_prefix = ""

"""
