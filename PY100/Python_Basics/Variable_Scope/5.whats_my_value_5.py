# What will the following code do and why?
a = 1


def my_function():
    print(a)
    a = 2


my_function()

# It raises a NameError as trying to print the value of variable a before initialization.
# Python detects that a is being assigned within the my_function function and therefore treats it as a local variable. However, since we are trying to print the local a variable's value before it has been assigned a value, we get an error.
