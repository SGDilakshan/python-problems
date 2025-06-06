# Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence

import string

def check_word_in_sentence(sentence, word):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator).lower()
    cleaned_word = word.lower()
    words = cleaned_sentence.split()
    return cleaned_word in words

sentence = input("Enter a sentence: ")
word = input("Enter a word to check: ")

if check_word_in_sentence(sentence, word):
    print(f"The word '{word}' is present in the sentence.")
else:
    print(f"The word '{word}' is not present in the sentence.")
