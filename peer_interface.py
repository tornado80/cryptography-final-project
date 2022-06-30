import rpyc


class PeerInterface(rpyc.Service):
    def __init__(self, name):
        super(PeerInterface, self).__init__()
        self.server = None
        self.name = name

    def on_connect(self, conn: rpyc.Connection):
        self.server = conn.root
        self.server.log(f'{self.name} connected')
        print("connected")

    def on_disconnect(self, conn):
        print("disconnected")

    def exposed_log(self, message):
        print(f'Server: {message}')

    def exposed_get_name(self):
        return self.name
