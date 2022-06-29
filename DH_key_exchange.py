from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import dh


class DHParameters(object):
    _cls = None

    def __init__(self, generator, key_size, backend=default_backend()):
        self.generator = generator
        self.key_size = key_size
        self.backend = backend
        self.parameters = dh.generate_parameters(
            generator=self.generator, 
            key_size=self.key_size, 
            backend=self.backend
        )

    def get_private_key(self):
        return self.parameters.generate_private_key()

    def get_public_key(self):
        return self.parameters.generate_private_key().public_key()
    
    @staticmethod
    def get_instance():
        if DHParameters._cls is None:
            DHParameters._cls = DHParameters(generator=2, key_size=512)
        return DHParameters._cls


class DHKeyExchange(object):
    def __init__(self):
        parameters = DHParameters.get_instance()
        self.private_key = parameters.get_private_key()
        self.public_key = self.private_key.public_key()
        self.backend = default_backend()

    def get_shared_key(self, other_peer_public_key) -> bytes:
        self.shared_key = self.private_key.exchange(other_peer_public_key)
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=self.backend
        ).derive(self.shared_key)
