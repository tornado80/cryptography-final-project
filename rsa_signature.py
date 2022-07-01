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
    def load_private_key(private_key_path: str) -> (RSAPrivateKey, str):
        with open(private_key_path, 'r') as private_key_file:
            pem = private_key_file.read()
            private_key = serialization.load_pem_private_key(
                pem.encode('utf-8'),
                password=None,
                backend=default_backend()
            )
        return private_key

    @staticmethod
    def public_key_from_str(public_key_str: str):
        return serialization.load_pem_public_key(
            public_key_str.encode('utf-8'),
            backend=default_backend()
        )

    @staticmethod
    def load_public_key(public_key_path: str):
        with open(public_key_path, 'r') as public_key_file:
            public_key = RSASignature.public_key_from_str(public_key_file.read())
        return public_key

    @staticmethod
    def convert_private_key_to_pem(private_key: RSAPrivateKey) -> str:
        return private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')

    @staticmethod
    def public_key_to_pem(public_key: RSAPublicKey):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    def convert_public_key_to_pem(self) -> str:
        return self.public_key_to_pem(self.__public_key)

    @staticmethod
    def save_private_key(private_key_path: str, private_key: RSAPrivateKey):
        with open(private_key_path, 'w') as private_key_file:
            private_key_file.write(
                RSASignature.convert_private_key_to_pem(private_key)
            )

    @staticmethod
    def save_public_key(public_key_path: str, public_key: RSAPublicKey):
        with open(public_key_path, 'w') as public_key_file:
            public_key_file.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ).decode('utf-8')
            )

    @classmethod
    def create_scheme(cls):
        private_key, public_key = cls.generate_rsa()
        return cls(private_key, public_key)

    @classmethod
    def create_scheme_from_private_key(cls, private_key: RSAPrivateKey):
        public_key = private_key.public_key()
        return cls(private_key, public_key)

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
