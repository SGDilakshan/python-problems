# Create a program that counts how many times each element appears in a list using a dictionary.

def count_occurrences(input_list):
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Example list
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

occurrences = count_occurrences(numbers)

print("Element occurrences:", occurrences)