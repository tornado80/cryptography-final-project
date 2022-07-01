from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

from rsa_signature import RSASignature
from utils import convert_to_bytes


class CertificateAuthority:
    def __init__(self):
        self.rsa_signature_scheme: RSASignature = None

    def set_private_key_and_public_key(self, private_key: RSAPrivateKey, public_key: RSAPublicKey):
        self.rsa_signature_scheme = RSASignature(private_key, public_key)

    @property
    def public_key(self):
        return self.rsa_signature_scheme.public_key

    def issue_certificate(self, certificate_owner_public_key: bytes) -> bytes:
        return self.rsa_signature_scheme.sign(certificate_owner_public_key)

