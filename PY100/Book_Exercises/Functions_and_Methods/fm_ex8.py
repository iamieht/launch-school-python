# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# It will raise an error (TypeError: foo() takes 2 positional arguments, but 3 were given) as we are invoking the function foo with one extra positional argument than parameters defined in the function definitiong