import cryptomath
import random
from user import User

from typing import Tuple

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes

PublicKey = Tuple[int, int]
PrivateKey = Tuple[int, int]


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


def generate_rsa() -> (PrivateKey, PublicKey):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=512,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    n = public_key.public_numbers().n
    a, b = private_key.private_numbers().d, public_key.public_numbers().e
    return (n, a), (n, b)


def blind(message: int, signer_public_key: PublicKey) -> (int, int):
    n, b = signer_public_key
    opening_value = find_relative_prime_number(n)
    blinded_message = (message * pow(opening_value, b, n)) % n
    return opening_value, blinded_message


def sign(blinded_message: int, signer_private_key: PrivateKey):
    n, a = signer_private_key
    return pow(blinded_message, a, n)


def unblind_signature(blind_signature: int, opening_value: int, signer_public_key: PublicKey):
    n, b = signer_public_key
    r_inv = pow(opening_value, -1, n)
    return (blind_signature * r_inv) % n


def verify(message: int, message_signature: int, singer_public_key: PublicKey):
    n, b = singer_public_key
    return pow(message_signature, b, n) == message


if __name__ == '__main__':
    bob = User("Bob")
    msg = bob.public_key.public_numbers().e
    msg += bob.public_key.public_numbers().n

    msg_hash = digest_message_to_int(msg.to_bytes(128, byteorder='big'))

    sk, pk = generate_rsa()
    r, blind_message = blind(msg_hash, pk)
    signature = sign(blind_message, sk)
    unblind_sign = unblind_signature(signature, r, pk)
    print(verify(msg_hash, unblind_sign, pk))
