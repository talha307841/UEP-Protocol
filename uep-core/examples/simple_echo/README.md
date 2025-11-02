# Simple Echo Service Example

This directory contains an example implementation of a simple echo service using the Universal Exchange Protocol (UEP) system. The echo service demonstrates how to set up a basic service that receives messages and sends them back to the sender.

## Getting Started

To run the simple echo service, follow these steps:

1. **Clone the Repository**:
   Clone the `uep-core` repository to your local machine.
   ```bash
   git clone <repository-url>
   cd uep-core
   ```

2. **Install Dependencies**:
   Make sure you have the required dependencies installed. You can use the provided `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Echo Service**:
   Start the echo service using the command line interface provided by the UEP system.
   ```bash
   python -m uep_core.cli --service echo
   ```

4. **Send a Message**:
   You can send a message to the echo service using the command line interface or by using a gRPC client.

## Example Usage

Once the echo service is running, you can send a message like this:

```bash
python -m uep_core.client --send "Hello, UEP!"
```

The service will respond with:

```
Response: Hello, UEP!
```

## Conclusion

This simple echo service serves as a basic example of how to implement a service using the UEP system. You can extend this example to create more complex services and integrate various AI models or microservices as needed. For more information, refer to the [documentation](../../docs/api.md) and [protocol specifications](../../docs/protocol-spec.md).