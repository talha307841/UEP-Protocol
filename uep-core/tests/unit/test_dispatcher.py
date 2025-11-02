import pytest
from uep_core.core.dispatcher import MessageDispatcher
from uep_core.schemas.message import Message

@pytest.fixture
def dispatcher():
    return MessageDispatcher()

def test_route_message_to_ai_model(dispatcher):
    message = Message(type="ai_model", content="Test content")
    response = dispatcher.dispatch(message)
    assert response == "Message routed to AI model"

def test_route_message_to_microservice(dispatcher):
    message = Message(type="microservice", content="Test content")
    response = dispatcher.dispatch(message)
    assert response == "Message routed to microservice"

def test_route_invalid_message(dispatcher):
    message = Message(type="invalid", content="Test content")
    response = dispatcher.dispatch(message)
    assert response == "Error: Invalid message type"