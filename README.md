# 🧠 UEP-Core (Universal Exchange Protocol)

**UEP-Core** is a modular, high-performance **gRPC-based communication protocol** that enables **AI models, microservices, and systems** to exchange information seamlessly — whether it’s **text, embeddings, binary data, or metadata**.

This project provides a foundation for building scalable AI ecosystems where multiple models and services can talk to each other efficiently, securely, and asynchronously.

---

## 🚀 Features

- ⚙️ **Universal Exchange Layer** — unified interface for text, embeddings, and binary data  
- 🔗 **gRPC-based Communication** — low latency and type-safe protocol  
- 🧩 **Modular Handlers** — easily extend to plug in new AI model endpoints  
- 🧠 **Async Support** — fully asynchronous implementation using `grpc.aio`  
- 📦 **Model Registration System** — register and discover available models dynamically  
- 📡 **Bidirectional Streaming** — real-time message exchange  
- 🧰 **Developer Friendly** — clear structure, typed interfaces, and CI integration  

---

## 🏗️ Project Structure

uep-core/
├── src/uep_core/
│ ├── protos/
│ │ ├── uep.proto # Protocol Buffers definitions
│ │ └── compiled stubs # Generated gRPC Python stubs
│ ├── server/
│ │ ├── grpc_server.py # Asynchronous gRPC server
│ │ ├── handlers/
│ │ │ ├── base_handler.py # Base handler abstraction
│ │ │ └── text_handler.py # Example text handler
│ ├── client/
│ │ ├── grpc_client.py # Async gRPC client
│ └── utils/
│ └── logger.py # Structured logging utilities
├── tests/
│ └── test_grpc_server.py # Unit tests using pytest
├── requirements.txt # Dependencies
├── pyproject.toml # Build configuration
├── Makefile # Developer commands
├── README.md # This file
└── .gitignore

yaml
Copy code

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/uep-core.git
cd uep-core
2️⃣ Create and Activate Virtual Environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🧩 Compile Protocol Buffers
The .proto file defines all gRPC message types and services.
To generate the Python gRPC stubs:

bash
Copy code
make protos
Or manually:

bash
Copy code
python -m grpc_tools.protoc \
    -I src/uep_core/protos \
    --python_out=src/uep_core/protos \
    --grpc_python_out=src/uep_core/protos \
    src/uep_core/protos/uep.proto
🖥️ Run the gRPC Server
Start the async server:

bash
Copy code
make run-server
Or directly:

bash
Copy code
python src/uep_core/server/grpc_server.py
💬 Run the gRPC Client
Send test messages using the client:

bash
Copy code
make run-client
Or directly:

bash
Copy code
python src/uep_core/client/grpc_client.py
The client will:

Register a test model

Send a sample message

Receive and display a response

🧪 Run Tests
All tests use pytest with pytest-asyncio for async support.

bash
Copy code
make test
Or directly:

bash
Copy code
pytest -v
Ensure pytest is imported in each test file:

python
Copy code
import pytest
🧱 Core Components
🔹 uep.proto
Defines all message schemas and RPC services for:

ModelRegistration

UEPRequest

UEPResponse

UEPExchangeService

🔹 grpc_server.py
Implements the async gRPC server that:

Registers AI models

Handles incoming requests

Routes data to appropriate handlers (text, embeddings, etc.)

🔹 grpc_client.py
Implements the async gRPC client that:

Connects to the UEP server

Sends and receives messages (unary or streaming)

🔹 handlers/
Contains specific handlers for different model types.
Example: text_handler.py for mock text response or LLM simulation.

🔹 logger.py
Custom structured logger using loguru for better traceability.

🧰 Makefile Commands
Command	Description
make protos	Compile protobuf definitions
make run-server	Run gRPC server
make run-client	Run gRPC client
make test	Run all tests
make format	Auto-format code using black + isort

🧪 Example RPC Flow
pgsql
Copy code
Client                Server
  |                      |
  |--- RegisterModel --->|  (model info saved)
  |<---- Response --------|
  |--- SendMessage ------>|  (process request)
  |<---- Response --------|
Example message:

json
Copy code
{
  "request_id": "12345",
  "type": "text",
  "content": "Hello, world!",
  "metadata": {"sender": "client-1"}
}
Response:

json
Copy code
{
  "response_id": "abcde",
  "type": "text",
  "content": "Echo: Hello, world!"
}
🧩 CI/CD Pipeline
Located at .github/workflows/ci.yml:

Installs dependencies

Compiles protobuf files

Runs pytest

Lints code with black and flake8

Runs on every push and pull request

🧠 Tech Stack
Component	Technology
Language	Python 3.10+
RPC Framework	gRPC + Protobuf
Async Runtime	grpc.aio
Testing	pytest, pytest-asyncio
Logging	loguru
CI/CD	GitHub Actions

📚 Future Enhancements
🔒 Add authentication & encryption layers

🧠 Add LLM/Embedding handlers (e.g., OpenAI, Hugging Face)

📡 Add WebSocket gateway for browser interaction

📈 Add monitoring via Prometheus & Grafana

🧩 Add FlatBuffers integration for ultra-fast binary data

🤝 Contributing
Contributions are welcome!
Please fork this repo, make your changes, and submit a pull request.
Ensure all tests pass before submitting.

🧾 License
This project is licensed under the MIT License — see the LICENSE file for details.

💡 Author
Muhammad Talha Yousaf
📧 muhammadtalhayousaf3@gmail.com
💼 LinkedIn

🧩 UEP-Core — bridging AI models with a universal communication protocol.