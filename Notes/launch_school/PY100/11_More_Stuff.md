# More Stuff

## Function Composition

- **Composition** occurs when a function call is used as an argument to another function call, which may, in turn, be passed to another function call.
- The return value of the inner function call is used as the argument to the outer function.

```python
print(list(range(3, 17, 4)))
```

**Note**: Ask Simone about what she understands about this sentence: "Composition works best when each function except the outermost returns a usable value." What is an unusable value?

## Method Chaining

- Is similar to function composition but applies to methods rather than functions.

```python
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
```
- To use method chaining, you start by calling a method on an appropriate object. If that method returns another object, you can use it to call another method.
- You can chain as many method calls as necessary, though it can get messy if you chain more than 2 or 3 methods on a single line.
- Chaining only works when each method in the chain (except the last) returns an object with at least one helpful method.

## Modules

- You can use code from other Python files in your programs. These files are called **modules**.

### The import and from Statements

- The `import` statement is used in Python to load code from Python modules into your code.
- The most basic way to load a module is to write `import module_name`, where `module_name` is the module's name. The `import` statement(s) are conventionally coded at the very top of the program file:

```python
import math

print(math.sqrt(math.pi))   # 1.7724538509055159
```

- both `sqrt` and `pi` are fully qualified names: both names are prefixed with the module name and a period (`.`). These fully qualified names mean you don't have to worry about naming conflicts with your code or other modules.
- If you don't want to write `math.` every time you use a function or constant from the module, you can import just the names you want by using the `from` statement:

```python
from math import pi, sqrt

print(sqrt(pi))             # 1.7724538509055159
```

- This`from` statement imports the `math` module's `pi` and `sqrt` identifiers into your program. You can then use those names without qualification. Be aware, though, that `from` circumvents the naming conflict benefits of `import`.
- You can also use an alias to avoid having to write `math.` every time you use something from the `math` module:

```python
import math as m

print(m.sqrt(m.pi))         # 1.7724538509055159
```

### The math Module

```python
import math
print(math.sqrt(36))        # 6.0
print(math.sqrt(2))         # 1.4142135623730951
```

### The datetime Module

- Python's `datetime` module provides classes for creating and manipulating objects representing a time and date.

```python
from datetime import datetime as dt

date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)                   # Saturday
```

## Function Definition Order

```python
def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()
```

- When Python encounters a `def` statement, it merely reads the function definition into memory. It saves it away as an object in the heap. The function's body isn't executed until it's called explicitly. In this code, this read-and-save-but-don't-execute process occurs when Python encounters both functions. When we eventually invoke `top` on line 7, Python knows what and where `top` and `bottom` are.
- Python also knows what code those function contain. Thus, when `top` tries to invoke `bottom`, Python only has to find and call the `bottom` function object. That means the code runs correctly even though `bottom` was defined after `top` was.
- you should define all your functions before you try to invoke the first one. This is why Pythonistas almost always put the main program code at the bottom of the program after declaring all functions.

## The global and nonlocal Statements

- By default, Python assumes that all variables that are assigned a value inside a function are local variables. Even if a variable by the same name exists in an outer scope, Python will create a new local variable if the variable's name appears on the left side of an assignment.

```python
greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
```

- Python's `global` and `nonlocal` statements let the programmer override this behavior. They tell Python to use a variable that is defined elsewhere. Python will not create a new local variable when `global` or `nonlocal` is used to override this behavior.
- In the case of `global`, Python is told to look to the outermost scope (the global scope) for the variable to be used. It works in any function.
- The `nonlocal` statement, however, only works in nested functions: functions that are defined inside an outer function. When Python processes a `nonlocal` statement, it looks for the associated variable in one of the outer functions.

```python
greeting = 'Salutations'

def well_howdy(who):
    global greeting
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
```

```python
def outer():
    def inner1():
        def inner2():
            nonlocal foo
            foo = 3
            print(f`inner1 -> {foo}`)

        nonlocal foo
        foo = 2
        inner2()
        print(f`inner2 -> {foo}`)

    foo = 1
    inner1()
    print(f`outer -> {foo}`)

outer()

inner1 -> 3
inner2 -> 3
outer -> 3
```

