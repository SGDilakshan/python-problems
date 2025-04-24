# Given a list of names, concatenate them into a single string separated by spaces.

def concatenate_names(names):
    return " ".join(names)

name_list = ["Dilakshan", "Ravi", "Ram", "Kumar", "Shajini"]
concatenated_string_with_spaces = concatenate_names(name_list)

print("Concatenated string with spaces:", concatenated_string_with_spaces)