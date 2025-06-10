# Implement a function that removes a key-value pair from a dictionary.

def remove_key_value_pair(dictionary, key):
    try:
        value = dictionary.pop(key)
        return value
    except KeyError:
        print("Key not found in the dictionary.")

dictionary = {"a": 1, "b": 2, "c": 3}
removed_value = remove_key_value_pair(dictionary, "b")
print("Removed value:", removed_value)
print("Updated dictionary:", dictionary)
