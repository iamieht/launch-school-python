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


