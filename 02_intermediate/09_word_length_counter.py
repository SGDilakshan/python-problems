# Given a list of words, count the number of words with more than five characters.

word_list = ["apple", "banana", "kiwi", "grape", "strawberry", "blueberry"]

count = 0
for word in word_list:
    if len(word) > 5:
        count += 1

print("Number of words with more than five characters:", count)