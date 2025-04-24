# Create a function to reverse a given string.

def reverse_string(s):
    return s[::-1]

string = input("Enter the String: ")
reversed_str = reverse_string(string)

print("Original string:", string)
print("Reversed string:", reversed_str)