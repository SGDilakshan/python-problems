# Create a function to count the number of vowels in a given string.

def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

# Get input from the user
user_input = input("Enter the string: ")
vowel_count = count_vowels(user_input)

print(f"The number of vowels in '{user_input}' is: {vowel_count}")