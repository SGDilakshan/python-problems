# Write a Python program to find the length of the longest word in a sentence.

def longest_word_length(sentence):
    words = sentence.split()
    max_length = 0

    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    return max_length

sentence = input("Enter the sentence: ")
print("Length of the longest word:", longest_word_length(sentence))
