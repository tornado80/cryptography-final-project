from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

import cryptomath
import random

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


def find_relative_prime_number(n):
    while range(10):
        p = random.randint(2, n - 1)
        if cryptomath.gcd(p, n) == 1:
            return p
    raise ValueError("Apocalypse")


def digest_message_to_int(message: bytes):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(message)
    hashed_message = digest.finalize()
    return int.from_bytes(hashed_message, byteorder='big')


def convert_int_to_bytes(int_value: int):
    return int_value.to_bytes(int_value.bit_length() // 8 + 1, byteorder='big')


def convert_bytes_to_int(bytes_value: bytes):
    return int.from_bytes(bytes_value, byteorder='big')


def blind(message: int, signer_public_key: RSAPublicKey) -> (int, int):
    n, b = signer_public_key.public_numbers().n, signer_public_key.public_numbers().e
    opening_value = find_relative_prime_number(n)
    blinded_message = (message * pow(opening_value, b, n)) % n
    return opening_value, blinded_message


def sign(blinded_message: int, signer_private_key: RSAPrivateKey):
    p, q = signer_private_key.private_numbers().p, signer_private_key.private_numbers().q
    n, a = p * q, signer_private_key.private_numbers().d
    return pow(blinded_message, a, n)


def unblind_signature(blind_signature: int, opening_value: int, signer_public_key: RSAPublicKey):
    n, b = signer_public_key.public_numbers().n, signer_public_key.public_numbers().e
    r_inv = cryptomath.findModInverse(opening_value, n)
    return (blind_signature * r_inv) % n


def verify(message: int, message_signature: int, singer_public_key: RSAPublicKey):
    n, b = singer_public_key.public_numbers().n, singer_public_key.public_numbers().e
    return pow(message_signature, b, n) == message

