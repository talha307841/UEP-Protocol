# UEP Protocol Specification

## Overview

The Universal Exchange Protocol (UEP) is designed to facilitate seamless communication between various AI models and microservices. This document outlines the specifications for the UEP, including message formats, service definitions, and communication patterns.

## Protocol Version

- **Version**: 1.0
- **Release Date**: YYYY-MM-DD

## Message Formats

### Request Message

The request message structure is defined as follows:

```json
{
  "header": {
    "message_id": "string",
    "timestamp": "string",
    "source": "string",
    "destination": "string",
    "type": "string"
  },
  "body": {
    "data": "object",
    "metadata": {
      "model": "string",
      "service": "string"
    }
  }
}
```

- **header**: Contains metadata about the message.
  - **message_id**: Unique identifier for the message.
  - **timestamp**: Time when the message was created.
  - **source**: Identifier for the sender (model or service).
  - **destination**: Identifier for the intended recipient (model or service).
  - **type**: Type of the message (e.g., request, response, error).

- **body**: Contains the actual data being sent.
  - **data**: The main content of the message.
  - **metadata**: Additional information about the message.
    - **model**: The model that is processing the request.
    - **service**: The service that is processing the request.

### Response Message

The response message structure is defined as follows:

```json
{
  "header": {
    "message_id": "string",
    "timestamp": "string",
    "source": "string",
    "destination": "string",
    "type": "string"
  },
  "body": {
    "data": "object",
    "status": "string",
    "error": "string"
  }
}
```

- **header**: Same as in the request message.

- **body**: Contains the response data.
  - **data**: The result of the request.
  - **status**: Status of the response (e.g., success, failure).
  - **error**: Error message if the request failed.

## Service Definitions

### AI Model Service

- **Endpoint**: `/ai_model`
- **Methods**:
  - `process`: Accepts a request message and returns a response message.

### Microservice

- **Endpoint**: `/microservice`
- **Methods**:
  - `execute`: Accepts a request message and returns a response message.

## Communication Patterns

The UEP supports various communication patterns, including:

- **Request-Response**: A client sends a request and waits for a response.
- **Publish-Subscribe**: Clients can subscribe to specific topics and receive messages when published.
- **Broadcast**: A message is sent to all connected clients.

## Error Handling

Errors are communicated through the response message's `status` and `error` fields. Common error codes include:

- `400`: Bad Request
- `404`: Not Found
- `500`: Internal Server Error

## Conclusion

The UEP provides a flexible and extensible framework for communication between AI models and microservices. By adhering to this protocol specification, developers can ensure compatibility and interoperability within the UEP ecosystem.