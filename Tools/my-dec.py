import hmac
import binascii
import base64
import hexdump
from Crypto.Cipher import AES

AES_KEY = binascii.unhexlify("de979e567e7eaea164b708da4115758f")
HMAC_KEY = binascii.unhexlify("7ab84ee8afe97e7aa6fa9f12d59ea301")
encrypt_data = "hex"

def decrypt(encrypted_data, iv_bytes, signature, AES_KEY, hmac_key):
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv_bytes)
    return cipher.decrypt(encrypted_data)

encrypt_data = bytes.fromhex(encrypt_data)
try:
       encrypt_data_l = encrypt_data[4:]
       data1 = encrypt_data_l[:-16]
       signature = encrypt_data_l[-16:]
       iv_bytes = b"abcdefghijklmnop"
       dec = decrypt(data1, iv_bytes, signature, AES_KEY, HMAC_KEY)
except:
       dec = decrypt(encrypt_data, iv_bytes, signature, AES_KEY, HMAC_KEY)

print("counter: {}".format(int.from_bytes(dec[:4], byteorder='big', signed=False)))
print("任务返回长度: {}".format(int.from_bytes(dec[4:8], byteorder='big', signed=False)))
print("任务输出类型: {}".format(int.from_bytes(dec[8:12], byteorder='big', signed=False)))
print(hexdump.hexdump(dec[:1000]))
open('secret.pcapng','wb').write(dec[64:-76])