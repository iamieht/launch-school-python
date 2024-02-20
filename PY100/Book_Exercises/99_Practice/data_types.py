# 1. Identify the data types

print(type('True').__name__)            # => str
print(type(False).__name__)             # => bool
print(type((1, 2, 3)).__name__)         # => tuple
print(type(1.5).__name__)               # => float
print(type([1, 2, 3]).__name__)         # => list
print(type(2).__name__)                 # => int
print(type(range(5)).__name__)          # => range
print(type({1, 2, 3}).__name__)         # => set
print(type(None).__name__)              # => NoneType
print(type({'foo': 'bar'}).__name__)    # => dict
