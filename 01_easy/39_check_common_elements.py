# Create a program that checks if two sets have any elements in common.

def have_common_elements(set1, set2):
    return bool(set1.intersection(set2))

# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 15, 16, 17, 18, 19}

if have_common_elements(set1, set2):
    print("The sets have elements in common.")
else:
    print("The sets do not have elements in common.")