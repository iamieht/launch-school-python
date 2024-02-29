# What will the following code do and why?
a = 1


def my_function():
    a = 2


my_function()
print(a)

# 1 is printed
# The variable a initialized at the top level has the value 1. Inside the function, a new local variable a is initialized and assigned the value 2. This local variable a has no effect on the global variable a. When we call print(a) after invoking my_function, it refers to the global variable a, which still has the value 1.
