# 🔐 AES Encryption & Decryption in Python

This project demonstrates how to **encrypt** and **decrypt** messages using **AES (CBC mode)** with a key derived from a custom secret string via SHA-256. It uses the [`pycryptodome`](https://pypi.org/project/pycryptodome/) library for cryptographic operations.

## 📦 Requirements

- Python 3.x
- pycryptodome

Install dependencies:

```bash
pip install pycryptodome
```

## 📁 Files

- `encrypt.py` – Contains both encryption and decryption functions with an example usage
- `decrypt.py` – Script that only decrypts a previously encrypted message

## 🔑 How It Works

1. A **secret key** (string) is hashed using SHA-256 to produce a 32-byte key.
2. A **random IV** (initialization vector) is generated for each encryption.
3. The plaintext is **padded**, **encrypted**, and **base64-encoded**.
4. The output is a string that can be safely stored or transmitted.
5. During decryption, the IV is extracted from the first 16 bytes.

---

## ✅ Example Usage

### 🔒 Encryption (`encrypt.py`)

```python
from encrypt import encrypt

message = "สวัสดี"
secret_key = "my-secret-key"

encrypted = encrypt(message, secret_key)
print("ข้อความที่เข้ารหัส:", encrypted)
```

### 🔓 Decryption (`decrypt.py`)

```python
from decrypt import decrypt

encrypted_message = "xxxx..."  # Output from encryption
secret_key = "my-secret-key"

decrypted = decrypt(encrypted_message, secret_key)
print("ข้อความที่ถอดรหัส:", decrypted)
```

---

## 🔐 Security Notes

- This uses AES in **CBC mode**, which is secure **only if IV is unique per message** (which it is, thanks to `get_random_bytes(16)`).
- The encryption key is derived using **SHA-256** from the given secret key string.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
