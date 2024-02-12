# Functions and Methods

- Blocks of code that run as a separate unit.
- Benefits:
    - Reduce repetite code
    - Easy code reuse
    - improve code readability and maintainability.
- Methods are limited to specific objects

## Calling Functions

- Using a function means **calling**, **invokling**, **executing** or **running** it.
- **Flow**: 
    - Python encounters a function call
    - It transfers program flow to the code that comprises the function and executes that code.
    - When the code finish, the function **returns** a value to the code that invoked it.
    - The calling code uses or not the return value.
    - Executions resumes from where the function was called.

- To invoke a function, write function's name followed by a pair of parentheses `()`. Example:

```python
def hello():            #
    print('Hello')      # These 3 lines contain the function definition
    return True         #

hello()         # invoking function; ignore return value
print(hello())  # using return value in a `print` call
```
- Functions can take one or more command-separated **arguments** between the parentheses. They usually use arguments to modify the actions they take.

```python
print('hello', 'good-bye', 'farewell')
```

## Built-in Functions

### `min` and `max`

- They are used to determine a collection's minimun and maximun values.
- The collection's objects must have an ordering that recognizes the `<` and `>` operators for comparing any pair of those objects.

```python
print(min(-10, 5, 12, 0, -20))      # -20
print(max(-10, 5, 12, 0, -20))      # 12

print(min('over', 'the', 'moon'))   # 'moon'
print(max('over', 'the', 'moon'))   # 'the'

print(max(-10, '5', '12', '0', -20))
# TypeError: '>' not supported between instances
# of 'str' and 'int'
```

### `ord` and `chr`

