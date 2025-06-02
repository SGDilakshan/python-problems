# Given a list of names, count the number of names that start with a vowel.

def vowel_start(names):
    count = 0
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for name in names:
        if name.startswith(vowels):
            count += 1
    return count

name_list = ["Ravi", "Abinaiya", "Abi", "Eran", "Vobee", "Dilakshan", "Jathurshy"]
print("Number of names starting with a vowel:", vowel_start(name_list))
