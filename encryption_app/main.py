import argparse
from getpass import getpass
from cipher import SymmetricCipher
from key_manager import KeyManager

def main():
    parser = argparse.ArgumentParser(description="Simple AES-256 encryption app")
    sub = parser.add_subparsers(dest="command")

    # Basis commands
    sub.add_parser("gen-key", help="Generate a new symmetric key")
    sub.add_parser("encrypt", help="Encrypt text")
    sub.add_parser("decrypt", help="Decrypt text")

    # Opslag en laden van sleutel met wachtwoord
    save = sub.add_parser("save-key", help="Encrypt and save a key with a password")
    save.add_argument("path", help="Pad om de sleutel op te slaan")
    load = sub.add_parser("load-key", help="Load a key protected by a password")
    load.add_argument("path", help="Pad van opgeslagen sleutel")

    # Demo command om alles in één keer te laten zien
    sub.add_parser("demo", help="Run a demo encryption/decryption session")

    args = parser.parse_args()

    try:
        if args.command == "gen-key":
            key = KeyManager.generate_key()
            print("Generated key (hex):", key.hex())

        elif args.command == "encrypt":
            key_hex = input("Enter key (hex, 64 characters): ").strip()
            if len(key_hex) != 64:
                raise ValueError("Sleutel moet 64 hex characters zijn (256 bits).")
            cipher = SymmetricCipher(bytes.fromhex(key_hex))
            text = input("Text to encrypt: ").strip()
            print("Encrypted JSON:", cipher.encrypt(text))

        elif args.command == "decrypt":
            key_hex = input("Enter key (hex, 64 characters): ").strip()
            if len(key_hex) != 64:
                raise ValueError("Sleutel moet 64 hex characters zijn (256 bits).")
            cipher = SymmetricCipher(bytes.fromhex(key_hex))
            encrypted = input("Paste encrypted JSON: ").strip()
            print("Decrypted:", cipher.decrypt(encrypted))

        elif args.command == "save-key":
            key_hex = input("Enter key (hex, 64 characters): ").strip()
            if len(key_hex) != 64:
                raise ValueError("Sleutel moet 64 hex characters zijn (256 bits).")
            password = getpass("Enter password to encrypt key: ")
            KeyManager.save_encrypted(bytes.fromhex(key_hex), password, args.path)
            print(f"Key saved securely to {args.path}")

        elif args.command == "load-key":
            password = getpass("Enter password to decrypt key: ")
            key = KeyManager.load_encrypted(password, args.path)
            print("Loaded key (hex):", key.hex())

        elif args.command == "demo":
            print("=== Demo sessie ===")
            key = KeyManager.generate_key()
            print("Generated key (hex):", key.hex())

            cipher = SymmetricCipher(key)
            sample_text = "Hello World!"
            print("Plaintext:", sample_text)
            encrypted = cipher.encrypt(sample_text)
            print("Encrypted JSON:", encrypted)
            decrypted = cipher.decrypt(encrypted)
            print("Decrypted text:", decrypted)
            print("=== Demo klaar ===")

        else:
            parser.print_help()

    except Exception as e:
        print("Fout:", e)

if __name__ == "__main__":
    main()
