# How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?
# It expects one argument: an iterable
# A TypeError will be raised
separator = '-'

# proper usage with one argument
names = ['Bob', 'Jo', 'Kim']
result = separator.join(names)
print(result)                           # Bob-Jo-Kim

# calling with no arguments
# result = separator.join()             # raises TypeError

# calling with multiple arguments
# result = separator.join('Bob', 'Jo')  # raises TypeError
