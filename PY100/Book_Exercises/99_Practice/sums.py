def sums(integer):
    result = 0

    for num in range(integer + 1):
        result += num

    return result


def get_number(prompt):
    entry = input(prompt)
    return int(entry)


number = get_number('Enter a number: ')
result = sums(number)

print(f'Result of the sum from 1 to {number} is: {result}')
