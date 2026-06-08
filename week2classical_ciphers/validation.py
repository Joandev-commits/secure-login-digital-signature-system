def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def get_valid_input():
    text = input("Enter message to encrypt: ").strip()
    if not text:
        print("Error: Message cannot be empty.")
        return None, None
    if not text.isalpha():
        print("Error: Message must contain letters only.")
        return None, None

    try:
        shift = int(input("Enter shift value (1-25): "))
        if not 1 <= shift <= 25:
            print("Error: Shift must be between 1 and 25.")
            return None, None
    except ValueError:
        print("Error: Shift must be a number.")
        return None, None

    return text, shift

text, shift = get_valid_input()
if text:
    print(f"Encrypted: {caesar_encrypt(text, shift)}")