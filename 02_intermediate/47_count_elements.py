# Count Vowels, Consonants, Digits, and Special Characters

def count_elements(text):
    vowels = "aeiouAEIOU"
    vowel_count = consonant_count = digit_count = special_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():
            special_count += 1

    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)
    print("Digits:", digit_count)
    print("Special Characters:", special_count)

# Example usage
user_input = input("Enter a string: ")
count_elements(user_input)
