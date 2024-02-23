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
