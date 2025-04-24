# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

sentence = input("Enter the sentence: ")
original_sentence = sentence  # Save the original input for display
sentence = sentence.replace(" ", "").lower()

# Use a set to check for all alphabet letters
unique_chars = set(sentence)

# Check if the unique characters contain all the letters of the alphabet
alphabets = set("abcdefghijklmnopqrstuvwxyz")

if alphabets.issubset(unique_chars):
    print(f"'{original_sentence}' is a pangram.")
else:
    print(f"'{original_sentence}' is not a pangram.")