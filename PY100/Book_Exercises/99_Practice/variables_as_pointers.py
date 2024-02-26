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

# set1 and set2 reference the same object in memory, as in line 10 set2 was assigned a shallow copy of set1
