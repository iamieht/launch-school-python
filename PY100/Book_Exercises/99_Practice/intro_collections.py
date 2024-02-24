# 1. If you have a list named people, how can you determine the number of entries in that list?
people = []
print(len(people))

# 2. Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
stuff = ('hello', 'world', 'bye', 'now')
stuff_list = list(stuff)
stuff_list[2] = 'goodbye'
stuff = tuple(stuff_list)
print(stuff)

# Tuples are immutable sequences, so one possiblity is to create a list out of the tuple, change the element and create a tuple back out of the list.

# 3. Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.
# Differences:      # Tuples are immutable / Lists are mutable.
# Tuples literal () / List literal []
# Similarities:     # Both are sequences
# Both are heterogeneous

# 4. Why can we treat strings as sequences?
# Because they are ordered, you can access the idividual characters with indexing.

# 5. How do the set types differ from the sequence types?
# Sets are unordered collections of unique elements. Their elements cannot be accessed via indexing.

# 6. Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.
pi = 3.141592
str_pi = str(pi)
print(str_pi)

# 7. Without running the following code, identify the numbers that are included in each of the following ranges:
print(list(range(1, 6)))         # 1, 2, 3, 4, 5
print(list(range(7)))            # 0, 1, 2, 3, 4, 5, 6
print(list(range(3, 15, 4)))     # 3, 7, 11
print(list(range(3, 8, -1)))     # []
print(list(range(8, 3, -1)))     # 8, 7, 6, 5, 4

# 8. How would you print all the numbers in the following range?
range(3, 17, 4)
print(list(range(3, 17, 4)))
