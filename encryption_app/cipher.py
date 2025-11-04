from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, base64, json


class SymmetricCipher:

    def __init__(self, key: bytes):
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes (256 bits).")
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        aesgcm = AESGCM(self.key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)

        data = {
            "nonce": base64.b64encode(nonce).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }
        return json.dumps(data)

    def decrypt(self, encrypted_json: str) -> str:
        data = json.loads(encrypted_json)
        aesgcm = AESGCM(self.key)
        nonce = base64.b64decode(data["nonce"])
        ciphertext = base64.b64decode(data["ciphertext"])
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        return plaintext.decode()
