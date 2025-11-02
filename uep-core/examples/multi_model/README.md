# Multi-Model Example for UEP System

This directory contains an example implementation of the Universal Exchange Protocol (UEP) system using multiple AI models. The goal of this example is to demonstrate how to set up and communicate between different models and microservices within the UEP framework.

## Overview

In this example, we will showcase how to integrate multiple AI models that can communicate with each other through the UEP system. Each model can be treated as a microservice, allowing for modular and scalable architecture.

## Prerequisites

- Python 3.8 or higher
- Required Python packages (see `requirements.txt`)
- Docker (for containerized deployment)
- Basic understanding of gRPC and microservices architecture

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/uep-core.git
   cd uep-core
   ```

2. **Install Dependencies**

   It is recommended to use a virtual environment. You can create one using `venv` or `conda`.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Example**

   To start the multi-model example, you can use the provided shell script:

   ```bash
   ./scripts/start-local.sh
   ```

   This script will set up the necessary services and start the UEP server.

## Example Models

In this example, we will use the following models:

- **Model A**: A natural language processing model that processes text input.
- **Model B**: An image recognition model that analyzes images.

Each model will be registered with the UEP system and will be able to send and receive messages.

## Communication Flow

1. **Model A** receives a text input and processes it.
2. The processed output is sent to **Model B** for further analysis.
3. **Model B** returns the results back to **Model A** or to the client.

## Testing the Example

You can run integration tests to ensure that the multi-model communication is functioning as expected:

```bash
pytest tests/integration/test_end_to_end.py
```

## Conclusion

This example demonstrates the flexibility and modularity of the UEP system, allowing for seamless communication between multiple AI models and microservices. For more detailed information on the UEP system, refer to the documentation in the `docs` directory.