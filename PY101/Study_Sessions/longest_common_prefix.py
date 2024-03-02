# Problem
"""
# Write a function to find the longest common prefix string amongst a list of strings.
# If there is no common prefix, return an empty string.
"""
# Algorithm
"""
- Define a function lcp with a list of strings as single parameter
- Sort the list by size in ascending order
- Determine the number of elements in the list
- Initialize a variable longest_common_prefix with an empty string
- loop over the first element of the list (shortest)
- compare each character of the first element with each character of the rest of the elements:
    - if they are equal, assign it to the variable longest_common_prefix
    - else: break and return longest_common_prefix
"""


def lcp(lst):
    longest_common_prefix = ''
    # check if lst is empty or has one element
    if len(lst) == 1:
        return lst[0]

    if not lst:
        return longest_common_prefix

    lst.sort(key=len)
    min_length = len(lst[0])

    for idx in range(min_length):
        for idx_elements in range(len(lst)):
            if lst[idx_elements][idx] != lst[0][idx]:
                return longest_common_prefix

        longest_common_prefix += lst[0][idx]

    return longest_common_prefix


# Examples
str1 = []
print(lcp(str1))
str2 = ["bob"]
print(lcp(str2))
str3 = ["flower", "flow", "flight"]
print(lcp(str3))
str4 = ["bob", "charles", "sally"]
print(lcp(str4))
