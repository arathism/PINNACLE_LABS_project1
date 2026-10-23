# Text Encryption and Decryption Using Python

## Project Overview

This project is a simple cybersecurity application that encrypts and decrypts text messages using Python and the Cryptography library.

It demonstrates the importance of encryption in protecting the confidentiality and integrity of data.

## Objectives

- Understand the fundamentals of text encryption.
- Encrypt plain-text messages.
- Decrypt encrypted messages using a secret key.
- Learn basic Python cryptography.
- Practice building and testing a cybersecurity application.

## Technologies Used

- Python
- Visual Studio Code
- Cryptography library
- Fernet authenticated encryption

## Features

- Encrypt text messages.
- Decrypt previously encrypted messages.
- Generate and save a secret key.
- Handle invalid encrypted input.
- Provide a simple command-line interface.

## Installation

Install Python and open the project folder in VS Code.

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

## How to Use

1. Run the application.
2. Choose option 1 to encrypt a message.
3. Copy the encrypted message.
4. Choose option 2 to decrypt it.
5. Paste the encrypted message.
6. Verify that the original message is recovered.

## Security Notes

- Keep the secret key private.
- Do not upload `secret.key` to GitHub.
- Anyone with the secret key can decrypt messages protected by it.
- This project is an educational demonstration and is not a complete secure messaging application.

## Conclusion

This project demonstrates how text encryption and decryption work and why protecting secret keys is important for cybersecurity.