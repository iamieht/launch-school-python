# Write a function that takes a single integer argument and prints a message that describes whether:

# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def get_range(int):
    if int < 0:
        print(f'{int} is less than 0')
    elif int <= 50:
        print(f'{int} is between 0 and 50')
    elif int <= 100:
        print(f'{int} is between 51 and 100')
    else:
        print(f'{int} is greater than 100')

get_range(-1) # The value is less than 0
get_range(0)  # The value is between 0 and 50
get_range(50) # The value is between 0 and 50
get_range(51) # The value is between 51 and 100
get_range(100) # The value is between 51 and 100
get_range(101) # The value is greater than 100