from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

def generate_keypair(name):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    print(f"{name} generated a 2048-bit RSA key pair.")
    return private_key, public_key

def encrypt_message(message, public_key, sender, receiver):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"\n{sender} encrypted message using {receiver}'s public key.")
    print(f"Encrypted (hex): {ciphertext.hex()[:60]}...")
    return ciphertext

def decrypt_message(ciphertext, private_key, receiver):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"\n{receiver} decrypted message using their private key.")
    print(f"Decrypted message: {plaintext.decode()}")
    return plaintext.decode()

print("=== Secure Message Transmission Simulation ===")
print("\n-- Key Generation --")
alice_private, alice_public = generate_keypair("Alice (Sender)")
bob_private, bob_public = generate_keypair("Bob (Receiver)")

print("\n-- Encryption --")
message = "Login credentials verified. Access approved."
print(f"Original message: {message}")
ciphertext = encrypt_message(message, bob_public, "Alice", "Bob")

print("\n-- Decryption --")
decrypted = decrypt_message(ciphertext, bob_private, "Bob")

print(f"\nTransmission successful: {message == decrypted}")