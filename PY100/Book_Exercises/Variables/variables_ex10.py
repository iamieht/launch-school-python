# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd'        # reassignment
obj.upper()         # neither
obj = obj.lower()   # reassignment
print(len(obj))     # neither
obj = list(obj)     # reassignment
obj.pop()           # mutation
obj[2] = 'X'        # mutation
obj.sort()          # mutation
set(obj)            # neither
obj = tuple(obj)    # reassignment