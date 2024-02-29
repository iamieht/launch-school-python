# What will the following code do and why?
if True:
    my_value = 20

print(my_value)  # => 20

# On line 5 the value 20, referenced by the variable my_variable will be printed, as the If condition on line 2 will always evaluate to a truthy value.

# In Python, variables initialized inside a block (like inside an if statement) are accessible outside of that block. Thus, the variable my_value initialized inside the if block on line 2 can be accessed and printed on line 4. The output of the print(my_value) statement is 20.

# What do you think will happen if we run the following code instead:
if False:
    my_new_value = 42

print(my_new_value)

# The variable my_new_value is in the global scope but never initialized as the if condition always evaluate to a falsy value and the block code is never executed, so a NameError exception is raised.
