from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded) + unpadder.finalize()

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"Encrypted file: {input_file}")
    print(f"Decrypted file: {output_file}")
    print(f"\nDecrypted contents:")
    print(plaintext.decode())
    print("Decryption successful.")

with open("secret.key", "rb") as f:
    key = f.read()

decrypt_file("encrypted.bin", "decrypted.txt", key)