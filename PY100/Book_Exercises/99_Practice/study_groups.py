# 1 Truthiness and Short-Circuit Evaluation


# print(3 and 'foo')   # last evaluated op: 'foo'
# print('foo' and 3)   # last evaluated op: 3
# print(0 and 'foo')   # last evaluated op: 0
# print('foo' and 0)   # last evaluated op: 0

# print(3 or 'foo')    # last evaluated op: 3
# print('foo' or 3)    # last evaluated op: 'foo'
# print(0 or 'foo')    # last evaluated op: 'foo'
# print('foo' or 0)    # last evaluated op: 'foo'
# print('' or 0)       # last evaluated op: 0
# print(None or [])    # last evaluated op: []


# 2 Ask user for a number and return the sums of the values from 1 up to that number inclusive.

# Enter a number: 6
# Result = 21 (which is 1 + 2 + 3 + 4 + 5 + 6)


# 2 Extract the individual digits of a number

# def get_number(prompt):
#     entry = input(prompt)
#     return int(entry)


# def get_length_number(number):
#     return len(str(number))


# def extract_digits(number):
#     num_digits = dict()
#     for digit in range(1, get_length_number(number) + 1):
#         num_digits[digit] = number % 10
#         number = number // 10

#     return num_digits


# def digits_2_places(key):
#     match key:
#         case 1:
#             return "Ones"
#         case 2:
#             return "Tens"
#         case 3:
#             return "Hundreds"
#         case 4:
#             return "Thousands"
#         case 5:
#             return "Ten Thousand"
#         case 6:
#             return "Hundred Thousands"
#         case 7:
#             return "Millions"
#         case 8:
#             return "Ten Millions"
#         case 9:
#             return "Hundred Millions"
#         case 10:
#             return "Billions"


# number = get_number("Enter a number: ")
# num_digits = extract_digits(number)

# for place, value in num_digits.items():
#     print(f'{digits_2_places(place)} place is: {value}')


# match/case

# number = 10


# def greater(number):
#     match (number > 10):
#         case True:
#             return True
#         case False:
#             return False


# print(greater(number))

my_dict = {
    range(5): 'Test',
    'a': 'Test2',
}
print(my_dict[range(5)])  # => raises a Key Error
# print(my_dict[range[2]])  # => raises a TypeError
# print(my_dict.get(range(5)))  # => returns None
