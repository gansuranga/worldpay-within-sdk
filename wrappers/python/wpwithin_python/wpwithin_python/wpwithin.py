"""Wrapper class for WPWithin Service."""

import os
import time
import sys
import threading
from pkg_resources import resource_filename
import thriftpy
from thriftpy.rpc import make_client
from thriftpy.protocol.binary import TBinaryProtocolFactory
from thriftpy.transport.buffered import TBufferedTransportFactory

from .wpwithin_types import Error
from .converters import ConvertToThrift, ConvertFromThrift
from .launcher import run_rpc_agent, start_server
from .make_simple_server import make_simple_server

THRIFT_WPW_PATH = resource_filename(__name__, 'wpwithin.thrift')
wpw_thrift = thriftpy.load(THRIFT_WPW_PATH,
                           module_name="wpw_thrift",
                           include_dirs=[os.path.dirname(THRIFT_WPW_PATH)])

THRIFT_TYPES_PATH = resource_filename(__name__, 'wptypes.thrift')
wptypes_thrift = thriftpy.load(THRIFT_TYPES_PATH,
                               module_name="wptypes_thrift",
                               include_dirs=[os.path.dirname(THRIFT_TYPES_PATH)])


class WPWithin(object):
    """Wrapper class for thrift generated struct WPWithin."""

    def __init__(self,
                 host,
                 port,
                 start_rpc=True,
                 rpc_dir=None,
                 start_callback_server=False,
                 callback_port=None,
                 event_listener=None):
        """Initialise WPWithin object.

        host (integer): Client host
        port (integer): Client port
        (optional) start_rpc (boolean): Whether to start an rpc agent. Defaults to True.
        (optional) rpc_dir: path to directory with rpc agent launchers. If not specified,
        will search for the files in ./wpw-bin/ and $WPW_HOME/bin, in that order.
        (optional) start_callback_server (boolean): Whether to start a callback server.
        Defaults to False. If True, callback_port and event_listener must be specified.
        (optional) callback_port (integer): port to listen for callback events
        (optional) event_listener: instance of a class which implements AbstractEventListener.
        """

        if start_callback_server and (callback_port is None or event_listener is None):
            raise ValueError('No callback port or listener provided')

        self._thrift_client = make_client(wpw_thrift.WPWithin,
                                          host=host,
                                          port=port,
                                          proto_factory=TBinaryProtocolFactory(),
                                          trans_factory=TBufferedTransportFactory())

        if start_rpc:
            self._rpc = run_rpc_agent(port,
                                      rpc_dir,
                                      start_callback_server,
                                      callback_port)
            time.sleep(1)

        if start_callback_server:
            self._server = make_simple_server(wpw_thrift.WPWithinCallback,
                                              event_listener,
                                              host=host,
                                              port=callback_port)

            self._server_thread = threading.Thread(target=start_server,
                                                   args=([self._server]))

            self._server_thread.daemon = True
            self._server_thread.start()

    def shutdown(self):
        """Close all processes started."""

        self._thrift_client.close()

        if hasattr(self, '_server'):
            self._server.close()

        if hasattr(self, '_rpc'):
            self._rpc.kill()

        sys.exit(0)

    def setup(self, name, description):
        """Setup the thrift client."""
        try:
            self._thrift_client.setup(name, description)
        except wptypes_thrift as err:
            raise Error(err.message)

    def add_service(self, svc):
        """Add service svc to the client.

        svc: instance of Service.
        """
        service = ConvertToThrift.service(svc)
        try:
            self._thrift_client.addService(service)
        except wptypes_thrift as err:
            raise Error(err.message)

    def remove_service(self, svc):
        """Remove service svc to the client.

        svc: instance of Service.
        """
        service = ConvertToThrift.service(svc)
        try:
            self._thrift_client.removeService(service)
        except wptypes_thrift as err:
            raise Error(err.message)

    def init_consumer(self,
                      scheme,
                      hostname,
                      port,
                      url_prefix,
                      client_id,
                      hce_card,
                      psp_config):
        """Initialise a consumer on the client.

        hce_card: instance of HCECard
        psp_config: Payment Service Provider details.
        Must include psp_name and api_endpoint. Example:
        {
           "psp_name": "worldpayonlinepayments",
           "api_endpoint": "https://api.worldpay.com/v1",
        }
        For more details see:
        https://github.com/WPTechInnovation/worldpay-within-sdk/wiki/Worldpay-Total-US-(SecureNet)-Integration#usage
        """
        card = ConvertToThrift.hce_card(hce_card)
        try:
            self._thrift_client.initConsumer(scheme,
                                             hostname,
                                             port,
                                             url_prefix,
                                             client_id,
                                             card,
                                             psp_config)
        except wptypes_thrift as err:
            raise Error(err.message)

    def init_producer(self, psp_config):
        """Initialise a producer on the client.

        psp_config: Payment Service Provider details. For details see:
        https://github.com/WPTechInnovation/worldpay-within-sdk/wiki/Worldpay-Total-US-(SecureNet)-Integration#usage
        """
        try:
            self._thrift_client.initProducer(psp_config)
        except wptypes_thrift as err:
            raise Error(err.message)

    def get_device(self):
        return ConvertFromThrift.device(self._thrift_client.getDevice())

    def start_service_broadcast(self, timeout_ms):
        """Start broadcasting services added to client.

        If timeout_ms=0, broadcasts indefinetely.
        """
        try:
            self._thrift_client.startServiceBroadcast(timeout_ms)
        except wptypes_thrift as err:
            raise Error(err.message)

    def stop_service_broadcast(self):
        try:
            self._thrift_client.stopServiceBroadcast()
        except wptypes_thrift as err:
            raise Error(err.message)

    def device_discovery(self, timeout_ms):
        """Return list of ServiceMessage found on the network."""
        try:
            service_messages = self._thrift_client.deviceDiscovery(timeout_ms)
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            svc_messages = []
            for val in service_messages:
                svc_messages.append(ConvertFromThrift.service_message(val))
            return svc_messages

    def request_services(self):
        """Return list of ServiceDetails found on the network."""
        try:
            service_details = self._thrift_client.requestServices()
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            svc_details = []
            for val in service_details:
                svc_details.append(ConvertFromThrift.service_details(val))
            return svc_details

    def get_service_prices(self, service_id):
        """Return list of Price for specified service."""
        try:
            prices = self._thrift_client.getServicePrices(service_id)
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            wprices = []
            for val in prices:
                wprices.append(ConvertFromThrift.price(val))
            return wprices

    def select_service(self, service_id, number_of_units, price_id):
        """Send request to buy number_of_units of service_id at price_id.

        Return TotalPriceResponse, to be used as argument for WPWithin.make_payment.
        """
        try:
            service = self._thrift_client.selectService(service_id, number_of_units, price_id)
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.total_price_response(service)

    def make_payment(self, request):
        """Pay for service.

        request: TotalPriceResponse returned from WPWithin.select_service.
        """
        trequest = ConvertToThrift.total_price_response(request)
        try:
            response = self._thrift_client.makePayment(trequest)
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.payment_response(response)

    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            token_received = self._thrift_client.beginServiceDelivery(
                service_id,
                token,
                units_to_supply)
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.service_delivery_token(token_received)

    def end_service_delivery(self, service_id, service_delivery_token, units_received):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            token_received = self._thrift_client.endServiceDelivery(service_id,
                                                                    token,
                                                                    units_received)
        except wptypes_thrift as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.service_delivery_token(token_received)
