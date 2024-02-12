# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# We get an error (NameError: name 'foo' is not defined), as name 'foo' has function scope and is not available in the global scope.

# Main Scope / Top level scope / Global Scope / Outer Scope