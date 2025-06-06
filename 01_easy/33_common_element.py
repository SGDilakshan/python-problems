# Create a program that finds the common elements between two lists and stores them in a new list.

def common_element(list1, list2):
    set_list1 = set(list1)
    set_list2 = set(list2)
    new_list = list(set_list1.intersection(set_list2))
    return new_list

list1 = [2, 3, 5, 8, 9, 10]
list2 = [1, 3, 5, 7, 9, 13]

print(common_element(list1, list2))
