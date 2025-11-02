from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class UEPMessage:
    """Base class for UEP messages."""
    message_type: str
    payload: Dict[str, Any]

@dataclass
class RequestMessage(UEPMessage):
    """Class for request messages."""
    request_id: str

@dataclass
class ResponseMessage(UEPMessage):
    """Class for response messages."""
    request_id: str
    status: str
    data: Any

class UEPProtocolV1:
    """Universal Exchange Protocol Version 1."""

    @staticmethod
    def serialize_message(message: UEPMessage) -> str:
        """Serialize a UEP message to a string format."""
        return f"{message.message_type}:{message.payload}"

    @staticmethod
    def deserialize_message(serialized_message: str) -> UEPMessage:
        """Deserialize a string format message back to a UEPMessage."""
        message_type, payload_str = serialized_message.split(":", 1)
        payload = eval(payload_str)  # Use a safer method in production
        if message_type == "request":
            return RequestMessage(message_type=message_type, **payload)
        elif message_type == "response":
            return ResponseMessage(message_type=message_type, **payload)
        else:
            raise ValueError("Unknown message type")

    @staticmethod
    def validate_message(message: UEPMessage) -> bool:
        """Validate the structure of a UEP message."""
        if isinstance(message, RequestMessage):
            return "request_id" in message.payload
        elif isinstance(message, ResponseMessage):
            return "request_id" in message.payload and "status" in message.payload
        return False

    @staticmethod
    def create_request(request_id: str, payload: Dict[str, Any]) -> RequestMessage:
        """Create a request message."""
        return RequestMessage(message_type="request", request_id=request_id, payload=payload)

    @staticmethod
    def create_response(request_id: str, status: str, data: Any) -> ResponseMessage:
        """Create a response message."""
        return ResponseMessage(message_type="response", request_id=request_id, status=status, data=data)