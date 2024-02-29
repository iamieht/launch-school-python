# What will the following code do and why?
x = 10


def my_function():
    x = x + 5
    print(x)


my_function()

# It will raise an error: In the function my_function, when we attempt to reassign the value of x by incrementing it, Python assumes that x is a local variable since we're assigning it inside the function. However, since it is uninitialized, we get an error. If we wanted to modify the global x, we would need to use the global keyword.
