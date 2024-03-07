# Problem (P)

# Build a program that asks the user to enter the length and width of a room, and let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

# - Input:
#   - unit of measure (meters or feet)
#   - lenght (float)
#   - width (float)
# - Output:
#   - area in unit of measure and conversion to meter or feet (float)

# - Explicit Rules:
#   - 1 square meter == 10.7639 square feet
# - Implicit Rules:
#   - The ouput is: "Room's area is: XX square meters / XX square feet
#   - area = length * width
#   - round up to 2 decimal places


# Data Structures
# - Primitive floats

# Algorithm
# - Define a function get_input with parameter prompt
#   - Initialize a variable value with input(prompt)
#   - Return the value
# - Define a function room_area with 3 parameters (uom (string), length and width) of type floats
#   - If uom is meters:
#       - Initialize a variable area_in_meters = length * width
#       - Initialize a variable area_in_sqf = area_in_meters * 10.7639
#   - If uom is feet:
#       - Initialize a variable area_in_feet = length * width
#       - Initialize a variable area_in_meters = area_in_feet / 10.7639
#   - Print: The room's area is: area_in_meters / area_in_sqf

# Code
def get_input(prompt):
    value = input(prompt)
    return value

def room_area(length, width):
    area = length * width
    return area

def meters_2_feet(meters):
    return meters * 10.7639

def feet_2_meters(feet):
    return feet / 10.7639

    print(
        f"Room's area is {area_in_meters:.2f} square meters "
        f"({area_in_feet:.2f} square feet).")

print("Welcome to Calculate Room's Area")
uom = get_input("Enter the Unit of Measure: Meters(m) / Feet(f) ")
length = float(get_input(f"Enter the length of the room in "
                    f"{"Meters" if uom == 'm'   else "Feet" } "))

width = float(get_input(f"Enter the width of the room in "
                    f"{"Meters" if uom == 'm'   else "Feet"} "))

if uom == 'm':
    area_in_meters = room_area(length, width)
    area_in_feet   = meters_2_feet(area_in_meters)
    print(f"Room's area is {area_in_meters:.2f} square meters "
          f"({area_in_feet:.2f} square feet.)")
elif uom == 'f':
    area_in_feet = room_area(length, width)
    area_in_meters = feet_2_meters(area_in_feet)
    print(f"Room's area is {area_in_feet:.2f} square feet "
          f"({area_in_meters:.2f} square meters)")
    
# Examples/Test Cases (E)
# room_area(5, 10)
# # => Room's area is: "50,0 square meters / 538,195 square feet"
# room_area(2.8, 7.9)
# => Room's area is: "22,12 square meters / 236,806 square feet"
# room_area(length, width)
# => Room's area is: "50,0 square meters / 538,195 square feet"
