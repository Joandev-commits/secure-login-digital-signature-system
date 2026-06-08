import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def aes_encrypt(plaintext, key):
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return iv, ciphertext

def test_performance(size_label, data_size):
    message = os.urandom(data_size)
    results = {}

    for bits in [128, 192, 256]:
        key = os.urandom(bits // 8)
        start = time.perf_counter()
        for _ in range(50):
            aes_encrypt(message, key)
        elapsed = (time.perf_counter() - start) / 50
        results[bits] = elapsed

    print(f"\nData size: {size_label}")
    for bits, elapsed in results.items():
        print(f"  AES-{bits}: {elapsed*1000:.4f} ms")

print("=== AES Performance Testing ===")
test_performance("Small  (100 bytes)",   100)
test_performance("Medium (1,000 bytes)", 1000)
test_performance("Large  (10,000 bytes)",10000)

print("\nConclusion: AES-256 provides the strongest security with")
print("acceptable performance for the Secure Login System.")