# Write a Python program that checks if a given password is strong.
# A strong password should:
# Be at least 8 characters long
# Contain at least one uppercase letter
# Contain at least one lowercase letter
# Contain at least one digit
# Contain at least one special character (e.g., !@#$%^&*())

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak password. Must be at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return "Weak password. Must include at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Weak password. Must include at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Weak password. Must include at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak password. Must include at least one special character."

    return "Strong password."

# Example usage
password = input("Enter a password to check: ")
print(check_password_strength(password))
