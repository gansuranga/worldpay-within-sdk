"""Wrapper class for WPWithin Service."""

import os
from pkg_resources import resource_filename
import thriftpy

from .wpwithin_types import Error
from .converters import ConvertToThrift, ConvertFromThrift

thrift_types_path = resource_filename(__name__, 'wptypes.thrift')
wptypes_thrift = thriftpy.load(thrift_types_path,
                               module_name="wptypes_thrift",
                               include_dirs=[os.path.dirname(thrift_types_path)])
import wptypes_thrift as wpt


class WPWithin(object):
    """Wrapper class for thrift generated struct WPWithin."""

    def __init__(self, thrift_client):
        """Create instance of WPWithin.

        thrift_client: client created with wpwithin.create_client()
        """
        self.thrift_client = thrift_client

    def setup(self, name, description):
        """Setup the thrift client."""
        try:
            self.thrift_client.setup(name, description)
        except wpt.Error as err:
            raise Error(err.message)

    def add_service(self, svc):
        """Add service svc to the client.

        svc: instance of Service.
        """
        service = ConvertToThrift.service(svc)
        try:
            self.thrift_client.addService(service)
        except wpt.Error as err:
            raise Error(err.message)

    def remove_service(self, svc):
        """Remove service svc to the client.

        svc: instance of Service.
        """
        service = ConvertToThrift.service(svc)
        try:
            self.thrift_client.removeService(service)
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
            self.thrift_client.initConsumer(scheme,
                                            hostname,
                                            port,
                                            url_prefix,
                                            client_id,
                                            card,
                                            psp_config)
        except wpt.Error as err:
            raise Error(err.message)

    def init_producer(self, psp_config):
        """Initialise a producer on the client.

        psp_config: Payment Service Provider details. For details see:
        https://github.com/WPTechInnovation/worldpay-within-sdk/wiki/Worldpay-Total-US-(SecureNet)-Integration#usage
        """
        try:
            self.thrift_client.initProducer(psp_config)
        except wpt.Error as err:
            raise Error(err.message)

    def get_device(self):
        return ConvertFromThrift.device(self.thrift_client.getDevice())

    def start_service_broadcast(self, timeout_ms):
        """Start broadcasting services added to client.

        If timeout_ms=0, broadcasts indefinetely.
        """
        try:
            self.thrift_client.startServiceBroadcast(timeout_ms)
        except wpt.Error as err:
            raise Error(err.message)

    def stop_service_broadcast(self):
        try:
            self.thrift_client.stopServiceBroadcast()
        except wpt.Error as err:
            raise Error(err.message)

    def device_discovery(self, timeout_ms):
        """Return list of ServiceMessage found on the network."""
        try:
            service_messages = self.thrift_client.deviceDiscovery(timeout_ms)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            svc_messages = []
            for val in service_messages:
                svc_messages.append(ConvertFromThrift.service_message(val))
            return svc_messages

    def request_services(self):
        """Return list of ServiceDetails found on the network."""
        try:
            service_details = self.thrift_client.requestServices()
        except wpt.Error as err:
            raise Error(err.message)
        else:
            svc_details = []
            for val in service_details:
                svc_details.append(ConvertFromThrift.service_details(val))
            return svc_details

    def get_service_prices(self, service_id):
        """Return list of Price for specified service."""
        try:
            prices = self.thrift_client.getServicePrices(service_id)
        except wpt.Error as err:
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
            service = self.thrift_client.selectService(service_id, number_of_units, price_id)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.total_price_response(service)

    def make_payment(self, request):
        """Pay for service.

        request: TotalPriceResponse returned from WPWithin.select_service.
        """
        trequest = ConvertToThrift.total_price_response(request)
        try:
            response = self.thrift_client.makePayment(trequest)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.payment_response(response)

    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            token_received = self.thrift_client.beginServiceDelivery(
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
            token_received = self.thrift_client.endServiceDelivery(service_id,
                                                                   token,
                                                                   units_received)
        except wpt.Error as err:
            raise Error(err.message)
        else:
            return ConvertFromThrift.service_delivery_token(token_received)
