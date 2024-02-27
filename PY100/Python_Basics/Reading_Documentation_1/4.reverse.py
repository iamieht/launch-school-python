# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

string = 'hello'
reversed_string = string[::-1]
reversed_string2 = "".join(list(reversed(string)))
print(reversed_string)
print(reversed_string2)
