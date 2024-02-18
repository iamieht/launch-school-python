# Without running this code, what will it print? Why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    "Monty Python": "The Life of Brian",
    "Airplane!": "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2["Monty Python"] = "Holy Grail"
print(dict1["Monty Python"])  # => 'The Life of Brian'

# dict2 is a shallow copy of dict1, meaning that both are different objects. Murating one doesn't affect the other.

# The constructor call dict(dict1) creates a new dict that contains the same key/value pairs as dict1. Thus, dict2 is not the same object as dict1. When we change the value associated with the 'Monty Python' key in dict2, we don't see a corresponding change in dict1.

# This code demonstrates that two identical objects aren't necessarily the same object. If you assign an object associated with variable a to variable b, the variables share that object. However, if the value assigned to b is an entirely new object, there is no sharing, even if the values are identical.
