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

