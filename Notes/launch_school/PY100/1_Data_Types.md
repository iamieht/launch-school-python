# Intro

* Data in any programming language has different data types.
* Data types determine what can and what cannot be done with the data.
* Everything you do in Python involves data and data types.
* Everything with a value in Python is an **object**. Each **object** has an associated **data type** or **type**, which has an associated **class**.
* **Objects** are instances of a **class**.

## Data Types in Python

**NOTE**: Python has no concept of "primitive" vs "non-primitive"... instead, types are either "simple" or "compound"

|Data Type|Class|Category|Kind|Mutable|
|---|---|---|---|---|
|integers|`int`|numerics|Primitive|No|
|floats|`float`|numerics|Primitive|No|
|boolean|`bool`|booleans|Primitive|No|
|strings|`str`|text sequences|Primitive|No|
||||||
|ranges|`range`|sequences|Non-primitive|No|
|tuples|`tuple`|sequences|Non-primitive|No|
|lists|`list`|sequences|Non-primitive|**Yes**|
|dictionaries|`dict`|maps|Non-primitive|**Yes**|
|sets|`set`|sets|Non-primitive|**Yes**|
|frozen sets|`frozenset`|sets|Non-primitive|No|
||||||
|functions|`function`|functions|_--?--_|No|
|`NoneType`|`NoneType`|nulls|_--?--_|No|


What are primitive types?

* The most fundamental data types

What are non-primitive types?

* Also called **collection** types, they collect multiple items in a single object.

What is the definition of mutable/immutable?

* Mutable types are types whose objects can be changed after they are created.
* Immutable types cannot be changed after they are created.

## Literals

* Are used to represent most data type values.
* A literal is any syntactic notation used to represent an object in source code.
* They are used to represent most data types.
* Examples:

```python
'Hello, world!'   # str literal
3.141592          # float literal
True              # bool literal
{'a': 1, 'b': 2}  # dict literal
[1, 2, 3]         # list literal
(4, 5, 6)         # tuple literal
{7, 8, 9}         # set literal
```

* Not all objects have literal forms and we need to use the type constructor to create these objects:

``` python
range(10)         # Range of numbers: 0-9
range(1, 11)      # Range of numbers: 1-10
set()             # Empty set
frozenset([1, 2]) # Frozen set of values: 1 and 2
```

## Numeric Values

* Represent numbers.

### Integers

- Data Type: *int* 
- Represent integers
- Can't use commas or periods for grouping. Underscores can be used.
- No pre-defined limit size, only limited by memory.
- Examples:

```python
1
2
-3
234891234
131_587_465_014_410_491
```

### Floats

- Data Type: *float*
- Represent floating point numbers (real numbers)
- Can't use commas or periods for grouping. Underscores can be used.
- Examples:

```python
1.0
1.4142
-3.14159
42348.912346
131_587_465.014_410_491
```

### Boolean Values

- Data Type: *bool*
- Represent binary states such as True or False.
- Sometimes act like numeric values (shouldn't be used for that purpose):

```python
>>> 3 + True
4
>>> True == 1
True
```

### Text Sequences

- are strings of characters:

```python
'Hello!'
"He's pining for the fjords!"
'1969-07-20'
f'{greeting}! My name is {my_name}'
r'\w+\d+'
```

- A **string** is a text sequence of Unicode characters.
- **string literals** can be written with single, double or triple quotes:

```python
'Hi there'                      # Single quotes
"Monty Python's Flying Circus"  # Double quotes

# Triple single quotes
'''King Arthur: "What is your name?"
Black Knight: "None shall pass!"
King Arthur: "What is your quest?"
Black Knight: "I have no quarrel with you,
               but I must cross this bridge."
'''

# Triple double quotes
"""Man: "Is this the right room for an argument?"
Other Man: "I've told you once."
Man: "No you haven't!"
"""
```

- You can escape characters with (" \\ ")
- The backslash or escape character tells the computer that the next character isn't syntactic but part of the string.
- You can access the individual characters in a string with the [] indexing syntax.

```python
print("""My nickname is "Wolfy". What's yours?""")
print('My nickname is "Wolfy". What\'s yours?')
print("My nickname is \"Wolfy\". What's yours?")
```

- String literals with prefix **r** are **raw string literals**. They don't recognize escapes.
- String literals with prefix **f** are **f-strings**(formatted string literals). They enable an operation called **string interpolation**:
```python
f'Blah {expression} blah.'
```
* The characters in a text sequence are not objects.

### Functions

- Are reusable code designed to perform an action.
- Functions have a data type `functions`

### None

- Represent the absence of a value. Also represent missing, unset, unavailable data and error indication.
- Data type: `NoneType`
- Literal: `None`

### Sequences

- Represent an ordered collection of objects. The objects can be access using a numeric index.

#### Lists and Tuples

- Both may contain any objects.
- Lists literal: [value1, value2, value3, ...]
- Tuples literal: (value1, value2, value3, ...)
- Objects inside are called elements
- The order of the elements is significant.
- The objects can be accessed with the [0, lenofSequence -1] indexing syntax.
- Use indexing syntax to reassign specific list elements.
- Lists are mutables
- Tuples are immutable
- Python perform optimizations on Tuples: reduce storage and improve performance.
- Something special about Tuples with one element:

```python
my_tuple = (1)
print(type(my_tuple))        # <class 'int'>

my_tuple = (1,)
print(type(my_tuple))        # <class 'tuple'>
```

#### Ranges

- A **range** is a sequence of integers between two endpoints.
- Mostly used for iteration.
- Range doesn't produce the integers before a program ask for it. This optimizes memory. They are lazy sequences.
- Examples

```python
>>> tuple(range(5))
(0, 1, 2, 3, 4)

>>> tuple(range(5, 10))
(5, 6, 7, 8, 9)

>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]

>>> list(range(0, -5, -1))
[0, -1, -2, -3, -4]

>>> my_range = range(5, 10)
>>> my_range[3]               # 8
```

### Maps

- Represent an unordered collection of objects stored as key-value pairs.
- Keys are usually represented by strings and are a unique identifier for a specific object in the map.
- The value is the object associated with the Key.
- **dictionary (dict)** is the most common Map in Python
- Literal: **dict** {}
- Elements are separated by commas. {key:value,...}
- You can access objects in a dict with the [] key access syntax
- You can use almost any immutable object as a key in a dict; it doesn't have to be a string
- The only significant requirement for keys is that they are hashable. immutable types are almost always hashable, while mutable types are almost always non-hashable.
- Example:

```python
>>> my_dict = {
...     'dog': 'barks',
...     'cat': 'meows',
...     'pig': 'oinks',
... }
{'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}

>>> my_dict = {
...     'dog': 'barks',
...     'cat': 'meows',
...     'pig': 'oinks'
... }
...
>>> my_dict['cat']
'meows'

>>> my_dict['bird']
KeyError: 'bird'
```

### Sets

- Represent an unordered collection of unique immutable (and hashable) objects.
- The objects are called the members of the set.
- Literal: {value1, value2, value3,}
- Empty sets must be created with the set constructor.
- There are two set types: ordinary sets (class **set**) and frozen sets (class **frozenset**)
- Frozen sets are immutable and lack literal syntax. The function **frozenset** must be used to create one.
- You can use almost any immutable value as a set member.The only significant requirement is that the objects must be hashable.
- Examples:

```python
>>> d1 = {}         # Empty dict
>>> print(type(d1))
<class 'dict'>

>>> s1 = set()      # Empty set
>>> print(s1)
set()

# Create a set from a literal
>>> s2 = {2, 3, 5, 7, 11, 13}
>>> print(s2)
{2, 3, 5, 7, 11, 13}

# Create a set from a string
>>> s3 = set("hello there!")
{'t', 'o', 'e', 'l', ' ', 'h', '!', 'r'}

>>> s5 = frozenset([1, 2, 3])
>>> print(s5)
frozenset({1, 2, 3})

>>> s6 = frozenset((1, 2, 3))
>>> print(s6)
frozenset({1, 2, 3})

>>> s7 = frozenset({1, 2, 3})
>>> print(s7)
frozenset({1, 2, 3})

>>> s8 = frozenset(range(1, 4))
>>> print(s8)
frozenset({1, 2, 3})
```

