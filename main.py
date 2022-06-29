from DH_key_exchange import DHKeyExchange
from Symmetric_key import SymmetricKey

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh

class Parameters(object):
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


class User(object):
    parameters = Parameters(generator=2, key_size=512)

    def __init__(self, name):
        self.name = name
        self.private_key = self.parameters.get_private_key()
        self.public_key = self.private_key.public_key()
        self.shared_key = None
        self.session = None

    def generate_shared_key(self, other_peer_key):
        self.shared_key =  DHKeyExchange(self.private_key, self.public_key).get_shared_key(other_peer_key)
        self.session = SymmetricKey(self.shared_key)
        return self.shared_key


if __name__ == '__main__':
    alice = User('Alice')
    bob = User('Bob')
    alice_shared_key = alice.generate_shared_key(bob.public_key)
    bob_shared_key = bob.generate_shared_key(alice.public_key)
    print(alice_shared_key == bob_shared_key)

    iv, msg = alice.session.encrypt(b"a secret messagea secret messa")
    print(bob.session.decrypt(iv, msg))
