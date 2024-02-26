# 1. The following code causes an infinite loop (a loop that never stops iterating). Why?
# counter = 0

# while counter < 5:
#     print(counter)

# The code doesn't modify the value of counter, so the expression counter < 5 is always truthy, causing an infinite loop

# 2. Age.py
import random
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

# 7. Write a find_integers function that returns a list of all the integers from my_tuple:
print('-' * 60)


def find_integers(iterable):
    return [element for element in iterable if type(element) is int]


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

# 8. Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings:
print('-' * 60)
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {element: len(element)
           for element in my_set if len(element) % 2 != 0}
print(my_dict)

# 9. Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n:
print('-' * 60)


def factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= num

    return result


print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

# 10. The following code uses the randrange function from Python's math library to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds a random number that matches the last number in the range. Refactor the code so it doesn't require two different invocations of randrange:

# highest = 10
# number = random.randrange(highest + 1)
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)
print('-' * 60)
highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# 11. Print all of the even numbers in the following list of nested lists. This time, don't use any for loops:
print('-' * 60)
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

index = 0
while index < len(my_list):
    subindex = 0
    nested_lst = my_list[index]
    while subindex < len(nested_lst):
        if nested_lst[subindex] % 2 == 0:
            print(nested_lst[subindex])

        subindex += 1
    index += 1
