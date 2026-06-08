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

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

message = "DIGITAL"

print("=== Caesar Cipher ===")
c_enc = caesar_encrypt(message, 4)
c_dec = caesar_decrypt(c_enc, 4)
print(f"Original:  {message}")
print(f"Encrypted: {c_enc}")
print(f"Decrypted: {c_dec}")

print("\n=== Vigenere Cipher ===")
v_enc = vigenere_encrypt(message, "KEY")
v_dec = vigenere_decrypt(v_enc, "KEY")
print(f"Original:  {message}")
print(f"Encrypted: {v_enc}")
print(f"Decrypted: {v_dec}")