# Create a set of unique numbers from a list of numbers.

class UniqueNumberSet:
    def __init__(self, numbers):
        self.number_list = numbers
        self.number_set = set(numbers)

    def display_unique_numbers(self):
        print(self.number_set)

numbers = [1, 2, 3, 4, 5, 6, 2, 4, 3, 4, 3, 2, 1, 4, 2, 10]
unique_numbers = UniqueNumberSet(numbers)
unique_numbers.display_unique_numbers()
