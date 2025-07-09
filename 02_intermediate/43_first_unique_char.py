# Write a function to find the first non-repeating character in a string and return its index.
# If all characters repeat, return -1.

# first_unique_char.py

from collections import Counter

def first_unique_char(s: str) -> int:
    count = Counter(s)

    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    s = input("Enter a string: ")
    result = first_unique_char(s)
    if result != -1:
        print(f"First non-repeating character is '{s[result]}' at index {result}")
    else:
        print("No non-repeating character found.")
