# main.py (Kurv1x)
import os
import base64
import re


def Generator(length):
    raw_bytes = os.urandom(length)
    base64_encoded = base64.b64encode(raw_bytes).decode()
    salt = re.sub(r'[^A-Za-z0-9]', '', base64_encoded)
    return salt


print(Generator(19))
