import base64
import os
from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AESCipher:
    def __init__(self, passphrase: str):
        self.key = passphrase.encode("utf-8").ljust(32, b"0")[:32]

    def encrypt(self, plaintext: str) -> str:
        iv = get_random_bytes(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ct = cipher.encrypt(pad(plaintext.encode("utf-8"), AES.block_size))
        return base64.b64encode(iv + ct).decode("utf-8")

    def decrypt(self, b64_blob: str) -> str:
        raw = base64.b64decode(b64_blob)
        iv, ct = raw[:16], raw[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode("utf-8")


class DESCipher:
    def __init__(self, passphrase: str):
        self.key = passphrase.encode("utf-8").ljust(8, b"0")[:8]

    def encrypt(self, plaintext: str) -> str:
        iv = get_random_bytes(8)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        ct = cipher.encrypt(pad(plaintext.encode("utf-8"), DES.block_size))
        return base64.b64encode(iv + ct).decode("utf-8")

    def decrypt(self, b64_blob: str) -> str:
        raw = base64.b64decode(b64_blob)
        iv, ct = raw[:8], raw[8:]
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), DES.block_size)
        return pt.decode("utf-8")


class RSACipher:
    def __init__(self, key_dir="rsa_keys"):
        os.makedirs(key_dir, exist_ok=True)
        priv_path = os.path.join(key_dir, "private.pem")
        pub_path = os.path.join(key_dir, "public.pem")

        if os.path.exists(priv_path) and os.path.exists(pub_path):
            self.private_key = RSA.import_key(open(priv_path, "rb").read())
            self.public_key = RSA.import_key(open(pub_path, "rb").read())
        else:
            key = RSA.generate(2048)
            self.private_key = key
            self.public_key = key.publickey()
            with open(priv_path, "wb") as f:
                f.write(self.private_key.export_key())
            with open(pub_path, "wb") as f:
                f.write(self.public_key.export_key())

    def encrypt(self, plaintext: str) -> str:
        cipher = PKCS1_OAEP.new(self.public_key)
        ct = cipher.encrypt(plaintext.encode("utf-8"))
        return base64.b64encode(ct).decode("utf-8")

    def decrypt(self, b64_blob: str) -> str:
        cipher = PKCS1_OAEP.new(self.private_key)
        pt = cipher.decrypt(base64.b64decode(b64_blob))
        return pt.decode("utf-8")


def main():
    print("=" * 55)
    print("   TEXT ENCRYPTION TOOL — AES | DES | RSA")
    print("=" * 55)

    while True:
        print("\nChoose algorithm:")
        print("  1. AES (recommended, symmetric)")
        print("  2. DES (legacy, symmetric — for comparison only)")
        print("  3. RSA (asymmetric, public/private keypair)")
        print("  4. Exit")
        choice = input("Enter choice [1-4]: ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3"):
            print("Invalid choice, try again.")
            continue

        action = input("Encrypt or Decrypt? [e/d]: ").strip().lower()

        if choice in ("1", "2"):
            passphrase = input("Enter a passphrase/key: ").strip()
            cipher = AESCipher(passphrase) if choice == "1" else DESCipher(passphrase)
        else:
            cipher = RSACipher()
            print("(Using RSA keypair in ./rsa_keys/ — generated on first run)")

        if action == "e":
            text = input("Enter text to encrypt: ")
            try:
                result = cipher.encrypt(text)
                print(f"\nEncrypted (Base64):\n{result}")
            except Exception as e:
                print(f"Error: {e}")
        elif action == "d":
            text = input("Enter Base64 ciphertext to decrypt: ").strip()
            try:
                result = cipher.decrypt(text)
                print(f"\nDecrypted text:\n{result}")
            except Exception as e:
                print(f"Error: {e} (wrong key, or corrupted/invalid ciphertext)")
        else:
            print("Invalid action.")


if __name__ == "__main__":
    main()