# Intro to Collections

## Collection Types

- Collections are objects that contain zero or more **member objects**, often called **elements**.
- There are 3 main categories of collection: sequences, maps, and sets.

## What are Sequences?

- Sequences are types that maintain an **ordered** collection of objects (also: elements or values) that can be **indexed** by whole numbers.
- Ordered collections are collections organized in some sequence: a first element, a second element, a third element, and so on. Indexed sequences associate every object member with a whole number (0, 1, 2, etc.) that can be used to access or modify that object. 

```python
letters = ['a', 'b', 'c']
print(letters[0])         # a (first element)
print(letters[1])         # b (second element)
print(letters[2])         # c (third element)
```

- Lists and tuples are **heterogeneous**; they may contain different kinds of objects, including other sequences.
- Ranges are **homogenous**; they always contain integers.
- Strings are a form of sequence called a **text sequence**. They differ from ordinary sequences in two main ways:
    - Strings are homogenous; all characters in a string are, um, characters.
    - Characters are not a distinct kind of object; they are merely strings of length 1.
    - A string's individual characters are not separate strings until you reference a character.
    - Strings are not actual collections since the characters inside the string aren't objects.


## What are Sets?

- Sets are types that maintain an **unordered** collection of unique objects (also called **elements** or **members**).
- Sets cannot be indexed.
- **Unordered** means no well-defined order exists for the objects in a set.
- There are two types of set types: sets (mutable) and frozen sets (immutable).
- Both are **heterogeneous**

```python
letters = {'a', 'b', 'c', 'b', 'a'}
print(letters)
# {'a', 'c', 'b'} (order may differ)

letters.add('c')
print(letters)
# {'a', 'c', 'b'} (order may differ)
```

## What are Maps?

- Maps are types that maintain an **unordered** collection of **key/value** pairs (also called elements or members).
- Maps are accessed by their keys.
- Dictionary or `dict` type.
- Dicts are mutable.
- The keys in a dict must be unique.
- Keys must be "hashable" values (immutable).
- The values in each key/value pair may be any object.

```python
d = {'a': 1, (1, 3): 3, 1: 'x'}
print(d)         # {'a': 1, (1, 3): 3, 1: 'x'}
print(d['a'])    # 1
print(d[(1, 3)]) # 3
print(d[1])      # 'x'

d['a'] = 'A'
print(d)        # {'a': 'A', (1, 3): 3, 1: 'x'}
```

## Sequence Constructors

- You can also use special functions called **constructors** to create new objects. In fact, sometimes you can't use literals; you must use constructors to create ranges, frozen sets, and empty sets.

### String Constructor

- `str()` and `str(Python object)`

```python
str()            # returns '' (empty string)
str('abc')       # returns 'abc'
str(42)          # returns '42'
str(3.141592)    # returns '3.141592'
str(False)       # returns 'False'
str(None)        # returns 'None'
str(range(3, 7)) # returns 'range(3, 7)'
str([1, 2, 3])   # returns '[1, 2, 3]'

class Person:
    def __init__(self, name):
        self.name = name

str(Person('May'))
# returns '<\_\_main\_\_.Person object at 0x...>'
```

### Range Constructor

It comes in 3 forms:

- `range(start, stop, step)`
    - This constructor generates a sequence of integers between start and stop - 1 with an increment of step between each consecutive integer.
    - You can use a negative step to generate a sequence in reverse order. In this case, the range ends at stop + 1. 

```python
r = range(5, 12, 2)
print(list(r))            # [5, 7, 9, 11]

r = range(12, 8, -1)
print(list(r))            # [12, 11, 10, 9]

r = range(12, 5, -2)
print(list(r))            # [12, 10, 8, 6]
```

- `range(start, stop)`

    - When you omit the step argument, Python uses a default value of 1. Hence, range(start, stop) is identical to range(start, stop, 1).

- `range(stop)`

    - When you omit the start argument, Python uses a default value of 0 for start. Hence, range(stop) is identical to range(0, stop, 1).

- Ranges are **lazy sequences**: they don't create any element values until your program needs them.

### The List, Tuple, Set, and Frozen Set Constructors

Lists, tuples, sets, and frozen sets share two common constructor forms:

- `list()` or `list(iterable)`
- `tuple()` or `tuple(iterable)`
- `set()` or `set(iterable)`
- `frozenset()` or `frozenset(iterable)`

- The constructors with no arguments create an empty list, tuple, set, or frozen set, as appropriate: a sequence or set with no members.
- The constructors that take an iterable argument expect an object that Python can iterate: an iterable. From the built-in types, the iterables include all sequences, text strings, sets, and maps.

```python
my_str = 'Python'

my_list = list(my_str)
print(my_list)  # ['P', 'y', 't', 'h', 'o', 'n']

my_tuple = tuple(my_list)
print(my_tuple) # ('P', 'y', 't', 'h', 'o', 'n')

my_set = set(my_tuple)
print(my_set)   # {'t', 'o', 'n', 'h', 'P', 'y'}
```











Questions:

1. In the following example:
letters = 'abθde'
char = letters[2]
print(char is letters[2])     # False
They are explaining the reason why char is letters[2] is False with this sentence: "They have the same value but are distinct objects."
My question is: they are different objects, because letters[2] always return a copy of the character? So Python basically creates in memory a new PyObject that contains the value in letters[2]? So char has a different object than letters[2]
Makes sense?

2. If we avoid interning, then these two code snippets will print `True`:

```python
letters = ['a', 'b', 'θ', 'd', 'e']
char = letters[2]
print(char is letters[2])     # True
```

```python
letters = 'abθde'
char = letters[2]
print(char is letters[2])     # False
```

How switching to a non-ASCII character, we could show that characters in a string aren't objects.?