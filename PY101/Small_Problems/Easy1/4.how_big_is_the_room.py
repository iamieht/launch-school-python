# Problem (P)

# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

# - Input:
#   - lenght in meters (float)
#   - width in meters (float)
# - Output:
#   - area in square meters (float)
#   - area in square feets  (float)

# - Explicit Rules:
#   - input is always in meters represented by a float number
#   - 1 square meter == 10.7639 square feet
# - Implicit Rules:
#   - The ouput is: "Room's area is: XX square meters / XX square feet
#   - area = length * width
#   - round up to 2 decimal places


# Data Structures
# - Primitive floats

# Algorithm
# - Define a function room_area with 2 parameters (length and width) of type floats
#   - Initialize a variable area_in_meters = length * width
#   - Initialize a variable area_in_sqf = area_in_meters * 10.7639
#   - Print: The room's area is: area_in_meters / area_in_sqf

# Code
def room_area(length, width):
    area_in_meters = length * width
    area_in_feet = area_in_meters * 10.7639

    print(
        f"Room's area is {area_in_meters:.2f} square meters "
        f"({area_in_feet:.2f} square feet).")


length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))

# Examples/Test Cases (E)
# room_area(5, 10)
# # => Room's area is: "50,0 square meters / 538,195 square feet"
# room_area(2.8, 7.9)
# => Room's area is: "22,12 square meters / 236,806 square feet"
room_area(length, width)
# => Room's area is: "50,0 square meters / 538,195 square feet"
