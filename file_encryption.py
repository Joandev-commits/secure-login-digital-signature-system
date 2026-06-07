import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

    print(f"Original file:  {input_file} ({len(plaintext)} bytes)")
    print(f"Encrypted file: {output_file} ({len(iv + ciphertext)} bytes)")
    print(f"IV:             {iv.hex()}")
    print(f"Encryption successful.")

key = os.urandom(32)
encrypt_file("plaintext.txt", "encrypted.bin", key)

# save key for decryption in next script
with open("secret.key", "wb") as f:
    f.write(key)

print("\nKey saved to secret.key for decryption.")