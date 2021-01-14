# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mouse_pb2 as mouse__pb2


class MouseSenderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.mouseStream = channel.unary_stream(
                '/mouseSenderPackage.MouseSender/mouseStream',
                request_serializer=mouse__pb2.EventString.SerializeToString,
                response_deserializer=mouse__pb2.EventString.FromString,
                )


class MouseSenderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def mouseStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MouseSenderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'mouseStream': grpc.unary_stream_rpc_method_handler(
                    servicer.mouseStream,
                    request_deserializer=mouse__pb2.EventString.FromString,
                    response_serializer=mouse__pb2.EventString.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mouseSenderPackage.MouseSender', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MouseSender(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def mouseStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mouseSenderPackage.MouseSender/mouseStream',
            mouse__pb2.EventString.SerializeToString,
            mouse__pb2.EventString.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
