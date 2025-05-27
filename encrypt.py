from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib

# ฟังก์ชันสร้างกุญแจจาก secret key ที่เป็น string
def get_key(secret_key: str) -> bytes:
    return hashlib.sha256(secret_key.encode()).digest()

# เข้ารหัสข้อความ
def encrypt(plaintext: str, secret_key: str) -> str:
    key = get_key(secret_key)
    iv = get_random_bytes(16)  # สร้าง IV แบบสุ่ม
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext).decode()

# ถอดรหัสข้อความ
def decrypt(encoded_ciphertext: str, secret_key: str) -> str:
    key = get_key(secret_key)
    raw = base64.b64decode(encoded_ciphertext)
    iv = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

# ✅ ตัวอย่างการใช้งาน
if __name__ == "__main__":
    secret_key = "my-secret-key"
    message = "สวัสดี"

    # ✅ เข้ารหัส
    encrypted = encrypt(message, secret_key)
    print("ข้อความที่เข้ารหัส:", encrypted)