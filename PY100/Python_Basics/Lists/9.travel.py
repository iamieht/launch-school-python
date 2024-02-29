# Write a function that, without using the built-in in operator, checks whether a specific destination is included within destinations.
def contains(place, destination):
    for city in destination:
        if city == place:
            return True

    return False


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
