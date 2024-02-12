# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# It will raise an error (TypeError: foo() missing 1 erquired positional argument: 'first') as at least one argument must be supplied to the invocation of the function as only 2 parameters out of 3 have default valuesg