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
