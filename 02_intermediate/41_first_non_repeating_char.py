# Write a program to find the first non-repeating character in a given string.

def first_non_repeating_char(s):
    s_lower = s.lower()
    char_count = {}

    # Count occurrences (case-insensitive)
    for char in s_lower:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character in original case
    for i, char in enumerate(s_lower):
        if char_count[char] == 1:
            print(f"First non-repeating character: {s[i]}")
            return
    print("No non-repeating character found")

# Input from user
string = input("Enter a string: ")
first_non_repeating_char(string)
