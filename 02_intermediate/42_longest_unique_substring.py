# Write a Python program to find the longest substring without repeating characters in a given string. Also return the length of that substring.

def longest_unique_substring(s):
    start = 0
    max_length = 0
    max_substring = ""
    char_index = {}

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = i
        current_length = i - start + 1
        if current_length > max_length:
            max_length = current_length
            max_substring = s[start:i + 1]

    return max_substring, max_length


# Input from user
input_str = input("Enter a string: ")
substring, length = longest_unique_substring(input_str)

print(f"Longest substring without repeating characters: '{substring}'")
print(f"Length: {length}")
