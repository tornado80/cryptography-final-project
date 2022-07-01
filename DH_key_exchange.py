from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import dh

class DHParameters(object):
    _cls = None

    def __init__(self, generator, key_size, backend=default_backend()):
        self.generator = generator
        self.key_size = key_size
        self.backend = backend
        p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
        g = 2
        params_numbers = dh.DHParameterNumbers(p, g)
        self.parameters = params_numbers.parameters(default_backend())

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

    def get_public_key_pem(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def get_shared_key(self, other_peer_public_key) -> bytes:
        self.shared_key = self.private_key.exchange(other_peer_public_key)
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=self.backend
        ).derive(self.shared_key)

    @staticmethod
    def public_key_from_str(public_key_str: str):
        return serialization.load_pem_public_key(
            public_key_str.encode('utf-8'),
            backend=default_backend()
        )