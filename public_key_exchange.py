from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


class PublicKeyExchange:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key
        self.other_peer_public_key = None
        self.backend = default_backend()

    def register_other_peer_public_key(self, other_peer_public_key):
        self.other_peer_public_key = other_peer_public_key
    

    def sign(self, message: bytes):
        """" message has to be a multiple of 16"""
        signature = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    def verify(self, message, signature):
        if self.other_peer_public_key is None:
            raise Exception('No public key registered')
        
        try:
            self.other_peer_public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
