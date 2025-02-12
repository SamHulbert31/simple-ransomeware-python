import os
from cryptography.fernet import Fernet

# This script decrypts files encrypted by encrypt.py. It is for educational purposes only.

# Load encryption key
try:
    with open('thekey.key', 'rb') as keyfile:
        secretkey = keyfile.read()
except FileNotFoundError:
    print("Decryption key not found. Ensure 'thekey.key' is in the directory.")
    exit()

files = []

# Find encrypted files
for file in os.listdir():
    if file in ('encrypt.py', 'decrypt.py', 'thekey.key', 'README.md', '.gitignore', 'requirements.txt'):
        continue
    if os.path.isfile(file):
        files.append(file)

# Request user input for decryption
secretphrase = "unlock"

user_phrase = input("Enter the secret phrase (hint: 'unlock'):\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, 'rb') as f:
            contents = f.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, 'wb') as f:
            f.write(contents_decrypted)
    print("Files successfully decrypted.")
else:
    print("Incorrect secret phrase. Please run again.")
