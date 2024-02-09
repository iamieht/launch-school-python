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
