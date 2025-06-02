# Given a list of names, print all names starting with the letter ‘A’.

name_list = ["Ram", "arun", "Vijay", "Shankavi", "Kumari", "Aarani", "Abi"]

for name in name_list:
    if name.upper().startswith('A'):
        names = name.capitalize()
        print(names)