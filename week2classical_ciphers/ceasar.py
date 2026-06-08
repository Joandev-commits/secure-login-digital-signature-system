def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, 26 - shift)

message = "SECURITY"
shift = 4

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"Original:  {message}")
print(f"Shift:     {shift}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")