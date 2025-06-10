# Given two dictionaries, merge them into a single dictionary

class DictionaryMerger:
    def __init__(self, dict1, dict2):
        self.dict1 = dict1
        self.dict2 = dict2

    def merge(self):
        self.dict1.update(self.dict2)
        return self.dict1

# Example usage
dic1 = {1: "January", 2: "February", 3: "March", 4: "April"}
dic2 = {5: "May", 6: "June", 7: "July", 8: "August"}

merger = DictionaryMerger(dic1, dic2)
merged_dict = merger.merge()
print(merged_dict)
