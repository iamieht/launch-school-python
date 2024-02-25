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

# 6. What will the following code print?
print('abc-def'.isalpha())          # False
print('abc_def'.isalpha())          # False
print('abc def'.isalpha())          # False
print('abc def'.isalpha() and       # False
      'abc def'.isspace())
print('abc def'.isalpha() or        # False
      'abc def'.isspace())
print('abcdef'.isalpha())           # True
print('31415'.isdigit())            # True
print('-31415'.isdigit())           # False
print('31_415'.isdigit())           # False
print('3.1415'.isdigit())           # False
print(''.isspace())                 # False

# 7. Write Python code to replace all the : characters in the string below with +.
# Solution 1
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_split = info.split(':')
info = '+'.join(info_split)
print(info)

# Solution 2
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)

# 8. Explain why the code below prints different values on lines 94 and 95.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# Line 94: first extracts a slice from text ranging from index 21 through index 35. That returns the string 'for the fjords'.

# Line 95: does a search for the rightmost f between indexes 21 and 35. Since the f occurs at index 29, that's what the method returns.

# 9. Write some code to replace the value 6 in the following nested list with 606:
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][-2] = 606
print(stuff)
