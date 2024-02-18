# Without running this code, what will it print? Why?
set1 = {42, "Monty Python", ("a", "b", "c")}
set2 = set1
set1.add(range(5, 10))
print(set2)  # => {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# Set2 references the same object in memory as set1, so mutating one set influences what the other set contains. This code also demonstrates that assigning a variable to another variable doesn't create a new object. Instead, Python copies a reference from the original variable (set1) into the target variable (set2).
