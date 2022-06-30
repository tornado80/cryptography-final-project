from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric import padding

from rsa_signature import RSASignature
from utils import convert_to_bytes


class CertificateAuthority:
    def __init__(self):
        self.rsa_signature_scheme = RSASignature()

    @property
    def public_key(self):
        return self.rsa_signature_scheme.public_key

    def issue_certificate(self, certificate_owner_public_key: RSAPublicKey) -> bytes:
        return self.rsa_signature_scheme.sign(convert_to_bytes(certificate_owner_public_key))

