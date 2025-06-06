# Create a function that takes a list of strings and returns the list sorted by the length of the strings.

def sorted_str_by_length(string):
    return sorted(string, key=len)

string = ["Apple", "dog", "cat", "monkey", "dilli", "kohli"]
print(sorted_str_by_length(string))