# Implement a function to find the length of the longest substring without repeating characters in a given string.

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    start = max_length = 0

    for i, char in enumerate(s):
        # If the character is already in the map and is inside the current window
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1  # Move the start to next of previous char occurrence
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example usage
if __name__ == "__main__":
    test_string = "pwwkew"
    print(f"Input: {test_string}")
    print(f"Output: {length_of_longest_substring(test_string)}")
