# Create a program that checks if one set is a subset of another.

def is_subset(small_set, large_set):
    return small_set.issubset(large_set)

# Example sets
small_set = {2, 4}
large_set = {1, 2, 3, 4, 5}

if is_subset(small_set, large_set):
    print("The first set is a subset of the second set.")
else:
    print("The first set is not a subset of the second set.")
