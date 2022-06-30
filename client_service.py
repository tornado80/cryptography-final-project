from user import User
from session_end_point import SessionEndPoint
import argparse
import rpyc


class UserService(rpyc.Service):
    def __init__(self, name):
        super(UserService, self).__init__()
        self._user = User(name)
        self.name = name
        self.network = None
        self.peers = {}

    def on_connect(self, conn):
        self.network = conn.root
        print('Connected to the server')

    def exposed_get_name(self):
        return self.name

    def exposed_get_public_key(self):
        return self._user.public_key

    def exposed_start_end_point(self, other_end_name):
        if other_end_name in self.peers:
            raise Exception('Session already started')
        peer_pk = self.network.access(other_end_name).get_public_key()
        self.peers[other_end_name] = (SessionEndPoint(), peer_pk)

    def exposed_get_dh_public_key(self, other_end_name):
        if other_end_name not in self.peers:
            raise Exception('Session not started')
        return self._user.sign_dh_public_key(self.peers[other_end_name])

    def exposed_register_dh_public_key(self, other_end_name):
        if other_end_name not in self.peers:
            raise Exception('Session not started')
        peer = self.network.access(other_end_name)
        peer_dh_pk, signature = peer.get_dh_public_key()
        session, peer_pk = self.peers[other_end_name]
        if not self._user.verify_peer_dh_public_key(
                peer_pk,
                peer_dh_pk,
                signature):
            raise Exception('Invalid signature')
        session.register_peer_dh_public_key(peer_dh_pk)
        session.start_session()

    def exposed_start_communication(alice, bob_name):
        bob = alice.network.access(bob_name)
        alice.exposed_start_end_point(bob_name)
        bob.start_end_point(alice.get_name())
        alice.exposed_register_dh_public_key(bob_name)
        bob.register_dh_public_key(alice.get_name())

    def exposed_send_message(self, bob_name, message):
        if bob_name not in self.peers:
            raise Exception('Session not started')
        session, peer_pk = self.peers[bob_name]
        bob = self.network.access(bob_name)
        iv, msg, mac = session.encrypt(message)
        print(f'{self.name} sent: {message}')
        bob.receive_message(self.get_name(), iv, msg, mac)

    def exposed_receive_message(self, bob_name, iv, message, mac):
        if bob_name not in self.peers:
            raise Exception('Session not started')
        session, peer_pk = self.peers[bob_name]
        text = session.decrypt(iv, message, mac)
        print(f'{self.name} received: {text}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=18861)
    parser.add_argument('--name', type=str)
    parser.add_argument('--CA-file-path', type=str)
    args = parser.parse_args()

    name = input()

    connection = rpyc.connect('localhost', args.port, service=UserService(
        name
    ), config={'allow_all_attrs': True})
    connection.root.register_connection(connection, name)

