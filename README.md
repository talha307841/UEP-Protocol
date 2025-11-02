# 🧠 UEP Protocol — Unified Embedding Protocol for Model-to-Model Communication

UEP (Unified Embedding Protocol) is a high-performance communication framework that enables **AI models (e.g., LLMs, TTS, ASR, etc.)** to exchange **embeddings and structured messages** efficiently across different runtime environments using **low-latency transports** such as gRPC, HTTP, and MQTT.

It is designed for **model-to-model communication**, allowing systems like **TTS → LLM → Vision Model** to share embeddings directly in real time using **FlatBuffers** or **protobuf-based** binary encoding.

---

## 🚀 Key Features

- ⚡ **Ultra-low-latency transport layer** (gRPC / HTTP / MQTT)
- 🔄 **Model-to-model communication** via shared embeddings
- 🧩 **Unified schema layer** (Pydantic + FlatBuffers)
- 🔐 **Secure and extensible** message transport
- 🧠 **Model registry** for dynamic model discovery and routing
- 🧪 **Test-ready modular architecture**
- 📦 **Pip-installable** package structure (`uep-core`)

---

## 📁 Project Structure

```
UEP-Protocol/
│
├── uep-core/
│   ├── src/uep_core/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── plugins/
│   │   │   ├── __init__.py
│   │   │   ├── registry.py          # ModelRegistry implementation
│   │   ├── transports/
│   │   │   ├── __init__.py
│   │   │   ├── base.py              # BaseTransport (abstract class)
│   │   │   ├── grpc.py              # gRPC transport
│   │   │   ├── http.py              # HTTP transport
│   │   │   ├── mqtt.py              # MQTT transport
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── message.py           # MessageSchema (Pydantic)
│   │   ├── protocols/
│   │   │   ├── uep_v1/              # Proto or FlatBuffer definitions
│   │   │   │   ├── uep_pb2.py
│   │   │   │   ├── uep_pb2_grpc.py
│   └── tests/
│       ├── unit/
│       │   ├── test_transports.py
│       │   ├── test_client.py
│       └── integration/
│           ├── test_end_to_end.py
```

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/UEP-Protocol.git
cd UEP-Protocol/uep-core

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v
```

---

## 🧠 Example Usage

```python
from uep_core.client import UEPClient

# Initialize client with gRPC transport
client = UEPClient(transport="grpc", host="localhost", port=50051)

# Send embedding to another model
response = client.send_embedding(model="tts_model", embedding=[0.123, 0.456, 0.789])
print(response)
```

---

## 🧩 Architecture Overview

The UEP Protocol enables AI models to communicate using **structured embeddings** encoded via **FlatBuffers** or **protobufs**.  
Each model (e.g., TTS, LLM, ASR) runs a **UEP microservice** that sends and receives embeddings asynchronously through a transport layer.

**Flow Example:**  
```
TTS Model → (Embedding) → UEP Transport → LLM Server
```

Each transport is a plugin that follows a shared interface.  
New transports or protocols can easily be added using the plugin architecture.

---

## 🧪 Testing

All unit tests and integration tests are located under the `tests/` directory.

```bash
PYTHONPATH=uep-core/src pytest -v
```

---

## 🏗️ Packaging

To build and install `uep-core` locally as a pip package:

```bash
cd uep-core
python -m build
pip install dist/uep_core-*.whl
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or PR on GitHub for any feature requests or bug reports.

---

## 📜 License

MIT License © 2025 — Muhammad Talha Yousaf  
