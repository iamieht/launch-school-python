# Write a function that returns the first element of a list provided as an argument.
def first(lst):
    if lst:
        return lst[0]
    else:
        return None


print(first(['Earth', 'Moon', 'Mars']))     # Earth
print(first([]))                            # None
