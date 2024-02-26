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
    - Within each iteration compare, the sub-string starting from curent index up to index + lenght of the target, with the string value target
    - If there is a match, increment by 1 the value of the variable count.
- Print 'Number of times {target} occurs is: ' + the value of count

## Code
```python
def count_target(s, target):
    count = 0
    for idx in range(len(s)):
        if s[idx:idx + len(target)] == target:
            count += 1
    
    print(f'Number of times {target} occurs is: {count}')
```
### Test Cases
count_target('azcbobobegghakl', 'bob')
count_target('kefbooblbboboboboobobobobobobb', 'bob')
count_target('qoboobvoboobbvhv', 'bob')

#### Lisa is trying to create the following list structure: `[['x'], [], [], [], []]`. Her program outputs `[['x']]`, but she doesn't know why or how to fix it. Explain to Lisa why her program outputs `[['x']]` and propose a fix.


my_list = 5 * [[]]

for nested_arr in my_list:
    print(id(nested_arr))

my_list[0].append('x')
# my_list.reverse()
print(my_list) # [['x']]


# What do the following output?
"".split()     # []
"".split("")   # []
"".split(" ")  # []
"".split("abc")# []

# What would you have to do to the string "012345678" in order to end up with a tuple that contains the odd numbers in reverse order?
string = "012345678"

tup = tuple(string[7:0:-2])
print(tup)

### CORA's ALGO (Code this)
"""
    - define a function, `find_substring` with two parameters: `string` and `substring`:
        - initialize variable `occurrences` to 0
        - initialize variable `should_search` to result of logical conditions:
            - `string` and `substring` both have a length greater than 0
            - `substring` has a length <= the length of `string`

        - if `should_search` is truthy:
            - initialize variable `start_index` to 0
            - initialize variable `stop_index` to (length of substring)
            - loop while `stop_index` is >= length of `string`
                - if `string` sliced from `start_index` to `stop_index` is == `substring`:
                    - increment occurrences by 1
                - increment `start_index` by 1
                - increment `stop_index` by 1

        - print `'Number of times <substring> occurs is: <occurrences>'`
    
    example:
    - find_substring('azcbobobegghakl', 'bob')    # Number of times bob occurs is: 2
    - find_substring('bob', 'bob')                # Number of times bob occurs is: 1
    - find_substring('', '')                      # Number of times  occurs is: 0
    - find_substring('azcbobobegghakl', 'alice')  # Number of times alice occurs is: 0
    - find_substring('hi', 'hmmmm')               # Number of times hmmmm occurs is: 0
"""

