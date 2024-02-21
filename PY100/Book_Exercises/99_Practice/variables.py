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
