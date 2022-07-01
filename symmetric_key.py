from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os


class SymmetricKey(object):

    def __init__(self, key):
        self.__key = key

    def encrypt(self, plaintext: bytes) -> (bytes, bytes):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.__key), modes.CTR(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return iv, ciphertext

    def decrypt(self, iv: bytes, ciphertext: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.__key), modes.CTR(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext
