from concurrent import futures
import grpc
from uep_core.protocols.uep_v1 import UEPServiceServicer, add_UEPServiceServicer_to_server
from uep_core.plugins.registry import ModelRegistry
from uep_core.logging import setup_logging

class UEPServer:
    def __init__(self, host='localhost', port=50051):
        self.host = host
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.registry = ModelRegistry()

    def start(self):
        setup_logging()
        add_UEPServiceServicer_to_server(UEPServiceServicer(self.registry), self.server)
        self.server.add_insecure_port(f'{self.host}:{self.port}')
        self.server.start()
        print(f'Server started on {self.host}:{self.port}')
        self.server.wait_for_termination()

    def stop(self):
        self.server.stop(0)

if __name__ == '__main__':
    uep_server = UEPServer()
    try:
        uep_server.start()
    except KeyboardInterrupt:
        uep_server.stop()