import copy

print("-------------- List - Shallow Copy---------------------")
list_org = [1, 2, 3]
list_shallow = list(list_org)
print(id(list_org))
print(id(list_shallow))
print(list_org is list_shallow)  # Expected False

print("-------------- List - Deep Copy---------------------")
list_org = [1, 2, 3]
list_deep = copy.deepcopy(list_org)
print(id(list_org))
print(id(list_deep))
print(list_org is list_deep)  # Expected False

print("-------------- List Nested - Shallow Copy---------------------")
list_org = [1, 2, 3, [4, 5, 6]]
list_shallow = list(list_org)
print(id(list_org))
print(id(list_shallow))
print(list_org is list_shallow)  # Expected False
print(list_org[3] is list_shallow[3])  # Expected True

print("-------------- List Nested - Deep Copy---------------------")
list_org = [1, 2, 3, [4, 5, 6]]
list_deep = copy.deepcopy(list_org)
print(id(list_org))
print(id(list_deep))
print(list_org is list_deep)  # Expected False
print(list_org[3] is list_deep[3])  # Expected False

print("-------------- Tuple - Shallow Copy---------------------")
tuple_org = (1, 2, 3)
tuple_shallow = tuple(tuple_org)
print(id(tuple_org))
print(id(tuple_shallow))
print(tuple_org is tuple_shallow)  # Expected True

print("-------------- Tuple - Deep Copy---------------------")
tuple_org = (1, 2, 3)
tuple_deep = copy.deepcopy(tuple_org)
print(id(tuple_org))
print(id(tuple_deep))
print(tuple_org is tuple_deep)  # Expected True

print("-------------- Tuple Nested - Shallow Copy---------------------")
tuple_org = (1, 2, 3, (4, 5, 6))
tuple_shallow = tuple(tuple_org)
print(id(tuple_org))
print(id(tuple_shallow))
print(tuple_org is tuple_shallow)  # Expected True
print(tuple_org[3] is tuple_shallow[3])  # Expected True

print("-------------- Tuple Nested - Deep Copy---------------------")
tuple_org = (1, 2, 3, (4, 5, 6))
tuple_deep = copy.deepcopy(tuple_org)
print(id(tuple_org))
print(id(tuple_deep))
print(tuple_org is tuple_deep)  # Expected True
print(tuple_org[3] is tuple_deep[3])  # Expected True

print("-------------- Set - Shallow Copy---------------------")
set_org = {1, 2, 3}
set_shallow = set(set_org)
print(id(set_org))
print(id(set_shallow))
print(set_org is set_shallow)  # Expected False

print("-------------- Set - Deep Copy---------------------")
set_org = {1, 2, 3}
set_deep = copy.deepcopy(set_org)
print(id(set_org))
print(id(set_deep))
print(set_org is set_deep)  # Expected False

print("-------------- Set Nested - Shallow Copy---------------------")
set_org = {1, 2, 3, frozenset({4, 5, 6})}
set_shallow = set(set_org)
print(id(set_org))
print(id(set_shallow))
print(set_org is set_shallow)  # Expected False

print("-------------- Set Nested - Deep Copy---------------------")
set_org = {1, 2, 3, frozenset({4, 5, 6})}
set_deep = copy.deepcopy(set_org)
print(id(set_org))
print(id(set_deep))
print(set_org is set_deep)  # Expected False

print("-------------- Frozenset - Shallow Copy---------------------")
frozen = frozenset({1, 2, 3})
frozen_shallow = frozenset(frozen)
print(id(frozen))
print(id(frozen_shallow))
print(frozen is frozen_shallow)  # Expected True

print("-------------- Frozenset - Deep Copy -----------------------")
frozen_deep = copy.deepcopy(frozen)
print(id(frozen))
print(id(frozen_deep))
print(frozen is frozen_deep)  # Expected False

print("-------------- Frozenset Nested - Shallow Copy---------------------")
frozen = frozenset({1, 2, 3, (4, 5, 6)})
frozen_shallow = frozenset(frozen)
print(id(frozen))
print(id(frozen_shallow))
print(frozen is frozen_shallow)  # Expected False (why if they are immutable as Tuples)

print("-------------- Frozenset Nested - Deep Copy -----------------------")
frozen_deep = copy.deepcopy(frozen)
print(id(frozen))
print(id(frozen_deep))
print(frozen is frozen_deep)  # Expected False (why if they are immutable as Tuples)

print("-------------- Dictionary - Shallow Copy---------------------")
dict_org = {"a": 1, "b": 2.0}
dict_shallow = dict(dict_org)
print(id(dict_org))
print(id(dict_shallow))
print(dict_org is dict_shallow)  # Expected False

print("-------------- Dictionary - Deep Copy---------------------")
dict_org = {"a": 1, "b": 2.0}
dict_deep = copy.deepcopy(dict_org)
print(id(dict_org))
print(id(dict_deep))
print(dict_org is dict_deep)  # Expected False

print("-------------- Dictionary with Tuple Key - Shallow Copy------------")
dict_org = {"a": 1, "b": 2, (1, 2): 3.0}
dict_shallow = dict(dict_org)
print(id(dict_org))
print(id(dict_shallow))
print(dict_org is dict_shallow)  # Expected False

print("-------------- Dictionary with Tuple Key - Deep Copy------------")
dict_org = {"a": 1, "b": 2, (1, 2): 3.0}
dict_deep = copy.deepcopy(dict_org)
print(id(dict_org))
print(id(dict_deep))
print(dict_org is dict_deep)  # Expected False

print("-------------- Simone Example 1 ------------")
dict1 = {
    "a": [[7, 1], ["aa", "aaa"]],
    "b": ((3, 2), ("bb", "bbb")),
}
dict2 = copy.deepcopy(dict1)
print(dict1 is dict2)
print(dict1["a"] is dict2["a"])
print(dict1["a"][0] is dict2["a"][0])
print(dict1["a"][1] is dict2["a"][1])
print(dict1["b"] is dict2["b"])
print(dict1["b"][0] is dict2["b"][0])
print(dict1["b"][1] is dict2["b"][1])

print("-------------- Simone Example 2 ------------")
dict1 = {
    "a": [[7, 1], ["aa", "aaa"]],
    "b": ([3, 2], ["bb", "bbb"]),
}
dict2 = copy.deepcopy(dict1)
# All of these should print False
print(dict1 is dict2)
print(dict1["a"] is dict2["a"])
print(dict1["a"][0] is dict2["a"][0])
print(dict1["a"][1] is dict2["a"][1])
print(dict1["b"] is dict2["b"])
print(dict1["b"][0] is dict2["b"][0])
print(dict1["b"][1] is dict2["b"][1])
