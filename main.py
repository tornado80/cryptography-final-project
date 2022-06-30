from rsa_signature import RSASignature
from user import User
from session_end_point import SessionEndPoint
from utils import convert_to_bytes

alice = User('Alice')
bob = User('Bob')

alice_end_point = SessionEndPoint()
bob_end_point = SessionEndPoint()

signed_dh_public_key_of_alice = alice.sign_dh_public_key(alice_end_point)
if not RSASignature.verify(
        alice.public_key,
        convert_to_bytes(alice_end_point.public_key), 
        signed_dh_public_key_of_alice):
    print("Alice's DH public key does not match with the signature.")
    exit()

signed_session_public_key_of_bob = bob.sign_dh_public_key(bob_end_point)
if not RSASignature.verify(
        bob.public_key,
        convert_to_bytes(bob_end_point.public_key), 
        signed_session_public_key_of_bob):
    print("Bob's DH public key does not match with the signature.")
    exit()

alice_end_point.register_peer_dh_public_key(bob_end_point.public_key)
alice_end_point.start_session()
bob_end_point.register_peer_dh_public_key(alice_end_point.public_key)
bob_end_point.start_session()

print(bob_end_point.shared_key == alice_end_point.shared_key)

iv, msg = alice_end_point.encrypt(b'fsdf, world!')

print(bob_end_point.decrypt(iv, msg))
