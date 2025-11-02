from websockets import WebSocketServerProtocol, serve
import asyncio
import json
import logging

class WebSocketTransport:
    def __init__(self, host='localhost', port=8765):
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
        # Process the incoming message
        logging.info(f"Received message: {message}")
        response = self.create_response(message)
        await self.send_response(response)

    def create_response(self, message: str) -> str:
        # Create a response based on the incoming message
        return json.dumps({"response": f"Echo: {message}"})

    async def send_response(self, response: str):
        # Send the response to all connected clients
        if self.connections:
            await asyncio.wait([conn.send(response) for conn in self.connections])

    async def start(self):
        server = await serve(self.handler, self.host, self.port)
        logging.info(f"WebSocket server started on ws://{self.host}:{self.port}")
        await server.wait_closed()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    transport = WebSocketTransport()
    asyncio.run(transport.start())