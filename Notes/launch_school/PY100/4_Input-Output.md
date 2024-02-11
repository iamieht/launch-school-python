# Input/Output

## Terminal Output

- `print`function: takes any value and prints it.
- The `print()` function works with all data types, but the formatting output is not always understandable to humans
- You can print multiple objects by just listing them one after the other as arguments to `print()`:

```python
>>> print(1, 2, 3, 'a', 'b')
1 2 3 a b

>>> print([1, 2, 3], 4, False, { 5, 6, 7, 8})
[1, 2, 3] 4 False {8, 5, 6, 7}
```

- keyword argument `sep` is used to separate the values printed.
- The `end` keyboard defines what `print()` prints after it prints the last argument. By default, it prints a newline (`\n`). The most common reasons for using `end` are compatibility with Windows (which sometimes needs a newline of `\r\n`) and for suppressing the newline altogether.

```python
>>> print(1, 2, 'a', 'b', sep=',', end=' <-\n')
1,2,a,b <-

>>> print('a', 'b', end='', sep=','); print('c', 'd', sep=',')
a,bc,d
```

- Note the semicolon (`;`) on line 4: that's an easy way to enter multiple statements on a single line. Mostly, you should only use semicolons like this in the REPL.

## Terminal Input

- `input()` is a built-in function that lets Python read input from the terminal.

```python
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f'The numbers {number1} and {number2} add to {sum}')
```
