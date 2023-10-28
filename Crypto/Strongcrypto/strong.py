from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

with open("plaintext.txt") as f:
    plaintext = f.read().strip()

assert all(
    [c.islower() or c == " " for c in plaintext]
), "invalid characters in plaintext"

private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)

public_key = private_key.public_key()

with open("rsakey.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )


x = [
    pow(ord(c), public_key.public_numbers().e, public_key.public_numbers().n)
    for c in plaintext
]
with open("ciphertext.txt", "w") as f:
    [print(f"{i:x}", file=f) for i in x]
