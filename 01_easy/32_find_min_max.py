# Write a program that finds the largest and smallest elements in a list.

num = [7, 5, 4, -3, 5, 9, -2, -4]

large = num[0]
small = num[0]

for i in num:
    if i > large:
        large = i
    if i < small:
        small = i

print("Largest Number", large)
print("Smallest Number", small)
