# 1. What happens when you run the following program? Why do we get that result?
def set_foo():
    foo = 'bar'


set_foo()
print(foo)

# We get a NameError: name 'foo' is not defined exception. This happens because in line 6 we pass to the print function a variable that doesn't exist in the global scope. The foo variable initialized in the function set_foo has a function scope and cannot be access outside of the function
