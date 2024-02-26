# 1. In your own words, explain the difference between these two expressions.
my_object1 == my_object2
my_object1 is my_object2

# The first expression compares whether the two objects have the same value
# The second expression compares whether both objects reference the same object.

# 2. Without running this code, what will it print? Why?
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)  # => {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# set1 and set2 reference the same object in memory.

# 3. Without running this code, what will it print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])  # => The Life of Brian

# dict2 is a new object (a shallow copy of dict1) in memory, so a modification of dict2 doesn't affect the referenced object of dict1

# 4. Without running this code, what will it print? Why?
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])  # => [1, 42, 3]

# dict2 is a shallow copy of dict1, so the nested elements are referenced to the same nested elements of the original dictionary. Any mutation of these nested elements will be visible by both objects.
