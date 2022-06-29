from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


class DHKeyExchange(object):

    def __init__(self, generator=2, key_size=2048, backend=default_backend()):
        self.generator = generator
        self.key_size = key_size
        self.backend = backend

        parameters = dh.generate_parameters(self.generator, self.key_size, self.backend)
        self.private_key = parameters.generate_private_key()
        self.public_key = self.private_key.public_key()

    
    def get_sessoin_key(self):
        self.shared_key = self.private_key.exchange(self.public_key)
        return self.shared_key
    
    def get_symmetric_key(self, shared_key):
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"handshake data",
            backend=self.backend
        )
        return hkdf.derive(shared_key)
