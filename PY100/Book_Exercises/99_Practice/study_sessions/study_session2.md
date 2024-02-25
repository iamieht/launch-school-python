# Feb 25 2024

## Code Snippets
### Without running the code(s) what is printed? why?
```python
# 1
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       

# 2
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)       

# 3
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:0:-1]
print(result)
```

### Without running the code(s) what is printed? why?
```python
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

result = zip(my_str, my_list, my_tuple, my_range)
print(list(result)) 
print(list(result))
```

## Problem Set
'''
Assume s is a string of lower case characters and target a matching string

Write a program that prints the number of times the string target occurs in s. For example, if s = 'azcbobobegghakl' and target='bob', then your program should print

Number of times bob occurs is: 2
'''

## Algo
- Define a function count_target with two parameters of type string
- Assign a variable count with the integer value 0
- Iterate over the string sequence
    - We need to work with indexes so iterate over the length of the string using i.e range constructor function
    - Within each iteration, compare the sub-string starting from curent index up to index + 3 with the string value target
    - If there is a match, increment by 1 the value of the variable count.
- Print 'Number of times {target} occurs is: ' + the value of count

## Code
```python
def count_target(s, target):
    count = 0
    for idx in range(len(s)):
        if s[idx:idx+3] == target:
            count += 1
    
    print(f'Number of times {target} occurs is: {count}')
```
### Test Cases
count_target('azcbobobegghakl', 'bob')
count_target('kefbooblbboboboboobobobobobobb', 'bob')
count_target('qoboobvoboobbvhv', 'bob')

