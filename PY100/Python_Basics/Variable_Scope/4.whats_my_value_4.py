# What will the following code do and why?
a = 1


def my_function():
    print(a)


my_function()

# It prints the value 1 referenced by variable a. Python searches in the lexical scope and finds the variable a initialized in the global scope.
# The variable a is initialized at the top level of our code and is initialized with the value 1. This makes it globally accessible throughout the code, including within the body of the my_function. When we invoke my_function, it prints the value of the global variable a, which is 1.
