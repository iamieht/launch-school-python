# Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result 

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str, my_list, my_tuple, my_range)))