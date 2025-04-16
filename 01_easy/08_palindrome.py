# Create a Python function to check if a given string is a palindrome.

string = input("Enter the word: ")
string_lower = string.lower()

if string_lower == string_lower[::-1]:
    print(string_lower,"is a Palindrome")
else:
    print(string_lower,"is not a Palindrome")