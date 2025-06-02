# Write a Python function to check if a given string is a palindrome.

def is_palindrome(text):
    if text == text[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

user_input = input("Enter String: ")
lower_text = user_input.lower()
print(user_input, "is", is_palindrome(lower_text))
