#pylint: disable=too-many-arguments

import thriftpy
from thriftpy.rpc import make_client, make_server
from thriftpy.protocol.binary import TBinaryProtocolFactory
from thriftpy.transport.buffered import TBufferedTransportFactory
import launcher
import time
import wpwithincallbacks

wptypes_thrift = thriftpy.load('wptypes.thrift', module_name="wptypes_thrift")

import wptypes_thrift as wpt

from ttypes import *
from converters import *


class WPWithin(object):
    def __init__(self, thriftClient):
        self.thriftClient = thriftClient

    def setup(self, name, description):
        try:
            self.thriftClient.setup(name, description)
        except wpt.Error as err:
            raise Error(err.message)

    def add_service(self, svc):
        service = ConvertToThrift.service(svc)
        try:
            self.thriftClient.addService(service)
        except wpt.Error as err:
            raise Error(err.message)

    def remove_service(self, svc):
        service = ConvertToThrift.service(svc)
        try:
            self.thriftClient.removeService(service)
        except wpt.Error as err:
            raise Error(err.message)

    def init_consumer(self,
                      scheme,
                      hostname,
                      port,
                      url_prefix,
                      client_id,
                      hce_card,
                      psp_config):
        card = ConvertToThrift.hce_card(hce_card)
        try:
            self.thriftClient.initConsumer(scheme,
                                           hostname,
                                           port,
                                           url_prefix,
                                           client_id,
                                           card,
                                           psp_config)
        except wpt.Error as err:
            raise Error(err.message)

    def init_producer(self, psp_config):
        try:
            self.thriftClient.initProducer(psp_config)
        except wpt.Error as err:
            raise Error(err.message)

    def get_device(self):
        return ConvertFromThrift.device(self.thriftClient.getDevice())

    def start_service_broadcast(self, timeout_ms):
        try:
            self.thriftClient.startServiceBroadcast(timeout_ms)
        except wpt.Error as err:
            raise Error(err.message)

    def stop_service_broadcast(self):
        try:
            self.thriftClient.stopServiceBroadcast()
        except wpt.Error as err:
            raise Error(err.message)

    def device_discovery(self, timeout_ms):
        try:
            service_messages = self.thriftClient.deviceDiscovery(timeout_ms)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            svc_messages = []
            for val in service_messages:
                svc_messages.append(ConvertFromThrift.service_message(val))
            return svc_messages

    def request_services(self):
        try:
            service_details = self.thriftClient.requestServices()
        except wpt.Error as err:
            raise Error(err.message)
        else:
            svc_details = []
            for val in service_details:
                svc_details.append(ConvertFromThrift.service_details(val))
            return svc_details

    def get_service_prices(self, service_id):
        try:
            prices = self.thriftClient.getServicePrices(service_id)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            wprices = []
            for val in prices:
                wprices.append(ConvertFromThrift.price(val))
            return wprices

    def select_service(self, service_id, number_of_units, price_id):
        try:
            service = self.thriftClient.selectService(service_id, number_of_units, price_id)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.total_price_response(service)

    def make_payment(self, request):
        trequest = ConvertToThrift.total_price_response(request)
        try:
            response = self.thriftClient.makePayment(trequest)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.payment_response(response)

    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            token_received = self.thriftClient.beginServiceDelivery(
                service_id,
                token,
                units_to_supply)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.service_delivery_token(token_received)

    def end_service_delivery(self, service_id, service_delivery_token, units_received):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            token_received = self.thriftClient.endServiceDelivery(service_id, token, units_received)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.service_delivery_token(token_received)


def run_rpc_agent(port, rpc_dir="./rpc-agent/", callback_port=None):
    return launcher.run_rpc_agent(rpc_dir, port, callback_port=callback_port)

def create_client(host,
                  port,
                  start_rpc,
                  start_callback_server=False,
                  callback_port=None,
                  callback_service=None,
                  rpc_dir=None):

    if start_callback_server and (callback_port is None or callback_service is None):
        raise ValueError('No callback port or service provided')

    wpw_thrift = thriftpy.load('wpwithin.thrift', module_name="wpw_thrift")

    return_dict = {}

    if start_rpc:
        if rpc_dir is None and not start_callback_server:
            proc = run_rpc_agent(port)
        elif rpc_dir is None:
            proc = run_rpc_agent(port, callback_port=callback_port)
        elif start_callback_server is None:
            proc = run_rpc_agent(port, rpc_dir=rpc_dir)
        else:
            proc = run_rpc_agent(port, rpc_dir=rpc_dir, callback_port=callback_port)
        return_dict['rpc'] = proc

    time.sleep(2)

    client = make_client(wpw_thrift.WPWithin,
                         host=host,
                         port=port,
                         proto_factory=TBinaryProtocolFactory(),
                         trans_factory=TBufferedTransportFactory())

    if start_callback_server:
        server = make_server(callback_service,
                             wpwithincallbacks,
                             host=host,
                             port=callback_port,
                             proto_factory=TBinaryProtocolFactory(),
                             trans_factory=TBufferedTransportFactory())
        return_dict['server'] = server

    if len(return_dict) > 0:
        return_dict['client'] = WPWithin(client)
        return return_dict

    return WPWithin(client)
