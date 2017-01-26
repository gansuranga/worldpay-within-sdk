#pylint: disable=too-many-arguments

"""
Converters between thriftpy generated types, and wrapper types in ttypes.py
"""

import thriftpy
from ttypes import *

wptypes_thrift = thriftpy.load('wptypes.thrift', module_name="wptypes_thrift")

import wptypes_thrift as wpt


class ConvertToThrift(object):
    @staticmethod
    def ppu(ppu):
        return wpt.PricePerUnit(amount=ppu.amount,
                                currencyCode=ppu.currency_code)

    @classmethod
    def price(cls, price):
        ppu = cls.ppu(price.price_per_unit)
        return wpt.Price(id=price.price_id,
                         description=price.description,
                         pricePerUnit=ppu,
                         unitId=price.unit_id,
                         unitDescription=price.unit_description)

    @classmethod
    def service(cls, service):
        thrift_prices = {}
        for key, value in service.prices.items():
            thrift_prices[key] = cls.price(value)
        return wpt.Service(id=service.service_id,
                           name=service.name,
                           description=service.description,
                           prices=thrift_prices)

    @staticmethod
    def hce_card(card):
        return wpt.HCECard(firstName=card.first_name,
                           lastName=card.last_name,
                           expMonth=card.exp_month,
                           expYear=card.exp_year,
                           cardNumber=card.card_number,
                           type=card.card_type,
                           cvc=card.cvc)

    @staticmethod
    def total_price_response(response):
        return wpt.TotalPriceResponse(serverId=response.server_id,
                                      clientId=response.client_id,
                                      priceId=response.price_id,
                                      unitsToSupply=response.units_to_supply,
                                      totalPrice=response.total_price,
                                      paymentReferenceId=response.payment_reference_id,
                                      merchantClientKey=response.merchant_client_key,
                                      currencyCode=response.currency_code)

    @staticmethod
    def service_delivery_token(token):
        return wpt.ServiceDeliveryToken(key=token.key,
                                        issued=token.issued,
                                        expiry=token.expiry,
                                        refundOnExpiry=token.refund_on_expiry,
                                        signature=token.signature)


class ConvertFromThrift(object):

    @staticmethod
    def ppu(ppu):
        return PricePerUnit(amount=ppu.amount, currency_code=ppu.currencyCode)

    @classmethod
    def price(cls, price):
        ppu = cls.ppu(price.pricePerUnit)
        return Price(price_id=price.id,
                     description=price.description,
                     price_per_unit=ppu,
                     unit_id=price.unitId,
                     unit_description=price.unitDescription)

    @classmethod
    def service(cls, service):
        prices = {}
        for key, value in service.prices.items():
            prices[key] = cls.price(value)
        return Service(service_id=service.id,
                       name=service.name,
                       description=service.description,
                       prices=prices)

    @classmethod
    def device(cls, device):
        services = {}
        for key, value in device.services.items():
            services[key] = cls.service(value)
        return Device(uid=device.uid,
                      name=device.name,
                      description=device.description,
                      services=services,
                      ipv4address=device.ipv4Address,
                      currency_code=device.currencyCode)

    @staticmethod
    def service_message(message):
        return ServiceMessage(device_description=message.deviceDescription,
                              hostname=message.hostname,
                              port_number=message.portNumber,
                              server_id=message.serverId,
                              url_prefix=message.urlPrefix,
                              scheme=message.scheme)

    @staticmethod
    def service_details(details):
        return ServiceDetails(service_id=details.serviceId,
                              service_description=details.serviceDescription)

    @staticmethod
    def total_price_response(response):
        return TotalPriceResponse(server_id=response.serverId,
                                  client_id=response.clientId,
                                  price_id=response.priceId,
                                  units_to_supply=response.unitsToSupply,
                                  total_price=response.totalPrice,
                                  payment_reference_id=response.paymentReferenceId,
                                  merchant_client_key=response.merchantClientKey,
                                  currency_code=response.currencyCode)

    @staticmethod
    def service_delivery_token(token):
        return ServiceDeliveryToken(key=token.key,
                                    issued=token.issued,
                                    expiry=token.expiry,
                                    refund_on_expiry=token.refundOnExpiry,
                                    signature=token.signature)

    @classmethod
    def payment_response(cls, response):
        token = cls.service_delivery_token(response.serviceDeliveryToken)
        return PaymentResponse(server_id=response.serverId,
                               client_id=response.clientId,
                               total_paid=response.totalPaid,
                               service_delivery_token=token)
