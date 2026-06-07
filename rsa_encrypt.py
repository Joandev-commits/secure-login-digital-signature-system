from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# Load public key
with open("keys/public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

message = "User:Joan|Role:Admin|Access:Granted"

# Encrypt using public key with OAEP padding
ciphertext = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save ciphertext for decryption
with open("keys/encrypted_message.bin", "wb") as f:
    f.write(ciphertext)

print("=== RSA Public Key Encryption ===")
print(f"\nOriginal message:  {message}")
print(f"Message length:    {len(message)} characters")
print(f"\nEncrypted (hex):   {ciphertext.hex()[:80]}...")
print(f"Ciphertext length: {len(ciphertext)} bytes")
print(f"\nEncryption successful using RSA-2048 with OAEP padding.")
print(f"Encrypted message saved to keys/encrypted_message.bin")