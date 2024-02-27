# How would you determine the index of the fruit "cherry" in this list?
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
idx_cherry = fruits.index('cherry') if 'cherry' in fruits else 'N/A'
print(idx_cherry)  # 2

# The index method, when applied to a list, returns the first occurrence of the specified value. However, if the value isn't found, it raises a ValueError. This is why it's often a good practice to first check whether the value exists in the list using the in keyword before attempting to find its index. This prevents potential runtime errors and makes your code more resilient to unexpected input.
