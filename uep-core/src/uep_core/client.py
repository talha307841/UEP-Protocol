from uep_core.transports.grpc import GrpcTransport

class UEPClient:
    def __init__(self, server_address):
        self.transport = GrpcTransport(server_address)

    def send_message(self, message):
        response = self.transport.send(message)
        return response

    def receive_message(self):
        message = self.transport.receive()
        return message

    def close(self):
        self.transport.close()