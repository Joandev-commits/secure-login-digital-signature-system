from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate RSA 2048-bit key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Serialize keys to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save keys to files
with open("keys/private_key.pem", "wb") as f:
    f.write(private_pem)

with open("keys/public_key.pem", "wb") as f:
    f.write(public_pem)

print("=== RSA 2048-bit Key Pair Generation ===")
print(f"\nPublic Key:")
print(public_pem.decode())
print(f"Private Key (first 3 lines shown for security):")
lines = private_pem.decode().split('\n')
for line in lines[:3]:
    print(line)
print("...")
print("\nKey pair saved to keys/ folder.")
print("Public key:  keys/public_key.pem")
print("Private key: keys/private_key.pem")