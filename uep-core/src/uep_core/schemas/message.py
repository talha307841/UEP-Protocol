from pydantic import BaseModel
from typing import Any, Dict, List, Union

class UEPMessage(BaseModel):
    message_id: str
    sender: str
    recipient: str
    payload: Any
    timestamp: str

class UEPRequest(UEPMessage):
    request_type: str
    parameters: Dict[str, Union[str, int, float, List[Any]]]

class UEPResponse(UEPMessage):
    status: str
    error: str = None
    result: Any = None