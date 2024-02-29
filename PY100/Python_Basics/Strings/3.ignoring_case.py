# Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.
name = 'Roger'
name2 = 'RoGER'

print(name.lower() == name2.lower())
print(name == 'DAVE')

string1 = "SS".lower()
string2 = "ß".lower()
print(string1 == string2)                         # False

string1_casefolded = "SS".casefold()
string2_casefolded = "ß".casefold()
print(string1_casefolded == string2_casefolded)   # True

# When comparing strings in a case-insensitive manner, one might initially try to use the str.lower method, which converts all characters in a string to lowercase. While this method works for many use cases, there are some scenarios in which it doesn't account for all variations in character case.

# The str.casefold method offers a more comprehensive approach to normalizing case than str.lower. It's primarily designed to facilitate case-insensitive string comparisons, especially in languages where conventional methods of converting to lowercase may fall short.

# For instance, the German letter "ß" is a unique lowercase character, but when capitalized, it becomes "SS". If you were to use lower, a string containing SS and another string containing ß would be considered different, even though they are semantically equivalent in German. With casefold, both are normalized to the same representation.
