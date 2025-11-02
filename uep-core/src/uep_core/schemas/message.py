from pydantic import BaseModel
from typing import Any, Dict, List, Union, Optional


class UEPMessage(BaseModel):
    message_id: Optional[str] = None
    sender: Optional[str] = None
    recipient: Optional[str] = None
    payload: Optional[Any] = None
    timestamp: Optional[str] = None


class UEPRequest(UEPMessage):
    request_type: Optional[str] = None
    parameters: Optional[Dict[str, Union[str, int, float, List[Any]]]] = None


class UEPResponse(UEPMessage):
    status: Optional[str] = None
    error: Optional[str] = None
    result: Optional[Any] = None


# Backwards-compatible/simple schemas used by tests
class Message(BaseModel):
    type: str
    content: Any


class MessageSchema(BaseModel):
    sender: str
    receiver: str
    content: Any
    message_type: str
