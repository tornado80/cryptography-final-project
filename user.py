from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

from rsa_signature import RSASignature
from session_end_point import SessionEndPoint
from utils import convert_to_bytes


class User(object):
    def __init__(self, name):
        self.name = name
        self.__rsa_signature_scheme = RSASignature()

    @property
    def public_key(self) -> RSAPublicKey:
        return self.__rsa_signature_scheme.public_key
    
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
