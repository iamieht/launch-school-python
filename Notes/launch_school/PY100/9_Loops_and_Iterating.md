# Loops and Iterating

- Loops runs while a given condition remains truthy or until it becomes falsy.
- Python loops mechanisms: for, while, comprehensions, generators and functional loops.

## while Loops

- Syntax: `while` `<conditional expression>:` `block of code`
- We must arrange to terminate the loop, otherwise the loop is an **infinite loop** 
- Each block run is called an **iteration**

```python
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
```

## for Loops

- Syntax: `for` element in `iterable`:

```python
for element in collection:
    # loop body: do something with the element
```

## Controlling Loops

- Keyword `continue`: starts a new loop iteration, it skips running the rest of the block and jumps ahead to the next iteration. The `continue` statement tells Python to start the next iteration of the nearest enclosing loop. You can't start a new iteration of an outer loop if you're currently in an inner (nested) loop.
- Keyword `break`: terminates the loop early. The `break` statement tells Python to terminate the nearest enclosing loop once we find the desired element. You can't break out of an outer loop if you're currently in an inner (nested) loop.

### Emulating Do/While Loops

- Suppose you want to iterate through a loop at least once, even if the condition is initially falsy, simulating a do/while looping structure (doesn't exist in Python). `break` helps simulating it.

```python
while True:
    # main loop code is here
    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break
```

## Simultaneous Iteration

- The `zip` function  is specifically designed to make simultaneous iteration easy.
- `zip` creates a lazy sequence that acts like a list of tuples.

```python
forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')
```

## Comprehensions

- Are ways of creating mutable collections from existing iterable collections.
- There are 3 types: **list, dict and set**.
- Comprehensions are expressions and not statements.
- You can use a comprehension on the right side of an assignment, as a function argument, as a return value, or any other place where you can use an expression that evaluates as a list, dict, or set. You can even use them as standalone expressions

### List Comprehensions

- They take an iterable collection and create a new list through iteration and optional selection.
- Syntax: `[ expression for element in iterable if condition]`
- The `if condition` portion is optional: it tells Python to select only certain elements from the `iterable`.
- The `for element in iterable` portion describes the iteration: it looks exactly like a `for` loop.
- The `expression` is a value that gets returned by each iteration of the loop.
- The `expression` in a comprehension often performs a **transformation**. It determines a new value based on an element from the original collection. Such comprehensions are called **transformations**.
- If the `if condition` portion is present, we say that the comprehension also performs **selection**.
- Multiple selection criteria act like nested `if` statements or as `and`-ed conditions. The selections combine, so only collection members matching all criteria are selected.

**transformative** list comprehension:

```python
squares = [ number * number for number in range(5) ]
print(squares)      # [0, 1, 4, 9, 16]
```

**selection** example:

```python
multiples_of_6 = [ number for number in range(20)
                   if number % 6 == 0 ]
print(multiples_of_6)      # [0, 6, 12, 18]
```

**selection** and **transformation**: 

```python
even_squares = [ number * number
                 for number in range(10)
                 if number % 2 == 0 ]
print(even_squares)      # [0, 4, 16, 36, 64]
```

**multiple selection**

```python
cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L' ]
print(names) # ['LEO']
```

### Dictionary Comprehensions

- **Dictionary comprehensions** are almost identical to list comprehensions. However, they create new dictionaries instead of lists.
- Syntax: `{ key: value for element in iterable if condition }`

```python
squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)
# pretty-printed for clarity.
{
    '1-squared': 1,
    '2-squared': 4,
    '3-squared': 9,
    '4-squared': 16,
    '5-squared': 25
}
```

### Set Comprehensions

- **Set comprehensions** look almost identical to dict comprehensions. However, they create a new set instead of a dict and only have one expression to the left of the word `for`
- Syntax: `{ expression for element in iterable if condition }`

```python
squares = { number + 1 for number in range(1, 6) }
print(squares)      # {2, 3, 4, 5, 6}
```
