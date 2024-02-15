pets = {
    "Cat": "Meow",
    "Dog": "Bark",
    "Bird": "Tweet",
}

# Write some code to print Bark by accessing the element associated with the key Dog.

print(pets["Dog"])
print(pets.get("Dog"))

# Write some code to print None when you try to print the value associated with the non-existent key, Lizard.

print(pets.get("Lizard"))

# Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.

print(pets.get("Lizard", "<silence>"))
