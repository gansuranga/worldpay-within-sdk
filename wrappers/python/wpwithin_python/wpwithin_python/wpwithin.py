"""Starts thrift client to be used with Worldpay Within."""

import os
import time
import threading
from pkg_resources import resource_filename
import thriftpy
from thriftpy.rpc import make_client
from thriftpy.protocol.binary import TBinaryProtocolFactory
from thriftpy.transport.buffered import TBufferedTransportFactory

from .wpwithin_service import WPWithin
from .launcher import run_rpc_agent
from .make_simple_server import make_simple_server


def start_server(server):
    """Start callback server."""
    server.serve()

def create_client(host,
                  port,
                  start_rpc,
                  start_callback_server=False,
                  callback_port=None,
                  event_listener=None,
                  rpc_dir=None):
    """Create thrift client for Worldpay Within Service.

    Return a WPWithin instance if start_rpc and start_callback_server are both False.
    If either is true, return a dictionary:
        return_dictionary['client'] -> WPWithin instance
        return_dictionary['rpc'] -> rpc process
        return_dictionary['server'] -> TSimpleServer object with callbacks server
        return_dictionary['server_thread'] -> thread to start server

    If start_callback_server is True, callback_port and event_listener must be specified.
    event_listener: instance of a class which implements AbstractEventListener.
    rpc_dir: path to the rpc agent launcher. Defaults to './rpc-agent/'
    """
    if start_callback_server and (callback_port is None or event_listener is None):
        raise ValueError('No callback port or listener provided')

    thrift_wpw_path = resource_filename(__name__, 'wpwithin.thrift')
    wpw_thrift = thriftpy.load(thrift_wpw_path,
                               module_name="wpw_thrift",
                               include_dirs=[os.path.dirname(thrift_wpw_path)])

    return_dict = {}

    if start_callback_server:
        if callback_port is None:
            raise TypeError("You must specify the callback port")
        elif event_listener is None:
            raise TypeError("You must provide an event listener")

    if start_rpc:
        if rpc_dir is None and not start_callback_server:
            proc = run_rpc_agent(port, rpc_dir="./rpc-agent/")
        elif rpc_dir is None:
            proc = run_rpc_agent(port, rpc_dir="./rpc-agent/", callback_port=callback_port)
        elif not start_callback_server:
            proc = run_rpc_agent(port, rpc_dir=rpc_dir)
        else:
            proc = run_rpc_agent(port, rpc_dir=rpc_dir, callback_port=callback_port)
        return_dict['rpc'] = proc

    time.sleep(1)

    client = make_client(wpw_thrift.WPWithin,
                         host=host,
                         port=port,
                         proto_factory=TBinaryProtocolFactory(),
                         trans_factory=TBufferedTransportFactory())

    if start_callback_server:
        server = make_simple_server(wpw_thrift.WPWithinCallback,
                                    event_listener,
                                    host=host,
                                    port=callback_port)
        return_dict['server'] = server
        return_dict['server_thread'] = threading.Thread(target=start_server,
                                                        args=([server]))

    if len(return_dict) > 0:
        return_dict['client'] = WPWithin(client)
        return return_dict

    return WPWithin(client)
