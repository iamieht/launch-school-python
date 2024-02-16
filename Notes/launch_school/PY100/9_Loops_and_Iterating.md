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

```python
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']
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

