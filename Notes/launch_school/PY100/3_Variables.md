# Variables

- Are labels that identify particular objects in a program
- Are labels attached to a specific value stored in a program's memory

## Variables and Variable Names

```python
answer = 41
print(answer)       # 41

answer = 42
print(answer)       # 42
```

In line 1, Python sets aside a bit of memory and stores the value `41` in that area. It also creates a variable named `answer`.

On line 3, we **reassign** the value `42` to the variable `answer`. Python makes `answer`refer to a new object. We are not changing the object that represents `41`, we are assigning a complete new value to the `answer` variable.

### Variable Naming

- A variable name must accurately and concisely describe the variable's data.
- **Identifiers** is a term used to refer to the following things:
	- Variable and constant names
	- Function and method names
	- Function and method parameter names
	- Class and module names

## Naming Conventions

- Names that follow Python naming conventions are **idiomatic**
- Those names that do not follow the naming conversions are **non-idiomatic** (still valid) or illegal (will raise syntax error)

### Naming conventions for most identifiers (excluding constants and class names):

- Use **snake_case** formatting.
- Names may contain lowercase letters, digits and underscores.
- Names should begin with a letter.
- Separate the words with a single underscore.
- Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
- Names may only use letters and digits from the standard ASCII character set
- Examples:

|Idiomatic Names|
|---|
|`foo`|
|`answer_to_ultimate_question`|
|`eighty_seven`|
|`index_2`|
|`index2`|

### Constant names (unchanging named values):

- Use **SCREAMING_SNAKE_CASE** formatting.
- Names may contain lowercase letters, digits and underscores.
- Names should begin with a letter.
- Separate the words with a single underscore.
- Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
- Names may only use letters and digits from the standard ASCII character set.
- The constant naming convention is advisory only. Python has no way to ensure that constants are never changed. Whether a constant ever changes is entirely up to the programmer, not Python.
- Examples:

|Idiomatic Names|
|---|
|`FOO`|
|`ANSWER_TO_ULTIMATE_QUESTION`|
|`EIGHTY_SEVEN`|
|`INDEX_2`|
|`INDEX2`|

### Class names:

- Use **PascalCase** also called **CamelCase** formatting.
- Names may contain uppercase and lowercase letters and digits.
- Names should begin with an uppercase letter.
- If the names has multiple words, capitalize each word.
- Examples:

|Idiomatic Names|
|---|
|`Foo`|
|`UltimateQuestion`|
|`FourLeggedPets`|
|`PythonVersion2Rules`|

### Non-idiomatic

- You can use letters, digits, and underscores in Python identifiers. Extended ASCII and Unicode letters and digits are allowed.
- You may not use punctuation characters, most special characters, or whitespace.
- You may not start identifiers with a digit.
- You may not use Python's reserved words such as `if`, `def`, `while`, `return`, and `pass` as names.
- Examples:

|Non-Idiomatic Names|Explanation|
|---|---|
|fourWayIntersection|camelCase|
|Schön|Extended ASCII|

|Illegal Names|Explanation|
|---|---|
|pass|Reserved word|
|3xy|Starts with digit|
|ultimate-question|Hyphen|
|one two three|Whitespace|
|is_lowercase?|Punctuation|
|is+lowercase|Special character|

## Creating and Reassigning Variables

- We create (initialize) a variable by simply giving it a value. That happens as part of an assignment statement:

```python
forename = 'Clare'            # initialization
```

- We can also give new values to variables by simply reassigning them:

```python
forename = 'Victor'           # reassignment
```

- Way to describe an assignment: The variable `foo`is assigned the value of `bar`.

### How Initialization and Reassignment Work

- When you initialize a variable, Python creates its initial value and sticks it somewhere in the computer's memory. It also allocates a small amount of memory for the variable itself, then places the value's memory address into the variable's spot in memory.
- Example:

```python
foo = 'abcdefghi'
```

Python creates the string `abcdefghi` somewhere in the memory. Next it will create a variable somewhere else in memory. Then associates the variable name with the address in memory. Then Python stores the address of the string at the address of the variable name.

![[Pasted image 20240210135549.png]]

Later we reassign the variable `foo`to another value:

```python
foo = 'Hello'
```

Python creates the new string `Hello` somewhere in memory. Since we already have a `foo`variable, Python replaces the value at variable's address with the new address of the value `Hello`. This breaks the connection with the original string and establishes a new one with the new string.

![[Pasted image 20240210135955.png]]

## Creating Constants

- Constants are created (initialized) in the same way as variables: by giving them a value:

```python
PINING_FOR = 'fjords'         # initialization
```

- Python does not support true constants. Instead, the **SCREAMING_SNAKE_CASE** naming convention is solely for programmers.

## Expressions and Assignment

- Assignment and reassignment often use expressions on the right side `=`to determine the desired value.
- Example:

```python
def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)                # 1764
```

- The expression on the right side of the `=` operator can be any valid expression.
- The variable to the left of the `=` operator is always the target variable for the resulting value. That is, the expression's value will be assigned to the variable.
- It's worth noting that the right side of an assignment is always completely evaluated before assigning the result to the variable.

```python
foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo ** 3      # foo is now 15.625
print(foo)          # prints 15.625
```

- In lines 2-7, the right side of each assignment is computed first using whatever value `foo` had most recently. Thus, `foo` was 42 on line 2, 40 on line 3, and so on. On each line, a computation is performed using the current value of `foo`. Python then reassigns the newly computed value to `foo`.

## Augmented Assignment

- It's a shorthand notation also called **assignment operators**, of the process of taking the current value of a variable, perform an arithmetic operation on the variable's value, and then reassign the variable to the newly computed value.

```python
foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625

bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc

bar = [1, 2, 3]     # bar is [1, 2, 3]
bar += [4, 5]       # + with lists appends
                    # bar is now [1, 2, 3, 4, 5]
print(bar)          # prints [1, 2, 3, 4, 5]

bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}
```

## Reassignment vs. Mutation

- There are two ways to change things in Python:
	- Change the **binding** of the variable by making it reference a new object (**Reassignment**).
	- Change the value of the object assigned (**bound**) to the variable (**Mutation**).
- **Reassignment** makes the variable name refer to a different object somewhere else in memory.
- **Mutation** does not change which object the variable refers to, instead it changes the object itself. After mutating an object assigned to a specific variable, the variable continues to refer to the same object (albeit altered) at the same memory location.
- **Reassigning** an element of a mutable collection doesn't reassign the variable; it mutates the collection.
- Examples:

```python
num = 3               # assignment (initialization)
my_list = [1, 2, 3]   # assignment (initialization)
my_dict = {           # assignment (initialization)
    'a': 1,
    'b': 2
}

num = 42              # Reassignment
my_list[1] = 42       # Reassignment of element,
                      # my_list is mutated!
my_dict['b'] = 3      # Reassignment of dict pair
                      # my_dict is mutated!

# You can still reassign the variables
my_list = (2, 3, 4)   # Reassignment
my_dict = { 'x': 0 }  # Reassignment
```
