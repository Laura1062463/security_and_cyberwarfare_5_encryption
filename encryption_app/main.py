import argparse
from getpass import getpass
from cipher import SymmetricCipher
from key_manager import KeyManager


def main():
    parser = argparse.ArgumentParser(description="Simple AES-256 encryption app")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("gen-key", help="Generate a new symmetric key")
    sub.add_parser("encrypt", help="Encrypt text")
    sub.add_parser("decrypt", help="Decrypt text")

    save = sub.add_parser("save-key", help="Encrypt and save a key with a password")
    save.add_argument("path")

    load = sub.add_parser("load-key", help="Load a key protected by a password")
    load.add_argument("path")

    args = parser.parse_args()

    if args.command == "gen-key":
        key = KeyManager.generate_key()
        print("Generated key (base64):", key.hex())

    elif args.command == "encrypt":
        key_hex = input("Enter key (hex): ").strip()
        cipher = SymmetricCipher(bytes.fromhex(key_hex))
        text = input("Text to encrypt: ")
        print(cipher.encrypt(text))

    elif args.command == "decrypt":
        key_hex = input("Enter key (hex): ").strip()
        cipher = SymmetricCipher(bytes.fromhex(key_hex))
        encrypted = input("Paste encrypted JSON: ")
        print("Decrypted:", cipher.decrypt(encrypted))

    elif args.command == "save-key":
        key_hex = input("Enter key (hex): ").strip()
        password = getpass("Enter password: ")
        KeyManager.save_encrypted(bytes.fromhex(key_hex), password, args.path)

    elif args.command == "load-key":
        password = getpass("Enter password: ")
        key = KeyManager.load_encrypted(password, args.path)
        print("Loaded key (hex):", key.hex())

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
