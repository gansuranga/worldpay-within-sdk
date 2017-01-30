from wpwithin_python import AbstractEventListener


class EventListener(AbstractEventListener):
    def beginServiceDelivery(self, service_id, service_delivery_token, units_to_supply):
        print("Begin Service Delivery")
        print("Service ID: {0}".format(service_id))
        print("Units to supply: {0}".format(units_to_supply))
        print("Service delivery token: {0}".format(service_delivery_token))

    def endServiceDelivery(self, service_id, service_delivery_token, units_received):
        print("End Service Delivery")
        print("Service ID: {0}".format(service_id))
        print("Units to supply: {0}".format(units_received))
        print("Service delivery token: {0}".format(service_delivery_token))
