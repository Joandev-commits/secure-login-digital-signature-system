from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# Load private key
with open("keys/private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

# Load encrypted message
with open("keys/encrypted_message.bin", "rb") as f:
    ciphertext = f.read()

# Decrypt using private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("=== RSA Private Key Decryption ===")
print(f"\nCiphertext length: {len(ciphertext)} bytes")
print(f"Ciphertext (hex):  {ciphertext.hex()[:80]}...")
print(f"\nDecrypted message: {plaintext.decode()}")
print(f"\nDecryption successful using RSA-2048 private key.")