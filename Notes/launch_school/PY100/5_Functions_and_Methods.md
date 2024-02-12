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

- `ord`: given a single character, returns an integer that represents the Unicode or ASCII code point of that character.

```python
print(ord('a'))               # 97
print(ord('A'))               # 65
print(ord('='))               # 61
print(ord('~'))               # 126
```
- `chr` is the inverse of `ord`: converts an integer into the corresponding Unicode character.

```python
print(chr(97))                # a
print(chr(65))                # A
print(chr(61))                # =
print(chr(126))               # ~
```

### `any` and `all`

- Both operate on iterable collections.
- `any` returns `True` if any element in a collection is truthy.
- `any` returns `False` if all the elements in a collection are falsy.
- `all` returns `True` if all the elements in a collection are truthy.
- `all` returns `False` if all elements in a collection are falsy.

```python
collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))       # False
print(any(collection2))       # True
print(any(collection3))       # True
print(any([]))                # False ("Are any of the members truthy? No.")

print(all(collection1))       # False
print(all(collection2))       # False
print(all(collection3))       # True
print(all([]))                # True ("Are all of the members truthy? Yes, because we would need sth falsy to return False.")
```
- `print(all[])` returns `True` because: this is termed a "vacuous truth"... since there is nothing in the list, there are no false elements in the list, and by definition all() can only return False when the list contains at least one False ...so, since all zero elements in the list are not False, all() "has to" return True (so as not to contradict itself)

## Functions for the REPL

### The id Function

- Returns an integer that serves as an object's **identity**. 
- Every object has a unique identity that does not change during the object's lifetime.
- The identity may be reused later in the program if the original object is discarded.
- In most cases, two instances of an object with the same value will always have two distinct identities. This is not always true.
- There is a process called **interning** use for optimization/performance in which string and integer values in memory are reused, so the id of both variables is the same:

```python
# Paste this code into the Python REPL
# Don't run it as a program

s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

s = 'supercalifragilisticexpialidocious'
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))         # True

x = 5
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False
```

### The dir Function

- Without arguments it returns a list of all **identifiers** in the current local scope.
- With an argument, returns a list of the object's attributes.
- Many of the names shown by `dir` begin and end with two underscores. These are called **dunder**(double-underscore) or **magic methods** and **magic variables**.
- An **identifier** is a name given to variables, functions, classes, modules, attributes and other objects.

### The help function

- prints some basic help on how to use modules, keywords, built-in functions, classes, etc.

## Creating Functions

```python
def func_name():
    func_body
```

- **docstring** is a documentation comment written inside a triple-quoted string at the beginning of a function's block. This documentation can be accessed with the `help()` function and the `__doc__` property.

```python
def say():
    """
    The say function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)
```

## Scope

- The **scope** of an identifier determines where you can use it.
- Python determines scope by looking at where you initialize the identifier.
- Identifiers have **function scope**: anything initialized inside a function is only available within the body of that function and nested functions. No code outside of the function body can access that identifier.
- **Variable Shadowing** is when a variable (assigned) in an inner scope "hides" (that is, makes inaccessible) another variable with the same name in an outer scope

```python
greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
```

- In the following example, Python looks for `greeting` in the **lexical scope**, which means that it searches all of outer scopes for the nearest definition of `greeting`.

```python
greeting = 'Salutations'

def well_howdy(who):
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
```

## Arguments and Parameters

- Arguments are values used when calling a function and they let you pass data from outside's function scope into the function so it can access that data.
- Parameters are the names between parentheses in the function definition. These are placeholders for potential arguments, while arguments are the values assigned to those placeholders.
- **Arguments** are objects passed to a function during invocation.
- **Parameters** are placeholders for the objects that will be passed to the function when it is invoked.
- **Function names and parameters are both considered variable names in Python**
- **Parameters** are **local variables**: they are defined localy within the function's body.
- A function's name is global or local, depending on whether it is at the program's top level or nested inside a class, module or another function.

## Return Values

- Functions return a result to the caller for later use with return values and the `return` statement.
- All Python function calls evakluate to a value (if the function doesn't raise an exception). By default the value is `None`, this is the **implicit return value**.
- When a `return` statement is used to return a specific value from a function, this is called an **explicit return value**.
- Functions that always return a Boolean value are called **predicates**.

