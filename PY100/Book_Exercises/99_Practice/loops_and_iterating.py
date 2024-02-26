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

# 3. Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.
print('-' * 60)
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1

print()
for element in my_list:
    print(element)

# 4. Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.
print('-' * 60)
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

print()
for element in my_list:
    if element % 2 != 0:
        print(element)

# 5. Print all of the even numbers in the following list of nested lists. Don't use any while loops.
print('-' * 60)
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for lst in my_list:
    for element in lst:
        if element % 2 == 0:
            print(element)

# 6. In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.
print('-' * 60)
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = ['even' if element % 2 == 0 else 'odd' for element in my_list]
print(new_list)
