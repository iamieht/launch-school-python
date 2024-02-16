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

- Syntax: `for` <element> `in` <iterable>:
