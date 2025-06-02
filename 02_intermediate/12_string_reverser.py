# Implement a function that reverses a given string.

def reverse_string(text):
    return text[::-1]

str_input = input("Enter the string: ")
print("Reversed string of", str_input, "is", reverse_string(str_input))