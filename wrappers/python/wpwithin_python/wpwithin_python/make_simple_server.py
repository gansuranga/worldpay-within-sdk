"""Create a simple, unthreaded server."""

from thriftpy.server import TSimpleServer
from thriftpy.transport import TServerSocket
from thriftpy.thrift import TProcessor


def make_simple_server(service, handler,
                       host="localhost",
                       port=9090):
    """Return a server of type TSimple Server.

    Based on thriftpy's make_server(), but return TSimpleServer instead of
    TThreadedServer.
    Since TSimpleServer's constructor doesn't accept kwargs, some arguments of
    make_server can't be used here. By default:
        client_timeout: None
        protocol: TBinaryProtocolFactory
        transport: TBufferedTransportFactory
    """
    processor = TProcessor(service, handler)

    if host and port:
        server_socket = TServerSocket(
            host=host, port=port, client_timeout=None)
    else:
        raise ValueError("Either host/port or unix_socket must be provided.")

    server = TSimpleServer(processor, server_socket)

    return server
