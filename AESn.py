import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encryption(self, raw_text):
        raw_text = self.__pad(raw_text)
        four = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, four)
        encrypted_text = cipher.encrypt(raw_text.encode())
        print(b64encode(four + encrypted_text).decode("utf-8")) 

    def decryption(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        four = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, four)
        raw_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        print(self.__unpad(raw_text))

    def __pad(self, raw_text):
        number_of_bytes_to_pad = self.block_size - len(raw_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_raw_text = raw_text + padding_str