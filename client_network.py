import rpyc


class CommunicationService(rpyc.Service):
    def __init__(self):
        super(CommunicationService, self).__init__()
        self.clients = {}

    def on_connect(self, conn: rpyc.Connection):
        self.clients[conn.root.get_name()] = conn

    def on_disconnect(self, conn):
        pass

    def exposed_log(self, message):
        print(message)

    def exposed_access(self, name):
        return self.clients[name]


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    server = ThreadedServer(CommunicationService(), port=18861)
    server.start()
