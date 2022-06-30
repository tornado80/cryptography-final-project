import rpyc
from rpyc.utils.server import ThreadedServer


class CommunicationService(rpyc.Service):
    def __init__(self):
        super(CommunicationService, self).__init__()
        self.clients = {}

    def on_connect(self, conn: rpyc.Connection):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_register_connection(self, conn, name):
        self.clients[name] = conn

    def exposed_log(self, message):
        print(message)

    def exposed_access(self, name):
        print(f"I am accessed by  {name}")
        obj = self.clients[name]
        print(f"I am accessed by  {obj}")
        return obj


if __name__ == "__main__":
    server = ThreadedServer(CommunicationService(), port=18861, protocol_config={"allow_public_attrs": True})
    server.start()
