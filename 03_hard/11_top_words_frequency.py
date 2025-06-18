# Write a program that takes a paragraph of text as input and prints the top 3 most frequent words, ignoring case and punctuation.

import re
from collections import Counter

def clean_text(text):
    # Remove punctuation and convert to lowercase
    return re.findall(r'\b\w+\b', text.lower())

paragraph = input("Enter a paragraph: ")
words = clean_text(paragraph)

# Count word frequencies
word_counts = Counter(words)

# Get the top 3 most common words
top_three = word_counts.most_common(3)

print("Top 3 words:")
for word, count in top_three:
    print(f"{word}: {count}")
