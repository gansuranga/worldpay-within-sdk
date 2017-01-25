import ttypes as types
import wpwithin
import time
import signal
import sys

out = wpwithin.createClient("127.0.0.1", 9090, True)

client = out['client']
agent = out['rpc']

client.setup("Python3 Device", "Sample Python3 producer device")

pricePerUnit = types.PricePerUnit(amount=650, currencyCode="GBP")
rwPrice = types.Price(id=1, description="Car Wash", pricePerUnit=pricePerUnit, unitId=1, unitDescription="Single wash")
service = types.Service(id=1, name="RoboWash", description="Car washed by robot", prices={1: rwPrice})

client.addService(service)

client.initProducer({"merchantClientKey": "T_C_6a38539b-89d0-4db9-bec3-d825779c1809", "merchantServiceKey": "T_S_6b0f27d5-3787-4304-a596-01160c49a55d"})
print("Start service broadcast")
client.startServiceBroadcast(0)

def signal_handler(signal, frame):
    print("shutting down...")
    agent.kill()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
   pass
