from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

import rsa_blind_signature


class CertificateAuthority:
    def __init__(self):
        self.__private_key = None
        self.__public_key = None

    def set_private_key_and_public_key(self, private_key: RSAPrivateKey, public_key: RSAPublicKey):
        self.__public_key = public_key
        self.__private_key = private_key

    @property
    def public_key(self):
        return self.__public_key

    def issue_certificate(self, certificate_owner_public_key: int) -> bytes:
        return rsa_blind_signature.convert_int_to_bytes(
            rsa_blind_signature.sign(certificate_owner_public_key, self.__private_key)
        )
