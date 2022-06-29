from DH_key_exchange import DHKeyExchange
from Symmetric_key import SymmetricKey
from Signature import RSASignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from session_end_point import SessionEndPoint


class User(object):
    def __init__(self, name):
        self.name = name
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=512,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.rsa_signature_scheme = RSASignature(self.private_key, self.public_key)

    def sign_dh_public_key(self, session_end_point: SessionEndPoint):
        return self.rsa_signature_scheme.sign(session_end_point.public_key)

    def verify_peer_dh_public_key(self, peer_dh_public_key, signature):
        return self.rsa_signature_scheme.verify(peer_dh_public_key, signature)


if __name__ == '__main__':
    alice = User('Alice')
    bob = User('Bob')

    alice_end_point = SessionEndPoint()
    bob_end_point = SessionEndPoint()

    signed_dh_public_key_of_alice = alice.sign_dh_public_key()
    if not bob.verify_key_session.verify(bob.public_key, signed_dh_public_key_of_alice):
        print('Alice public key is valid')
        exit()
    
    singed_session_public_key_of_bob = bob.verify_key_session.public_key
    if(not alice.verify_peer_public_key(alice.public_key, singed_session_public_key_of_bob)):
        print('Bob public key is valid')
        exit()

    alice_shared_key = alice.generate_shared_key(bob.public_key)
    bob_shared_key = bob.generate_shared_key(alice.public_key)
    print(alice_shared_key == bob_shared_key)

    iv, msg = alice.session.encrypt(b"a secret messagea secret message")
    print(bob.session.decrypt(iv, msg))
