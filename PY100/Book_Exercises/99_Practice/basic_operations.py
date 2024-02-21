# 1. Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value.

print('-------------String Concatenation-------------------')
my_name = 'Ivan' + ' ' + 'Hernandez'
print(my_name)

first_name = 'Ivan'
last_name = 'Hernandez'
print(first_name + ' ' + last_name)

### Explanation ###
# The plus operator joins when using a String data type.

print('-------------String Interpolation-------------------')
print(f'{first_name} {last_name}')

# f-strings enable string interpolation, which means you can "interpolate" expressions inside curly brackets and they will be evaluated and coerced into a string data type and passed as an argument of the print function, which will log the string to the terminal

print('-------------String Repetitive Concatenation')
print('Ivan ' * 3)

# The multiplication operator when used with string types enable to repetitive concatenation of a string. So the string "Ivan" is concatenated 3 times in the above example, so the print function will log "Ivan Ivan Ivan"

# 2. Extract the individual digits of 4936
print('--------------Extracting the digits of 4936----------')
number = 4936
ones = number % 10
number = number // 10
tens = number % 10
number = number // 10
hundreds = number % 10
number = number // 10
thousands = number % 10

print(f'One place is {ones}, Tens place is {tens}',
      f'Hundreds place is {hundreds}, Thousands place is {thousands}')
