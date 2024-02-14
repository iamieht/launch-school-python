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


