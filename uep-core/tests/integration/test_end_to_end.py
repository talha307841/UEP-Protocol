import pytest
from src.uep_core.server import start_server
from src.uep_core.client import UEPClient
from src.uep_core.schemas.message import MessageSchema

@pytest.fixture(scope="module")
def server():
    # Start the UEP server
    server_instance = start_server()
    yield server_instance
    server_instance.stop()

@pytest.fixture(scope="module")
def client():
    # Create a UEP client
    return UEPClient()

def test_end_to_end(server, client):
    # Prepare a test message
    test_message = MessageSchema(
        sender="test_model",
        receiver="test_service",
        content="Hello, UEP!",
        message_type="greeting"
    )

    # Send the message
    response = client.send_message(test_message)

    # Validate the response
    assert response is not None
    assert response.content == "Hello, test_model!"  # Assuming the service echoes back the sender's name
    assert response.message_type == "greeting_response"