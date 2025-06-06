# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import invocation_pb2 as invocation__pb2

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
        + f' but the generated code in invocation_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class InvocationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WindowControl = channel.unary_stream(
            '/invocation.InvocationService/WindowControl',
            request_serializer=invocation__pb2.windowControlReq.SerializeToString,
            response_deserializer=invocation__pb2.windowControlResp.FromString,
            _registered_method=True)
        self.EngineStart = channel.unary_stream(
            '/invocation.InvocationService/EngineStart',
            request_serializer=invocation__pb2.EngineStartReq.SerializeToString,
            response_deserializer=invocation__pb2.EngineStartResp.FromString,
            _registered_method=True)
        self.HonkFlash = channel.unary_stream(
            '/invocation.InvocationService/HonkFlash',
            request_serializer=invocation__pb2.HonkFlashReq.SerializeToString,
            response_deserializer=invocation__pb2.HonkFlashResp.FromString,
            _registered_method=True)
        self.Lock = channel.unary_stream(
            '/invocation.InvocationService/Lock',
            request_serializer=invocation__pb2.LockReq.SerializeToString,
            response_deserializer=invocation__pb2.LockResp.FromString,
            _registered_method=True)
        self.Unlock = channel.unary_stream(
            '/invocation.InvocationService/Unlock',
            request_serializer=invocation__pb2.LockReq.SerializeToString,
            response_deserializer=invocation__pb2.LockResp.FromString,
            _registered_method=True)


class InvocationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WindowControl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EngineStart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HonkFlash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InvocationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'WindowControl': grpc.unary_stream_rpc_method_handler(
            servicer.WindowControl,
            request_deserializer=invocation__pb2.windowControlReq.FromString,
            response_serializer=invocation__pb2.windowControlResp.SerializeToString,
        ),
        'EngineStart': grpc.unary_stream_rpc_method_handler(
            servicer.EngineStart,
            request_deserializer=invocation__pb2.EngineStartReq.FromString,
            response_serializer=invocation__pb2.EngineStartResp.SerializeToString,
        ),
        'HonkFlash': grpc.unary_stream_rpc_method_handler(
            servicer.HonkFlash,
            request_deserializer=invocation__pb2.HonkFlashReq.FromString,
            response_serializer=invocation__pb2.HonkFlashResp.SerializeToString,
        ),
        'Lock': grpc.unary_stream_rpc_method_handler(
            servicer.Lock,
            request_deserializer=invocation__pb2.LockReq.FromString,
            response_serializer=invocation__pb2.LockResp.SerializeToString,
        ),
        'Unlock': grpc.unary_stream_rpc_method_handler(
            servicer.Unlock,
            request_deserializer=invocation__pb2.LockReq.FromString,
            response_serializer=invocation__pb2.LockResp.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'invocation.InvocationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('invocation.InvocationService', rpc_method_handlers)

 # This class is part of an EXPERIMENTAL API.


class InvocationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WindowControl(request,
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
            '/invocation.InvocationService/WindowControl',
            invocation__pb2.windowControlReq.SerializeToString,
            invocation__pb2.windowControlResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EngineStart(request,
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
            '/invocation.InvocationService/EngineStart',
            invocation__pb2.EngineStartReq.SerializeToString,
            invocation__pb2.EngineStartResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HonkFlash(request,
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
            '/invocation.InvocationService/HonkFlash',
            invocation__pb2.HonkFlashReq.SerializeToString,
            invocation__pb2.HonkFlashResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Lock(request,
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
            '/invocation.InvocationService/Lock',
            invocation__pb2.LockReq.SerializeToString,
            invocation__pb2.LockResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Unlock(request,
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
            '/invocation.InvocationService/Unlock',
            invocation__pb2.LockReq.SerializeToString,
            invocation__pb2.LockResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
