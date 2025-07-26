# Write a Python program that takes a list of words and groups them into lists of anagrams.
# Two words are anagrams if they contain the same letters in a different order.

from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))  # Sort letters to form key
        anagram_map[key].append(word)

    return list(anagram_map.values())


# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Grouped Anagrams:", group_anagrams(words))
