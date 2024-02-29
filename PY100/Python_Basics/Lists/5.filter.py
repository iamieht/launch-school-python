# Count the number of elements in scores that are 100 or above.
scores = [96, 47, 113, 89, 100, 102]


def count_higher_than_100(lst):
    count = 0

    for element in lst:
        if element >= 100:
            count += 1

    return count


print(count_higher_than_100(scores))
