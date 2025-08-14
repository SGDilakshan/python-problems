# Write a Python program that takes two lists of numbers, merges them into one list, removes duplicates, and returns the list sorted in ascending order.

def merge_and_sort_unique(list1, list2):
    merged_list = list1 + list2
    unique_list = list(set(merged_list))
    unique_list.sort()
    return unique_list

list1 = [3, 5, 7, 3, 9]
list2 = [2, 5, 7, 10]
print(merge_and_sort_unique(list1, list2))
