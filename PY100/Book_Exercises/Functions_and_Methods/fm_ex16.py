# In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names:
## multiply: line 3 and 11
## get_num: line 6, 9 and 10
## float: line 7
## input: line 7
## print: line 12

# Parameters:
## left, right: line 3
## prompt: line 6