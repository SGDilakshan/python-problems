# Given a list of names, remove all duplicate names and print the unique names.

def remove_duplicate_name(names):
    seen = set()
    unique_names = []

    for name in names:
        if name not in seen:
            unique_names.append(name)
            seen.add(name)

    for unique_name in unique_names:
        print(unique_name)

names_list = ["Dilakshan", "Thinesh", "Dilakshan", "Sivanthan", "Abinash", "Abinash", "Sharuja"]
remove_duplicate_name(names_list)
