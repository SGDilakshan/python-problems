# Given a list of dictionaries, find the dictionary with the highest value for a specific key.

def find_dict_with_highest_value(lst_of_dicts, key):
    if not lst_of_dicts:
        return None

    max_dict = lst_of_dicts[0]
    max_value = max_dict.get(key, float("-inf"))

    for d in lst_of_dicts:
        value = d.get(key, float("-inf"))
        if value > max_value:
            max_value = value
            max_dict = d

    return max_dict

# Example usage
list_of_dicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 65},
    {"name": "David", "age": 40}
]

key_to_check = "age"
result = find_dict_with_highest_value(list_of_dicts, key_to_check)

print("Dictionary with the highest value for key '{}':".format(key_to_check), result)
