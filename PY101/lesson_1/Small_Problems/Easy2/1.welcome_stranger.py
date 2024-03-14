# PEDAC Template

# Problem (P)
# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.


# - Input:
#   - a list: contains 2 or more elements that represent a person's name
#   - a dictionary: contain two keys, title and occupation

# - Output:
#   - a String that contains a person's full name and person's title

# - Explicit Rules:
#   - a list contains 2 or more elements

# - Implicit Rules:

# Examples/Test Cases (E)
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# Data Structures
# - list
# - dictionary

# Algorithm
# - Declare a function greetings with two parameters full_name, occupation of type list and dictionary accordingly.
#   - Initialize a variable full name by joining the elements of the list separatered by spaces
#   - Initialize a variable occupation with the values of the dictionary joined and separated by spaces
#   - Assign the variable greeting with an f-string interpolating the variables full_name and occupation: f"Hello, {full_name}! Nice to have a {occupation} around."

# Code
def greetings(full_name, occupation):
    '''
    full_name: a list
    occupation: a dict with keys: title, occupation
    '''
    full_name = " ".join(full_name)
    occupation = " ".join(occupation.values())
    greeting = f"Hello, {full_name}! Nice to have a {occupation} around."

    return greeting


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
