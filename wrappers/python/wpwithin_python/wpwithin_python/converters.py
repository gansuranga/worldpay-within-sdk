"""Converters between thriftpy generated types, and wrapper types in wpwithin_types."""

import os
import thriftpy
from pkg_resources import resource_filename
from .wpwithin_types import PricePerUnit, \
                    Price, \
                    Service, \
                    Device, \
                    ServiceMessage, \
                    ServiceDetails, \
                    TotalPriceResponse, \
                    ServiceDeliveryToken, \
                    PaymentResponse

thrift_types_path = resource_filename(__name__, 'wptypes.thrift')
wptypes_thrift = thriftpy.load(thrift_types_path,
                               module_name="wptypes_thrift",
                               include_dirs=[os.path.dirname(thrift_types_path)])
import wptypes_thrift as wpt


class ConvertToThrift(object):
    """Convert from types in wpwithin_types to thriftpy generated ones."""

    @staticmethod
    def ppu(ppu):
        """Convert to thriftpy generated PricePerUnit."""
        return wpt.PricePerUnit(amount=ppu.amount,
                                currencyCode=ppu.currency_code)

    @classmethod
    def price(cls, price):
        """Convert to thriftpy generated Price."""
        ppu = cls.ppu(price.price_per_unit)
        return wpt.Price(id=price.price_id,
                         description=price.description,
                         pricePerUnit=ppu,
                         unitId=price.unit_id,
                         unitDescription=price.unit_description)

    @classmethod
    def service(cls, service):
        """Convert to thriftpy generated Service."""
        thrift_prices = {}
        for key, value in service.prices.items():
            thrift_prices[key] = cls.price(value)
        return wpt.Service(id=service.service_id,
                           name=service.name,
                           description=service.description,
                           prices=thrift_prices)

    @staticmethod
    def hce_card(card):
        """Convert to thriftpy generated HCECard."""
        return wpt.HCECard(firstName=card.first_name,
                           lastName=card.last_name,
                           expMonth=card.exp_month,
                           expYear=card.exp_year,
                           cardNumber=card.card_number,
                           type=card.card_type,
                           cvc=card.cvc)

    @staticmethod
    def total_price_response(response):
        """Convert to thriftpy generated TotalPriceResponse."""
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
        """Convert to thriftpy generated ServiceDeliveryToken."""
        return wpt.ServiceDeliveryToken(key=token.key,
                                        issued=token.issued,
                                        expiry=token.expiry,
                                        refundOnExpiry=token.refund_on_expiry,
                                        signature=token.signature)


class ConvertFromThrift(object):
    """Convert from thriftpy generated types to the ones in wpwithin_types."""

    @staticmethod
    def ppu(ppu):
        """Convert to wpwithin_types.PricePerUnit."""
        return PricePerUnit(amount=ppu.amount, currency_code=ppu.currencyCode)

    @classmethod
    def price(cls, price):
        """Convert to wpwithin_types.Price."""
        ppu = cls.ppu(price.pricePerUnit)
        return Price(price_id=price.id,
                     description=price.description,
                     price_per_unit=ppu,
                     unit_id=price.unitId,
                     unit_description=price.unitDescription)

    @classmethod
    def service(cls, service):
        """Convert to wpwithin_types.Service."""
        prices = {}
        for key, value in service.prices.items():
            prices[key] = cls.price(value)
        return Service(service_id=service.id,
                       name=service.name,
                       description=service.description,
                       prices=prices)

    @classmethod
    def device(cls, device):
        """Convert to wpwithin_types.Device."""
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
        """Convert to wpwithin_types.ServiceMessage."""
        return ServiceMessage(device_description=message.deviceDescription,
                              hostname=message.hostname,
                              port_number=message.portNumber,
                              server_id=message.serverId,
                              url_prefix=message.urlPrefix,
                              scheme=message.scheme)

    @staticmethod
    def service_details(details):
        """Convert to wpwithin_types.ServiceDetails."""
        return ServiceDetails(service_id=details.serviceId,
                              service_description=details.serviceDescription)

    @staticmethod
    def total_price_response(response):
        """Convert to wpwithin_types.TotalPriceResponse."""
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
        """Convert to wpwithin_types.ServiceDeliveryToken."""
        return ServiceDeliveryToken(key=token.key,
                                    issued=token.issued,
                                    expiry=token.expiry,
                                    refund_on_expiry=token.refundOnExpiry,
                                    signature=token.signature)

    @classmethod
    def payment_response(cls, response):
        """Convert to wpwithin_types.PaymentResponse."""
        token = cls.service_delivery_token(response.serviceDeliveryToken)
        return PaymentResponse(server_id=response.serverId,
                               client_id=response.clientId,
                               total_paid=response.totalPaid,
                               service_delivery_token=token)
