from public_key_exchange import PublicKeyExchange
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from session_end_point import SessionEndPoint
from utils import convert_to_bytes


class User(object):
    def __init__(self, name):
        self.name = name
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=512,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.public_key_exchange = PublicKeyExchange(self.private_key, self.public_key)

    
    def register_other_peer_dh_public_key(self, peer_dh_public_key):
        self.public_key_exchange.register_other_peer_public_key(peer_dh_public_key)
    
    def sign_dh_public_key(self, session_end_point: SessionEndPoint) -> bytes:
        return self.public_key_exchange.sign(convert_to_bytes(session_end_point.public_key))

    def verify_peer_dh_public_key(self, peer_dh_public_key, signature) -> bool:
        return self.public_key_exchange.verify(signature, peer_dh_public_key.private_bytes())