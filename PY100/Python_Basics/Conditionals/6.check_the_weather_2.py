# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. Feel free to add more cases besides 'sunny' and 'rainy'.
weather = 'snowy'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print(f"Grab your umbrella.")
    case 'snowy':
        print(f"Put on a jacket.")
    case _:
        print("Let's stay inside.")
