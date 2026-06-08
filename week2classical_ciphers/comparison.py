def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

message = "CRYPTOGRAPHY"

caesar_result = caesar_encrypt(message, 4)
vigenere_result = vigenere_encrypt(message, "KEY")

print(f"Original message:       {message}")
print(f"Caesar (shift 4):       {caesar_result}")
print(f"Vigenere (key=KEY):     {vigenere_result}")
print("\nDifferent outputs confirm each cipher uses a different method.")