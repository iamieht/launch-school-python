# 1. In your own words, explain the difference between these two expressions.
# import copy
# my_object1 == my_object2
# my_object1 is my_object2

# The first expression compares whether the two objects have the same value
# The second expression compares whether both objects reference the same object.

# 2. Without running this code, what will it print? Why?
import copy
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

# 5. Write some code to create a deep copy of the dict1 object and assign it to dict2.
dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1 is dict2)
print(dict1['a'] is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b'] is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# 6. The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1.
print('-' * 60)
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa'], 2],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1 is dict2)
print(dict1['a'] is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['a'][2] is dict2['a'][2])
print(dict1['b'] is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
