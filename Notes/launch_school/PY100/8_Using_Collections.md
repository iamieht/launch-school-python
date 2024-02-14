# Using Collections

## Indexing

- Is the process of using a whole number to access and alter an element of a sequence.
- All sequences, including string, support indexing.
- zero-based numbering is used
- The last index of a sequence is len(seq) - 1
- Negative indexes are used as well

```python
seq = ('a', 'b', 'c')
print(seq[0])  # a (1st element)
print(seq[1])  # b (2nd element)
print(seq[2])  # c (3rd element)
print(seq[3])  # IndexError: tuple index out of range

seq = ('a', 'b', 'c')
print(seq[-1])  # c (last element)
print(seq[-2])  # b (next to last element)
print(seq[-3])  # a (2nd to last element)
```

## Slicing

- **Slicing** augmentation: can extract or modify any number of consecutive elements simultaneously.
- Syntax: `seq[start:stop:step]`
- Negative indexes are also supported
- You get an empty slice when the start and stop values are the same.
- Slicing performs a shallow copy if the sequence contains any collections (lists or tuples).

```python
seq = 'abcdefghi'
print(seq[3:7])       # defg
print(seq[-6:-2])     # defg
print(seq[2:8:2])     # ceg
print(repr(seq[3:3])) # ''
print(seq[:])         # abcdefghi => returns a duplicated sequence
print(seq[::-1])      # ihgfedcba => returns a reverse copy of a sequence

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[3:7])       # [4, 5, 6, 7]
print(seq[-6:-2])     # [5, 6, 7, 8]
print(seq[2:8:2])     # [3, 5, 7]
print(seq[3:3])       # []
print(seq[:])         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => returns a duplicated sequence
print(seq[::-1])      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] returns a reverse copy of a sequence

seq = [[1, 2], [3, 4]]
seq_dup = seq[:]
print(seq[0] is seq_dup[0])   # True
```

## Key-Based Access

- Maps use key-based syntax.
- Any hashable object can be used as a key
- When using a non-existent key we get the error `KeyError:`
- `dict.get` method returns the value associated with a given key if they exists, otherwise produces a default return value (usually `None`, but other values can be specified)
- We can assign a new key to the dictionary: `my_dict['key'] = 'value'`
- We cannot use mutable keys.

```python
my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

print(my_dict['a'])                # abc
print(my_dict[37])                 # def
print(my_dict[(5, 6, 7)])          # ghi
print(my_dict[frozenset([1, 2])])  # jkl
print(my_dict['nothing'])     # KeyError: 'nothing'

my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

print(my_dict.get('a'))                 # abc
print(my_dict.get('nothing'))           # None
print(my_dict.get('nothing', 'N/A'))    # N/A
print(my_dict.get('nothing', 100))      # 100
```

## Common Collection Operations

### Non-Mutating Operations for Collections

#### Collection Membership

- The `in` operator determines whether the object to the operator's left is in the iterable collection on the right. Returns `True` if the item is in the collection, `False` otherwise.
- The `not in` operator is the inverse of `in`.
- With sequences and sets, both opertors compare the object for equality against each collection element.
- For maps, it checks whether the item is a key in the dictionary.
- For strings, it determines whether the right string contains the left string.

```python
seq = [4, 'abcdef', (True, False, None)]
print(4 in seq)                         # True
print(4 not in seq)                     # False
print('abcdef' in seq)                  # True
print('abcdef' not in seq)              # False
print('cde' in seq[1])                  # True
print('cde' not in seq[1])              # False
print('acde' in seq[1])                 # False
print('acde' not in seq[1])             # True
print((True, False, None) in seq)       # True
print((True, False, None) not in seq)   # False
print(3.14 in seq)                      # False
print(3.15 not in seq)                  # True
```

#### Minimun and Maximun Members

- `min` and `max` return the minimun and maximum members in an iterable collection.
- Any pair of the collection's elements must be comparable with the `<` and `>` operators.
- In most cases, you can't use `min` and `max` with heterogeneous collections, but it's possible in some situations (int and float)
- You can use them with multiple arguments instead of an iterable.

```python
my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '25', '-36', '-1'}

print(min(my_set1), max(my_set1))     # -63 25
print(min(my_set2), max(my_set2))     # -1 4
```
```python
>>> my_set = {1, 4, '-9', 16, '25', -36, -63, -1}
>>> min(my_set)
TypeError: '<' not supported between instances of
'str' and 'int'

>>> max(my_set)
TypeError: '>' not supported between instances of
'str' and 'int'
```
```python
my_set = {1, 3.14, -2.71}
print(min(my_set), max(my_set))      # -2.71 3.14
```

#### Summation

- `sum` function is used with iterable collections which elements are numeric values. It returns the sum of all the collection's numbers.
- `sum` cannot be used with strings

```python
numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(sum(numbers))                       # 88
```

#### Locating Indices and Counting

- `seq.index`method returns the index of the first element in the sequence that matches a given object. It raises a `ValueError` exception if the object is not found.
- Also works with strings. It searches for the first matching substring of a string.

```python
names = ['Karl', 'Grace', 'Clare', 'Victor',
         'Antonina', 'Allison', 'Trevor']
print(names.index('Clare'))   # 2
print(names.index('Trevor'))  # 6
print(names.index('Chris'))
# ValueError: 'Chris' is not in list

names = 'Karl Grace Clare Victor Antonina Trevor'
print(names.index('Clare'))   # 11
print(names.index('Trevor'))  # 33
print(names.index('Chris'))
# ValueError: substring not found
```

- `seq.count` returns the number of times a value occurs in the sequence.

```python
numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
print(numbers.count(1))       # 2
print(numbers.count(3))       # 1
print(numbers.count(4))       # 4
print(numbers.count(7))       # 0
```

#### Merging Collections

- `zip` function merges the members/elements of multiple iterables into a single list of tuples.
- Makes it easy to iterate through many collections simultaneously.
- Each tuple in the list contains objects from each iterable (tuple1 contains all 0-indexed elements, tuple2 contains all 1-indexed elements, tupleN all Nth-indexed elements).
- `zip's` result is a lazy sequence like `range`

```python
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))
# Pretty printed for clarity
# [
#   (1, 'Kim', None),
#   (2, 'Leslie', True),
#   (3, 'Bertie', False)
# ]
```

- `zip`'s collection arguments don't have to be of the same length. To enforce it, add `strict=True` to raise an exception in that case.

```python
zipped_iterables = zip(iterable1, iterable2, strict=True)
```

- If lengths are different and no `strict=True` is provided: `zip` stops after exhausting the shortest iterable, meaning the number of tuples in the generated list will be determined by the length of the shortest iterable

```python
result = zip(range(5, 10),    # length is 5
             range(1, 3),     # length is 2 (shortest)
             range(3, 7))     # length is 4
print(list(result)) # [(5, 1, 3), (6, 2, 4)]
```
- `zip` returns an iterator, meaning can only be consumed once.

```python
result = zip(range(5, 10),    # length is 5
             range(1, 3),     # length is 2 (shortest)
             range(3, 7))     # length is 4
print(list(result)) # [(5, 1, 3), (6, 2, 4)]
print(list(result)) # []
```

#### Operations on Dictionaries

- `dict.keys`: to get a list of keys
- `dict.values`: to get a list of values
- `dict.items`: to get a list of key/value pairs

```python
people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

print(people_phones.keys())
# dict_keys(['Chris', 'Pete', 'Clare'])

print(people_phones.values())
# Pretty printed for clarity
# dict_values([
#     '111-2222',
#     '333-4444',
#     '555-6666'
# ])

print(people_phones.items())
# Pretty printed for clarity
# dict_items([
#     ('Chris', '111-2222'),
#     ('Pete',  '333-4444'),
#     ('Clare', '555-6666')
# ])
```

- The lists returned are not ordinary lists, they are **dictionary view objects** that are tied to the dictionary.

```python
people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

keys = people_phones.keys()
values= people_phones.values()

print(keys)    # dict_keys(['Chris', 'Pete', 'Clare'])
print(values)
# dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)    # dict_keys(['Pete', 'Clare', 'Max'])
print(values)
# dict_values(['345-6789', '555-6666', '123-4567'])
```

### Operations for Mutable Sequences

#### Adding Elements to Mutable Sequences

- `seq.append`: appends a single object to the end of a mutable sequence

```python
numbers = [1, 2]

numbers.append(10)      # Append the number 10
print(numbers)          # [1, 2, 10]
```

- `seq.insert`: inserts an object before the element at a given index. If the index is equal or greater than the length of the sequence, the object will be appended. If the index is negative, it is count from the end of the sequence. Syntax: `seq.insert[before_index:element]`

```python
numbers = [1, 2]

numbers.insert(0, 8)    # Insert 8 before numbers[0]
print(numbers)          # [8, 1, 2]
numbers.insert(2, 6)    # Insert 6 before numbers[2]
print(numbers)          # [8, 1, 6, 2]
numbers.insert(100, 55) # Insert 55 before numbers[100]
print(numbers)          # [8, 1, 6, 2, 55]
numbers.insert(-3, 33)  # Insert 33 before the 3rd element
                        # from the end.
print(numbers)          # [8, 1, 33, 6, 2, 55]
```

- `seq.extend`: appends the content of an iterable sequence to the calling iterable sequence.

```python
numbers = [1, 2]

numbers.extend([7, 8])  # Append 7 and 8 to numbers
print(numbers)          # [1, 2, 7, 8]
```

#### Removing Elements from Mutable Sequences

- `seq.remove`: searches a sequence for a specific object and removes it. It raises `ValueError` is object doesn't exist.

```python
my_list = [2, 4, 6, 8, 10]

my_list.remove(8)
print(my_list)            # [2, 4, 6, 10]

my_list.remove(8)
# ValueError: list.remove(x): x not in list
```

- `seq.pop`: removes and returns an indexed element from a mutable sequence. If no index is given, it removes the last element in the sequence. Only works with mutable indexed sequences.

```python
my_list = [2, 4, 6, 8, 10]

print(my_list.pop(1))         # 4
print(my_list)                # [2, 6, 8, 10]

print(my_list.pop())          # 10
print(my_list)                # [2, 6, 8]

print(my_list.pop(4))
# IndexError: pop index out of range
```

- `seq.clear`: removes all elements from a sequence.

```python
my_list = [2, 4, 6, 8, 10]

my_list.clear()
print(my_list)                # []
```

### Sorting Collections

- `sorted()` function: creates and returns a sorted list from any iterable collection, mutable or immutable. Original collection is unchanged.

- `list.sort()` method: sorts and mutates the list. More perfomant than sorted function as it does an in-place sort (doesn't have to build a completely new list).

- Both do an ascending sort. You can reverse the sort with the keyword argument `reverse=True`.

```python
names = ('Grace', 'Clare', 'Allison', 'Trevor')
print(sorted(names))
# ['Allison', 'Clare', 'Grace', 'Trevor']

print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')

names = list(names)
print(names)
# ['Grace', 'Clare', 'Allison', 'Trevor']

print(names.sort())   # None
print(names)
# ['Allison', 'Clare', 'Grace', 'Trevor']

names = ['Grace', 'Clare', 'Allison', 'Trevor']
print(sorted(names, reverse=True))
# ['Trevor', 'Grace', 'Clare', 'Allison']

names.sort(reverse=True)
print(names) # ['Trevor', 'Grace', 'Clare', 'Allison']
```

- You can also pass a `key=func` keyword argument to tell sort or sorted how to determine what values it should sort. For instance, if you want to perform a case-insensitive sort on a list of strings, you can specify `key=str.lower`

```python
words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']

print(sorted(words, key=str.lower))
# ['123', 'abc', 'DEF', 'xyz']
```

### Reversing Sequences and Dictionaries

- `reverse()` function: reverses the order of elements in a sequence or dictionary. The returned value is a lazy sequence that contains the elements in the sequence or the keys from a dictionary.

- `list.reverse()` method: reverses and mutates the list

```python
names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)
print(reversed_names)
# <reversed object at 0x102848e50>
print(tuple(reversed(names))) # Requires extra memory
# ('Trevor', 'Allison', 'Clare', 'Grace')
print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')

names = list(names)
print(names.reverse())   # None
print(names)
# ['Trevor', 'Allison', 'Clare', 'Grace']

my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
reversed_dict = reversed(my_dict)
print(reversed_dict)
# <dict_reversekeyiterator object at 0x100d19f80>

print(list(reversed_dict))    # Requires extra memory
# ['jkl', 'pqr', 'xyz', 'abc']
```

```python
names = ('Grace', 'Clare', 'Allison', 'Trevor')
for name in reversed(names):
    print(name)
# Trevor
# Allison
# Clare
# Grace
```

## String Operations

### Letter Case

- `str.lower()`: returns a copy of the string with all the cased characters converted to lowercase.

- `str.upper()`: returns a copy of the string with all the cased characters converted to uppercase.

- `str.capitalize()`: returns a copy of the string with the first character capitalized and the rest converted to lowercase

```python
print("what's up?".capitalize())        # What's up?
print('456ABC'.capitalize())            # 456abc
```

- `str.swapcase()`: returns a copy of the string with every uppercase letter converted to lowercase, and viceversa.

```python
print("What's up?".swapcase())          # wHAT'S UP?
print('456ABC'.swapcase())              # 456abc
print('456ABC'.swapcase().swapcase())   # 456ABC
```

- Note that there are situations where str.swapcase().swapcase() does not return the original value of str. For instance:

```python
print('Straße'.swapcase().swapcase())   # Strasse
```

### Character Classification

Methods to test what sort of characters are present in a string.

- `str.isalpha()`: returns `True` is all characters of `str` are alphabetic, `False` otherwise or if string is empty.

```python
'Hello'.isalpha()      # True
'Good-bye'.isalpha()   # False: `-` is not a letter
'Four score'.isalpha() # False: space is not a letter
''.isalpha()           # False
```

- `str.isdigit()`: returns `True` if all characters of string are digits,`False` otherwise or if string is empty.

```python
'12340'.isdigit()      # True
'123.4'.isdigit()      # False: `.` is not a digit
'-1234'.isdigit()      # False: `-` is not a digit
''.isdigit()           # False
```

- `str.isalnum()`: returns `True` if string is composed entirely of letters and/or digits, `False` otherwise or if string is empty.

- `str.islower()`: returns `True` if all cased characters in string are lowercase letters, `False` otherwise of if string doesn't contain case characters.

- `str.isupper()`: returns `True` if all cased characters in string are uppercase, `False` otherwise of if the string contains no case characters.

- `str.isspace()`: returns `True` if all characters in string are **whitespace characters**, `False` otherwise or if string is empty. The whitespace characters include [ordinary spaces (` `), tabs (`\t`), newlines (`\n`), carriage returns (`\r`), vartical tabs (`\v`) and form feeds (`\f`), as well as some foreign characters that count as whitespace]


### Stripping Characters

- `str.strip()` method: returns a copy of string with leading and trailing whitespace characters removed.

```python
text = ' \t  abc def    \n\r'
print(repr(text))             # ' \t  abc def    \n\r'
print(repr(text.strip()))     # 'abc def'
```

- `str.strip()`: can also remove characters by providing a string argument. The characters inside this string are the ones you want removed.

```python
text = ' \t  abc def    \n\r'
print(repr(text.strip('abc'))) # ' \t  abc def    \n\r'

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))         # baacccabxyzabccb
print(text.strip('a'))         # baacccabxyzabccb
print(text.strip('ab'))        # cccabxyzabcc
print(text.strip('ba'))        # cccabxyzabcc
print(text.strip('abc'))       # xyz
print(text.strip('bc'))        # aaabaacccabxyzabccba

print(repr(text.strip('abcxyz'))) # ''
```
- `str.strip` removes individual characters, not substrings. That is, the order of the characters in the argument doesn't matter.

- `str.lstrip` method: is identical to `str.strip` except it only removes leading characters (the leftmost)

- `str.rstrip` method: removes trailing characters (the rightmost)

```python
text = 'aaabaacccabxyzabccba'

print(text.lstrip('a'))       # baacccabxyzabccba
print(text.rstrip('a'))       # aaabaacccabxyzabccb

print(text.lstrip('ab'))      # cccabxyzabccba
print(text.rstrip('ab'))      # aaabaacccabxyzabcc

print(text.lstrip('ba'))      # cccabxyzabccba
print(text.rstrip('ba'))      # aaabaacccabxyzabcc

print(text.lstrip('abc'))     # xyzabccba
print(text.rstrip('abc'))     # aaabaacccabxyz
```

### Splitting and Joining Strings

- `str.split()` method: returns a list of the words in the string. By default the separator is a whitespace character. You can tell Python what character string should act as a delimiter.

```python
text = '  Four     score and   seven years ago.   '
print(text.split())
# ['Four', 'score', 'and', 'seven', 'years', 'ago.']

print('no-spaces'.split()) # ['no-spaces']
```

```python
text = ',Four,score,and,,,seven,years,ago,'
print(text.split(','))
# Pretty printed for clarity
# [
#     '',
#     'Four',
#     'score',
#     'and',
#     '',
#     '',
#     'seven',
#     'years',
#     'ago',
#     ''
# ]
```
- Specifying a delimiter changes the splitting behavior. Instead of looking for runs of whitespace, it splits the string at every occurrence of the delimiter.

```python
text = '  Four     score and   seven years ago.   '
print(text.split(' '))
# Partially pretty printed for clarity
# ['', '', 'Four', '', '', '', '', 'score', 'and',
#  '', '', 'seven', 'years', 'ago.', '', '', '']
```

- `split` also recognizes multi-character delimiters. Thety must match exactly.

```python
text = 'Four<>score<:>and<>seven<>years<>ago'
print(text.split('<>'))
# ['Four', 'score<:>and', 'seven', 'years', 'ago']
```

- `str.splitlines` method: returns a list of lines from the string. It looks for line-ending characters like `\n`, `\r`, `\n\r` and other boundaries.

```python
text = '''
You were lucky to have a room. We used to have to
live in a corridor.
Oh we used to dream of livin' in a corridor!
Woulda' been a palace to us. We used to live in an
old water tank on a rubbish tip. We got woken up
every morning by having a load of rotting fish
dumped all over us.
'''

print(text.strip().splitlines())
# Pretty printed for clarity
[
    "You were lucky to have a room. We used to have to",
    "live in a corridor.",
    "Oh we used to dream of livin' in a corridor!",
    "Woulda' been a palace to us. We used to live in an",
    "old water tank on a rubbish tip. We got woken up",
    "every morning by having a load of rotting fish",
    "dumped all over us."
]
```

- `str.join` method: concatenates all strings in an iterable collection into a single long string.

```python
words = ['You', 'were', 'lucky']
print(''.join(words))         # Youwerelucky
print(' '.join(words))        # You were lucky
print(','.join(words))        # You,were,lucky
print('\n  '.join(words))
# You
#   were
#   lucky
```

### Finding Substrings

- `str.find()`: searches through string looking for the first occurrence of the argument and returns the index of the first matching substring, otherwise returns `-1`.

- `str.rfind()`: does the same but it searches from right to left (reverse).

```python
school = 'launch school'

print(school.find(' '))       # 6
print(school.find('l'))       # 0
print(school.find('h'))       # 5
print(school.find('hoo'))     # 9
print(school.find('x'))       # -1
print(school.find('N'))       # -1

print(school.rfind(' '))      # 6
print(school.rfind('l'))      # 12
print(school.rfind('h'))      # 9
print(school.rfind('hoo'))    # 9
print(school.rfind('oh'))     # -1
print(school.rfind('N'))      # -1
```

- You can also search slices by adding start and end arguments to the invocation. `str.find('substr', start:stop)`

```python
text = 'abc abc def abc'

print(text.find(' ', 4))         # 7
print(text.find(' ', 8))         # 11

print(text.find('c', 0, 2))      # -1
print(text.rfind('c', 3, 10))    # 6
```






