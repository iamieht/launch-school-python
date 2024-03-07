# Problem (P)

# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# - Input:
#   - Bill amount (float)
#   - Tip Percentage (float)
# - Output:
#   - Tip Amount (float)
#   - Total Bill Amount (float)
# - Explicit Rules:
# - Implicit Rules:

# Data Structures
# - Float

# Examples/Test Cases (E)
# print(tip_calculator(200, 20))  # => The tip is $40.00 / The total is $240.00

# Algorithm
# - Declare a function tip_calculator with 2 parameters (bill, tip)
#   - Initialize a variable tip_amount = bill * (tip / 100)
#   - Initialize a variable bill_amount = bill + tip_amount
#   - Return both values
# - Declare a function get_input(prompt)
#   - Initialize a variable value = input(prompt)
#   - Return value
# - Declare a main function with no parameters
#   - Initialize variable bill = get_input("What is the bill? ")
#   - Initialize a variable tip_percentage = get_input("What is the tip percentage? ")
#   - Initialize a tuple (bill_amount, tip_amount) = tip_calculator(bill, tip_percentage)
#   - Print(f"The tip is ${tip_amount}"")
#   - print(f"The total is ${bill_amount}"")

# Code
def get_input(prompt):
    value = input(prompt)
    return value


def tip_calculator(bill, tip):
    tip_amount = bill * (tip / 100)
    bill_amount = bill + tip_amount
    return bill_amount, tip_amount


def main():
    bill = float(get_input("What is the bill? "))
    tip_percentage = float(get_input("What is the tip percentage? "))
    bill_amount, tip_amount = tip_calculator(bill, tip_percentage)

    print(f"The tip is ${tip_amount:.2f}")
    print(f"The total is ${bill_amount:.2f}")


main()
