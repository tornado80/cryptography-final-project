from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

from rsa_signature import RSASignature
from session_end_point import SessionEndPoint
from utils import convert_to_bytes


class User:
    def __init__(self):
        self.__rsa_signature_scheme: RSASignature = None

    def set_private_key_and_public_key(self, private_key: RSAPrivateKey, public_key: RSAPublicKey):
        self.__rsa_signature_scheme = RSASignature(private_key, public_key)

    @property
    def public_key(self) -> RSAPublicKey:
        return self.__rsa_signature_scheme.public_key
    
    def get_public_key_pem(self) -> str:
        return self.__rsa_signature_scheme.convert_public_key_to_pem()
    
    def sign_dh_public_key(self, session_end_point: SessionEndPoint) -> bytes:
        return self.__rsa_signature_scheme.sign(convert_to_bytes(session_end_point.public_key))

    def verify_peer_dh_public_key(self,
                                  peer_public_key: RSAPublicKey,
                                  peer_dh_public_key: DHPublicKey,
                                  signature: bytes) -> bool:
        return self.__rsa_signature_scheme.verify(
            peer_public_key,
            convert_to_bytes(peer_dh_public_key),
            signature
        )
