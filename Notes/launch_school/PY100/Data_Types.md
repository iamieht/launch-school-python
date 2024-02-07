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
