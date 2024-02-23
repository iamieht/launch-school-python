# 1. What happens when you run the following program? Why do we get that result?
# def set_foo():
#     foo = 'bar'


# set_foo()
# print(foo)

# We get a NameError: name 'foo' is not defined exception. This happens because in line 6 we pass to the print function a variable that doesn't exist in the global scope. The foo variable initialized in the function set_foo has a function scope and cannot be access outside of the function

# 2. What does this program print? Why?
print("-" * 60)
foo = 'bar'


def set_foo():
    foo = 'qux'


set_foo()
print(foo)

# The program prints 'bar'. When invoking the print function and pass the foo variable, the one in scope at this level is the foo variable initialized at the top level (global scope). The local foo variable shadows the foo variable of the global scope and doesn't change its value.
print()
print("-" * 60)

# 3. Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.


def multiply(number1, number2):
    return number1 * number2


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print(f'{number1} * {number2} = {multiply(number1, number2)}')

# 4.Identify items in the code


def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result


product = multiply_numbers(2, 3, 4)

# function name:            # multiply_numbers
# function arguments:       # 2,3,4
# function definition:      # from line 40 to 42
# function body:            # line 41 - 42
# function parameters:      # num1, num2, num3
# function invocation:      # line 44
# function return value:    # result
# all identifiers:          # multiply_numbers, num1, num2, num3, result, product

# 5. What does the following code print?


def scream(words):
    return words + '!!!!'


scream('Yipeee')

# Nothin is printed. The following value: Yipeee!!!! is returned, but is not captured anywhere.

# 6. What does the following code print?


def scream(words):
    words = words + '!!!!'
    return
    print(words)


scream('Yipeee')

# Nothing is printed. There is a return statement without any variable or value before the print statement at the end of the function. The return value is not captured anywhere, so nothing is done with it.

# 7. Without running the following code, what do you think it will do?


def foo(bar, qux):
    print(bar)
    print(qux)


foo('Hello')

# An error will be raised, as the function foo is invoked with only one argument and two are expected.

# 8. Without running the following code, what do you think it will do?


def foo(bar, qux):
    print(bar)
    print(qux)


foo(42, 3.141592, 2.718)

# Error is raised, as duing the foo invocation we are passing 3 arguments, when 2 are expected.

# 9. Without running the following code, what do you think it will do?


def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo(42, 3.141592, 2.718)

# this code prints:
# 42
# 3.141592
# 2.718.

# 10. Without running the following code, what do you think it will do?

print()
print("-" * 60)


def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo(42, 3.141592)

# it prints:
# 42
# 3.141592
# 2 => default value as no third positional argument was passed to the function

# 11. Without running the following code, what do you think it will do?
print()
print("-" * 60)


def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo(42)

# it will print:
# 42
# 3 => default value used instead of second positional argument
# 2 => default value as no third positional argument was passed to the function

# 12. Without running the following code, what do you think it will do?


def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)


foo()

# An error will be raised as the function foo expects at least one argument to be passed to the function, as the first parameter has no default value.

# 13. Without running the following code, what do you think it will do?
# def foo(first, second=3, third):
#     print(first)
#     print(second)
#     print(third)

# foo(42)

# An error is raised. A default value is expected at the 3rd parameter, as the second parameter has a default value, so any subsequent parameter must have one

# 14. Identify all of the identifiers on each line of the following code.


def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names:       # multiply, get_num, float, input, print
# function parameters:  # left, right, prompt
# function arguments:   # "Enter the first number", "Enter the second         number", first_number, second_number, product
# variables:            # first_number, second_number, product and function names.

# 15. Using the code below, classify the identifiers as global, local, or built-in


def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Global:       # multiply, get_num, first_number, second_number, product
# Local:        # left, right, prompt
# Built-in      # float, input, print

# 16. In the code shown below, identify all of the function names and parameters present in the code


def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names:       # multiply, get_num, float, input, print
# parameters:           # left, right, prompt
