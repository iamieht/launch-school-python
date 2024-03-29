# 1. Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value.

print('-------------String Concatenation-------------------')
my_name = 'Ivan' + ' ' + 'Hernandez'
print(my_name)

first_name = 'Ivan'
last_name = 'Hernandez'
print(first_name + ' ' + last_name)

### Explanation ###
# The plus operator joins when using a String data type.
print()
print('-------------String Interpolation-------------------')
print(f'{first_name} {last_name}')

# f-strings enable string interpolation, which means you can "interpolate" expressions inside curly brackets and they will be evaluated and coerced into a string data type and passed as an argument of the print function, which will log the string to the terminal
print()
print('-------------String Repetitive Concatenation')
print('Ivan ' * 3)

# The multiplication operator when used with string types enable to repetitive concatenation of a string. So the string "Ivan" is concatenated 3 times in the above example, so the print function will log "Ivan Ivan Ivan"

# 2. Extract the individual digits of 4936
print()
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
print()
print("--------------print('5' + '10')---------------------------------")
print('5' + '10')

# The plus (+) operator concatenates the string operands '5' and '10', resulting in a nwe string '510', which is then passed as an argument to the print function, which will log the result in the terminal.

# 4. Refactor the code from the previous exercise to use coercion to print 15 instead.
print()
print("---------------Coercion-----------------------------------------")
print(int('5') + int('10'))

# We see coercion in action in this piece of code. We explicitely tell Python to coerce the string operands into an integer by using the int constructor function and passing the argument "5" and the argument "10" respectively. The result will be the integer 15 which will be passed as an argument to the print function to log it in the terminal

# 5. Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:
print()
print("---------------IndexError: list index out of range--------------")

print("foo=['a', 'b', 'c']")
print('foo[3]')      # will this result in an error?

# Yes, this will raise the exception IndexError: list index out of range as we are trying to access an element from an index that doesn't exist. Python only allows indexing with Inbound indexes. This error is typically known as off-by-one error.

# 6. To what value does the following expression evaluate?
print()
print("--------------'foo' == 'Foo'-------------------------------------")
print('foo' == 'Foo')

# This expression evaluates to the boolean value False as string comparison is case sensitive, so 'foo' is not the same as 'Foo', due to the capital 'F'.

# 7.What will the following code do? Why?
print()
print("----------------ValueError--------------------------------------------")
print("int('3.1415')")

# We are trying to explicitly coerce the string value '3.1414' into an integer by invoking the int construction function, but this will throw an error as the constructor cannot convert a string into an integer when the string value is not a valid integer representation. In this case the string is similar to a float. The int constructor function will raise an error if we pass anything except digits.

# 8. To what value does the following expression evaluate?
print()
print("---------------'12' < '9'----------------------------------------------")
print('12' < '9')

# The expression evaluates as True. When doing String comparisons, Python performs a character-by-character comparison from left to right. So, Python starts comparing '1' < '9' and the result is True, so it stops comparing the remaining characters as the left operand is longer than the right operand
