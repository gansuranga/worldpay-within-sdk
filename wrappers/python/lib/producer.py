import signal
import sys
import ttypes as types
import wpwithin


out = wpwithin.create_client("127.0.0.1", 9090, True)
client = out['client']
agent = out['rpc']

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

price_per_unit = types.PricePerUnit(amount=650, currency_code="GBP")

rw_price = types.Price(price_id=1,
                       description="Car Wash",
                       price_per_unit=price_per_unit,
                       unit_id=2,
                       unit_description="Single wash")

service = types.Service(service_id=1,
                        name="RoboWash",
                        description="Car washed by robot",
                        prices={1: rw_price})

client.add_service(service)

print("Start service broadcast")
client.start_service_broadcast(0)

def signal_handler(signal_number, stack_frame):
    print("shutting down...")
    agent.kill()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    pass
