# 1. Identify the data types and class

print(type('True').__name__)            # => String, `str`
print(type(False).__name__)             # => Boolean, `bool
print(type((1, 2, 3)).__name__)         # => Tuple, `tuple`
print(type(1.5).__name__)               # => Float, `float`
print(type([1, 2, 3]).__name__)         # => List, `list`
print(type(2).__name__)                 # => Integer, `int``
print(type(range(5)).__name__)          # => Range, `range``
print(type({1, 2, 3}).__name__)         # => Set,   `set``
print(type(None).__name__)              # => NoneType, `NoneType``
print(type({'foo': 'bar'}).__name__)    # => Dicionary, `dict``

# The data type is the universal type label, the class is the actual type (class) in Python that implements the data type

# For ranges, Python doesn't have a literal syntax to create them, so we need to use a constructor function range() to build one

# None represents the absence of a value
