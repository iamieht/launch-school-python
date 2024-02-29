# What will the following code do and why?
def my_function():
    a = 1

    if True:
        print(a)


my_function()

# 1 is printed.
# Variables initialized in the same scope where a block begins can be accessed inside the block. In our case, the variable a is initialized within the function my_function and then accessed inside the if statement block. Therefore, the print(a) statement on line 5 outputs the value 1 when my_function is invoked.
