import threading
import time
import signal
import sys
from callbacks_event_listener import EventListener
from wpwithin_python import create_client,\
                            PricePerUnit,\
                            Price,\
                            Service,\
                            CommonPSPKeys,\
                            WorldpayPSPKeys,\
                            WP_PSP_NAME


out = create_client("127.0.0.1",
                    9090,
                    True,
                    True,
                    9092,
                    EventListener())

client = out['client']
agent = out['rpc']
server_thread = out['server_thread']
server = out['server']

client.setup("Python3 Device", "Sample Python3 producer device")

psp_config = {
    CommonPSPKeys.psp_name: WP_PSP_NAME,
    CommonPSPKeys.hte_public_key: "T_C_6a38539b-89d0-4db9-bec3-d825779c1809",
    CommonPSPKeys.hte_private_key: "T_S_6b0f27d5-3787-4304-a596-01160c49a55d",
    WorldpayPSPKeys.wp_api_endpoint: "https://api.worldpay.com/v1",
    WorldpayPSPKeys.wp_merchant_client_key: "T_C_6a38539b-89d0-4db9-bec3-d825779c1809",
    WorldpayPSPKeys.wp_merchant_service_key: "T_S_6b0f27d5-3787-4304-a596-01160c49a55d"
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

server_thread.daemon = True
server_thread.start()

print("Start service broadcast")
client.start_service_broadcast(0)

should_run = True
def signal_handler(signal_number, stack_frame):
    print("shutting down...")

    global should_run

    server.close()

    agent.kill()

    should_run = False

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

time.sleep(20)
print("stop broadcast")
client.stop_service_broadcast()

while should_run:
    pass

sys.exit(0)
