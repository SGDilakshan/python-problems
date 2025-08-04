# Reverse Words in a Sentence (Not Characters)

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

# Example usage
sentence = input("Enter a sentence: ")
print(reverse_words(sentence))
