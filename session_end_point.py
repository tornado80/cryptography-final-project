from DH_key_exchange import DHKeyExchange
from Symmetric_key import SymmetricKey

from Crypto.Util.Padding import pad, unpad

class SessionEndPoint:
    def __init__(self):
        self.dh_key_exchange_scheme = DHKeyExchange()
        self.symmetric_key_scheme = None
        self.peer_dh_public_key = None
        self.shared_key = None

    @property
    def public_key(self):
        return self.dh_key_exchange_scheme.public_key

    
    def encrypt(self, message: bytes):
        if self.symmetric_key_scheme is None:
            raise Exception('Session is not started')
        return self.symmetric_key_scheme.encrypt(pad(message, 16))


    def decrypt(self, iv, message):
        if self.symmetric_key_scheme is None:
            raise Exception('Session is not started')
        return unpad(self.symmetric_key_scheme.decrypt(iv, message), 16)
    

    def register_dh_public_key(self, peer_dh_public_key):
        self.peer_dh_public_key = peer_dh_public_key
        self.shared_key = self.dh_key_exchange_scheme.get_shared_key(peer_dh_public_key)

    def start_session(self) -> bytes:
        if self.shared_key is None:
            raise Exception('Shared key is not registered')
        
        self.symmetric_key_scheme = SymmetricKey(self.shared_key)
        return self.symmetric_key_scheme