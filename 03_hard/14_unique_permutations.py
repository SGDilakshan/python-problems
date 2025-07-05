# Write a Python function that returns all possible unique permutations of a given string.
# Make sure it works even if the string has duplicate characters.

from itertools import permutations


def unique_permutations(s):
    # Generate all permutations
    all_perms = permutations(s)

    # Use a set to remove duplicates
    unique = set([''.join(p) for p in all_perms])

    return list(unique)


# Example usage
input_str = input("Enter a string: ")
result = unique_permutations(input_str)

print("Unique permutations:")
for r in result:
    print(r)

