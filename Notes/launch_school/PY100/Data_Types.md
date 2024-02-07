# Intro

* Data in any programming language has different data types.
* Data types determined what and what not can be done with the data.
* Everything with a value in Python is an **object**. Each **object** has an associated **data type** or **type**, which has an associated **class**.
* **Objects** are instances of a **class**.

## Data Types in Python

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