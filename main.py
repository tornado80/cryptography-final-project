from user import User
from session_end_point import SessionEndPoint
from utils import convert_to_bytes


alice = User('Alice')
bob = User('Bob')

alice.register_other_peer_dh_public_key(bob.public_key)
bob.register_other_peer_dh_public_key(alice.public_key)

alice_end_point = SessionEndPoint()
bob_end_point = SessionEndPoint()

###############################################################################
signed_dh_public_key_of_alice = alice.sign_dh_public_key(alice_end_point)
if not bob.public_key_exchange.verify(
        convert_to_bytes(alice_end_point.public_key), 
        signed_dh_public_key_of_alice):
    print('Alice public key is not valid')
    exit()

signed_session_public_key_of_bob = bob.sign_dh_public_key(bob_end_point)
if not alice.public_key_exchange.verify(
        convert_to_bytes(bob_end_point.public_key), 
        signed_session_public_key_of_bob):
    print('Bob public key is not valid')
    exit()
###############################################################################

alice_end_point.register_dh_public_key(bob_end_point.public_key)
alice_end_point.start_session()
bob_end_point.register_dh_public_key(alice_end_point.public_key)
bob_end_point.start_session()

print(bob_end_point.shared_key == alice_end_point.shared_key)

iv, msg = alice_end_point.symmetric_key_scheme.encrypt(b"a secret messagea secret message")

print(bob_end_point.symmetric_key_scheme.decrypt(iv, msg))
