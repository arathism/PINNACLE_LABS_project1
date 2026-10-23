# Text Encryption Tool — AES | DES | RSA

A Python command-line tool that encrypts and decrypts text using three widely used cryptographic algorithms: AES, DES, and RSA. Built as part of the Pinnacle Labs Cybersecurity Internship.

## Overview

| Algorithm | Type | Key Size | Notes |
|-----------|------|----------|-------|
| AES | Symmetric | 256-bit | Industry-standard encryption used today |
| DES | Symmetric | 64-bit (56-bit effective) | Included for educational comparison; considered insecure by modern standards |
| RSA | Asymmetric | 2048-bit keypair | Uses a public/private key pair; keys are auto-generated on first run |

## Features

- Interactive command-line menu
- Encrypt and decrypt text with AES, DES, or RSA
- AES and DES use CBC mode with a randomly generated IV per message, so identical plaintext never produces identical ciphertext
- RSA uses OAEP padding with an auto-generated 2048-bit keypair
- Output is Base64-encoded for easy copying and sharing

## Requirements

- Python 3.8+
- pycryptodome

## Installation

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

\`\`\`bash
python text_encryption.py
\`\`\`

Follow the on-screen menu to choose an algorithm (AES / DES / RSA), choose Encrypt or Decrypt, then enter your key/passphrase and text.

### Example

\`\`\`
Enter choice [1-4]: 1

Encrypt or Decrypt? [e/d]: e

Enter a passphrase/key: mypassword123

Enter text to encrypt: Hello World

Encrypted (Base64):
NGE/iOfU4ortlAfhhayDVm5i7lAmjcuUFRJFQ3PFhA8=


## How It Works

- **AES/DES**: A passphrase is used to derive a fixed-length symmetric key. Each encryption generates a random IV, which is stored alongside the ciphertext so decryption can recover it.
- **RSA**: A 2048-bit keypair is generated on first run and saved to `rsa_keys/`. The public key encrypts; the private key decrypts — demonstrating asymmetric cryptography.

## Disclaimer

DES is included only for educational comparison. Its short key length makes it unsuitable for securing real data — use AES for any practical purpose.

## Author

Arathi Shekhar Munavalli
