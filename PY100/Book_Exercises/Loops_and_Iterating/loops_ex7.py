# Write a find_integers function that returns a list of all the integers from my_tuple:


def find_integers(tuple):
    list_of_int = []
    for element in tuple:
        if type(element) is int:
            list_of_int.append(element)

    return list_of_int


my_tuple = (1, "a", "1", 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)  # [1, 3, -4]
