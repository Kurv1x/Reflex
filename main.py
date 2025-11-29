import base64
import hashlib
import os

from cryptography.fernet import Fernet


def fernet_key_from_password(password: str, salt: bytes):
    raw_key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200_000, dklen=32)
    return base64.urlsafe_b64encode(raw_key)


# --- Get user data ---
password = input("Password for encryption: ")
data = input("Data to encrypt: ").encode()

salt = os.urandom(16)
key = fernet_key_from_password(password, salt)
f = Fernet(key)

encrypted = f.encrypt(data)

print("\n=== Your Encrypted Payload ===")
print(encrypted)
print("\n=== Your Salt (save this!) ===")
print(base64.b64encode(salt).decode())
