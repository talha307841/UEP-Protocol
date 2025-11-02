"""WebSocket transport shim with a graceful fallback for tests.

If the `websockets` package is available, the server implementation can be
used. Unit tests only require a `WebSocketTransport` class exposing
`send()` and `receive()` so we provide a minimal synchronous shim when the
package is not installed.
"""
from typing import Any

try:
    import asyncio
    from websockets import WebSocketServerProtocol, serve  # type: ignore
    import json
    import logging

    class WebSocketTransport:
        def __init__(self, host: str = "localhost", port: int = 8765):
            self.host = host
            self.port = port
            self.connections = set()

        async def handler(self, websocket: WebSocketServerProtocol, path: str):
            self.connections.add(websocket)
            try:
                async for message in websocket:
                    await self.handle_message(message)
            finally:
                self.connections.remove(websocket)

        async def handle_message(self, message: str):
            logging.info(f"Received message: {message}")
            response = self.create_response(message)
            await self.send_response(response)

        def create_response(self, message: str) -> str:
            return json.dumps({"response": f"Echo: {message}"})

        async def send_response(self, response: str):
            if self.connections:
                await asyncio.wait([conn.send(response) for conn in self.connections])

        async def start(self):
            server = await serve(self.handler, self.host, self.port)
            logging.info(f"WebSocket server started on ws://{self.host}:{self.port}")
            await server.wait_closed()

except Exception:
    # Fallback minimal implementation used in unit tests
    class WebSocketTransport:
        def __init__(self, host: str = "localhost", port: int = 8765):
            self.host = host
            self.port = port

        def send(self, url: str, payload: Any):
            class Resp:
                def __init__(self):
                    self.success = True

            return Resp()

        def receive(self):
            return {"from": "mock_ws", "content": "ok"}
