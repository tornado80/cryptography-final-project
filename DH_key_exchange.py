from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


class DHKeyExchange(object):

    def __init__(self, private_key, public_key):
        self.public_key = public_key
        self.private_key = private_key
        self.backend = default_backend()


    def get_shared_key(self, other_peer_key):
        self.shared_key = self.private_key.exchange(other_peer_key)
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=self.backend
        ).derive(self.shared_key)
