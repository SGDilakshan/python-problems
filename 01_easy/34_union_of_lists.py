# Implement a function that takes two lists and returns their union (all unique elements from both lists).

list1 = [1,3,5,7,9,11,13,15,17,19]
list2 = [2,3,5,7,11,13,17,19]

set1 = set(list1)
set2 = set(list2)
union = set1.union(set2)
print(union)