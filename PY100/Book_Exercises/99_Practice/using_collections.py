# 1. Write Python code to print the seventh number of range(0, 25, 3).
my_range = range(0, 25, 3)
print(my_range[6])

# 2. Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

# print('Launch School'[4:10])
my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start: start + 6])
