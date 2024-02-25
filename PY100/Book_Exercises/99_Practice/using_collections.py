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
new_list = list(org_tuple[1:-1])
new_list.reverse()
new_tuple = tuple(new_list)
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

# 4. Dictionaries
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# 4.1 Write some code to print Bark by accessing the element associated with the key Dog.
print(pets['Dog'])
print(pets.get('Dog'))

# 4.2 Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
print(pets.get('Lizard'))

# 4.3 Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.
print(pets.get('Lizard', '<silence>'))

# 5. Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']          # cannot because is not hashable as lists are mutable
{'a': 1, 'b': 2}    # dict are mutables as well so cannot be used
range(5)
{1, 4, 9, 16, 25}   # sets cannot be used as they are mutable
3
0.0
frozenset({1, 4, 9, 16, 25})
