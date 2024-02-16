# Print all of the even numbers in the following list of nested lists. Don't use any while loops.
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for element in my_list:
    for num in element:
        if num % 2 == 0:
            print(num)
