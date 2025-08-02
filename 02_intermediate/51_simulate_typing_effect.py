# Simulate a Typing Effect in the Console

import time
import sys

def type_text(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline after finishing

# Example usage
sentence = "Welcome to Python World!"
type_text(sentence, delay=0.07)
