# 1. Write Python code to print the seventh number of range(0, 25, 3).
my_range = range(0, 25, 3)
print(my_range[6])

# 2. Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

# print('Launch School'[4:10])
my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start: start + 6])

# 3. Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).
# Solution 1
org_tuple = (1, 2, 3, 4, 5)
new_tuple = list(org_tuple[1:-1])
new_tuple.reverse()
new_tuple = tuple(new_tuple)
print(new_tuple)

# Solution 2
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       # (4, 3, 2)

# Solution 3
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)       # (4, 3, 2)

# Solution 4
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:0:-1]
print(result)
