import os
from typing import Union

from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

from rsa_signature import RSASignature


def convert_to_bytes(public_key: Union[DHPublicKey, RSAPublicKey]) -> bytes:
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo    
    )


def load_default_private_and_private_key(path: str) -> (RSAPrivateKey, RSAPublicKey):
    if os.path.exists(path):
        private_key = RSASignature.load_private_key(path)
        public_key = private_key.public_key()
        return private_key, public_key
    else:
        private_key, public_key = RSASignature.generate_rsa()
        RSASignature.save_private_key(path, private_key)
        return private_key, public_key
