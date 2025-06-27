# Create a program that removes duplicate elements from a list using a set.

def remove_duplicates(input_list):
    return list(set(input_list))

# Example list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

unique_numbers = remove_duplicates(numbers)

print("List after removing duplicates:", unique_numbers)