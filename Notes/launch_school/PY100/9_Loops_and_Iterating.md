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

### Using while Loops with Sequences

```python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
```

- We initialized `names`, `upper_names`, and `index` before the loop. We don't want to initialize them inside the loop; they would get reset during every iteration.

## for Loops

- Syntax: `for` <element> `in` <iterable>

```python`
`names = ['Chris', 'Max', 'Karis', 'Victor']`
`upper_names = []`
 
`for name in names:`
    `upper_name = name.upper()`
    `upper_names.append(upper_name)`
    `# Deleted: index += 1`

`print(upper_names);`
`# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']`
```

- Using a `for` loop with a dict iterates over the dict keys by default.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)
# a
# b
# c
```

- If you want the values or pairs, you can request them with the values or items methods

```python 
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)
# 1
# 2
# 3
```

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)
# ('a', 1)
# ('b', 2)
# ('c', 3)
```

- A more Pythonic way to iterate over both the keys and values simultaneously is to use tuple unpacking:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key} = {value}')
```

### Nested Loops

- With nested `for` loops, you start with the outer loop and assign the variable to the first element of its collection (`suit` and `suits`). You then process the inner loop in its entirety. Here, we match the first suit with every possible card rank, appending each card to the deck.
- Once the inner loop finishes processing, control returns to the outer loop. Working with the second element of the outer loop's collection, it again iterates over the inner loop's collection. This continues until all members of the outer loop's collection have been processed.

```python
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)
```

## Controlling Loops

### Continuing a Loop with next iteration

- `continue` starts a new loop iteration
- When a loop encounters the `continue` keyword, it skips running the rest of the block and jumps ahead to the next iteration.
- The `continue` statement tells Python to start the next iteration of the nearest enclosing loop. You can't start a new iteration of an outer loop if you're currently in an inner (nested) loop.

```python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names);
# ['CHRIS', 'KARIS', 'VICTOR']
```

### Breaking out of a loop

- `break` terminates the loop early
- The `break` statement tells Python to terminate the nearest enclosing loop once we find the desired element. You can't break out of an outer loop if you're currently in an inner (nested) loop.

```python
numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break

    index += 1

print(found_item)
```

### Emulating Do/While Loops

- Suppose you want to iterate through a loop at least once, even if the condition is initially falsy.

```python
while True:
    # main loop code is here
    answer = input('Play again? (y/n) ')
    if answer == 'n':
        break
```

## Simultaneous Iteration

- The `zip` function is specifically designed to make simultaneous iteration easy. 

```python
forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames)
for forename, surname in zipped_names:
    print(f'{forename} {surname}')
```

- Note that `zip` takes care of the potential problem of dealing with lists of different sizes

## Comprehensions

- Are ways of creating mutable collections from existing iterable collections.
- There are 3 types: list, dict and set.
- Comprehensions are expressions and not statements.
- You can use a comprehension on the right side of an assignment, as a function argument, as a return value, or any other place where you can use an expression that evaluates as a list, dict, or set. You can even use them as standalone expressions

```python
[print(foo) for foo in collection]
```

### List Comprehensions

- They take an iterable collection and create a new list through iteration and optional selection.
- Format: `[ expression for element in iterable if condition ]`
- The `if condition` portion is optional.
- The `for element in iterable` describes the iteration
- The `expression` is a value that gets returned by each iteration of the loop. Python collects all the return values and puts them in a new list.
- The `expression` in a comprehension ofter performs a **transformation**. It determines a new value based on an element from the original collection. Such comprehensions are called **transformations**.
- If the `if condition` portion is present, the comprehension also performs **selection**. With selections, it's not uncommon to return the original values from the collection.

- Transformation example:
```python
squares = [ number * number for number in range(5) ]
print(squares)      # [0, 1, 4, 9, 16]
```

- Selection example:
```python
multiples_of_6 = [ number for number in range(20)
                   if number % 6 == 0 ]
print(multiples_of_6)      # [0, 6, 12, 18]
```

- Transformation and Selection example:
```python
even_squares = [ number * number
                 for number in range(10)
                 if number % 2 == 0 ]
print(even_squares)      # [0, 4, 16, 36, 64]
```

- Multiple selection criterias act like nested if statements or as 'and' conditions. Only collection members matching al criterial are selected.
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

- Comprehensions can also have multiple for loop components. For instance, let's generate a deck of cards based on a list of the suits and a list of the ranks:

```python
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = [ f'{rank} of {suit}'
         for suit in suits
         for rank in ranks ]
print(deck)
```

### Dictionay Comprehensions

- Almost identical to list comprehensions, but they create new dictionaries instead of lists.
- The most significant difference is that the expression component is now a key/value pair, each given by another expression.

```python
{ key: value for element in iterable if condition }
```

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

- **Set comprehensions** look almost identical to dict comprehensions. However, they create a new set instead of a dict and only have one expression to the left of the word for:

```python
{ expression for element in iterable if condition }
```

```python
squares = { number + 1 for number in range(1, 6) }
print(squares)      # {2, 3, 4, 5, 6}
```

### Why No Tuple, Range, or String Comprehensions?

- Comprehensions don't build their results all at once. Each kind of comprehension works something like this:

```python
result = empty_collection               # [], {}, set()
for item in collection:
    result.append(item)
```

- As you can see, our result starts as an empty collection. We then modify the result collection during each iteration by appending a new item to result. From this, it's clear that the result must be a mutable type. Tuples are immutable, so Python can't have tuple comprehensions.

- Since ranges and strings are also immutable, comprehensions can't create them.