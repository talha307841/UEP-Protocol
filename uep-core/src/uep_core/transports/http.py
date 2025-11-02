from flask import Flask, request, jsonify
from uep_core.schemas.message import MessageSchema
from uep_core.plugins.registry import ModelRegistry

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message_schema = MessageSchema()
    errors = message_schema.validate(data)
    
    if errors:
        return jsonify({'errors': errors}), 400

    message = message_schema.load(data)
    response = ModelRegistry.dispatch_message(message)
    
    return jsonify(response), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)