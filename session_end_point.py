from cryptography.hazmat.primitives.asymmetric.dh import DHPublicKey

from DH_key_exchange import DHKeyExchange
from symmetric_key import SymmetricKey
from Crypto.Util.Padding import pad, unpad


class SessionEndPoint:
    def __init__(self):
        self.__dh_key_exchange_scheme = DHKeyExchange()
        self.__symmetric_key_scheme: SymmetricKey = None
        self.__shared_key: bytes = None

    @property
    def shared_key(self) -> bytes:
        return self.__shared_key

    @property
    def public_key(self) -> DHPublicKey:
        return self.__dh_key_exchange_scheme.public_key
    
    def encrypt(self, message: bytes) -> (bytes, bytes):
        if self.__symmetric_key_scheme is None:
            raise Exception('Session is not started')
        return self.__symmetric_key_scheme.encrypt(pad(message, 16))

    def decrypt(self, iv, message) -> bytes:
        if self.__symmetric_key_scheme is None:
            raise Exception('Session is not started')
        return unpad(self.__symmetric_key_scheme.decrypt(iv, message), 16)

    def register_peer_dh_public_key(self, peer_dh_public_key):
        self.__shared_key = self.__dh_key_exchange_scheme.get_shared_key(peer_dh_public_key)

    def start_session(self):
        if self.shared_key is None:
            raise Exception('Shared key is not registered')
        self.__symmetric_key_scheme = SymmetricKey(self.shared_key)
        return self.__symmetric_key_scheme
