# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# It will raise an error, as it is required to have a default value in the subsequent positional parameter in the function definition, in this case the 3rd parameter, as the second parameter has a default value