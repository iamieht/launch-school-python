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
            return "Ones"
        case 2:
            return "Tens"
        case 3:
            return "Hundreds"
        case 4:
            return "Thousands"
        case 5:
            return "Ten Thousand"
        case 6:
            return "Hundred Thousands"
        case 7:
            return "Millions"
        case 8:
            return "Ten Millions"
        case 9:
            return "Hundred Millions"
        case 10:
            return "Billions"


number = get_number("Enter a number: ")
num_digits = extract_digits(number)

for place, value in num_digits.items():
    print(f'{digits_2_places(place)} place is: {value}')
