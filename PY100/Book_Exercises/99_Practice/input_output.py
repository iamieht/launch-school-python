# 1. Write a program named greeter.py. The program should ask for your name, then output Hello, NAME! where NAME is the name you entered
print("--------------- greeter.py -------------------------------")
name = input("What is your name? ")
print(f'Hello, {name}!')

# In the first line, we initialize a variable name which references the string value read from the terminal using the input() function with a specific prompt. The return value is a string. In the next line we do a string interpolation using f-string and interpolating the variable name in the string Hello and wraping it up in a print function invocation.
