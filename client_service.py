from user import User
from session_end_point import SessionEndPoint
import argparse
import rpyc


class UserService(rpyc.Service):
    def __init__(self, name):
        super(UserService, self).__init__()
        self._user = User()
        self.name = name
        self.network = None
        self.peers = {}

    def on_connect(self, conn):
        self.network = conn.root
        print('Connected to the server')

    def exposed_get_name(self):
        return self.name


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=18861)
    parser.add_argument('--name', type=str)
    parser.add_argument('--CA-file-path', type=str)
    args = parser.parse_args()

    connection = rpyc.connect('localhost', args.port, service=UserService(
        args.name
    ))

