# Given a string, write a function to remove all vowels from it and return the modified string.

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in text:
        if letter not in vowels:
            result += letter
    return result

string = input("Enter the string: ")
print("String without vowels:", remove_vowels(string))
