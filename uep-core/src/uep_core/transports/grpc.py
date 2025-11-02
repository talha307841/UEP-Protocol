from concurrent import futures
import grpc
from uep_core.protocols.uep_v1 import uep_pb2_grpc, uep_pb2

class UEPServicer(uep_pb2_grpc.UEPServicer):
    def SendMessage(self, request, context):
        # Handle incoming message and return a response
        response = uep_pb2.MessageResponse()
        response.status = "Received"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    uep_pb2_grpc.add_UEPServicer_to_server(UEPServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()