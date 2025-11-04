import os, json, base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class KeyManager:

    @staticmethod
    def generate_key() -> bytes:
        return os.urandom(32) 

    @staticmethod
    def save_encrypted(key: bytes, password: str, path: str):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=200_000
        )
        kek = kdf.derive(password.encode())
        aes = AESGCM(kek)
        nonce = os.urandom(12)
        wrapped = aes.encrypt(nonce, key, None)

        data = {
            "salt": base64.b64encode(salt).decode(),
            "nonce": base64.b64encode(nonce).decode(),
            "key": base64.b64encode(wrapped).decode()
        }
        with open(path, "w") as f:
            json.dump(data, f)
        print(f"Encrypted key saved to {path}")

    @staticmethod
    def load_encrypted(password: str, path: str) -> bytes:
        with open(path, "r") as f:
            data = json.load(f)

        salt = base64.b64decode(data["salt"])
        nonce = base64.b64decode(data["nonce"])
        wrapped = base64.b64decode(data["key"])

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=200_000
        )
        kek = kdf.derive(password.encode())
        aes = AESGCM(kek)
        key = aes.decrypt(nonce, wrapped, None)
        return key
