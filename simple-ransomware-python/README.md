# Simple Ransomware (Educational Purposes Only)

This is a simple Python script that demonstrates basic ransomware functionality. The script is for educational purposes only and should **not** be used for malicious intent. The code demonstrates how files can be encrypted and decrypted using the **Fernet** symmetric encryption from the **cryptography** library.

## Features
- **Encrypt**: The `encrypt.py` script encrypts files in the current directory using a randomly generated key.
- **Decrypt**: The `decrypt.py` script decrypts files using the generated key, provided the correct secret phrase is entered.

## Setup

### Prerequisites
1. Python 3.x
2. `cryptography` library

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/simple-ransomware.git
    ```

2. Install the necessary dependencies:
    ```bash
    pip install cryptography
    ```

### Usage

1. **Encrypt files**: Run `encrypt.py` to encrypt files in the current directory.
    ```bash
    python encrypt.py
    ```

2. **Decrypt files**: Run `decrypt.py` and enter the secret phrase when prompted.
    ```bash
    python decrypt.py
    ```

### Important Notes:
- This script is **for educational purposes only**. Do not use this for malicious activities.
- Modify and use responsibly!
