"""Wrapper types for all structs used in the WPWithin thrift service."""

class Error(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class PricePerUnit(object):
    def __init__(self, amount, currency_code):
        """Create price per unit.

        currency_code: 3 letter currency code
        """
        self.amount = amount
        self.currency_code = currency_code


class Price(object):
    def __init__(self,
                 price_id,
                 description,
                 price_per_unit,
                 unit_id,
                 unit_description):
        """Create price for service.

        price_per_unit: instance of PricePerUnit
        """
        self.price_id = price_id
        self.description = description
        self.price_per_unit = price_per_unit
        self.unit_id = unit_id
        self.unit_description = unit_description


class Service(object):
    def __init__(self, service_id, name, description, prices=None):
        """Create Service.

        prices: list of instances of Price
        """
        self.service_id = service_id
        self.name = name
        self.description = description
        self.prices = prices


class HCECard(object):
    def __init__(self,
                 first_name,
                 last_name,
                 exp_month,
                 exp_year,
                 card_number,
                 card_type,
                 cvc):
        self.first_name = first_name
        self.last_name = last_name
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.card_number = card_number
        self.card_type = card_type
        self.cvc = cvc


class Device(object):
    def __init__(self,
                 uid,
                 name,
                 description,
                 services,
                 ipv4address,
                 currency_code):
        """Create device on the network.

        services: list of instances of Service
        currency_code: 3 letter currency code
        """
        self.uid = uid
        self.name = name
        self.description = description
        self.services = services
        self.ipv4address = ipv4address
        self.currency_code = currency_code


class ServiceMessage(object):
    def __init__(self,
                 device_description,
                 hostname,
                 port_number,
                 server_id,
                 url_prefix,
                 scheme):
        self.device_description = device_description
        self.hostname = hostname
        self.port_number = port_number
        self.server_id = server_id
        self.url_prefix = url_prefix
        self.scheme = scheme


class ServiceDetails(object):
    def __init__(self, service_id, service_description):
        self.service_id = service_id
        self.service_description = service_description


class TotalPriceResponse(object):
    def __init__(self,
                 server_id,
                 client_id,
                 price_id,
                 units_to_supply,
                 total_price,
                 payment_reference_id,
                 merchant_client_key,
                 currency_code):
        self.server_id = server_id
        self.client_id = client_id
        self.price_id = price_id
        self.units_to_supply = units_to_supply
        self.total_price = total_price
        self.payment_reference_id = payment_reference_id
        self.merchant_client_key = merchant_client_key
        self.currency_code = currency_code


class ServiceDeliveryToken(object):
    def __init__(self, key, issued, expiry, refund_on_expiry, signature):
        self.key = key
        self.issued = issued
        self.expiry = expiry
        self.refund_on_expiry = refund_on_expiry
        self.signature = signature


class PaymentResponse(object):
    def __init__(self, server_id, client_id, total_paid, service_delivery_token):
        self.server_id = server_id
        self.client_id = client_id
        self.total_paid = total_paid
        self.service_delivery_token = service_delivery_token
