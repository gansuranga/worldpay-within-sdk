import signal
import sys
from wpwithin_python import create_client, PricePerUnit, Price, Service, AbstractEventListener


class EventListener(AbstractEventListener):
    def begin_service_delivery(self, service_id, service_delivery_token, units_to_supply):
        print("Begin Service Delivery")
        print("Service ID: {0}".format(service_id))
        print("Units to supply: {0}".format(units_to_supply))
        print("Service delivery token: {0}".format(service_delivery_token))

    def end_service_delivery(self, service_id, service_delivery_token, units_received):
        print("End Service Delivery")
        print("Service ID: {0}".format(service_id))
        print("Units to supply: {0}".format(units_received))
        print("Service delivery token: {0}".format(service_delivery_token))


out = create_client("127.0.0.1",
                    9090,
                    False,
                    True,
                    9092,
                    EventListener())

client = out['client']
# agent = out['rpc']
server = out['server']

client.setup("Python3 Device", "Sample Python3 producer device")

psp_config = {
    "psp_name": "worldpayonlinepayments",
    "hte_public_key": "T_C_6a38539b-89d0-4db9-bec3-d825779c1809",
    "hte_private_key": "T_S_6b0f27d5-3787-4304-a596-01160c49a55d",
    "api_endpoint": "https://api.worldpay.com/v1",
    "merchant_client_key": "T_C_6a38539b-89d0-4db9-bec3-d825779c1809",
    "merchant_service_key": "T_S_6b0f27d5-3787-4304-a596-01160c49a55d"
}

client.init_producer(psp_config)

price_per_unit = PricePerUnit(amount=650, currency_code="GBP")

rw_price = Price(price_id=1,
                 description="Car Wash",
                 price_per_unit=price_per_unit,
                 unit_id=2,
                 unit_description="Single wash")

service = Service(service_id=1,
                  name="RoboWash",
                  description="Car washed by robot",
                  prices={1: rw_price})

client.add_service(service)

print("Start service broadcast")
client.start_service_broadcast(0)

def signal_handler(signal_number, stack_frame):
    print("shutting down...")
    # agent.kill()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    pass
