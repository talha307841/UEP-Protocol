# API Documentation for UEP System

## Overview

The Universal Exchange Protocol (UEP) system provides a standardized way for communication between multiple AI models and microservices. This document outlines the API endpoints and methods available in the UEP system.

## API Endpoints

### 1. Message Sending

- **Endpoint:** `/api/v1/send`
- **Method:** `POST`
- **Description:** Sends a message to the specified model or service.
- **Request Body:**
  ```json
  {
    "model": "string",
    "message": {
      "type": "string",
      "payload": {}
    }
  }
  ```
- **Response:**
  - **200 OK:** Message successfully sent.
  - **400 Bad Request:** Invalid message format.
  - **404 Not Found:** Model not found.

### 2. Model Registration

- **Endpoint:** `/api/v1/models/register`
- **Method:** `POST`
- **Description:** Registers a new model or service with the UEP system.
- **Request Body:**
  ```json
  {
    "name": "string",
    "type": "string",
    "config": {}
  }
  ```
- **Response:**
  - **201 Created:** Model successfully registered.
  - **400 Bad Request:** Invalid registration data.

### 3. Model Status

- **Endpoint:** `/api/v1/models/{model_name}/status`
- **Method:** `GET`
- **Description:** Retrieves the status of a registered model.
- **Response:**
  - **200 OK:** Returns the status of the model.
  - **404 Not Found:** Model not found.

### 4. List Models

- **Endpoint:** `/api/v1/models`
- **Method:** `GET`
- **Description:** Lists all registered models and services.
- **Response:**
  - **200 OK:** Returns a list of models.
  ```json
  [
    {
      "name": "string",
      "type": "string",
      "status": "string"
    }
  ]
  ```

## Error Handling

All API responses include an error message in the following format:

```json
{
  "error": {
    "code": "string",
    "message": "string"
  }
}
```

## Conclusion

This API documentation provides a comprehensive overview of the endpoints available in the UEP system. For further details on message formats and protocol specifications, please refer to the [Protocol Specification](protocol-spec.md) document.