# 1. Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name      Classification
# -------------------------
# index          idiomatic
# CatName        non-idiomatic   CamelCase is used which is reserved for Classes
# lazy_dog       idiomatic
# quick_Fox      non-idiomatic   all letters must be in lowercase
# 1stCharacter   illegal         must start with a character
# operand2       idiomatic
# BIG_NUMBER     non-idiomatic   SCREAMING_SNAKE_CASE reserved for constants
# π              non-idiomatic   non ASCII character

# 2. Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name      Classification
# -------------------------
# index          idiomatic
# CatName        non-idiomatic   CamelCase is used which is reserved for Classes
# lazy_dog       idiomatic
# quick_Fox      non-idiomatic   all letters must be in lowercase
# 1stCharacter   illegal         must start with a character
# operand2       idiomatic
# BIG_NUMBER     non-idiomatic   SCREAMING_SNAKE_CASE reserved for constants
# π              non-idiomatic   non ASCII character

# 3. Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name      Classification
# -------------------------
# index         non-idiomatic   must be in SCREAMING_SNAKE_CASE
# CatName       non-idiomatic   must be in SCREAMING_SNAKE_CASE
# snake_case    non-idiomatic   must be in SCREAMING_SNAKE_CASE
# LAZY_DOG3     idiomatic
# 1ST           illegal         invalid 1st character, cannot be a digit
# operand2      non-idiomatic   must be in SCREAMING_SNAKE_CASE
# BIG_NUMBER    idiomatic
# π             non-idiomatic   not an ASCII character

# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# Name      Classification
# -------------------------
# index         non-idiomatic   must use CamelCase format
# CatName       idiomatic
# Lazy_Dog      non-idiomatic   there is an underscode separating the words
# 1ST           illegal         cannot start with a number
# operand2      non-idiomatic   must use CamelCase format
# BigNumber3    idiomatic
# Πi            non-idiomatic   not an ASCII character

# 5. Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string value 'Victor' in each greeting.
name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')

# First we create a variable name that holds the value 'Victor'. Then we invoke the print function we use an f-string containing a literal string and inside curly braces we interpolate the variable name, which references the value 'Victor'.

# 6. Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now.

print()
print("-------------------age.py---------------------------------------")
age = 46
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# 7. What happens when you run the following code? Why?
print()
print("-----------------------Reassignment of Constants--------------------")
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# In line 74 we initialize a constant NAME with the string value 'Victor' and the next 3 lines we do a string concatenation of a greting + the constant NAME and we pass it to the print function. In Line 79 we reassignt the constant NAME, which is a bad practice as constant must not me reassigned. Unfortunately Python does not have true constants, so we use the SCREAMING_SNAKE_CASE name convention to reflect the constant in out programs.

# 8. Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.
print()
print("------------------ Balance after 5 years -----------------------------")
balance = 1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print(balance)
