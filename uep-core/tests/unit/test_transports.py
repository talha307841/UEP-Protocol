import pytest
from uep_core.transports.http import HttpTransport
from uep_core.transports.grpc import GrpcTransport
from uep_core.transports.websocket import WebSocketTransport

@pytest.fixture
def http_transport():
    return HttpTransport()

@pytest.fixture
def grpc_transport():
    return GrpcTransport()

@pytest.fixture
def websocket_transport():
    return WebSocketTransport()

def test_http_transport_send(http_transport):
    response = http_transport.send("http://example.com", {"data": "test"})
    assert response.status_code == 200

def test_grpc_transport_send(grpc_transport):
    response = grpc_transport.send("example_service", {"data": "test"})
    assert response.success is True

def test_websocket_transport_send(websocket_transport):
    response = websocket_transport.send("ws://example.com", {"data": "test"})
    assert response.success is True

def test_http_transport_receive(http_transport):
    message = http_transport.receive()
    assert message is not None

def test_grpc_transport_receive(grpc_transport):
    message = grpc_transport.receive()
    assert message is not None

def test_websocket_transport_receive(websocket_transport):
    message = websocket_transport.receive()
    assert message is not None