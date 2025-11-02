PROTO_DIR=src/uep_core/protocols
PROTO=uep.proto

.PHONY: protos test run-server run-client

protos:
	@echo "Compiling protobufs in $(PROTO_DIR)"
	python -m grpc_tools.protoc \
		--proto_path=$(PROTO_DIR) \
		--python_out=$(PROTO_DIR) \
		--grpc_python_out=$(PROTO_DIR) \
		$(PROTO_DIR)/$(PROTO)

test:
	PYTHONPATH=$(shell pwd)/src pytest -q

run-server:
	python -m uep_core.transports.grpc

run-client:
	python -m uep_core.client
