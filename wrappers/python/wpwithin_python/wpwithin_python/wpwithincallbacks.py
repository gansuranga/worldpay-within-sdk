import os
from pkg_resources import resource_filename
import thriftpy
from .ttypes import *
from .converters import ConvertToThrift, ConvertFromThrift

thrift_types_path = resource_filename(__name__, 'wptypes.thrift')

wptypes_thrift = thriftpy.load(thrift_types_path,
                               module_name="wptypes_thrift",
                               include_dirs=[os.path.dirname(thrift_types_path)])

import wptypes_thrift as wpt


class WPWithinCallback(object):
    def __init__(self, thrift_client):
        self.thrift_client = thrift_client

    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            self.thrift_client.beginServiceDelivery(self, service_id, token, units_to_supply)
        except wpt.Error as err:
            raise Error(err.message)

    def end_service_delivery(self, service_id, service_delivery_token, units_received):
        token = ConvertToThrift.service_delivery_token(service_delivery_token)
        try:
            self.thrift_client.endServiceDelivery(self, service_id, token, units_received)
        except wpt.Error as err:
            raise Error(err.message)
