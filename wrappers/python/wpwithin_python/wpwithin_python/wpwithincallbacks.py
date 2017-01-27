class AbstractEventListener(object):
    """Abstract class with methods required by WPWithin Callback Service.
    For examples, see
    https://github.com/WPTechInnovation/worldpay-within-sdk/tree/feature/python-wrapper/wrappers/python/wpwithin_python/examples
    """

    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        raise NotImplementedError("You should implement this method in a derived class.")

    def end_service_delivery(self, service_id, service_delivery_token, units_received):
        raise NotImplementedError("You should implement this method in a derived class.")
