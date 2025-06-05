# Write a function to remove all duplicate characters from a given string.

def duplicate_string_remove(input_str):
    result = []
    seen = set()
    for char in input_str:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

string = "madam"
print(duplicate_string_remove(string))