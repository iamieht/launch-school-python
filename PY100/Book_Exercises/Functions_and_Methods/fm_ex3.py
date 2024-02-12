# Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(number1, number2):
    return number1 * number2

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

number1 = get_number("Enter the first number: ")
number2 = get_number("Enter the second number: ")
product = multiply(number1, number2)

print(f'{number1} * {number2} = {product}')