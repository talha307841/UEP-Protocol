from typing import Any, Dict
import requests

class MicroserviceAdapter:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def send_request(self, endpoint: str, data: Dict[str, Any]) -> Any:
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get_response(self, endpoint: str) -> Any:
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()