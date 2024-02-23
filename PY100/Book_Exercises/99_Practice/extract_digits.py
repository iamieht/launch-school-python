def get_number(prompt):
    entry = input(prompt)
    return int(entry)


def get_length_number(number):
    return len(str(number))


def extract_digits(number):
    num_digits = dict()
    for digit in range(1, get_length_number(number) + 1):
        num_digits[digit] = number % 10
        number = number // 10

    return num_digits


def digits_2_places(key):
    match key:
        case 1:
            return "ones"
        case 2:
            return "tens"
        case 3:
            return "hundreds"
        case 4:
            return "thousands"
        case 5:
            return "ten thousand"
        case 6:
            return "hundred thousands"
        case 7:
            return "millions"
        case 8:
            return "ten millions"
        case 9:
            return "hundred millions"
        case 10:
            return "billions"


def get_place_values(key):
    PLACE_VALUES = {
        1:  'ones',
        2:  'tens',
        3:  'hundreds',
        4:  'thousands',
        5:  'ten thousand',
        6:  'hundred thousands',
        7:  'millions',
        8:  'ten millions',
        9:  'hundred millions',
        10: 'billions',
    }
    return PLACE_VALUES.get(key, None)


def main():
    number = get_number("Enter a positive integer: ")
    num_digits = extract_digits(number)

    for key, value in num_digits.items():
        # print(f'The {digits_2_places(place)} place is: {value}')
        print(f'The {get_place_values(key)} place is: {value}')


main()
