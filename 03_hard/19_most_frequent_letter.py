# Write a Python program to find the most frequent letter in a given string (ignoring spaces and case sensitivity). If multiple letters have the same highest frequency, return the alphabetically first one.

def most_frequent_letter(text):
    text = text.lower().replace(" ", "")
    freq = {}

    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    max_count = max(freq.values())
    most_frequent = sorted([k for k, v in freq.items() if v == max_count])[0]

    return most_frequent

# Example usage
input_text = "Sssssssssimple Python Practice"
print("Most frequent letter:", most_frequent_letter(input_text))
