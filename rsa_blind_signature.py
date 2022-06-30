import cryptomath
import random
from user import User


def rsa_generate(bits=1024):
    # Generates public and private keys and saves them to a file.
    p = cryptomath.findPrime(bits)
    q = cryptomath.findPrime(bits)
    phi = (p - 1) * (q - 1)
    n = p * q
    found_encryption_key = False
    while not found_encryption_key:
        a = random.randint(2, phi - 1)
        if cryptomath.gcd(a, phi) == 1:
            found_encryption_key = True
    b = cryptomath.findModInverse(a, phi)
    sk = (n, a)
    pk = (n, b)
    return sk, pk


def blind_message(message, pk):
    n, b = pk
    r = random.randint(2, n - 1)
    blind_message = (message * pow(r, b, n)) % n
    return r, blind_message


def sign(blind_message, sk):
    n, a = sk
    return pow(blind_message, a, n)


def unblind_signature(blind_sign, r, pk):
    n, b = pk
    r_inv = cryptomath.findModInverse(r, n)
    return (blind_sign * r_inv) % n


def verify(message, signature, pk):
    n, b = pk
    return pow(signature, b, n) == message


if __name__ == '__main__':
    bob = User("Bob")
    msg = bob.public_key.public_numbers().e
    sk, pk = rsa_generate()
    r, blind_message = blind_message(int(msg), pk)
    signature = sign(blind_message, sk)
    unblind_sign = unblind_signature(signature, r, pk)
    print(verify(msg, unblind_sign, pk))
