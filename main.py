from DH_key_exchange import DHKeyExchange
from Symmetric_key import SymmetricKey
from Signature import RSASignature

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class User(object):
    def __init__(self, name):
        self.name = name
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=512,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        
        self.verify_key_session = RSASignature(self.private_key, self.public_key)

        ###############################################
        self.exchange_key_session = DHKeyExchange()

        self.communication_session = None
        self.shared_key = None
        ###############################################
    
    def sign_public_key(self):
        return self.verify_key_session.sign(self.exchange_key_session.public_key)
    

    def verify_peer_public_key(self, public_key, signature):
        return self.verify_key_session.verify(public_key, signature)


    def generate_shared_key(self, other_peer_key):
        self.shared_key =  self.exchange_key_session.get_shared_key(other_peer_key)
        self.session = SymmetricKey(self.shared_key)
        return self.shared_key


if __name__ == '__main__':
    alice = User('Alice')
    bob = User('Bob')

    singed_session_public_key_of_alice = alice.sign_public_key()
    if(not bob.verify_key_session.verify(bob.public_key, singed_session_public_key_of_alice)):
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
