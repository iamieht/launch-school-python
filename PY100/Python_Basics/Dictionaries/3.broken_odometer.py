# delete the 'mileage' key and its associated value from car.
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

car.pop('mileage')
# del car['mileage']
print(car)
