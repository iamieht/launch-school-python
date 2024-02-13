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