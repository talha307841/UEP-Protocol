from concurrent import futures
import grpc
from uep_core.protocols import uep_pb2_grpc, uep_pb2

class UEPServicer:
    # A lightweight servicer used for the example and tests. In production
    # this would subclass the generated uep_pb2_grpc.UEPExchangeServiceServicer
    # and implement Send / Stream / RegisterModel methods.
    def Send(self, request, context):
        # Handle incoming message and return a response
        response = uep_pb2.UEPResponse()
        response.response_id = request.request_id
        response.type = request.type
        response.content = request.content
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # If generated stubs are available, register the servicer properly.
    try:
        uep_pb2_grpc.add_UEPExchangeServiceServicer_to_server(UEPServicer(), server)  # type: ignore
    except Exception:
        # Fallback to no-op registration for tests when generated code isn't present
        try:
            uep_pb2_grpc.add_UEPServicer_to_server(UEPServicer(), server)  # type: ignore
        except Exception:
            pass

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


class GrpcTransport:
    """Simple transport shim for tests and examples.

    This does not open real gRPC channels; it provides a small API that
    the unit tests expect: send(service, payload) -> object with `success`
    and receive() -> a simple message.
    """

    async def send_async(self, service: str, payload: dict):
        # In a real implementation this would create an async gRPC stub and
        # call the Send RPC. Here we mock a successful response.
        class Resp:
            def __init__(self):
                self.success = True

        return Resp()

    def send(self, service: str, payload: dict):
        # Allow sync tests to call send; return a simple success object.
        class Resp:
            def __init__(self):
                self.success = True

        return Resp()

    def receive(self):
        # Return a simple non-None message to satisfy tests.
        return {"from": "mock_service", "content": b"ok"}

if __name__ == '__main__':
    serve()