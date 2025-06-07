# Write a Python program to count the occurrences of each element in a given list.

def count_occurrences(lst):
    counts = {}
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts

words = ["apple", "elephant", "dilakshan", "ten", "ten", "AmmA"]
occurrences = count_occurrences(words)

for element, count in occurrences.items():
    print(f"'{element}' occurs {count} times.")
