from rsa_signature import RSASignature
from user import User
from session_end_point import SessionEndPoint
from utils import convert_to_bytes
from certificate_authority import CertificateAuthority

alice = User('alice')
bob = User('bob')


CA = CertificateAuthority(*RSASignature.generate_rsa())

alice.set_private_key_and_public_key(*RSASignature.generate_rsa())
bob.set_private_key_and_public_key(*RSASignature.generate_rsa())

certificate_public_key_alice = CA.issue_certificate(alice.public_key)
certificate_public_key_bob = CA.issue_certificate(bob.public_key)


# Bob checks the certificate of Alice
if not RSASignature.verify(
            CA.public_key,
            convert_to_bytes(alice.public_key),
            certificate_public_key_alice):
    print('Alice\'s public key is not verified')
    exit()


# Alice checks the certificate of Bob
if not RSASignature.verify(
            CA.public_key,
            convert_to_bytes(bob.public_key),
            certificate_public_key_bob):
    print('Bob\'s public key is not verified')
    exit()


alice_end_point = SessionEndPoint()
bob_end_point = SessionEndPoint()

signed_dh_public_key_of_alice = alice.sign_dh_public_key(alice_end_point)
if not RSASignature.verify(
        alice.public_key,
        convert_to_bytes(alice_end_point.public_key), 
        signed_dh_public_key_of_alice):
    print("Alice's DH public key does not match with the signature.")
    exit()

signed_dh_public_key_of_bob = bob.sign_dh_public_key(bob_end_point)
if not RSASignature.verify(
        bob.public_key,
        convert_to_bytes(bob_end_point.public_key), 
        signed_dh_public_key_of_bob):
    print("Bob's DH public key does not match with the signature.")
    exit()

alice_end_point.register_peer_dh_public_key(bob_end_point.public_key)
alice_end_point.start_session()
bob_end_point.register_peer_dh_public_key(alice_end_point.public_key)
bob_end_point.start_session()

print(bob_end_point.shared_key == alice_end_point.shared_key)

iv, msg, mac = alice_end_point.encrypt(b'fsdf, world!')

print(bob_end_point.decrypt(iv, msg, mac))
