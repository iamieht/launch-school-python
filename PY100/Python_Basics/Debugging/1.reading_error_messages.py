def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n


find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# Parameter of the function is a collection (sequence) but only primitives are passed as arguments. Too many arguments in the first function invocation
# Second invocation 'int' is not iterable
