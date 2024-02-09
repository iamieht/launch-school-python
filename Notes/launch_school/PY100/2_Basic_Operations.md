# Basic Operations

### Kinds of Types

- **Built-in**: they are part of Python.
- **Standard**: Available from modules that can be imported into your programs. (i.e math)
- **Non-Standard**: third party or own

## Arithmetic Operations

|Operator|Operation|
|---|---|
|`+`|Addition|
|`-`|Subtraction|
|`*`|Multiplication|
|`/`|Division|
|`//`|Integer division|
|`%`|Modulo|
|`**`|Exponentiation|

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

The `//` operator returns the largest whole number less than or equal to the floating point result.
In case of negative numbers the result is rounded towards negative infinitive, as far away from zero as possible, so print(16 // -3)    # -6 instead of -5

Simone's explanation:

This is quite simple when you visualise a number line: -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6Let's start at zero. Going right means the numbers _increase,_ whilst going left means the numbers _decrease_.So, integer division indeed returns the largest whole number _less than or equal to_ (<=) the floating-point result.  
16//3 -> 5.33333...  -> 5 (because rounding 5.33333 _down_ gives us 5 (find the floating-point result on the number line and move _left_))So... now let's consider 16//-3.  
16//-3 -> -5.33333... -> ? (well, if we consult our number line again, our dear -5 "sits" between -6 and -5. Which of these two numbers is _less_ (i.e. to the _left_)? Well, -6. So, this means rounding -5.33333... _down_ results in -6 ![:slightly_smiling_face:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-medium/1f642@2x.png))

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

|ype A|Type B|Result type|
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