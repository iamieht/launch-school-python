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

