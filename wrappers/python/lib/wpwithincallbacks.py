import thriftpy
from ttypes import *

wptypes_thrift = thriftpy.load('wptypes.thrift', module_name="wptypes_thrift")

import wptypes_thrift as wpt
from converters import *


class WPWithinCallback(object):
    def __init__(self, thrift_client):
        self.thrift_client = thrift_client

    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            self.thriftClient.beginServiceDelivery(self, service_id, token, units_to_supply)
        except wpt.Error as err:
            raise Error(err.message)

    def end_service_delivery(self, service_id, service_delivery_token, units_received):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            self.thriftClient.endServiceDelivery(self, service_id, token, units_received)
        except wpt.Error as err:
            raise Error(err.message)
