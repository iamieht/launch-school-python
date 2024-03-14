
# Problem (P)
# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.

# - Input:
#   - noun: string
#   - verb: srting
#   - adjective: string
#   - adverb: string

# - Output:
#   - a story of type string

# - Explicit Rules:
#   - Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

# - Implicit Rules:

# Examples/Test Cases (E)
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly
# Output:
# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

# Data Structures

# Algorithm
# - Declare a function get_value(prompt)
#   - Initialize a variable value = input(prompt)
#   - return value
# - Declare a function madlibs that takes 4 arguments: noun, verb, adjective, adverb
#   - Returns an f-string: (f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"


# Code
def get_value(prompt):
    value = input(prompt)
    return value


def madlibs(noun, verb, adjective, adverb):
    return (f"Do you {verb} your {adjective} {noun} {adverb}?"
            f" That's hilarious!\n"
            f"The {adjective} {noun} {verb}s {adverb} over the lazy dog.\n"
            f"The {noun} {adverb} {verb}s up to Joe's blue turtle.")


def main():
    noun = get_value("Enter a noun: ")
    verb = get_value("Enter a verb: ")
    adjective = get_value("Enter an adjective: ")
    adverb = get_value("Enter an adverb: ")
    print()
    print(madlibs(noun, verb, adjective, adverb))


main()
