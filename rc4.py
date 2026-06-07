def rc4_keystream(key, length):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    keystream = []
    i = j = 0
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 256])
    return keystream

def rc4_encrypt(message, key):
    key_bytes = [ord(c) for c in key]
    keystream = rc4_keystream(key_bytes, len(message))
    encrypted = [ord(c) ^ k for c, k in zip(message, keystream)]
    return encrypted

def rc4_decrypt(encrypted, key):
    key_bytes = [ord(c) for c in key]
    keystream = rc4_keystream(key_bytes, len(encrypted))
    decrypted = "".join(chr(c ^ k) for c, k in zip(encrypted, keystream))
    return decrypted

message = "SecureLogin"
key = "SECRET"

encrypted = rc4_encrypt(message, key)
decrypted = rc4_decrypt(encrypted, key)

print(f"Original:  {message}")
print(f"Key:       {key}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"\nDecryption successful: {message == decrypted}")