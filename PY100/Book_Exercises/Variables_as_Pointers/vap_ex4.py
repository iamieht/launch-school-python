# Without running this code, what will it print? Why?
dict1 = {
    "a": [1, 2, 3],
    "b": (4, 5, 6),
}

dict2 = dict(dict1)
dict1["a"][1] = 42
print(dict2["a"])  # => [1, 42, 3]

# dict2 is a shallow copy of dict1, and since we have a nested element as part of the values, these have their own location in memory independant from the address in memory of the dictionary. Since shallow copies create a new object for the outermost level, the inner objects are references to the original inner object.
