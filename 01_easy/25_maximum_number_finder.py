# Implement a program that finds the largest number in a list.

list = [47, -92, 16, 75, -23, 58, 34, 89, 61, 7, 145]
max = list[0]

for i in list:
    if i > max:
        max = i
print("Maximum Number in the list is",max)