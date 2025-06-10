# Write a program that finds the most frequent element in a Iist.

from collections import Counter

class MostFrequentFinder:
    def __init__(self, data):
        self.data = data

    def most_frequent(self):
        counts = Counter(self.data)
        most_common_element = max(counts, key=counts.get)
        return most_common_element

# Example usage
data_list = [1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9]
finder = MostFrequentFinder(data_list)
result = finder.most_frequent()
print("The most frequent element in the list is:", result)