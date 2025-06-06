# Given a list of words, find the word with the maximum length and its length.

words = ["apple", "elephant", "dilakshan", "ten", "Software"]

max_word_length = 0
max_word = ""

for word in words:
    if len(word) > max_word_length:
        max_word_length = len(word)
        max_word = word

print("Maximum word:", max_word)
print("Maximum length:", max_word_length)