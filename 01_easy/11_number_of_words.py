# Create a program that takes a sentence as input and counts the number of words in it.

sentence = input("Enter the sentence: ")
no_of_words_in_sentence = len(sentence.split())

print(f'"{sentence}" is made of {no_of_words_in_sentence} words.')
