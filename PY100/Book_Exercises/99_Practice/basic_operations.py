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

# In this example there are two arithmetic operations, modulus and integer division. Modulus returns the remainder of a division, so 4936 divided by 10 is 493.6, modulus 10, returns 6, which in this case is a remainder. When doing integer divion, the return value is a whole number that is less than or equal the floating point result, in this case 4936 // 10 is 493, remainder 6.

# 3. What does the following code do? Why?

print('5' + '10')

# The plus (+) operator concatenates the string operands '5' and '10', resulting in a nwe string '510', which is then passed as an argument to the print function, which will log the result in the terminal.
