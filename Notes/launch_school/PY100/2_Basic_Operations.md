# Basic Operations

### Kinds of Types

- **Built-in**: they are part of Python.
- **Standard**: Available from modules that can be imported into your programs. (i.e math)
- **Non-Standard**: third party or own

## Arithmetic Operations

|Operator|Operation|
|---|---|
|`+`|[[#Addition]] |
|`-`|[[#Subtraction]] |
|`*`|[[#Multiplication]] |
|`/`|[[#Division]] |
|`//`|[[#Integer division]] |
|`%`|[[#Modulo]] |
|`**`|[[#Exponentiation (powers)]] |

### Addition

```python
print(38 + 4)      # 42
print(38.4 + 41.9) # 80.3

# mixing integers & floats
print(38 + 41.5)   # 79.5
```

### Subtraction

```python
print(38 - 4)      # 34
print(38.4 - 41.9) # -3.5

# mixing integers & floats
print(38 - 41.5)   # -3.5
```

### Multiplication

```python
print(38 * 4)      # 152
print(38.4 * 41.1) # 1578.24

# mixing integers & floats
print(38 * 41.5)   # 1577.0
```

### Division

```python
print(16 / 4)      # 4.0
print(16 / 2.5)    # 6.4
```

The result is always a [[1_Data_Types#Floats|float]]

### Integer division

```python
print(16 // 3)     # 5
print(16 // -3)    # -6
print(16 // 2.3)   # 6.0
print(-16 // 2.3)  # -7.0
```

[[Community_Explanations#^Simones-explanation-Integer-Division |Simone's Explanation on Integer Division]]

### Exponentiation (powers)

```python
print(16 ** 3)     # 4096
```

### Modulo

```python
# 15 // 3 is 5; what's the remainder?
print(15 % 3)   # 0
print(16 % 3)   # 1
print(17 % 3)   # 2
print(18 % 3)   # 0
```

- The result of the operation is called a modulus and not remainder.
- As long as both numbers have the same sign, modulo and remainder are equivalent operations.
- There is one situation where you can safely use `%` without worrying about negative numbers: when you only care about divisibility. If `x % y == 0`, then `x` is evenly divisible by `y`. It doesn't matter whether `x` or `y` is negative.

### Floating Point Imprecision

```python
print(0.1 + 0.2 == 0.3)       # False
```

- One way around the problem in Python is to use the `math.isclose` function:

```python
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

- You can also use the `decimal.Decimal` type to make precise computations:

```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')
# True
```

- always use strings with `decimal.Decimal`. You can use float values. However, you will lose the benefit of precise computation if you do.

## Equality Comparison

- Equality:

```python
print(42 == 42)       # True
print(42 == 43)       # False
print('foo' == 'foo') # True (works with strings)
print('FOO' == 'foo') # False (Case matters)
```

- Inequality:
```python
print(42 != 42)       # False
print(42 != 43)       # True
print('foo' != 'foo') # False (works with strings)
print('FOO' != 'foo') # True (Case matters)
```

- If `a` and `b` have different data types, `a == b` usually returns `False` while `a != b` returns `True`. However, numbers are an exception: all built-in and standard number types can be compared for equality without regard to their specific types. Thus, `1 == 1.0` is `True`.
- f `a` and `b` have the same data type, `a == b` almost always returns `True` if the two objects have the same value, while `a != b` returns `False`.
- When working with standard and non-standard types, all bets are off. While most non-builtin types obey the same rules, not all do. The only way to be sure is to study the documentation, look at the source code, or try to determine the behavior from tests.

## Ordered Comparisons

```python
print(42 < 41)           # False
print(42 < 42)           # False
print(42 <= 42)          # True
print(42 < 43)           # True

print('abc' < 'abcdef')  # True
print('abcdef' < 'abc')  # False
print('abc' < 'abc')     # False
print('abc' <= 'abc')    # True
print('abd' < 'abcdef')  # False

print('3' < '24')        # False
print('24' < '3')        # True
```

```python
print(42 > 41)           # True
print(42 > 42)           # False
print(42 >= 42)          # True
print(42 > 43)           # False

print('abc' > 'abcdef')  # False
print('abcdef' > 'abc')  # True
print('abc' > 'abc')     # False
print('abc' >= 'abc')    # True
print('abcdef' > 'abd')  # False

print('3' > '24')        # True
print('24' > '3')        # False
```

- Python compares strings character-by-character from left to right in both strings. The comparison stops as soon as Python reaches a decision.
- `'abcdef' > 'abc'`. In this example, the strings have unequal sizes. Furthermore, the longer string is identical up to the shorter string's length. Python returns `True` here; when it can no longer take characters from the shorter string, it concludes that the longer string has the greater value. Similar behaviors occur with the other ordered comparison operators.
- It's also worth noting that even numeric strings are compared character by character. Thus, `'3' > '24'` returns `True` since the character `3` is greater than the character `2`.
- In general, numeric characters in a string are less than alphabetic characters, and uppercase letter characters are less than lowercase letters.
- As with `==` and `!=`, many other types besides numbers and strings work with the ordered comparison operators. For instance, you can compare sets with these operators to determine if set a is a subset or superset of set b. You can also compare lists and tuples: like string comparisons, list and tuple comparison goes element by element to determine which object is less than or greater than the other:

```python
print({3, 1, 2} < {2, 4, 3, 1})         # True
print({3, 1, 2} > {2, 4, 3, 1})         # False
print({2, 4, 3, 1} > {3, 1, 2})         # True

print([1, 2, 3] < [1, 2, 3, 4])         # True
print([1, 4, 3] < [1, 3, 3])            # False
print([1, 3, 3] < [1, 4, 3])            # True
```


## String Concatenation

- Use + and * operators to join strings
```python
>>> 'foo' + 'bar'
'foobar'
```

```python
print('abc' * 3)              # 'abcabcabc'
print(3 * 'abc')              # 'abcabcabc'
```


## Coercion

- **Type coercion**: changing a data type, usually to perform an operation

#### Strings to Numbers

- The **int** and **float** functions coerce a string or another number to a number respectively:

```python
print(int('5'))               # 5
print(float('3.141592'))      # 3.141592
```

#### Numbers to Strings

- The `str` function coerce numbers to strings.
- `str` can convert most Python values to a valid string.

```python
print(str(5))                 # '5'
print(str(3.141592))          # '3.141592'
```

#### Implicit Coercion

- **Explicit coercion**: when using functions like `str`, `int`, `float` to coerce values from one type to another.
- **Implicit coercion**: when Python does it. When you use `print()` to print an object -- any object -- `print` will implicitly coerce it to a string before printing it:

```python
# (Unnecessary) Explicit coercion
print(str(3))           # 3
print(str(False))       # False
print(str([1, 2, 3]))   # [1, 2, 3]
print(str({4, 5, 6}))   # {4, 5, 6}

# Implicit coercion
print(3)                # 3
print(False)            # False
print([1, 2, 3])        # [1, 2, 3]
print({4, 5, 6})        # {4, 5, 6}
```

- Implicit coercion also occurs when mixing numbers of different types in an expression:

|Type A |Type B|Result type|
|---|---|---|
|int|float|float|
|int|Decimal|Decimal|
|int|Fraction|Fraction|
|float|Decimal|--error--|
|float|Fraction|Fraction|
|Decimal|Fraction|--error--|

- Python implicitly coerces `True` to the integer value 1 and `False` to 0:
```python
print(True + True + True)     # 3
print(True + 1 + 1.0)         # 3.0
print(False * 5000)           # 0
```

- One last implicit coercion is the truthiness coercion. Python can use any value, regardless of type, in a conditional expression in an `if` or `while` statement.

### Determining Types

- `type` function determines the type of an object:

```python
print(type(1))         # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type('abc'))     # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type(None))      # <class 'NoneType'>

foo = 42               # Variables work, too
print(type(foo))       # <class 'int'>
```

- If you just want the class name, you can access the `__name__` property from the result:

```python
print(type('abc').__name__)   # str
print(type(False).__name__)   # bool
print(type([]).__name__)      # list
```

- you can use `type` with the `is` operator:

```python
print(type('abc') is str)     # True
print(type('abc') is int)     # False
print(type(False) is bool)    # True
print(type([]) is list)       # True
print(type([]) is set)        # False
```

- you may want to consider using the `isinstance` function, which determines whether an object is an instance of a particular type. It takes inheritance into account:

```python
print(isinstance('abc', str))    # True
print(isinstance([], set))       # False

class A:
    pass

class B(A):
    pass

b = B()

print(type(b).__name__) # B
print(type(b) is B)     # True
print(type(b) is A)     # False (b's type is
                        # not A)
print(isinstance(b, B)) # True
print(isinstance(b, A)) # True (b is instance of A and B)
```


### String Representations

- `str` and `repr` return a string representation of any object.
- `str` output is intended for human readability.
- `repr` is lower-level and returns a string that can be use to create a new instance of the object.

```python
my_str = 'abc'
print(my_str)       # abc
print(str(my_str))  # abc (same as print(my_str))
print(repr(my_str)) # 'abc' (note the quotes)
```

### Collection and String Lengths

- All built-in collection types (strings, sequences, maps and sets) have lengths.
- The length of a string is the number of characters in the string
- The length of other collections is the number of elements in the collection.
- Function `len` determines the length:

```python
print(len('Launch School'))       # 13 (string)
print(len(range(5, 15)))          # 10 (range)
print(len(range(5, 15, 3)))       # 4 (range)
print(len(['a', 'b', 'c']))       # 3 (list)
print(len(('d', 'e', 'f', 'g')))  # 4 (tuple)
print(len({'foo': 42, 'bar': 7})) # 2 (dict)
print(len({'foo', 'bar', 'qux'})) # 3 (set)
```

### Indexing and Key Access

- Strings, ranges, lists and tuples support indexed access to its elements.
- Indices begin at 0 up to 1 less than the length of the string or collection.
- Index outside the range raise an `IndexError`:

```python
my_str = "abc"                # string
print(my_str[0])              # 'a'
print(my_str[1])              # 'b'
print(my_str[2])              # 'c'
print(my_str[3])
# IndexError: string index out of range

my_range = range(5, 8)         # range
print(my_range[0])             # 5
print(my_range[1])             # 6
print(my_range[2])             # 7
print(my_range[3])
# IndexError: range object index out of range

my_list = [4, 5, 6]           # list
print(my_list[0])             # 4
print(my_list[1])             # 5
print(my_list[2])             # 6
print(my_list[3])
# IndexError: list index out of range

my_list = [4, 5, 6]           # list
print(my_list[0])             # 4
print(my_list[1])             # 5
print(my_list[2])             # 6
print(my_list[3])
# IndexError: list index out of range
```

- Dictionaries use keys instead of indexes.
- Using a key that doesn't exist produces an error:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])           # 1
print(my_dict['b'])           # 2
print(my_dict['c'])           # 3
print(my_dict['d'])           # KeyError: 'd'
```

#### Using [] to update Elements

- Lists and Dictionaries let you use [] operator to replace collection elements.
- You cannot use [] to create new list elements, but you can with Dictionaries.
- Strings, ranges, tuples and frozen sets do not support using [] because they are immutable.
- Sets are mutable but do not support indexing.

```python
my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list)          # [1, 2, 6, 4]
my_list[4] = 10
# IndexError: list assignment index out of range

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

my_dict['pig'] = 'snorts'
print(my_dict)
# Pretty printed for clarity
# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts'
# }

my_dict['fish'] = 'glub glub'
print(my_dict)
# Pretty printed for clarity
# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts',
#     'fish': 'glub glub'
# }
```

### Expressions and Statements

- An **expression** combines values, variables, operators and calls to functions to produce a new object. Expressions must be evaluated to determine the expression's value. 
- You can think of an expression as something that has a value.
- Examples:
	- Literals: `5`, `'Karl'`, `3.141592`, `True`, `None`
	- Variable references: `foo` or `name` when these variables have been previously defined.
	- Arithmetic operations: `x + y` or `a * b - 5`.
	- Comparison operations: `'x' == 'x'` or `'x' < 'y'`.
	- String operations: `'x' + 'y'` or `'x' * 32`.
	- Function calls: `print('Hello')` or `len('Python')`.
	- Any valid combination of the above that evaluates to a single object.
- A **statement** is an instruction that tells Python to perform an action of some kind.
- Statements do not return values.
- Examples:
	- Assignment: like `x = 5`. This doesn't evaluate as a value; it assigns a value to a variable.
	- Control flow: such as `if`, `else`, `while`, `for`, and so on. These determine the flow of your program but don't evaluate as a value themselves.
	- Function and class definitions: using `def` or `class`.
	- Return statements: like `return x`, which tells a function to exit and return a value. `return` itself doesn't return a value; it informs the function what value it should return.
	- Import statements: such as `import math`.

Key differences:

- Expressions always return a value; statements do not.
- Expressions are often part of statements. For example, in the statement `y = x + 5`, `x + 5` is an expression.
- Statements often represent bigger chunks of functionality like loops or conditionals; expressions deal with determining values.

Stand-alone expressions that are both statements and expressions:

3 + 4            # Simple expression
print('Hello')   # Function call; returns None
my_list.sort()   # Method call; returns None