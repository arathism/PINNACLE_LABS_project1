import os
from cryptography.fernet import Fernet, InvalidToken


KEY_FILE = "secret.key"


def generate_key():
    """Generate and save a new encryption key."""
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    return key


def load_key():
    """Load the existing key or create one if it doesn't exist."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()

    return generate_key()


def encrypt_message(cipher, message):
    """Encrypt a text message."""
    encrypted = cipher.encrypt(message.encode("utf-8"))
    return encrypted.decode("utf-8")


def decrypt_message(cipher, encrypted_message):
    """Decrypt an encrypted message."""
    decrypted = cipher.decrypt(
        encrypted_message.encode("utf-8")
    )
    return decrypted.decode("utf-8")


def main():
    key = load_key()
    cipher = Fernet(key)

    while True:
        print("\n===================================")
        print(" TEXT ENCRYPTION AND DECRYPTION")
        print("===================================")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")

            encrypted = encrypt_message(cipher, message)

            print("\nEncrypted message:")
            print(encrypted)

        elif choice == "2":
            encrypted_message = input(
                "Enter the encrypted message: "
            ).strip()

            try:
                decrypted = decrypt_message(
                    cipher, encrypted_message
                )

                print("\nDecrypted message:")
                print(decrypted)

            except InvalidToken:
                print(
                    "\nError: Invalid encrypted message "
                    "or incorrect key."
                )

            except UnicodeDecodeError:
                print("\nError: Unable to decode the message.")

        elif choice == "3":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()