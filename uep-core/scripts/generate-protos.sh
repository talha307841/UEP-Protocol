#!/bin/bash

# This script generates the protobuf files for the Universal Exchange Protocol (UEP) system.

PROTO_DIR="./src/uep_core/protocols"
OUT_DIR="./src/uep_core/protocols/generated"

# Create output directory if it doesn't exist
mkdir -p $OUT_DIR

# Generate protobuf files
python -m grpc_tools.protoc -I$PROTO_DIR --python_out=$OUT_DIR --grpc_python_out=$OUT_DIR $PROTO_DIR/*.proto

echo "Protobuf files generated in $OUT_DIR"