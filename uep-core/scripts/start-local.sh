#!/bin/bash

# Start the UEP server and client locally

# Load environment variables from .env file if it exists
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Start the UEP server
echo "Starting UEP server..."
python3 -m src.uep_core.server &

# Wait for the server to start
sleep 5

# Start the UEP client
echo "Starting UEP client..."
python3 -m src.uep_core.client

# Wait for the client to finish
wait