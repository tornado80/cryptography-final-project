from cryptography.hazmat.primitives import hashes, hmac


class HMAC:
    def __init__(self, key: bytes) -> None:
        self.key = key

    def gen_mac(self, msg: bytes) -> bytes:
        h = hmac.HMAC(self.key, hashes.SHA256())
        h.update(msg)
        mac = h.finalize()
        return mac

    def vrfy_mac(self, msg: bytes, mac: bytes) -> bool:
        h = hmac.HMAC(self.key, hashes.SHA256())
        h.update(msg)
        try:
            h.verify(mac)
            return True
        except:
            return False
