# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# It will raise an error (Type error: foo() missing 1 erquierd positional argument: 'qux') as the number of arguments in the function invocation is less than the number of parameters in the function definition