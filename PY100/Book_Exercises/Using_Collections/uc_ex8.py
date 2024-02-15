# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# Line 5 returns a new string from index 21 up to 35. This new string has the letter f located in index 8

# Line 6 searches for the letter f within the index range 21 up to 35 in the same string, so the length is different thant the string returned in line 5.