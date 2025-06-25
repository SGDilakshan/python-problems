# Write a Python program that takes a paragraph of text as input and prints the number of unique words (case-insensitive and ignoring punctuation), as well as the longest word(s) in the paragraph.

import re

def clean_text(text):
    # Remove punctuation and convert to lowercase
    return re.findall(r'\b\w+\b', text.lower())

paragraph = input("Enter a paragraph: ")
words = clean_text(paragraph)

# Get unique words using a set
unique_words = set(words)

# Find the maximum length of any word
max_length = max(len(word) for word in unique_words)

# Find all words with the maximum length
longest_words = [word for word in unique_words if len(word) == max_length]

print(f"Number of unique words: {len(unique_words)}")
print("Longest word(s):")
for word in longest_words:
    print(f"{word} (length {max_length})")
