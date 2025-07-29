# Decode an Encoded String

def decode_string(s):
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, repeat = stack.pop()
            current_str = prev_str + current_str * repeat
        else:
            current_str += char

    return current_str


# Example usage
s = "3[a2[c]]"
print("Decoded string:", decode_string(s))  # Output: accaccacc
