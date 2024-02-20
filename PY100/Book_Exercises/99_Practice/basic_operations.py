# 1. Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value.

print('-------------String Concatenation-------------------')
my_name = 'Ivan' + ' ' + 'Hernandez'
print(my_name)

first_name = 'Ivan'
last_name = 'Hernandez'
print(first_name + ' ' + last_name)

print('-------------String Interpolation-------------------')
print(f'{first_name} {last_name}')

print('-------------String Repetitive Concatenation')
print('Ivan ' * 3)

# 2. Extract the individual digits of 4936
print('--------------Extracting the digits of 4936----------')
number = 4936
one = number % 10
number = number // 10
tens = number % 10
number = number // 10
hundreds = number % 10
number = number // 10
thousands = number % 10

print(f'One place is {one}, Tens place is {tens}',
      f'Hundreds place is {hundreds}, Thousands place is {thousands}')
