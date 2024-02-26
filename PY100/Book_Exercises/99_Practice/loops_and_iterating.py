# 1. The following code causes an infinite loop (a loop that never stops iterating). Why?
# counter = 0

# while counter < 5:
#     print(counter)

# The code doesn't modify the value of counter, so the expression counter < 5 is always truthy, causing an infinite loop

# 2. Age.py
age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')

for year in range(10, 50, 10):
    print(f'In {year} years, you will be {age + year} years old.')
