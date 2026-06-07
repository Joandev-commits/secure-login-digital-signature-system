import time

def rc4_keystream(key, length):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
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
    return [ord(c) ^ k for c, k in zip(message, keystream)]

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def lcg_encrypt(message, seed):
    x = seed
    result = []
    for char in message:
        x = (1664525 * x + 1013904223) % 256
        result.append(ord(char) ^ x)
    return result

message = "A" * 1000
key = "SECRET"

# RC4
start = time.perf_counter()
for _ in range(100):
    rc4_encrypt(message, key)
rc4_time = (time.perf_counter() - start) / 100

# Caesar
start = time.perf_counter()
for _ in range(100):
    caesar_encrypt(message, 4)
caesar_time = (time.perf_counter() - start) / 100

# LCG
start = time.perf_counter()
for _ in range(100):
    lcg_encrypt(message, 42)
lcg_time = (time.perf_counter() - start) / 100

print("=== Encryption Performance Results ===")
print(f"Message size: {len(message)} characters\n")
print(f"Caesar Cipher:  {caesar_time*1000:.4f} ms")
print(f"LCG XOR Cipher: {lcg_time*1000:.4f} ms")
print(f"RC4 Cipher:     {rc4_time*1000:.4f} ms")
print(f"\nFastest: {'Caesar' if caesar_time < lcg_time and caesar_time < rc4_time else 'LCG' if lcg_time < rc4_time else 'RC4'}")
print(f"RC4 is suitable for real-time encryption due to its low overhead.")