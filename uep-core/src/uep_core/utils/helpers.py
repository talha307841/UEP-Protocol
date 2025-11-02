def generate_unique_id():
    import uuid
    return str(uuid.uuid4())

def validate_message_schema(message):
    required_fields = ['id', 'type', 'payload']
    for field in required_fields:
        if field not in message:
            raise ValueError(f"Missing required field: {field}")
    return True

def log_error(error_message):
    import logging
    logging.error(error_message)

def format_response(status, data=None, error=None):
    response = {
        'status': status,
        'data': data,
        'error': error
    }
    return response