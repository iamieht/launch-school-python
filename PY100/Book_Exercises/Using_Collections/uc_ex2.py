# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

string = "Launch School"
print(string[4:10])

start = string.find("c")
print(string[start : start + 6])
