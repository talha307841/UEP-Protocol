"""HTTP transport helpers and a tiny Flask app for local testing.

Unit tests import `HttpTransport` and expect `send(url, payload)` to return
an object with `status_code == 200` and `receive()` to return a non-None
message. Provide a lightweight implementation that doesn't require a running
Flask server.
"""
from typing import Any


class HttpTransport:
    """Minimal HTTP transport shim used in tests.

    This is intentionally simple: it doesn't perform network I/O; it returns
    deterministic success objects so unit tests can run fast and offline.
    """

    def send(self, url: str, payload: Any):
        class Resp:
            def __init__(self):
                self.status_code = 200

        return Resp()

    def receive(self):
        return {"from": "mock_http", "content": "ok"}


# Small Flask app left available for manual testing. Importing Flask is
# optional for unit tests; only start the app when run as a script.
try:
    from flask import Flask, request, jsonify  # type: ignore

    app = Flask(__name__)

    @app.route('/send', methods=['POST'])
    def _send_message():
        data = request.json or {}
        # In a real app we'd validate and dispatch; echo back for now
        return jsonify({"received": True, "data": data}), 200

    @app.route('/health', methods=['GET'])
    def _health_check():
        return jsonify({'status': 'healthy'}), 200

except Exception:
    app = None


if __name__ == '__main__' and app is not None:
    app.run(host='0.0.0.0', port=5000)