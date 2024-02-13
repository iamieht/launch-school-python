my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal? 
#   Yes they are equal as both contain the same elements

# Are the lists assigned to my_list and another_list the same object? 
#   No, they are different objects. The constructof function list() creates a shallow copy of the original list, creating a new object.

# Are the nested lists at index 3 of my_list and another_list equal? 
# Yes they are equal as both elements are the same

# Are the nested lists at index 3 of my_list and another_list the same object? 
#   Yes they are, the list constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied. 