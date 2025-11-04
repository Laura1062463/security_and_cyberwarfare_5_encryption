from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64
import json

class SymmetricCipher:
    """
    Class voor symmetrische AES-256-GCM encryptie en decryptie.
    """

    def __init__(self, key: bytes):
        if len(key) != 32:
            raise ValueError("Key must be 32 bytes (256 bits).")
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        """
        Versleutel een plaintext string naar JSON met nonce en ciphertext.
        """
        if not plaintext.strip():
            raise ValueError("Plaintext mag niet leeg zijn.")

        aesgcm = AESGCM(self.key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)

        data = {
            "nonce": base64.b64encode(nonce).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

        return json.dumps(data)

    def decrypt(self, encrypted_json: str) -> str:
        """
        Ontsleutel een versleutelde JSON string terug naar plaintext.
        """
        if not encrypted_json.strip():
            raise ValueError("Encrypted input mag niet leeg zijn.")

        try:
            data = json.loads(encrypted_json)
            nonce = base64.b64decode(data["nonce"])
            ciphertext = base64.b64decode(data["ciphertext"])
        except (KeyError, ValueError, json.JSONDecodeError):
            raise ValueError("Ongeldige versleutelde data.")

        try:
            aesgcm = AESGCM(self.key)
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)
            return plaintext.decode()
        except Exception:
            raise ValueError("Decryptie mislukt. Controleer de sleutel of de input.")