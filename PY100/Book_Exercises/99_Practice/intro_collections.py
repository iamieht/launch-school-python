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
