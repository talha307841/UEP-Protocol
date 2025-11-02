"""Protocol definitions and compiled gRPC/python stubs.

This package may contain generated files `uep_pb2.py` and
`uep_pb2_grpc.py` created by `grpc_tools.protoc`. We try to import them
here so callers can simply `from uep_core.protocols import uep_pb2, uep_pb2_grpc`.
"""

try:
	from . import uep_pb2  # type: ignore
	from . import uep_pb2_grpc  # type: ignore
except Exception:
	# During development the generated modules might not exist yet. That's
	# fine — callers should handle None or import failures as needed.
	uep_pb2 = None  # type: ignore
	uep_pb2_grpc = None  # type: ignore