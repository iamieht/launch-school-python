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
