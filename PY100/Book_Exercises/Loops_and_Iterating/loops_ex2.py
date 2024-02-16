# Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.

age = int(input("How old are you? "))

print()
print(f"You are {age} years old.")


for year in range(10, 50, 10):
    print(f"In {year} years, you will be {age + year} years old.")
