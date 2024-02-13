# Flow Control

- **Flow Control** is the path that you want your data to take when writing programs.

## Conditionals

- Fork(s) in the road. Python evaluates the conditional and tells the data where to go.
- **Block** is one or more Python statements.
- `else` block isn't a proper statement; it's part of the `if` statement.
- You have as many `elif` blocks as you need. They are evaluated in the order they appear in the code.
- All statements in a block must be indented from the statement that begins the block. The indentation in a block must be consistent.

```python
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')
```

## Comparisons

- Comparison operators return a Boolean value: `True` or `False`.
- **Operands** are the expressions to the left and right of an operator.

### `==`

- The **equality operator** returns `True` when the operands have equal values, `False` otherwise.
- In most cases, operands must have the same type and value to be equals. There are some cases where you can mix types.

```python
print(5 == 5)          # True
print(5 == 4)          # False

print('abc' == 'abc')  # True
print('abc' == 'abcd') # False

print(5 == '5')        # False

print([1, 2, 3] == [1, 2, 3]) # True
print([1, 2, 3] == [3, 2, 1]) # False

print(5 == float(5))                # True

big_num = 12345678901234567
print(float(big_num) == big_num)    # False
```

### `!=`

- The **inequality operator** is `==`'s inverse. 

```python
print(5 != 5)             # False
print(5 != 4)             # True
print('abc' != 'abc')     # False
print('abc' != 'aBc')     # True
print(5 != '5')           # True
```

### `<` and `<=`

- The **less than operator** (`<`) returns `True` when the value of the left operand has a value that is less than the value on the right, `False` otherwise.
- The **less than or equal to operator** (`<=`) is similar, but it also returns `True` when the values are equal.

```python
print(4 < 5)              # True
print(5 < 4)              # False
print(5 < 5)              # False

print(4 <= 5)             # True
print(5 <= 4)             # False
print(5 <= 5)             # True

print('4' < '5')          # True
print('5' < '4')          # False
print('5' < '5')          # False

print('42' < '402')       # False
print('42' < '420')       # True
print('420' < '42')       # False
```

### `>` and `>=`

- The **greater than operator** (`>`) returns `True` when the value of the left operand has a value that is greater than the value on the right, `False` otherwise.
- The **greater than or equal to operator** (`>=`) returns `True` when the values are equal. 

```python
print(4 > 5)              # False
print(5 > 4)              # True
print(5 > 5)              # False

print(4 >= 5)             # False
print(5 >= 4)             # True
print(5 >= 5)             # True

print('4' > '5')          # False
print('5' > '4')          # True
print('5' > '5')          # False

print('42' > '402')       # True
print('42' > '420')       # False
print('420' > '42')       # True
```

## Logical Operators

### `not`

- The **not operator** returns `True` when its operand is `False` and `False` when the operand is `True`.
- `not` takes a single operand, so it's called **unary operator**.
- Operators that take two operators are **binary operators**.

```python
print(not True)           # False
print(not False)          # True
print(not(4 == 4))        # False
print(not(4 != 4))        # True
```

### `and` and `or`

- The `and` operator returns `True` when both operands are `True`. It returns `False` when either operand is `False`.
- The `or` operator returns `True` when either operand is `True` and `False` when both operands are `False`

| **A**     |   **B**   |   **A and B** |   **A or B**  |
|-----------|-----------|---------------|---------------|
|   `True`  |   `True`  |   `True`      |   `True`      |
|   `True`  |   `False` |   `False`     |   `True`      |
|   `False` |   `True`  |   `False`     |   `True`      |
|   `False` |   `False` |   `False`     |   `False`     |

## Short Circuits

- The `and` and `or` operators use **short circuit evaluation** to evaluate their operands.

```python
is_red(item) and is_portable(item)
is_green(item) or has_wheels(item)
```

- The first expression returns True when item is red and portable.
- If either condition is False, then the overall result must be False.
- If the program determines that item is not red, it doesn't have to determine whether it is also portable.Python short-circuits the rest of the expression by terminating evaluation if it determines that item isn't red. It doesn't need to call is_portable() since it already knows the expression must be False.

## Truthiness

- Python can evaluate every object's **truthiness** (Do not confuse with the terms `True` or `False` or Boolean).
- Truthiness arises in conditional expressions (`if` and `while`). They don't need to produce Boolean values.
- Built-in falsy values:
    - `False`, `None`
    - all numeric `0` values (integers, floats, complex)
    - empty strings: `''`
    - empty collections: `[]`, `()`, `{}`, `set()`, `frozenset()`, and `range(0)`
    - Custom data types can also define additional falsy value(s)

```python
value = 5                     # 5 is truthy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')
```

### Truthiness and Short-Circuit Evaluation

- Logical operators don't always return `True` or `False`.
- They only care about the truthiness of their operands. 
- In each case, they evaluate as the object that evaluates last in the expression.

```python
print(3 and 'foo')   # last evaluated op: 'foo'
print('foo' and 3)   # last evaluated op: 3
print(0 and 'foo')   # last evaluated op: 0
print('foo' and 0)   # last evaluated op: 0

print(3 or 'foo')    # last evaluated op: 3
print('foo' or 3)    # last evaluated op: 'foo'
print(0 or 'foo')    # last evaluated op: 'foo'
print('foo' or 0)    # last evaluated op: 'foo'
print('' or 0)       # last evaluated op: 0
print(None or [])    # last evaluated op: []
```


