# 1. Write a program named greeter.py. The program should ask for your name, then output Hello, NAME! where NAME is the name you entered
print("--------------- greeter.py -------------------------------")
name = input("What is your name? ")
print(f'Hello, {name}!')

# In the first line, we initialize a variable name which references the string value read from the terminal using the input() function with a specific prompt. The return value is a string. In the next line we do a string interpolation using f-string and interpolating the variable name in the string Hello and wraping it up in a print function invocation.

# 2. Modify the greeter.py program to ask for the user's first and last names separately, then greet the user with their full name.
print()
print("---------------- updated greeter.py --------------------------")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print(f'Hello, {first_name} {last_name}!')

# 3. Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now.
print()
print("-------------------- age.py ------------------------------------")
age = input("How old are you? ")
age = int(age)
print()
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')
