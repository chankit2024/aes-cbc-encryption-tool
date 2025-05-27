from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib

def get_key(secret_key: str) -> bytes:
    return hashlib.sha256(secret_key.encode()).digest()

def decrypt(encoded_ciphertext: str, secret_key: str) -> str:
    key = get_key(secret_key)
    raw = base64.b64decode(encoded_ciphertext)
    iv = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

# ✅ ใช้ข้อความที่เข้ารหัสไว้แล้ว
encrypted_message = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret_key = "my-secret-key"

decrypted = decrypt(encrypted_message, secret_key)
print("ข้อความที่ถอดรหัส:", decrypted)
