from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey


class RSASignature:
    def __init__(self, private_key: RSAPrivateKey, public_key: RSAPublicKey):
        self.__private_key = private_key
        self.__public_key = public_key

    @property
    def public_key(self):
        return self.__public_key

    def sign(self, message: bytes):
        """" message length has to be a multiple of 16"""
        signature = self.__private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    @staticmethod
    def load_private_key(private_key_path: str):
        with open(private_key_path, 'rb') as private_key_file:
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key

    @staticmethod
    def load_public_key(public_key_path: str):
        with open(public_key_path, 'rb') as public_key_file:
            public_key = serialization.load_pem_public_key(
                public_key_file.read(),
                backend=default_backend()
            )
        return public_key

    def save_private_key(self, private_key_path: str):
        with open(private_key_path, 'wb') as private_key_file:
            private_key_file.write(
                self.__private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

    def save_public_key(self, public_key_path: str):
        with open(public_key_path, 'wb') as public_key_file:
            public_key_file.write(
                self.__public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    @staticmethod
    def generate_rsa() -> (RSAPrivateKey, RSAPublicKey):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=512,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def verify(signer_public_key: RSAPublicKey, message: bytes, signature: bytes):
        try:
            signer_public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
