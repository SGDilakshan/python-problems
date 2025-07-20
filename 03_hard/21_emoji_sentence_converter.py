# Write a Python program that takes a sentence as input and replaces certain words with their corresponding emojis using a predefined dictionary. If a word doesn't match, keep it unchanged.

def convert_to_emoji(sentence):
    emoji_dict = {
        "love": "❤️",
        "pizza": "🍕",
        "coffee": "☕",
        "cat": "🐱",
        "dog": "🐶",
        "sun": "☀️",
        "moon": "🌙",
        "happy": "😊",
    }

    # Split sentence into words and punctuation
    words = re.findall(r'\w+|[^\w\s]', sentence, re.UNICODE)

    # Replace words with emojis if found in dictionary
    converted = [
        emoji_dict.get(word.lower(), word) if word.isalpha() else word
        for word in words
    ]

    # Rebuild the sentence with proper spacing
    result = ''
    for i, token in enumerate(converted):
        if i > 0 and re.match(r'\w', token) and re.match(r'\w', converted[i - 1]):
            result += ' '
        elif i > 0 and token not in ",.!?":
            result += ' '
        result += token

    return result


# 🚀 Program entry point
if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    result = convert_to_emoji(user_input)
    print("Converted sentence:", result)
