from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

from rsa_signature import RSASignature
from utils import convert_to_bytes


class CertificateAuthority:
    def __init__(self, private_key: RSAPrivateKey, public_key: RSAPublicKey):
        self.rsa_signature_scheme = RSASignature(private_key, public_key)

    @property
    def public_key(self):
        return self.rsa_signature_scheme.public_key

    def issue_certificate(self, certificate_owner_public_key: RSAPublicKey) -> bytes:
        return self.rsa_signature_scheme.sign(convert_to_bytes(certificate_owner_public_key))
