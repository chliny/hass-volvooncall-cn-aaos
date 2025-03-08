# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import fuel_pb2 as fuel__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in fuel_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FuelServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFuel = channel.unary_stream(
            '/services.vehiclestates.fuel.FuelService/GetFuel',
            request_serializer=fuel__pb2.GetFuelReq.SerializeToString,
            response_deserializer=fuel__pb2.GetFuelResp.FromString,
            _registered_method=True)


class FuelServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFuel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FuelServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetFuel': grpc.unary_stream_rpc_method_handler(
            servicer.GetFuel,
            request_deserializer=fuel__pb2.GetFuelReq.FromString,
            response_serializer=fuel__pb2.GetFuelResp.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'services.vehiclestates.fuel.FuelService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('services.vehiclestates.fuel.FuelService', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class FuelService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFuel(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/services.vehiclestates.fuel.FuelService/GetFuel',
            fuel__pb2.GetFuelReq.SerializeToString,
            fuel__pb2.GetFuelResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
