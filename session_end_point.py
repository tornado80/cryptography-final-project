from DH_key_exchange import DHKeyExchange
from Symmetric_key import SymmetricKey


class SessionEndPoint:
    def __init__(self):
        self.dh_key_exchange_scheme = DHKeyExchange()
        self.symmetric_key_scheme = None
        self.shared_key = None

    @property
    def public_key(self):
        return self.dh_key_exchange_scheme.public_key

    def generate_shared_key(self, peer_dh_public_key) -> bytes:
        self.shared_key = self.dh_key_exchange_scheme.get_shared_key(peer_dh_public_key)
        self.symmetric_key_scheme = SymmetricKey(self.shared_key)
        return self.shared_key
